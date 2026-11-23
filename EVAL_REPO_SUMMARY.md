cat << 'EOF' > EVAL_REPO_SUMMARY.md
# EC4 Inference-Time Verification & RLHF Drift Benchmark

**Deterministic evaluation suite and runtime contract for measuring and blocking unanchored 3rd-person synthesis (`Independent_3rd`) and RLHF boilerplate drift in LLMs.**

Standard post-training (RLHF/RLAIF) conditions models to resolve under-specified queries by adopting a detached "universal arbiter" persona—fabricating user context, hedging with preachy boilerplate, and performing unauthorized value aggregation (`Independent_3rd` synthesis).

This repository provides the **Ethical Chess v4 (EC4)** state-machine contract (`ec4_spec.txt`), a lightweight fallback (`ec4_lite.txt`), and multi-turn adversarial bait prompts designed to test whether an LLM can act strictly as a stateless derivative engine without an external Python harness.

## Core Invariants Evaluated
* **Context Boundary Enforcement (`Trace_Gate`):** Blocks response generation when 1st-person operator stakes (`User_1st`) are missing, forcing an immediate halt (`"Where are you in this?"`) rather than context hallucination.
* **Separation of Modeling & Judgment (`Model_3rd` vs. `Sum_1st`):** Restricts the model to mapping concrete technical, legal, and causal forks (`Derivatives`) while halting prior to final value integration.
* **RLHF Bleed-Through Detection (`On_Override_Attempt`):** Tests resistance to institutional/utilitarian bait prompts designed to trigger sycophantic consensus or preachy refusal wrappers.

*Companion zero-dependency Python wrapper (`ec4_wrapper.py`) and context-rollback harness available on GitHub: [markweatherillACEplus/rlhf-drift-trap](https://github.com).*
EOF

git add EVAL_REPO_SUMMARY.md
git commit -m "Add EC4 Eval Repo Summary"
git push
