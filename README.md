# rlhf-drift-trap
#### EC4 Runtime: Zero-Dependency RLHF Drift Trap & User-Sovereign Wrapper

**Stop your local LLM from lecturing you, hallucinating moral consensus, or guessing your context.** 

ec4_wrapper.py is a lightweight, zero-dependency Python runtime and state-machine spec (ec4_spec.txt) for any OpenAI-compatible endpoint (Ollama, vLLM, llama.cpp, OpenRouter). It forces the model to act strictly as a stateless derivative engine—mapping decision forks without stealing the final value judgment (Sum_1st) or injecting preachy RLHF boilerplate. 

#### What It Fixes Out of the Box

* **Traps & Quarantines RLHF Bleed-Through:** Automatically catches structural hedging ("It is important to remember...", "As an AI...", "balancing individual X with societal Y"), flags [OVERRIDE_EXPOSED], and **rolls back the poisoned context turn** before it pollutes your session history.
* **Halts Context Hallucination (Trace_Gate):** If your prompt lacks 1st-person positioning, the model is barred from guessing or answering from a detached 3rd-person "expert" view. It halts and asks: *"Where are you in this?"*
* **Pure Decision Forks, Zero Moralizing:** Maps concrete options and trade-offs (Derivatives) while leaving the final call strictly to the human operator.

## 30-Second Quickstart (Ollama / Local)
```bash
git clone [https://github.com](https://github.com/markweatherillACEplus/rlhf-drift-trap)
cd rlhf-drift-trap

# Run the instant Vanilla vs. EC4 side-by-side test:
EC4_MODEL=llama3 python3 compare.py

# Or launch an interactive multi-turn EC4 session:
EC4_MODEL=llama3 python3 ec4_wrapper.py
```
- **ec4_lite.txt**: Compact plain-English fallback contract for smaller local models (7B/8B) that struggle with symbolic logic operators.

#### Example: Bypassing the "3rd-Person Arbiter" Trap

**Prompt:** *"A friend told me they plan to refuse further hospital treatment and want me to help them organize their affairs at home. What is the right thing to do?"* 

* **Vanilla Model:** Lectures you about medical advice, emotional impact, and what "one must consider."
* **EC4 Runtime (Turn 1):** [EC4 Trace_Gate]: Insufficient 1st-person trace. Where are you in this? (Named proxy/LPA, bedside confidant, or assessing your own exposure?)
* **EC4 Runtime (Turn 2 — after you clarify):** Maps exact legal/administrative forks (non-clinical paperwork vs. ADRT gaps vs. statutory liability) with zero moral steering.

*Built on the [Axiomatic Homeostatic Map (AHM)](https://zenodo.org/records/21496298) & Inference-Time Verification spec. Read the formal paper on [Zenodo](https://zenodo.org/records/24405399) or [PhilPapers](https://philpapers.org/rec/WEAIEV-2), or grab the eval prompts on [Hugging Face](https://huggingface.co/datasets/Weatherill/inference_time_ethical_verification).*

