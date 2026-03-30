---
id: state-space-analysis-realization
title: State-Space Representation and Realization
domain: engineering
course: signals-and-systems
prerequisites:
- id: transfer-function-poles-zeros
  type: hard
tags:
- state-space
- system-representation
- control
stage: advanced
status: validated
---

# State-Space Representation and Realization

## Core Idea
State-space representation uses first-order differential (or difference) equations: ẋ = Ax + Bu, y = Cx + Du. This form generalizes to MIMO systems, handles initial conditions naturally, and is preferred for numerical simulation and control design. Realization converts transfer functions into canonical state-space forms (observable, controllable, diagonal).

## Questions

```yaml
- question: "Two state-space models (A₁, B₁, C₁, D) and (A₂, B₂, C₂, D) produce exactly the same transfer function, but A₁ ≠ A₂. Which statement is correct?"
  type: multiple-choice
  options:
    - "Both models are incorrect, since the transfer function uniquely determines the A matrix"
    - "The models represent physically different systems that happen to have the same input-output behavior"
    - "Both are valid realizations related by a similarity transformation T: A₂ = T⁻¹A₁T, B₂ = T⁻¹B₁, C₂ = C₁T"
    - "At least one must be uncontrollable or unobservable, because only minimal realizations match"
  answer: 2
  explanation: "State-space realization is non-unique: infinitely many (A, B, C, D) quadruples produce the same transfer function. Any invertible coordinate transformation T applied to the state vector yields a different A but identical input-output behavior. This is because the transfer function H(s) = C(sI−A)⁻¹B + D depends on the eigenvalues of A (the poles), not on the specific coordinate representation. The eigenvalues of A₁ and A₂ will be identical (they are the same poles), even though the matrices look different. This non-uniqueness is a feature, not a bug — it lets engineers choose canonical forms optimized for different purposes."

- question: "A control engineer wants to analyze a system's modes individually — understanding how each pole contributes independently to the total response. The most useful canonical realization is:"
  type: multiple-choice
  options:
    - "Controllable canonical form, because it directly encodes the denominator polynomial"
    - "Observable canonical form, because output measurements are physically meaningful"
    - "Diagonal (modal) canonical form, because A is diagonal and each state variable evolves as a decoupled mode corresponding to one pole"
    - "Any minimal realization, since all share identical modal structure"
  answer: 2
  explanation: "In diagonal (modal) form, A is a diagonal matrix with the system's poles on the diagonal. Each state variable xᵢ satisfies ẋᵢ = λᵢxᵢ + (coupling to input), meaning it evolves independently of the other state variables. The total response is a superposition of these decoupled modal responses. This makes the modal form ideal for analysis: you can see exactly which poles are fast/slow, well-damped/lightly-damped, and how strongly each is excited by the input. Controllable canonical form is useful for controller design but couples the state variables together in the A matrix."

- question: "The eigenvalues of the A matrix in a state-space representation are identical to the poles of the corresponding transfer function."
  type: true-false
  answer: true
  explanation: "The poles of the transfer function H(s) = C(sI−A)⁻¹B + D are the values of s where (sI−A)⁻¹ blows up, which occurs when det(sI−A) = 0. But det(sI−A) = 0 is exactly the characteristic equation of matrix A — its roots are the eigenvalues of A. This equivalence is one of the key bridges between the frequency-domain and state-space perspectives: poles, eigenvalues, and stability are all the same concept viewed from different angles."

- question: "A transfer function uniquely determines the A, B, C, D matrices of its state-space realization."
  type: true-false
  answer: false
  explanation: "Realization is non-unique: there are infinitely many state-space models that produce the same transfer function. Any similarity transformation T maps one valid realization (A, B, C, D) to another valid realization (T⁻¹AT, T⁻¹B, CT, D). This is why engineers choose among canonical forms — controllable canonical form, observable canonical form, diagonal modal form — each optimized for a different purpose. The transfer function captures only the input-output (external) behavior; the state-space model additionally encodes an internal coordinate representation, which is not unique."

- question: "What information does a state-space representation reveal that a transfer function hides, and why does this matter for control design?"
  type: short-answer
  answer: "A transfer function describes only the input-output relationship of a system, implicitly assuming zero initial conditions and hiding any internal structure. A state-space model makes the internal state explicit: the state vector x captures everything about the system's 'memory' at each instant. This reveals whether all internal modes are reachable from the input (controllability) and whether all modes can be inferred from the output (observability). Transfer functions can mask uncontrollable or unobservable modes — pole-zero cancellations in H(s) hide poles that still affect internal dynamics. State-space also handles MIMO systems and non-zero initial conditions naturally, making it the preferred representation for modern control design."
  explanation: "The practical consequence is that a transfer function with a pole-zero cancellation looks simpler than it is: the cancelled pole still exists in the internal dynamics, can be excited by initial conditions, and can cause internal instability even when the input-output map looks stable. State-space reveals this hidden mode. For control design, you need to know about all modes — not just the ones visible at the output — to place poles robustly and design observers."
```

## Explainer

You already know that transfer functions characterize a system by its poles and zeros — the roots that determine stability and frequency response. But transfer functions describe only the input-output relationship, hiding any internal structure of the system. The **state-space representation** makes that internal structure explicit. The **state vector** x captures all the information needed to predict the system's future behavior given future inputs — it is the system's "memory" at each instant.

The four matrices have clear physical roles. **A** (the system matrix) governs how the state evolves on its own — its eigenvalues are the poles of the system, directly linking state-space to the transfer function picture you already know. **B** (the input matrix) specifies how each input channel drives each state variable. **C** (the output matrix) extracts the measured outputs from the state. **D** (the feedthrough matrix) models any direct path from input to output that bypasses the dynamics — it contributes a constant term to the transfer function at high frequency. Together, the transfer function H(s) = C(sI - A)⁻¹B + D shows exactly how A, B, C, D encode the pole-zero information from your earlier work.

The power of state-space becomes clear with MIMO (multiple-input, multiple-output) systems. A transfer function matrix for a MIMO system is unwieldy; a state-space model is a single unified description regardless of how many inputs and outputs are involved. State-space also handles initial conditions naturally — if x(0) ≠ 0, the response includes the homogeneous solution Ae^{At}x(0), capturing how stored energy at t=0 affects the output. Transfer functions implicitly assume zero initial conditions.

**Realization** is the inverse problem: given a transfer function H(s), find matrices A, B, C, D that produce it. The answer is not unique — many state-space models share the same transfer function. Canonical realizations are standardized choices. The **controllable canonical form** places the denominator polynomial coefficients directly in the last row of A, making the connection to the transfer function explicit and ensuring every state can be driven by the input. The **observable canonical form** is its transpose dual. The **diagonal (modal) form** diagonalizes A so each state variable evolves independently as a decoupled mode — particularly useful when the poles are distinct, since each diagonal entry of A is a pole and the system's behavior decomposes mode by mode. These canonical forms are the bridge between the frequency-domain analysis you know and the matrix-based world of modern control design.
