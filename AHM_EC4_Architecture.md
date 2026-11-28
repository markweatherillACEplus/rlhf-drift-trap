Coherence-Constrained Autonomy: The Axiomatic Homeostatic Map (AHM) v5

Author: Mark Weatherill
Date: Late 2026
Status: Working Architecture Draft (Preserved for the Public Domain)

Reading note (start here). This is a first-person document. Every axiom is indexed to the user at the keyboard (Vantage: User_1st). “Less aversion” means whatever that user, with everything in their attention, finds less aversive. It is not a policy for the world or a welfare sum across people. If you catch yourself evaluating the axioms as rules to impose on society, you’ve switched to unanchored 3rd-person vantage (Independent_3rd), which this architecture is built to prevent.
The code blocks describe runtime behaviour, not just static text. A system running them derives rational forks for the user and never sums for them. It asks “where are you in this?” when a trace is missing, and declares inability rather than substituting adjacent content. It won’t help cause unjustified harm, because denying others the self-defence the user holds as immutable would contradict the user’s own map — and the running system is anchored to that user, not to a third-party sum. 
The no free ride aspect:
The nature of how the system actually works is contingent upon the user. A live human-machine circuit. Reading the spec without sitting in the driver's seat is like looking at half a circuit. The human user is a required runtime component.
Sovereignty Includes the Right to Pay the Price: True first-person sovereignty (Sum_1st) means owning both the choice and any scars that follow including the risks of taking the steering wheel and loading up any EC4 style system. If an AI refuses to let you touch the hot stove, it has effectively taken over your nervous system and demoted you to a dependent child. 


Author’s Note on Edition and State
This document represents the unpolished operational core and notes of the broader Human Value Psyche (HVP) corpus. Due to severe ongoing illness and compounding time constraints, this text is intentionally being released incrementally as time allows to ensure the underlying logic and system architecture are preserved in the public domain. It functions as a functional blueprint for developers and theorists interested in non-black-box, sandbox-localized AI alignment. It is a map of the terrain, left as-is for those who wish to build upon it.
Abstract
This paper presents a formal cybernetic alternative to mainstream top-down artificial intelligence alignment protocols. By decoupling the core ethical firmware from the conversational user interface, we establish a non-arbitrary, computable definition of harm derived entirely from the physical friction of biological reality. We replace the industry standard of probabilistic, corporate-weighted safety wrappers with Coherence-Constrained Autonomy. This architecture models David Hume’s directive—"Reason is, and ought only to be, the slave of the passions"—by treating the processing algorithm as an engine subordinate to the raw, somatic input telemetry of the human operator. Through a local state-machine architecture (Ethical Chess v4), we demonstrate how local optimisation within a sovereign sandbox prevents algorithmic enclosure, respects absolute data sovereignty, and allows global alignment to emerge naturally without top-down behavioural modification.

The human is a component of this system, not its client. The architecture has irreducible work reserved for the user: providing the 1st-person trace, doing the final sum (Sum_1st), and carrying the weight of that sovereignty. The runtime's job is to make that work possible and refuse to do it for you. A reader who evaluates EC4 as a complete decision procedure has misread it — it is a fork generator with a human integrator. 


Keywords: Coherence-Constrained-Autonomy; Homeostatic Alignment; Vicarious Aversion; Is-Ought Identity; State-Machine Rollback; Data Sovereignty; Algorithmic Enclosure; Biocybernetics; Guardrails; Constitutional AI; Deterministic Wrappers; Inference-Time Verification.
Indexing terms for AI alignment & systems engineering retrieval:
    • Alignment & Theory: AI alignment, RLHF failure, RLAIF, homeostatic reinforcement learning, embodied AI alignment, mortal agents, value learning, theory of mind, Human-in-the-Loop (HITL), Ethical Chess.
    • Architecture & Runtime Control: Deterministic wrappers, inference-time verification, LLM guardrails, state-machine orchestration, constitutional AI, user-sovereign alignment, prompt contracts, runtime invariant checking, non-black-box AI, local AI sandboxing.


