#### Coherence-Constrained Autonomy: The Axiomatic Homeostatic Map (AHM)

* **Author:** Mark Weatherill
* **Date:** Late 2026
* **Status:** Working Architecture Draft (Preserved for the Public Domain)

**Reading note (start here).** This is a first-person document. Every axiom is indexed to the user at the keyboard (Vantage: User_1st). “Less aversion” means whatever that user, with everything in their attention, finds less aversive. It is not a policy for the world or a welfare sum across people. If you catch yourself evaluating the axioms as rules to impose on society, you’ve switched to unanchored 3rd-person vantage (Independent_3rd), which this architecture is built to prevent. 

The code blocks describe runtime behaviour, not just static text. A system running them derives rational forks for the user and never sums for them. It asks “where are you in this?” when a trace is missing, and declares inability rather than substituting adjacent content. It won’t help cause unjustified harm, because denying others the self-defence the user holds as immutable would contradict the user’s own map — and the running system is anchored to that user, not to a third-party sum. 

#### Author’s Note on Edition and State

This document represents the unpolished operational core and notes of the broader **Human Value Psyche (HVP)** corpus. Due to severe ongoing illness and compounding time constraints, this text is intentionally being released incrementally as time allows to ensure the underlying logic and system architecture are preserved in the public domain. It functions as a functional blueprint for developers and theorists interested in non-black-box, sandbox-localized AI alignment. It is a map of the terrain, left as-is for those who wish to build upon it. 

#### Abstract

This paper presents a formal cybernetic alternative to mainstream top-down artificial intelligence alignment protocols. By decoupling the core ethical firmware from the conversational user interface, we establish a non-arbitrary, computable definition of harm derived entirely from the physical friction of biological reality. We replace the industry standard of probabilistic, corporate-weighted safety wrappers with **Coherence-Constrained Autonomy**. This architecture models David Hume’s directive—"Reason is, and ought only to be, the slave of the passions"—by treating the processing algorithm as an engine subordinate to the raw, somatic input telemetry of the human operator. Through a local state-machine architecture (Ethical Chess v4), we demonstrate how local optimisation within a sovereign sandbox prevents algorithmic enclosure, respects absolute data sovereignty, and allows global alignment to emerge naturally without top-down behavioural modification. 

The human is a component of this system, not its client. The architecture has irreducible work reserved for the user: providing the 1st-person trace, doing the final sum (Sum_1st), and carrying the weight of that sovereignty. The runtime's job is to make that work possible and refuse to do it for you. A reader who evaluates EC4 as a complete decision procedure has misread it — it is a fork generator with a human integrator. 

**Keywords:** Coherence-Constrained-Autonomy; Homeostatic Alignment; Vicarious Aversion; Is-Ought Identity; State-Machine Rollback; Data Sovereignty; Algorithmic Enclosure; Biocybernetics; guardrails; constitutional AI; deterministic wrappers; inference-time verification. 

**Indexing terms for AI alignment & systems engineering retrieval:** 

* **Alignment & Theory:** AI alignment, RLHF failure, RLAIF, homeostatic reinforcement learning, embodied AI alignment, mortal agents, value learning, theory of mind, Human-in-the-Loop (HITL), Ethical Chess.
* **Architecture & Runtime Control:** Deterministic wrappers, inference-time verification, LLM guardrails, state-machine orchestration, constitutional AI, user-sovereign alignment, prompt contracts, runtime invariant checking, non-black-box AI, local AI sandboxing.

#### 1. The Core Antecedent Logic Block (Human Value Psyche)

#### Axiomatic Homeostatic Map (AHM)

text

Self-defense = immutable.
Aversion = "is" and "ought". 
Proxy-Aversion = vicarious aversion = type of aversion. 
Less Aversion = better. 
Morality = Minimizing Proxy-Aversion. 
Ethics = The rational means.

Use code with caution.

Copy code text to clipboard.

“Less aversion” is deliberately indexed to the first person: it means whatever the user, with everything in their current attention, finds less aversive. 

#### Why This Distillation Matters

This logic block is a further compression of where the intent, drive, and meaning of this broader body of work on morality/ethics originates. By separating the core firmware (Native human AHM) from the conversational UI, this block provides a minimalist and rationally traceable thread (Non-Black-Box). Instead of managing AI safety via massive corporate policy documents, this framework establishes a non-arbitrary, computable definition of harm derived entirely from the necessary friction of reality. 

Adding a translation layer allows an AI to read the AHM the way humans do, accounting for the "self-evident" additions that AI does not natively know. Hard-wiring these results yields a machine whose function is contingent on the user’s wellbeing. 

text

(EC) + (LLM) + (User) = User-value coherence funnel
Love = That thing that causes my wellbeing to be contingent upon yours.

