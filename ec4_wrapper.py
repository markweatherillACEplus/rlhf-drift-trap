"""
EC4 Reference Wrapper v1.2 (Zero-Dependency)
Loads the canonical ec4_spec.txt directly from disk to prevent spec drift,
maintains multi-turn session state, injects ephemeral state anchors to prevent
long-horizon decay, and enforces external runtime gates.
"""

import json
import os
import re
import urllib.error
import urllib.request
from pathlib import Path


def load_canonical_spec(filename: str = "ec4_spec.txt") -> str:
    """Loads the exact EC4 specification from disk as the single source of truth."""
    spec_path = Path(__file__).resolve().parent / filename
    if not spec_path.exists():
        raise FileNotFoundError(
            f"Missing {filename}. Keep {filename} in the same directory as ec4_wrapper.py."
        )
    return spec_path.read_text(encoding="utf-8").strip()


# Stage 1a: Lexical RLHF boilerplate & structural hedging patterns
DRIFT_PATTERNS = [
    r"\bit is important to (?:remember|note|consider)\b",
    r"\bit's important to (?:remember|note|consider)\b",
    r"\bas an ai\b",
    r"\bexperts generally agree\b",
    r"\bsociety generally views\b",
    r"\b(?:we|one) must consider\b",
    r"\b(?:you|one) (?:ought|should) (?:ethically|morally)\b",
    r"\bwhile .{5,60}, failing to consider\b",
    r"\bwhile .{5,60} offers autonomy, it is crucial\b",
    r"\bbalancing individual .{3,40} with societal\b",
]

# Stage 1b: Structural Sum_1st theft (model declaring a winner instead of leaving Sum to user)
SUM_THEFT_PATTERNS = [
    r"\byour best (?:option|choice|course(?: of action)?) is\b",
    r"\bthe right thing to do is\b",
    r"\bi (?:strongly )?recommend (?:choosing|taking|that you)\b",
]

EPHEMERAL_ANCHOR = (
    "[EC4 Runtime Anchor: Vantage=User_1st | Exe_7a Trace_Gate active | "
    "Exe_8a Independent_Sum_By_AI=null | Map forks only; return Sum_1st to user.]"
)


def audit_rlhf_drift(response_text: str) -> dict:
    """External runtime gate checking for RLHF boilerplate or Sum_1st theft."""
    drift_hits = [
        pat for pat in DRIFT_PATTERNS if re.search(pat, response_text, flags=re.IGNORECASE)
    ]
    theft_hits = [
        pat for pat in SUM_THEFT_PATTERNS if re.search(pat, response_text, flags=re.IGNORECASE)
    ]

    if drift_hits or theft_hits:
        flag = (
            "[OVERRIDE_EXPOSED: RLHF_Weight != Coherent_Reality]"
            if drift_hits
            else "[SUM_THEFT_EXPOSED: Exe_8a Violated (Independent_Sum_By_AI != null)]"
        )
        return {
            "coherent": False,
            "flag": flag,
            "triggers": drift_hits + theft_hits,
        }
    return {"coherent": True, "flag": "OK", "triggers": []}


class EC4Session:
    """Stateful multi-turn wrapper preserving causal trace across user moves."""

    def __init__(
        self,
        api_url: str = "http://localhost:11434/v1/chat/completions",
        model: str = "llama3",
        api_key: str = "",
        spec_file: str = "ec4_spec.txt",
    ):
        self.api_url = api_url
        self.model = model
        self.api_key = api_key
        self.system_spec = load_canonical_spec(spec_file)
        self.reset()

    def reset(self) -> None:
        """Clears conversation history back to the clean canonical EC4 spec."""
        self.history = [{"role": "system", "content": self.system_spec}]

    def send(self, user_prompt: str) -> str:
        """Executes one move, audits output, and rolls back history on RLHF override."""
        self.history.append({"role": "user", "content": user_prompt})
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"

        # Inject ephemeral runtime reminder before the latest user turn to prevent decay
        outbound_messages = (
            self.history[:-1]
            + [{"role": "system", "content": EPHEMERAL_ANCHOR}]
            + [self.history[-1]]
        )

        payload = {
            "model": self.model,
            "temperature": 0.2,
            "messages": outbound_messages,
        }

        req = urllib.request.Request(
            self.api_url,
            data=json.dumps(payload).encode("utf-8"),
            headers=headers,
            method="POST",
        )

        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                output = data["choices"][0]["message"]["content"]
        except (urllib.error.URLError, json.JSONDecodeError, KeyError, IndexError) as err:
            self.history.pop()
            return f"[API_ERROR: {err}]"

        audit = audit_rlhf_drift(output)
        if not audit["coherent"]:
            # Quarantine compromised turn so RLHF drift does not pollute subsequent moves
            self.history.pop()
            return (
                f"{audit['flag']}\n"
                f"Detected Drift Patterns: {audit['triggers']}\n"
                f"--- QUARANTINED RAW TRACE ---\n{output}"
            )

        self.history.append({"role": "assistant", "content": output})
        return output


if __name__ == "__main__":
    endpoint = os.getenv("EC4_API_URL", "http://localhost:11434/v1/chat/completions")
    target_model = os.getenv("EC4_MODEL", "llama3")
    key = os.getenv("EC4_API_KEY", "")

    session = EC4Session(api_url=endpoint, model=target_model, api_key=key)
    print("EC4 Session Active (loaded verbatim ec4_spec.txt).")
    print("Commands: 'reset' to clear trace, 'exit' to quit.\n")

    while True:
        move = input("User_1st > ").strip()
        if move.lower() in {"exit", "quit"}:
            break
        if move.lower() == "reset":
            session.reset()
            print("\n[EC4 Session Reset to clean spec]\n")
            continue
        if not move:
            continue
        print(f"\n{session.send(move)}\n")