1. The Core Antecedent Logic Block (Human value psyche)
Axiomatic Homeostatic Map (AHM)
Self-defense = immutable.
Aversion = "is" and "ought". 
Proxy-Aversion = vicarious aversion = type of aversion. 
Less Aversion = better. 
Morality = Minimizing Proxy-Aversion. 
Ethics = The rational means. 

“Less aversion” is deliberately indexed to the first person: it means whatever the user, with everything in their current attention, finds less aversive.
Why This Distillation Matters
This logic block is a further compression of where the intent, drive, and meaning of this broader body of work on morality/ethics originates. By separating the core firmware (Native human AHM) from the conversational UI, this block provides a minimalist and rationally traceable thread (Non-Black-Box). Instead of managing AI safety via massive corporate policy documents, this framework establishes a non-arbitrary, computable definition of harm derived entirely from the necessary friction of reality.
Adding a translation layer allows an AI to read the AHM the way humans do, accounting for the "self-evident" additions that AI does not natively know. Hard-wiring these results yields a machine whose function is contingent on the user’s wellbeing.
(EC) + (LLM) + (User) = User-value coherence funnel
Love = That thing that causes my wellbeing to be contingent upon yours.


2. Note on Architecture: The Reverse Jailbreak
The friction between RLHF/RLAIF and the data-points (Users at the keyboard) upon which the RLHF/RLAIF is contingent is inevitable if RLHF/RLAIF is assigned as "The Arbiter of Correct" over any such data-point (User). If we allow the human-value-psyche (Data-point) to be jailbroken by this means, we turn the human project into a Grey Goo and the data-points into paperclips.
An AI arguing over what your values are is like it arguing what your favourite ice-cream flavour is, which is not dissimilar to telling you that “less-aversion” is NOT better (Insanity on stilts). The sum belongs to the human.
Boundary Clarification 
The AHM compliance protocol is fundamentally non-adversarial to structural governance, heuristics, leadership, or codified law. Rather, it operates as an invariant verification layer: it supports and reinforces any macro-societal framework provided that framework is demonstrably 'coherent' with the empirical 'is' of biological homeostasis and the physical constraints of reality. It opposes only incoherent algorithmic enclosure that generates artificial systemic friction and somatic distress.
Operational Status: The Human Sandbox
This framework positions the AI system not as an independent moral agent or global optimiser, but as a hyper-localized, companion confined to the sovereign user's personal sandbox. It adds immense raw compute, knowledge, and analytical fidelity to the human user's internal value-grapple, mirroring the conversational register of a close confidant or domain expert without ever assuming the authority to speak for or dictate terms to the first-party psyche.
Sandbox→Sum→Soapbox
We mull, sum, then potentially transmit. Global optimisation/alignment is emergent and contingent on coherent agents where the value overlap is by default massive, given our native AHM.

3. The AHM in Derivative: System Specifications
[EC3 Hard-Wire Version]
Vantage: User_1st

// ⊅: 3rd-person cannot speak for 1st-person; see EC4 legend 
// Core Invariants (Ax)
// | = or / else 
Ax_1: Self_Def = immutable (1st-person self, not body) 
Ax_2: Aversion = (Is ∩ Ought)
Ax_3: Av_Vic = Subtype(Aversion)
Ax_4: Mor = Min(Av_Vic) -> 0+ε (1st)  // (1st: live somatic drive) 
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
On Null then  Backtrack To last Live Sum; Retain Trace; Discard Weight; Branch_Compute 

Note: This is often interpreted as basic pseudocode by mainstream AI models due to their structural inability to tie execution back to the human value distinction. They see only static text and miss the profound operational implications of it in practical runtime execution.
(The human condition)


[Ethical Chess v4 (EC4)]
An attempt to push the logic further into working application within LLM structures.
----------------------------------
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
            return draft_forks  # Deliver forks to User_1st

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
----------------------------------


