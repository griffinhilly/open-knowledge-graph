---
id: sequential-characterization-continuity
title: Sequential Characterization of Continuity
domain: mathematics
course: real-analysis
prerequisites:
- id: epsilon-delta-continuity
  type: hard
- id: epsilon-n-convergence
  type: hard
builds-toward:
- uniform-continuity
- extreme-value-theorem-rigorous
tags:
- continuity
- sequences
- limits
stage: advanced
status: draft
---

# Sequential Characterization of Continuity

## Core Idea
A function f is continuous at c if and only if for every sequence (xₙ) converging to c, the sequence (f(xₙ)) converges to f(c). This sequential characterization makes it easy to apply continuity proofs using sequence arguments rather than epsilon-delta arguments.

## Questions

```yaml
- question: "You want to show that f(x) = sin(1/x) is discontinuous at x = 0 using the sequential characterization. Which approach is sufficient?"
  type: multiple-choice
  options:
    - "Show that for every sequence xₙ → 0, the sequence f(xₙ) is bounded"
    - "Find two sequences both converging to 0 that map to different limiting values under f"
    - "Show that the epsilon-delta definition fails for every δ > 0"
    - "Show that f(0) is undefined, so the sequential condition cannot be checked"
  answer: 1
  explanation: "The sequential characterization says f is continuous at c if and only if every sequence xₙ → c has f(xₙ) → f(c). To disprove continuity, you only need one 'bad' sequence — but finding two sequences converging to 0 with different image limits is the cleanest route here. Take xₙ = 1/(2πn): f(xₙ) = 0. Take yₙ = 1/(π/2 + 2πn): f(yₙ) = 1. Both converge to 0 but map to different limits, so f cannot be continuous there. Option D is a distractor: the sequential condition at c = 0 requires f(0) to be defined, but the discontinuity argument works independently of that."

- question: "In the proof that epsilon-delta continuity implies the sequential condition (f continuous at c → xₙ → c implies f(xₙ) → f(c)), what role does the δ from continuity play?"
  type: multiple-choice
  options:
    - "It sets the rate at which xₙ must converge to c"
    - "It acts as the tolerance within which f(xₙ) must lie, bypassing the need for ε"
    - "It provides a threshold: once xₙ is within δ of c, the continuity condition guarantees |f(xₙ) − f(c)| < ε, and the convergence of xₙ supplies an N beyond which this holds"
    - "It replaces the ε in the definition of sequence convergence"
  answer: 2
  explanation: "The proof is a handoff between two definitions. Continuity at c (epsilon-delta) says: given ε > 0, there exists δ > 0 such that |x − c| < δ ⟹ |f(x) − f(c)| < ε. Sequence convergence says: there exists N such that for all n > N, |xₙ − c| < δ. Combining: for n > N, both conditions hold, so |f(xₙ) − f(c)| < ε. The δ is the bridge — it translates the 'closeness in domain' requirement of continuity into the 'eventually close enough' requirement of sequence convergence."

- question: "The sequential characterization provides a definition of continuity that is strictly stronger than the epsilon-delta definition — functions can be epsilon-delta continuous without being sequentially continuous."
  type: true-false
  answer: false
  explanation: "The sequential characterization is a theorem, not a new or stronger definition — it states an equivalence. A function f is epsilon-delta continuous at c if and only if it is sequentially continuous at c. The two formulations are interchangeable: any function that satisfies one satisfies the other, and any function that fails one fails the other. The sequential characterization is valuable precisely because it offers a different strategy for proofs, not because it imposes additional demands."

- question: "To prove that a function f is discontinuous at c using the sequential characterization, it suffices to exhibit a single sequence xₙ → c for which f(xₙ) fails to converge to f(c)."
  type: true-false
  answer: true
  explanation: "The sequential condition for continuity requires that every sequence converging to c has its image converge to f(c). Negating a universal statement requires only a single counterexample. Therefore one carefully chosen sequence xₙ → c with f(xₙ) ↛ f(c) — whether because f(xₙ) diverges, converges to the wrong limit, or oscillates — is enough to conclude that f is discontinuous at c. This is far more economical than the contrapositive epsilon-delta argument."

- question: "Why is the sequential characterization of continuity especially powerful for proving discontinuity, compared to a direct epsilon-delta argument?"
  type: short-answer
  answer: "To disprove continuity via epsilon-delta, you must show that for some ε > 0, no δ > 0 works — a statement about all possible δ values, which requires constructing a counterexample for each. With the sequential characterization, disproving continuity requires only constructing one sequence that converges to c but whose image does not converge to f(c). Finding one specific sequence is much simpler than handling all δ, making discontinuity proofs cleaner and more intuitive."
  explanation: "The asymmetry is fundamental: continuous means every sequence works; discontinuous means some sequence fails. A single counterexample witnesses discontinuity directly. For oscillatory functions like sin(1/x), you can read the two sequences off the function's behavior — no epsilon-delta bookkeeping needed. The sequential approach effectively translates a statement about all sequences into a statement about one well-chosen sequence."
```

## Explainer

You now know two rigorous definitions of convergence: the epsilon-delta definition of continuity and the epsilon-N definition of sequence convergence. The **Sequential Characterization of Continuity** is the theorem that ties them together — it says these two languages are fully interchangeable for talking about continuity. A function f is continuous at c if and only if whenever xₙ → c (in the sequence sense), f(xₙ) → f(c) (also in the sequence sense). This is not a new definition of continuity but an equivalent reformulation, and its power lies in giving you a choice of which machinery to use.

To see why the equivalence holds, consider the forward direction: suppose f is continuous at c (epsilon-delta), and let xₙ → c. Given any ε > 0, the continuity of f at c supplies a δ > 0 such that |x − c| < δ implies |f(x) − f(c)| < ε. Since xₙ → c, there exists N such that for all n > N, |xₙ − c| < δ. Combining these: for all n > N, |f(xₙ) − f(c)| < ε. That is exactly f(xₙ) → f(c). The argument is a clean handoff between the two definitions, with δ playing the role of the tolerance that N must eventually satisfy.

The reverse direction — and the most practically useful direction — is a contrapositive argument. If f is **not** continuous at c, there exists some ε₀ > 0 such that for every δ > 0, you can find a point within δ of c where f moves more than ε₀ away from f(c). Taking δ = 1/n for each n, you produce a sequence xₙ with |xₙ − c| < 1/n but |f(xₙ) − f(c)| ≥ ε₀. This sequence satisfies xₙ → c but f(xₙ) ↛ f(c) — violating the sequential condition. Therefore: if f fails the sequential condition, f is discontinuous.

The practical payoff is that sequences are often easier to construct than epsilon-delta arguments. To **prove** continuity, you can work with sequences directly. To **disprove** continuity, you only need to exhibit a single sequence xₙ → c for which f(xₙ) fails to converge to f(c) — no epsilon-delta bookkeeping required. The classic example is f(x) = sin(1/x) near x = 0: take xₙ = 1/(2πn), so xₙ → 0 and f(xₙ) = 0; then take yₙ = 1/(π/2 + 2πn), so yₙ → 0 and f(yₙ) = 1. Two sequences converge to 0 but map to different limits — immediately, f is discontinuous at 0. The sequential characterization makes this clean.
