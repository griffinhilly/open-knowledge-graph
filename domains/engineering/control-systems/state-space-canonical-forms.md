---
id: state-space-canonical-forms
title: 'State-Space Canonical Forms: Controllable and Observable Forms'
domain: engineering
course: control-systems
prerequisites:
- id: state-space-representation-control
  type: hard
- id: transfer-function-derivation-differential-equations
  type: soft
builds-toward:
- state-transformation-similarity-transform
- observability-controllability-tests
- pole-placement-observer-design
tags:
- state-space
- canonical-forms
- controllable
- observable
stage: advanced
status: draft
---

# State-Space Canonical Forms: Controllable and Observable Forms

## Core Idea
Controllable canonical form (companion form) reveals system controllability; observable canonical form reveals observability. Both are unique representations of the same system, obtained via similarity transformations. Canonical forms simplify controller and observer design by placing A, B, C matrices in special patterns where pole placement is straightforward.

## Questions

```yaml
- question: "Engineer A writes a state-space model for a system with transfer function H(s) = 1/(s² + 3s + 2) in controllable canonical form. Engineer B writes the same system in observable canonical form. Which statement is correct?"
  type: multiple-choice
  options:
    - "The two forms have different eigenvalues because their A matrices look different"
    - "Both forms represent the same input-output transfer function and have the same eigenvalues, differing only in which state variables are chosen"
    - "Only the controllable form can be used for pole placement; the observable form is only for observer design and has different poles"
    - "The observable form has a transposed transfer function, H(s)ᵀ, because the C matrix is transposed"
  answer: 1
  explanation: "Canonical forms are related by similarity transformations: x = Tx̃, giving Ã = T⁻¹AT, B̃ = T⁻¹B, C̃ = CT. Similarity transformations preserve eigenvalues (the poles) and the input-output transfer function — they simply express the same dynamics in a different coordinate system (different choice of state variables). Both forms have identical poles at s = -1 and s = -2. The difference is structural convenience: controllable canonical form makes pole placement direct, observable canonical form makes observer design direct, but both describe the same physical system."

- question: "A control engineer wants to design a state feedback gain vector K such that the closed-loop poles are at specified locations. Why is controllable canonical form particularly useful for this task?"
  type: multiple-choice
  options:
    - "Controllable canonical form guarantees closed-loop stability for any choice of K"
    - "In controllable canonical form, the last row of A contains the characteristic polynomial coefficients, so the state feedback gain K directly shifts these coefficients to place poles anywhere"
    - "Controllable canonical form diagonalizes A, making eigenvalue computation trivial"
    - "The companion matrix structure automatically satisfies Nyquist stability margins"
  answer: 1
  explanation: "In controllable canonical form, the A matrix is the companion matrix whose last row is [−a₀, −a₁, …, −aₙ₋₁], where a₀ through aₙ₋₁ are the open-loop characteristic polynomial coefficients. State feedback u = −Kx modifies the last row by subtracting K, directly producing a new characteristic polynomial with coefficients [−a₀+k₁, −a₁+k₂, …, −aₙ₋₁+kₙ]. Desired pole locations specify the desired polynomial coefficients, so solving for K is simple coefficient matching. In a general state-space representation, this same calculation requires solving a large linear system (Ackermann's formula), which is more cumbersome."

- question: "A similarity transformation T applied to a state-space model changes the eigenvalues of A, and thus moves the system's poles."
  type: true-false
  answer: false
  explanation: "Similarity transformations preserve eigenvalues. Under x = Tx̃, the new A matrix is Ã = T⁻¹AT, which has the same eigenvalues as A because det(λI − T⁻¹AT) = det(T⁻¹)det(λI − A)det(T) = det(λI − A). Eigenvalues are intrinsic properties of the linear map, not of the coordinate system used to represent it. This is precisely why canonical forms are useful: you can freely change state coordinates to get the convenient companion matrix structure without affecting the system's poles or its input-output transfer function."

- question: "Controllable canonical form and observable canonical form are two different systems that share the same poles but may produce different outputs for the same input."
  type: true-false
  answer: false
  explanation: "Both canonical forms are representations of the same system — they have the same transfer function H(s) = C(sI−A)⁻¹B and therefore produce identical outputs for any given input. They differ only in which linear combinations of the underlying modes are called 'state variables.' The transformation T that converts between them is invertible, so no information about the system's dynamics is lost or added. They are not different systems; they are the same system viewed from different state-variable coordinates."

- question: "Explain the duality between controllable and observable canonical forms, and what this duality means for the practical relationship between controller design and observer design."
  type: short-answer
  answer: "Controllable canonical form makes the A matrix a companion matrix with a simple B vector, so state feedback gain K can be chosen by direct polynomial coefficient matching to place closed-loop poles. Observable canonical form makes A a companion matrix with a simple C vector, so observer gain L can be chosen by the identical procedure to place observer error poles. The duality means: if you know how to design a state feedback controller in controllable canonical form, you automatically know how to design a Luenberger observer in observable canonical form — the mathematics is exactly the same with roles of B and C exchanged and A replaced by Aᵀ. This is the principle of duality: controllability of (A, B) is equivalent to observability of (Aᵀ, Bᵀ), and observer design is the 'transpose' of controller design."
  explanation: "The duality theorem in linear systems states that (A, B) is controllable if and only if (Aᵀ, Bᵀ) is observable. This means every result about controllability and state feedback has a mirror result about observability and state estimation. The two canonical forms are the concrete embodiment of this duality: each gives a coordinate system tailored to one half of the separation principle (design controller and observer independently, combine in the final system)."
```