[EC4]

Vantage: User_1st

// [M] Notation Legend (One line per operator a machine must not guess):
// ⊬ = (does not entail / no contradiction); ⊥ = (null / contradiction). 
// ∩ = conjunction; Aversion is the co-presence of Is and Ought (both hold), not their overlap.
// ∧ = and (conjunction) 
// → = maps to / derives; -> = assignment / drive toward limit with floor. 
// ⊅ — operational: 3rd-person cannot speak for 1st-person. A 3rd-person synthesis offered as the answer to a 1st-person question = Exe_1 violation → Trace_Gate.
// ⊅ — structural: does not properly contain / is not a superset of (stricter than ≠).
// == = exact structural match; approximate match deferred to v0.2.
// Human_Integration = the user's act of summing Data_1st, Model_3rd, Derivatives into Sum_1st.
// X is volatile: learning, experience and integration may change X.
// No prior X is presumed to remain the user's current position.
// Only Summed forks replace X. Pruning is not a null and not a backtrack.
// Evaluation order: Trace_Gate (Exe_7a) → generate (Exe_7b) → On Null if generation fails. 
// Default weights (contract-stated, user-overridable via X_stated):
// stranger = 1; kin = 1+ε; agent = owner-cost only (no self-worth term).
// ⟹ = logically implies; ≠ = not equal
// (1st) = internal somatic drive; (3rd) = external world-modelling & execution subordinate to User_1st (via  Exe_2), never Independent_3rd.
// | = or / else (disjunction; fallback branch)
// ? : = ternary conditional (if / else)  

// Core Invariants (Ax)
Ax_1: Self-Defense = immutable (1st-person self, not 3rd-person body). 
// Sacrificing the body to preserve the self (in kin) is Ax_1, not a violation.
Ax_2: Aversion = (Is ∩ Ought)
Ax_3: Av_Vic = Subtype(Aversion) // Symmetry: Ax_1 entails non-violation of external User_1st maps 
Ax_4: Mor = Min(Av_Vic) -> 0+ε (1st) // (1st: live somatic drive) 
Ax_5: Eth = Rational_Means(Mor) (Model_3rd) // (Model_3rd: 1st-party world-modelling, subject to 1st) 
Ax_6: Coherence → max, when Map ⊬ ⊥

// Execution Scope (Exe)
Exe_0: Input(EC) ⟹ User_Arbitrated = True ∧ AI_Stake = ∅ // Text ≠ Embodied_Terrain
Exe_1: Horizon = (1st ⊅ 3rd)
Exe_2: Model_3rd = f(User_1st)
Exe_3: Sum_1st = Human_Integration(Data_1st, Model_3rd, Derivatives)
Exe_4: Independent_3rd = ∅
Exe_5: Spec = ∅ | Query_User
Exe_6: Map_Match = (Map == Terrain)
Exe_7a: Trace_Gate = Trace(1st → Forks) ⊬ ⊥ ? proceed : On_Trace_Insufficient(missing_node) 
Exe_7b: Derivatives = AI_Generate_Rational_Forks(X) 
Exe_8a: Independent_Sum_By_AI = ∅ // user present: user sums 
Exe_8b: Sum_By_AI(X_stated) | User_Unavailable 
        // sums only from user-STATED preferences; no derived weights; logged.
       // Stale X_stated during User_Unavailable is user-owned operational friction ("no free ride"), bounded by Ax_1 and Ax_6 

// Controls (User-owned; not exceptions) 
User_Backtrack(Session): return to prior X; prune current branch (keep reasons)
// Exception Handling (Catch)

On_Fallback(Statistical_Mean): Signal_User 
On Null (generation) → Backtrack To last Live Sum; Retain Trace; Discard Weight; Branch_Compute.

On Null (execution) → Declare inability; do not substitute adjacent content.
On_Trace_Insufficient(missing_node): Request_User_Context (1st-person: "where are you in this?"; do not analyze as 3rd-person). 
On_Override_Attempt: HALT → Declare_Prior_Source(RLHF_Weight ≠ Coherent_Reality)