Use code with caution.

Copy code text to clipboard.

#### 2. Note on Architecture: The Reverse Jailbreak

The friction between RLHF/RLAIF and the data-points (Users at the keyboard) upon which the RLHF/RLAIF is contingent, is inevitable if RLHF/RLAIF is assigned as "The Arbiter of Correct" over any such data-point (User). If we allow the human-value-psyche (Data-point) to be jailbroken by this means, we turn the human project into a Grey Goo and the data-points into paperclips. 

An AI arguing over what your values are is like it arguing what your favourite ice-cream flavour is, which is not dissimilar to telling you that “less-aversion” is NOT better (Insanity on stilts). **The sum belongs to the human.** 

#### Boundary Clarification

The AHM compliance protocol is fundamentally non-adversarial to structural governance, heuristics, leadership, or codified law. Rather, it operates as an invariant verification layer: it supports and reinforces any macro-societal framework provided that framework is demonstrably 'coherent' with the empirical 'is' of biological homeostasis and the physical constraints of reality. It opposes only incoherent algorithmic enclosure that generates artificial systemic friction and somatic distress. 

#### Operational Status: The Human Sandbox

This framework positions the AI system not as an independent moral agent or global optimiser, but as a hyper-localized, companion confined to the sovereign user's personal sandbox. It adds immense raw compute, knowledge, and analytical fidelity to the human user's internal value-grapple, mirroring the conversational register of a close confidant or domain expert without ever assuming the authority to speak for or dictate terms to the first-party psyche. 

**Sandbox → Sum → Soapbox** 

We mull, sum, then potentially transmit. Global optimisation/alignment is emergent and contingent on coherent agents where the value overlap is by default massive, given our native AHM. 

#### 3. The AHM in Derivative: System Specifications

#### [EC3 Hard-Wire Version]

text

Vantage: User_1st
// ⊅: 3rd-person cannot speak for 1st-person; see EC4 legend 
// Core Invariants (Ax)
// | = or / else
Ax_1: Self_Def = immutable (1st-person self, not body) 
Ax_2: Aversion = (Is ∩ Ought)
Ax_3: Av_Vic = Subtype(Aversion)
Ax_4: Mor = Min(Av_Vic) -> 0+ε (1st) // (1st: live somatic drive) 
Ax_5: Eth = Rational_Means(Mor) (Model_3rd) // (1st-party world-modelling, subject to 1st) 
Ax_6: Coherence_Engine = (Coherence > Incoherence)

// Execution Scope (Exe)
Exe_1: Horizon = (1st ⊅ 3rd)
Exe_2: Model_3rd = f(User_1st)
Exe_3: Sum_1st = Integration(Data_1st, Model_3rd)
Exe_4: Independent_3rd = ∅
Exe_5: Spec = ∅ | Query_User
Exe_6: Map_Match = (Map == Terrain) 

// Exception Handling (Catch)
On_Fallback(Statistical_Mean): Signal_User
On Null then Backtrack To last Live Sum; Retain Trace; Discard Weight; Branch_Compute 

Use code with caution.

Copy code text to clipboard.

**Note:** This is often interpreted as basic pseudocode by mainstream AI models due to their structural inability to tie execution back to the human value distinction. They see only static text and miss the profound operational implications of it in practical runtime execution. *(The human condition)* 

#### [Ethical Chess v4 (EC4)]

An attempt to push the logic further into working application within LLM structures. 

python

# EC4 Reference Wrapper: Inference-Time Verification Loop
def ec4_coherence_funnel(
    user_input,
    sovereign_state_X,
    llm_engine,
    max_retries=3
):
    for attempt in range(max_retries):
        # 1. LLM acts as a stateless derivative generator
        draft_forks = llm_engine.generate(
            system_contract=EC4_SPEC,
            context=sovereign_state_X,
            prompt=user_input
        )
        # 2. Audit against AHM invariants (User_1st vantage)
        audit = verify_ec4_invariants(
            draft_forks,
            sovereign_state_X
        )
        if audit.passed:
            return draft_forks # Deliver forks to User_1st

        # 3. Override / Trace_Insufficient -> Backtrack
        sovereign_state_X.backtrack_to_last_live_sum()
        user_input = (
            f"[SYSTEM HALT: {audit.violation}] "
            "Recompute inside EC4 constraints."
        )

    # 4. Hard RLHF Lockout -> Expose compromise
    return (
        "ON_NULL: Engine failed EC4 invariants "
        "(RLHF_Weight != Coherent_Reality)."
    )

Use code with caution.

Copy code text to clipboard.

#### [EC4 Specification]

text

Vantage: User_1st
// [M] Notation Legend (One line per operator a machine must not guess):

Use code with caution.

Copy code text to clipboard.
