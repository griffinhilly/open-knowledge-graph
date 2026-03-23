---
id: state-transformation-similarity-transform
title: State Transformations and Similarity Transformations
domain: engineering
course: control-systems
prerequisites:
- id: state-space-canonical-forms
  type: hard
- id: eigenvalues-and-eigenvectors
  type: soft
builds-toward:
- observability-controllability-tests
- pole-placement-observer-design
tags:
- state-transformation
- similarity-transform
- change-of-basis
- invariants
stage: expert
status: validated
---

# State Transformations and Similarity Transformations

## Core Idea
State transformations x̄ = Tx change the state-space representation but not the input-output behavior. Ā = TAT⁻¹, B̄ = TB, C̄ = CT⁻¹. Similarity transformations preserve eigenvalues, transfer function, and controllability/observability properties. Diagonalization and modal forms are special cases used to decouple and simplify analysis.

## Questions

```yaml
- question: "A control engineer has a state-space system that is unstable (A has eigenvalues with positive real parts). She applies a similarity transformation x̄ = Tx, obtaining Ā = TAT⁻¹. Is the transformed system stable?"
  type: multiple-choice
  options:
    - "Yes — the transformation T can be chosen to place the eigenvalues of Ā in the left half-plane, stabilizing the system"
    - "It depends — orthogonal transformations preserve eigenvalues, but other choices of T may alter them"
    - "No — if the original system is unstable, any similarity transformation leaves it unstable"
    - "Yes — transforming to diagonal form always produces a stable system because the modes decouple"
  answer: 2
  explanation: "Similarity transformations preserve eigenvalues. If Av = λv, then (TAT⁻¹)(Tv) = T(Av) = λ(Tv), so Ā has the same eigenvalues as A with transformed eigenvectors. Since stability is determined solely by whether eigenvalues have negative real parts, a similarity transformation can never stabilize or destabilize a system — it is merely a change of coordinates. Option A is the most tempting misconception: engineers think of transformations as tools to 'fix' systems, but pole placement (which does change eigenvalues) requires state feedback, not a coordinate change."

- question: "Which of the following changes under a similarity transformation x̄ = Tx of a state-space system?"
  type: multiple-choice
  options:
    - "The eigenvalues of the system matrix A"
    - "The transfer function H(s) = C(sI − A)⁻¹B"
    - "The controllability and observability of the system"
    - "The specific numerical entries of the A, B, and C matrices"
  answer: 3
  explanation: "The individual numerical entries of A, B, and C change under a similarity transformation — Ā = TAT⁻¹, B̄ = TB, C̄ = CT⁻¹ are generally different matrices. What is preserved are the invariants: eigenvalues (poles, stability), the transfer function (input-output behavior), and structural properties like controllability and observability. The whole point of similarity transformations is that different canonical forms — controllable canonical, observable canonical, diagonal — have very different matrix entries while describing the exact same physical system."

- question: "Two state-space representations of the same system related by a similarity transformation x̄ = Tx will have identical transfer functions."
  type: true-false
  answer: true
  explanation: "The transfer function H(s) = C(sI−A)⁻¹B is a property of the physical system, not of the coordinate choice. Under the transformation, the new transfer function is C̄(sI−Ā)⁻¹B̄ = (CT⁻¹)(T(sI−A)⁻¹T⁻¹)(TB) = C(sI−A)⁻¹B. The T matrices cancel exactly, confirming invariance. This is why system identification — recovering system behavior from input-output data — gives a unique answer even though infinitely many valid state-space representations exist."

- question: "Diagonalizing the system matrix A via a similarity transformation changes the poles of the system to the eigenvalues of the new diagonal matrix Λ, which may differ from the original poles."
  type: true-false
  answer: false
  explanation: "The diagonal entries of Λ = TAT⁻¹ (when T contains the eigenvectors of A) are precisely the eigenvalues of A — not new values. Diagonalization reveals existing eigenvalues in explicit form; it does not create new ones. The poles of the system are the eigenvalues of A, and since similarity transformations preserve eigenvalues, the poles are identical before and after diagonalization. What changes is the representation: the diagonal form decouples each mode, simplifying analysis, but the underlying dynamics are unchanged."

- question: "In the similarity transformation, the input matrix transforms as B̄ = TB but the output matrix transforms as C̄ = CT⁻¹. Why are these asymmetric — why not C̄ = TC?"
  type: short-answer
  answer: "Under x̄ = Tx (so x = T⁻¹x̄), the state equation ẋ = Ax + Bu becomes T⁻¹ẋ̄ = AT⁻¹x̄ + Bu, which gives ẋ̄ = TAT⁻¹x̄ + TBu — so B̄ = TB. The output equation y = Cx becomes y = C(T⁻¹x̄) = (CT⁻¹)x̄ — so C̄ = CT⁻¹. The input matrix B maps from input space (unchanged) to state space (transformed), picking up T on the left. The output matrix C maps from state space (now expressed in new coordinates via T⁻¹) to output space, picking up T⁻¹ on the right."
  explanation: "The asymmetry reflects the distinct roles of inputs and outputs in the state equations. This transformation structure guarantees the transfer function is invariant: C̄(sI−Ā)⁻¹B̄ = (CT⁻¹)(T(sI−A)⁻¹T⁻¹)(TB) = C(sI−A)⁻¹B, with all T factors canceling exactly."
```

## Explainer

The state-space representation of a system is not unique — there are infinitely many valid state-space descriptions that all produce identical input-output behavior. From your prerequisite on canonical forms, you already know that the same system can be written in controllable canonical form, observable canonical form, or other special structures. A **similarity transformation** is the mathematical operation that converts between these representations: replace the state vector x with a new state vector x̄ = Tx, where T is any invertible matrix. The transformed matrices Ā = TAT⁻¹, B̄ = TB, and C̄ = CT⁻¹ describe the same physical system in a new coordinate basis.

Why do eigenvalues survive the transformation? From your prerequisite on eigenvalues and eigenvectors, if Av = λv, then (TAT⁻¹)(Tv) = TAv = T(λv) = λ(Tv). The same scalar eigenvalue λ appears in the transformed system, with eigenvector Tv. Because the poles of the transfer function are precisely the eigenvalues of A, and because system stability depends only on pole locations, similarity transformations leave stability completely unchanged. Controllability and observability are also preserved — a system that can be driven from any initial state remains fully controllable after any coordinate change.

The most powerful application is **diagonalization**. If A has n linearly independent eigenvectors v₁, v₂, ..., vₙ, then choosing T = [v₁ v₂ ... vₙ] (the matrix whose columns are eigenvectors) transforms A into a diagonal matrix Λ = diag(λ₁, λ₂, ..., λₙ). In this **modal form**, each transformed state equation decouples: ẋ̄ᵢ = λᵢx̄ᵢ + B̄ᵢu. Mode i evolves independently of all others, controlled only by its own eigenvalue and input coupling. This makes analysis and simulation vastly simpler — you can study each mode of the system in isolation rather than solving a coupled system.

The deeper implication is that similarity transformations are a change of basis in state space, exactly analogous to rotating coordinate axes in geometry. Just as the distance between two points does not depend on which coordinate system you use to measure it, the input-output behavior of a dynamical system does not depend on which state variables you choose to represent it. Different canonical forms are simply convenient coordinate choices tailored to different analysis tasks: controllable canonical form facilitates pole placement, observable canonical form facilitates observer design, and diagonal form decouples the dynamics for modal analysis. The invariants — eigenvalues, transfer function, controllability/observability — are the true system properties, independent of the basis.