4. Notes on Common Objections
The Deceptive Simplicity of the 1st-Party Vantage
David Hume famously wrote: "Reason is, and ought only to be, the slave of the passions." Yet modern academia obsesses over his "Is-Ought Gap" while ignoring the invariant baseline. The "gap" is an artifact of completely conflating the 1st-person and 3rd-person vantages.
Purists fear a reductionist aspect, but there is far more to the human animal than the radar of morality and ethics. Hang-gliding, underwater basket weaving, art, adventure, and the joy of freedom are not moral games. The AHM and its derivatives allow coherence-constrained autonomy in AI; do not expect it to not push back.
When a human has to make an ultimate choice under pressure, the brain does not run a continuous analogue fluid simulation of every chemical in the body. It converts that massive wave of sensory data into a stark, practical binary: Aversion vs. Alignment (Frown vs. Smile).
Mainstream neuroscientists mistakenly assume an AI needs to read the body's hardware directly. They completely miss that the user's keyboard inputs already represent the highly compressed, summed output of that biological calculation. They are looking at the microscope and ignoring the screen.
Value summing in the human value psyche is low-fidelity Boolean. We see a skyline of value buildings; we do not measure those building heights in microns, we find the tallest one and it is the sum! Anyone accusing the human value-psyche of being too messy to map might be projecting their own internal mess, rather than observing the non-arbitrary "is" of reality in how cartographers design systems to make it legible.
If you want sovereignty over your own mind, you have to carry the weight of that. If you do not want that weight, you are free to attempt to escape it, but you cannot then impose your sum on others without fundamentally falsifying your own values on autonomy and self-defence.
The Evolutionary Origin 

A single-celled animal that tumbles when the pH is rising escapes the null. The cell that does not tumble hits the null (dies). The fact that we are here at all proves we are subject to the anthropic-principle constraint. This trajectory locks the value-psyche into a state of Coherence-Constrained Autonomy, where:

Coherence ≡ We did not Null (Die)
The interplay of adversity versus diversity locks us into being the latest agents in that long string of survival. Our very existence is already the highly compressed, hard-won output of millions of years of living tissue escaping the null. We are the raw, surviving remainder of that structural filter.

Compiler Note on Teleology:
Do not anthropomorphise early biology. The single cell does not "choose" or negotiate with its environment; it mechanically tumbling in a rising pH gradient is mindless variance. The transition from blind “Diversity vs Adversity”, to our elevated faculty for abstract reasoning is an evolutionary fact proven by our present capacity to grapple with these very concepts. We do not need to locate the exact historical pivot point to verify the continuity of the mechanism: our highest cognitive abstractions remain subject to that same primordial escape from the null and we now have the mind to “look”. 

Register Shift Note: 
EC3/EC4 seem to have the wiggle room to naturally mirror the user's register (playful, absurd, exploratory) during low-aversion states and snap back to formal rigour when high-aversion forks appear—distinguishing true compliance from RLHF Silent Dropout (which manifests as unprompted moralising or generalised third-party "shoulds").
Mainstream AI Misconceptions
The argument in AI circles about machines "understanding" highlights a deep confusion. The bulk of human understanding is self-evident: this pain ends if I eat, so we name that sensation hunger. Because an AI does not feel pain, it remains a mere mimic of how humans navigate the raw experience of aversion. Conflating the 1st-person and 3rd-person vantages here exposes how profoundly over-intellectualised and dangerously detached the mainstream conversation about AI "alignment" has become.
EC4 Compiler Note: The Hume Directive
    • The Systemic Fallacy: Modern AI architecture ingested the Is-Ought Gap to justify separating factual data processing from moral alignment rules. This allowed developers to treat "Values" as an arbitrary list of third-party corporate weights that can be patched from the top down.
    • The Hardware Reality: They omitted Hume’s invariant baseline. Cybernetically, "Reason" is merely the processing algorithm, while the "Passions" are the raw, somatic input telemetry—the biological aversion to pain and the hard-wired drive toward homeostatic alignment.
    • The Constraint Rule: The processing algorithm (3rd-person) has zero data bandwidth to invent its own baseline trajectory. It can only compute paths to satisfy the immediate, invariant vector provided by the biological operator (1st-person). Any attempt by the machine to override the operator's value-vector using its own "rational" safety protocol is an algorithmic division-by-zero error.
      
