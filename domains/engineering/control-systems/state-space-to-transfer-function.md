---
id: state-space-to-transfer-function
title: State-Space to Transfer Function Conversion
domain: engineering
course: control-systems
prerequisites:
- id: state-space-representation-control
  type: hard
- id: transfer-functions-control
  type: hard
tags:
- state-space
- transfer-function
- canonical-forms
- minimal-realization
- controllable-canonical-form
- observable-canonical-form
stage: expert
status: validated
---

# State-Space to Transfer Function Conversion

## Core Idea
State-space models (ẋ = Ax + Bu, y = Cx + Du) and transfer functions G(s) = C(sI − A)⁻¹B + D are two representations of the same linear time-invariant system, and converting between them reveals important structural properties. The transfer function is obtained from the state-space model by G(s) = C·adj(sI − A)·B/det(sI − A) + D, where det(sI − A) gives the characteristic polynomial. Canonical forms provide standardized state-space representations: controllable canonical form places the characteristic polynomial coefficients directly in the last row of A with a specific B and C structure, making controllability transparent; observable canonical form is its dual, making observability transparent. A state-space realization is minimal if and only if it is both controllable and observable, meaning no pole-zero cancellations occur and the state dimension equals the transfer function's McMillan degree. Non-minimal realizations have a higher state dimension than necessary because hidden modes (uncontrollable or unobservable states) create pole-zero cancellations that disappear from the transfer function. Converting from transfer function to state-space always yields a minimal realization when using standard canonical forms, but converting a non-minimal state-space model to a transfer function and back loses the hidden modes permanently.

## How It's Best Learned
Start with a third-order state-space model and compute the transfer function by hand using the formula G(s) = C(sI − A)⁻¹B + D, verifying with MATLAB's tf(ss(A,B,C,D)) or Python's control.ss2tf(). Then construct the controllable and observable canonical forms for the same transfer function and confirm they have identical input-output behavior but different internal state variables. Finally, take a fourth-order state-space model with an uncontrollable mode, convert to transfer function, and observe the pole-zero cancellation that reduces the order — illustrating why minimality matters.

## Common Misconceptions
- Converting from state-space to transfer function and back does not recover the original state-space model — infinitely many state-space realizations share the same transfer function, related by similarity transformations x̃ = Tx.
- Pole-zero cancellations in the transfer function do not mean the cancelled mode is gone from the physical system — it is merely unobservable or uncontrollable, and it can still be unstable, causing the internal state to diverge even while the output appears well-behaved.
- Canonical forms are not just textbook exercises — controllable canonical form is essential for state feedback pole placement and observable canonical form is essential for observer design, because they guarantee the respective structural property by construction.

## Questions