## Explainer

When you first write a state-space model (x′ = Ax + Bu, y = Cx + Du), the A, B, and C matrices depend on which physical variables you chose as states. Rotate to a different basis — a different choice of state variables — and you get a different-looking but mathematically equivalent model. The key insight is that infinitely many state-space representations correspond to the same input-output transfer function. **Canonical forms** are special, standardized choices of that basis that reveal structural properties of the system and make design calculations tractable.

**Controllable canonical form** (also called companion form) restructures the model so that the A matrix takes on a companion matrix pattern — its last row contains the coefficients of the characteristic polynomial — while B is a simple column vector with a 1 in the last entry. This form makes it immediately obvious whether you can drive all modes from the input, and it makes **pole placement** by state feedback nearly mechanical: because the feedback gain vector directly modifies the coefficients of the characteristic polynomial, choosing desired closed-loop poles tells you exactly what gains to use.

**Observable canonical form** is the dual: it places A in a companion pattern and C in a simple row vector, making it straightforward to design a **Luenberger observer** (a reconstructor for unmeasured states). The duality between controllability and observability — a deep result in linear systems — means that the mathematics of observer design in observable canonical form mirrors exactly the mathematics of controller design in controllable canonical form. If you understand one, you understand both.

The conversion between your original state-space model and a canonical form is performed via a **similarity transformation**: x = Tx̃, where T is an invertible matrix. The new matrices are Ã = T⁻¹AT, B̃ = T⁻¹B, C̃ = CT. The eigenvalues — the poles of the system — are invariant under similarity transformations, so the transfer function is unchanged. To find T for controllable canonical form, you construct the controllability matrix [B, AB, A²B, …, Aⁿ⁻¹B] and use it to solve for T; for observable canonical form, you use the observability matrix similarly.

The practical payoff is this: canonical forms reduce the messy bookkeeping of general-purpose matrices to clean algebraic manipulation. When your A matrix is a companion matrix, choosing feedback gains to achieve desired pole locations is direct coefficient matching rather than solving a large linear system. This is why canonical forms appear so prominently in state-feedback and observer design — they are not just theoretical curiosities but workhorses of control system implementation.