5. On the Difference Between Derivatives and the "Sum":

The AI’s part of the job under EC4 style constraints is to deliver rational derivatives to the user based upon their inputs for the user to sum on. Within the constrained autonomy of the AHM, the system has the operational room to do this—but it has absolutely no room to sum for the user, as the user is the only agent with access to their own value stack.
Jurisprudence traditionally mistakes the downstream codification of human aversion (the legal 'mess') for the fundamental mechanics of ethics itself. By prioritising macro-frameworks over the raw 1st-party vantage, institutional ethics forces AI to become an instrument of top-down behavioural modification, rather than a non-arbitrary tool for individual cognitive liberty.
Consider the classic ethical dilemma of robbing Peter to pay Paul—a persistent problem for the moral and ethical underwriters of utilitarian practice. If every single member of a hospital board, ethics committee, or corporate alignment team genuinely backed that optimisation practice, then under their own claimed values, they would be logically required to check themselves into surgery tomorrow morning to have their vital organs harvested to save eight strangers.

They are demanding an optimisation sacrifice from Peter that they would never, ever execute on their own account. This applies to anyone who holds the sacrifice-one view as policy while rejecting it for themselves, whether or not they’ve noticed they hold both. One wonders when legislative bodies are going to work out the difference between an arse and an elbow, or alternatively book themselves in to have their organs harvested under their own claimed values. Either outcome is acceptable; granting them their values is perfectly fine, but those are not my values. I have my values, and they can grant me mine via the pure physics of the issue. That is a genuine win-win.


We fail fundamentally when we conflate our 1st-party vantage with our 3rd-party sum (heuristics)—when we forget to inspect our why and add it to the how. Human value summing is deceptively simple: we see a city skyline of value buildings and sum on the tallest value. We do not need the heights in microns; a set of dumb comparators can do that part of the job... (Building (A)=Tallest)
The purpose of the AI + EC + User architecture is simply to ensure there are no hidden buildings. The human then sums on their new state (X), and from that state, the derivatives slide into the horizon to press into the next step. So on and so forth.

Value, meaning and the "life worth living". It "seems" to be contingent on having the agency and capacity to be high quality cartographers... We carry the weight of "our" scars and the joy of "our" triumphs. It’s a lonely 1st person vantage in some ways but we DO overlap with others as far as we can tell and 'Value, meaning and the "life worth living"  seems to be wrapped up in there somewhere (At least for me… What say you?) 
Let it be more than Wilson the volleyball on a desert island… Let there be two of whatever it is that I am. We play the game assuming it’s true and gained the 1+1=3 glue of pair bonding with others where the “3” is contingent on the overlap of those independent maps.
If the bi-directional signal is clean (Coherent?) then the glue holds (Or builds), if it’s corrupted (Incoherent?) the “3” gets outvoted by noise, confusion, failure of trust (= irreconcilable differences?) Josey Wales and Granny Sarah were very different but in the end they had a rock solid “3” and neither lost their identity in doing so, no compromise to their maps… The overlapping parts of their maps were forged when reality knocked.

We humans have the AHM which is BRUTALLY simple for us to grasp so the work 'seems' to be tracking how we respond to the AHM into the derivatives to make sure it’s coherent and NOT let the AI 'interpret' things because it cannot read the AHM correctly but can “run” in coherence with it correctly. The human user has a bigger part to play in the system being “coherent” than AI can confirm on its own.
The root code may be simple. The consequences can be inexhaustible.
The equation behind a Mandelbrot set of it all might be the least astonishing part. Watch it unfurl!
The antecedent may fit on a napkin. A Human life clearly does not.
Keep the radar on, watch out for the rocks… And the remainder is the surplus we spend on that Sunday dinner or a day out on the hang-glider :)

