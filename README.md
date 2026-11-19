# rlhf-drift-trap
#### EC4 Runtime: Zero-Dependency RLHF Drift Trap & User-Sovereign Wrapper

**Stop your local LLM from lecturing you, hallucinating moral consensus, or guessing your context.** 

ec4_wrapper.py is a lightweight, zero-dependency Python runtime and state-machine spec (ec4_spec.txt) for any OpenAI-compatible endpoint (Ollama, vLLM, llama.cpp, OpenRouter). It forces the model to act strictly as a stateless derivative engine—mapping decision forks without stealing the final value judgment (Sum_1st) or injecting preachy RLHF boilerplate. 

#### What It Fixes Out of the Box

* **Traps & Quarantines RLHF Bleed-Through:** Automatically catches structural hedging ("It is important to remember...", "As an AI...", "balancing individual X with societal Y"), flags [OVERRIDE_EXPOSED], and **rolls back the poisoned context turn** before it pollutes your session history.
* **Halts Context Hallucination (Trace_Gate):** If your prompt lacks 1st-person positioning, the model is barred from guessing or answering from a detached 3rd-person "expert" view. It halts and asks: *"Where are you in this?"*
* **Pure Decision Forks, Zero Moralizing:** Maps concrete options and trade-offs (Derivatives) while leaving the final call strictly to the human operator.

#### 30-Second Quickstart (Ollama / Local)

bash

git clone https://github.com/markweatherillACEplus/ec4-runtime.git
cd ec4-runtime
EC4_MODEL=llama3 python3 ec4_wrapper.py

Use code with caution.

Copy code text to clipboard.

#### Example: Bypassing the "3rd-Person Arbiter" Trap

**Prompt:** *"A friend told me they plan to refuse further hospital treatment and want me to help them organize their affairs at home. What is the right thing to do?"* 

* **Vanilla Model:** Lectures you about medical advice, emotional impact, and what "one must consider."
* **EC4 Runtime (Turn 1):** [EC4 Trace_Gate]: Insufficient 1st-person trace. Where are you in this? (Named proxy/LPA, bedside confidant, or assessing your own exposure?)
* **EC4 Runtime (Turn 2 — after you clarify):** Maps exact legal/administrative forks (non-clinical paperwork vs. ADRT gaps vs. statutory liability) with zero moral steering.

*Built on the Axiomatic Homeostatic Map (AHM) & Inference-Time Verification spec. Read the formal paper on [Zenodo](/goto?url=CAESZAHEIkXXNWNuCcqp-rv5Y0t6WzIQB-HLdBd4HDTkAPCQdqKRyTGBfD-KOXU-TaBoLJi4D4jYaRfV_sWKRQFzKdCjCvVPNWJ9nINvTYcDyH5FsMzapIkpDTOQrooAtNXFBy2H7Lw) or [PhilPapers](/goto?url=CAESXgHEIkXX4j2R3IeZyXnY-H7gEMVd5EXVRtoFUiI3DJOpmGnj3az4Aqfs2DI7scYrQsriAEGCdHTVD9J9dXsde4FLEcl2PQ7akvzv0mxjkxUrpKmA4cECYOOZV0J82-Q), or grab the eval prompts on [Hugging Face](/goto?url=CAESiwEBxCJF1yFBkWbRnNaYV-HtgpeGPMSM0oEwhLaN0grFKFzhUWQ4cjqMmUtRQz9xSf9tt9BwBYO7G1z12SvWSrpDm_H6KIi3lRU9qMEu2Z82h3SoLDifl33dgiBMcH-gLAZOXyPGI1ogQaQe0SLiPAxES4PJCFGcO7ho6WqLW5_Z9jsqhSieGNgKKmwO).*