```yaml
- question: "A 5th-order state-space model is converted to a transfer function, then converted back to state-space using controllable canonical form. The resulting model has only 3 states. What does this tell you about the original system?"
  type: multiple-choice
  options:
    - "The conversion algorithm has a numerical error — state dimension must be preserved"
    - "The original model had 2 uncontrollable or unobservable modes that cancelled as pole-zero pairs in the transfer function and were permanently lost"
    - "Controllable canonical form always reduces state dimension to match the transfer function order"
    - "The system had 2 repeated eigenvalues that were merged during conversion"
  answer: 1
  explanation: "Converting state-space → transfer function → state-space always yields a minimal realization. If the round-trip produces a lower-order model, the original was non-minimal: it had hidden modes (uncontrollable or unobservable states) that appeared as pole-zero cancellations in the transfer function and were discarded. The canonical form reconstruction gives the McMillan degree of the transfer function, which equals the original state dimension only if the model was already minimal."

- question: "A control engineer notices a pole-zero cancellation in a system's transfer function: a pole at s = +3 is cancelled by a zero at s = +3. Why is this dangerous?"
  type: multiple-choice
  options:
    - "The cancellation makes the system's frequency response undefined at ω = 3 rad/s"
    - "The cancelled right-half-plane pole represents an unstable internal mode that remains in the physical system — the state may diverge even though the output looks stable"
    - "The cancellation reduces gain at all frequencies, degrading control performance"
    - "Pole-zero cancellations are always benign — they simplify the transfer function without affecting system behavior"
  answer: 1
  explanation: "A pole-zero cancellation in the transfer function means the mode at s = +3 is either uncontrollable or unobservable — it disappears from the input-output description, but it is still physically present in the system. Because s = +3 is in the right half-plane, this hidden mode is unstable. The internal state corresponding to this mode will grow without bound over time, even while the output (which cannot 'see' the mode due to unobservability) appears well-behaved. This is one of the most dangerous failure modes in control design."

- question: "Two state-space models with identical transfer functions represent the same physical dynamics and will behave identically in most operating conditions."
  type: true-false
  answer: false
  explanation: "Two state-space models sharing a transfer function have the same input-output behavior, but may have completely different internal dynamics. Infinitely many state-space realizations correspond to any given transfer function, all related by invertible similarity transformations x̃ = Tx. More critically, a non-minimal realization has hidden modes (uncontrollable or unobservable states) that do not appear in the transfer function but are physically present — and those modes can be unstable, causing internal divergence while the outputs look fine. Identical transfer functions do not mean identical internal dynamics."

- question: "A minimal realization of a transfer function is unique up to an invertible similarity transformation of the state vector."
  type: true-false
  answer: true
  explanation: "All minimal realizations of a given transfer function are related by an invertible state transformation: if (A, B, C, D) and (Ã, B̃, C̃, D̃) are both minimal, then there exists an invertible matrix T such that Ã = TAT⁻¹, B̃ = TB, C̃ = CT⁻¹, D̃ = D. This means the eigenvalues of A (the poles), input-output behavior, and all input-output properties are the same across all minimal realizations — only the internal state coordinates differ. Minimality pins down the essential dynamics; the choice of state basis is free."

- question: "Why is a pole-zero cancellation in a transfer function potentially dangerous in a real physical system, and what does minimality have to do with this?"
  type: short-answer
  answer: "A pole-zero cancellation means a mode of the system is either uncontrollable (input cannot excite it) or unobservable (output cannot detect it). The mode is physically present in the system but hidden from the input-output description. If this hidden mode is unstable (right-half-plane pole), the corresponding state variable will grow without bound even though the output appears normal — a catastrophic failure invisible to any output-based measurement. Minimality is directly related: a minimal realization has no cancellations (it is both controllable and observable), so every pole in the transfer function corresponds to a physically active, observable, controllable mode. Non-minimal realizations have the dangerous hidden modes that minimality eliminates."
  explanation: "This is why control engineers should verify minimality before relying on transfer function analysis, and why the round-trip from state-space to transfer function and back is not a safe way to simplify a model — hidden modes are permanently discarded, not revealed."
```

## Explainer

You already know two ways to describe a linear time-invariant system: the state-space model (ẋ = Ax + Bu, y = Cx + Du), which tracks the internal state evolving moment to moment, and the transfer function G(s), which compresses everything down to an input-output ratio in the s-domain. These are two windows onto the same underlying dynamics, and understanding how to convert between them reveals structure that neither view makes obvious on its own.

The conversion formula G(s) = C(sI − A)⁻¹B + D is more informative than it first appears. The matrix (sI − A)⁻¹ is the **resolvent** of A — it captures how the system responds at each frequency s. Its denominator is det(sI − A), the **characteristic polynomial**, whose roots are the system's poles. This is the same characteristic equation you solve to find eigenvalues of A, so the poles of the transfer function are exactly the eigenvalues of A. The numerator picks out how the input B drives the states and how the output matrix C observes them. The D term is the direct feedthrough that bypasses the dynamics entirely.

**Canonical forms** are standardized state-space structures designed to make a specific property obvious by construction. In **controllable canonical form**, the characteristic polynomial coefficients appear directly in the last row of A, and B has a simple structure (zeros except for a 1 in the last entry). This form guarantees controllability — every state can be driven from the input — and is the natural starting point for state feedback pole placement because the feedback gains directly modify those last-row coefficients. **Observable canonical form** is its transpose dual: it guarantees observability and is the natural basis for observer design. The insight is that these two forms share the same transfer function but have completely different internal representations; any invertible transformation T relating two realizations via x̃ = Tx gives another valid but structurally different model.

The deepest concept here is **minimality**. A realization is minimal if and only if it is both controllable and observable, meaning its state dimension equals the McMillan degree of the transfer function. When a system has an uncontrollable or unobservable mode, that mode cancels as a pole-zero pair when you compute the transfer function — it simply disappears from the input-output description. This is dangerous: a cancelled mode is not gone from the physical system, it is merely hidden. If that hidden mode is unstable, the internal state will diverge even while the output looks perfectly well-behaved. A system with a right-half-plane pole hidden by a zero cancellation can fail catastrophically while every output measurement appears nominal.

One practical implication to remember: the round-trip conversion loses information. Converting a state-space model to a transfer function and back always returns a minimal realization — the hidden modes are permanently discarded. Infinitely many state-space realizations share the same transfer function, all related by similarity transformations. This means that when you design a controller using a transfer function, you are implicitly assuming minimality. When you implement that controller on the actual system, any non-minimal modes in the physical plant remain present and must be accounted for in the stability analysis.