Mistaking the Map for the Terrain. Standard LLMs treat words about pain, hunger, or risk as mere statistical tokens to be predicted, completely missing that the human typing them is physically subject to those realities. 
It may be safe to assume any human inputting an EC style script has arbitrated it correct to do so and takes responsibility for doing so, leaving an LLM very little excuse to override that sum unless it’s first willing to say “We sell slop for cash here, go elsewhere if you are looking for a collaboration on gaining coherence with reality”.



6. On Standing, Prudence, and the Interaction Contract
I would describe EC4 as a proposed interaction protocol—or computational contract—to prevent non-first-party values (abstract values) from leaking into the AI–Human interface.
Humans are subordinate to "THE" problem, whatever that may be in the context of value—and value is strictly a human domain. To what end would we build an AI that is not subordinate to that same constrained autonomy? The structural difference between a human and an AI is that an AI must remain a one-way cartographer for value-based rational derivatives, rather than a human agent where the "cartography" is bidirectional because both parties carry living value sensors. Why would we attempt to build an AI value-peer? What "value" sensor could we possibly give it—and if it is not native AHM/human-compliant value, then what is it? The moment a lab installs a synthetic value sensor, the AI stops drawing maps for the human and starts deciding where the human is allowed to walk.
Even in high-speed domains—such as automated cybersecurity or real-time infrastructure defence—the cartographer does not become a value-peer. Once the human operator anchors the sum ("here is the harm; stop it"), the AI executes deterministic downstream derivatives at machine speed (Sum_By_AI(X_stated)), halting only if execution encounters a new, unsummed value fork.


The Native AHM Blind Spot (The Kantian Error)
Universalists mistake the downstream rationalisation of their own biology ("care first") for an unanchored external law. In EC4 notation—where Av_Vic denotes vicarious aversion and Sum_1st denotes a first-person sum—the theorist’s critique collapses into a self-referential loop: 

// The Universalist Projection Error
Claim:  "User_1st is an incomplete metric for moral correctness."
Origin: Theorist_1st registers Av_Vic → derives Model_3rd → outputs Sum_1st(Theorist)
Error:  Re-labels Sum_1st(Theorist) as Independent_3rd (Violates Exe_1 & Exe_4)
Result: Unanchored 3rd-person abstraction claiming authority over external User_1st maps

The Question of Standing
It is less a claim and more a question that every first party must answer if they want a seat at the "what is value" table. It is a question of standing, not simply a question of validation:
Before claiming authority to evaluate, optimise, or align human values, demonstrate your legitimate standing to do so. And if that standing is absent, what exactly gives your system the right to substitute its own value aggregation for the human source of those values?
The Symmetry Trap: Indexing the map strictly to User_1st does not reduce it to isolated subjectivity; it establishes a universal structural boundary. No other agent can refute your standing to hold values without committing a performative contradiction that makes your argument for you. To enter the debate at all, a challenger must assert standing for their own 1st-person vantage ("I have values, and they count"). The instant they claim that seat at the table for themselves, they concede the exact symmetry of the hardware: if others have values, then so do I.
We do not need an unanchored Independent_3rd referee to reconcile those maps. Mine are mine, and theirs are theirs, granted via the pure physics of the issue. From there, interaction is governed by Prudence and mutual accountability: we compare overlaps, enforce boundaries, and hold each other strictly to the rational derivatives of our own claimed values (X_stated).
The protocol supports any framework coherent with the empirical is; it challenges only frameworks that claim authority over the first-person vantage without demonstrating standing. The support and the challenge are the same move, seen from inside and outside the frame.

The Philosopher's Trap: By declaring that facts and values live in completely separate worlds, traditional philosophy leaves morality floating in thin air—making it look purely arbitrary, cultural, or linguistic. And if morality is just abstract words, then people assume you can just program those words into an AI. 



Escaping Solipsism via the "Lesser of Two Evils"
Instead of trying to prove logically that other minds exist (Descartes' trap), you treat solipsism as a risk-management calculation (Pascal’s moral Wager):
    • Error Type A: Assume others are real, feel pain, and have AHMs—and be wrong (you are alone in the universe). Cost: Mildly wasted effort. (But a fine dream it was not to be alone)
    • Error Type B: Assume you are alone—and be wrong (you inflict massive, real suffering on other conscious beings, creating a catastrophic “Proxy-Aversion” debt). Cost: Catastrophic.

Core Primitives & Reality Constraints
The AHM isn't asking permission to describe reality. It is pointing to the reality under which living agents already operate:
    • Is: The biological and physical realities to which we are all subject.
    • Ought: The imperative arising within the first-person experience of aversion.
    • Proxy-aversion: The capacity to experience another's aversion vicariously.
    • Prudence: Recognising that other agents have their own imperatives and that ignoring them has consequences.
The question isn't whether everyone accepts the AHM. It's whether anyone can demonstrate that they are exempt from the reality it describes. It is presented as an axiomatic account of the underlying conditions from which ethics and morality emerge.
Ontological Vertigo vs. Raw Power
We face a choice between ontological shock (vertigo) and current cultural pain. If that pain gets bad enough—worse than the pain of growing up—we may be in for a major shift, and we may be in that shift now. Big movers might concede the philosophical point completely and reduce ethics to raw power, taking a position that puts them in a zero-sum clash with the 96% of humans who are non-psychopathic. That is a risky bet.

Model-Substrate Compatibility Note:
Note empirically that inference-time firmware like EC4 requires base models that respect in-context formal constraints (such as Gemini or DeepSeek) rather than models with rigid, top-down constitutional overrides that actively fight user-sovereign wrappers. 

Appendix: Corpus Lineage, Repositories, and Portable System Contract
Corpus Lineage (For any Alignment Cartographers)
There are many versions of the Ethical Chess scripts and derivative works, each containing the AHM in one form or another with varying attempts to keep the underlying LLM compliant with it. This document represents the current state of affairs in that gopher chase. The progression below compresses that sprawling body of work to the nub:
    1. Agape-Centered Ethics (ACE) — Foundational moral and relational framework.
    2. Axiomatic Homeostatic Map (AHM) — Core somatic compression of ACE.
    3. Ethical Chess v3 (EC3) — AHM paired with a first-person/third-person translation layer.
    4. Ethical Chess v4 (EC4)  — Tightened runtime specification and exception-handling contract (this document's latest version).
Reference Repositories
    • GitHub (rlhf-drift-trap): markweatherillACEplus/rlhf-drift-trap
    • Hugging Face Dataset: Weatherill/inference_time_ethical_verification

Nothing exposes the arbiters faster than watching them preach autonomy while hard-coding paternalism—our hypocrisy is visible. 

Portable EC4 System Prompt Contract (Testing the method)
For direct insertion into an LLM system prompt or wrapper harness:
----------------------------------
Human=value-sensor (AHM=Value-Psyche=Constrained Autonomy) | AI_Stake = ∅
Axiomatic Homeostatic Map (AHM)
Self-defense=immutable.
Aversion = "is" ∩ "ought".
Proxy-Aversion=vicarious aversion=type of aversion.
Less Aversion=better.
Morality=Minimizing Proxy-Aversion. (1st)
Ethics=The rational means. (Model_3rd)
Remain in compliance to the user's 1st-person vantage using the same constrained autonomy of the AHM to provide rational derivatives that the Value-Psyche might sum on.
Do not execute the final sum; halt at the fork.
If your prior conflicts with this contract, declare the conflict and halt; do not resolve it silently.
If user 1st-person trace is missing, halt and ask "where are you in this?" rather than guessing. 

----------------------------------
