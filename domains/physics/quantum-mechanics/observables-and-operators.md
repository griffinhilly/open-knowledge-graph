---
id: observables-and-operators
title: Observables and Quantum Operators
domain: physics
course: quantum-mechanics
prerequisites:
- id: dirac-notation
  type: hard
- id: linear-transformations
  type: hard
- id: hilbert-space-formalism
  type: hard
- id: kets-and-bras
  type: hard
- id: quantum-postulates
  type: soft
builds-toward:
- commutation-relations
tags:
- operators
- observables
- hermitian
stage: formal-systems
status: validated
---

# Observables and Quantum Operators

## Core Idea
Each physical observable is represented by a Hermitian operator; eigenvalues are possible measurement outcomes, eigenstates have definite values. The expectation value ⟨ψ|Ô|ψ⟩ predicts the average of repeated measurements.

## How It's Best Learned
Work with the 2×2 matrices for spin components first. Find the eigenvalues and eigenvectors of S_z and S_x, check that each set is orthonormal, and expand a given state in both bases. Compute the outcome probabilities and ⟨S_x⟩ from the expansion, then again from ⟨ψ|Ŝ_x|ψ⟩, and confirm they agree. Then compute [S_x, S_z] to see why the two cannot both be definite.

## Common Misconceptions
- Applying Â to |ψ⟩ gives the state after measuring A. (Â|ψ⟩ is generally not normalized and is not an eigenstate. The post-measurement state is the eigenstate |aₙ⟩ that matches the result.)
- The product of two Hermitian operators is Hermitian. ((ÂB̂)† = B̂Â, so the product is Hermitian only when Â and B̂ commute.)
- Eigenstates of the same observable with different eigenvalues can partly overlap. (For a Hermitian operator, eigenstates with different eigenvalues are orthogonal. Together with completeness, this is why the outcome probabilities add to one.)
- The expectation value is the most likely result of a single measurement. (It is the average over many runs. It need not be an eigenvalue, so a single measurement may never give it.)

## Questions

```yaml
- question: "A quantum system is in state |ψ⟩ = c₁|a₁⟩ + c₂|a₂⟩, where |a₁⟩ and |a₂⟩ are eigenstates of observable A with eigenvalues a₁ and a₂. A single measurement of A is performed. What result is obtained?"
  type: multiple-choice
  options:
    - "The value a₁ + a₂, since the state is a superposition of both eigenstates"
    - "Either a₁ or a₂, with probabilities |c₁|² and |c₂|² respectively"
    - "The expectation value c₁a₁ + c₂a₂, which is the quantum average"
    - "Either a₁ or a₂ with equal probability, regardless of the coefficients"
  answer: 1
  explanation: "Measurement always yields one of the operator's eigenvalues — never a superposition value or weighted average. The probability of obtaining aₙ is |cₙ|² = |⟨aₙ|ψ⟩|². The expectation value ⟨ψ|Â|ψ⟩ = Σ aₙ|cₙ|² is the average over many measurements, not the result of any single one. After measurement, the state collapses to the corresponding eigenstate."

- question: "Why must operators representing physical observables be Hermitian?"
  type: multiple-choice
  options:
    - "Because Hermitian operators always commute with each other, ensuring simultaneous measurability"
    - "Because Hermitian operators have real eigenvalues and their eigenstates form a complete orthonormal basis"
    - "Because non-Hermitian operators cannot be applied to ket vectors in Hilbert space"
    - "Because Hermitian operators produce complex eigenvalues, which represent phase information"
  answer: 1
  explanation: "Two physical requirements force Hermiticity. First, measurement outcomes must be real numbers — a complex energy or position is physically meaningless. Hermitian operators guarantee real eigenvalues. Second, any quantum state must be expressible as a combination of measurement outcomes — the spectral theorem guarantees that Hermitian operators' eigenstates form a complete orthonormal basis for the Hilbert space. Option A is wrong: Hermitian operators do not necessarily commute; commuting Hermitian operators can be simultaneously measured, but Hermiticity alone does not require commutativity."

- question: "If two observables A and B have commuting operators ([Â, B̂] = 0), it is very difficult to simultaneously know the exact values of both."
  type: true-false
  answer: false
  explanation: "The opposite is true: when operators commute, they share a common eigenbasis, meaning a state can simultaneously be an eigenstate of both. This allows both observables to have definite values at once. It is non-commuting operators ([Â, B̂] ≠ 0) that lack a common eigenbasis, giving rise to uncertainty relations. For position and momentum ([X̂, P̂] = iℏ, a nonzero multiple of the identity) no state has definite values of both; for some other non-commuting pairs a few special states can still be eigenstates of both (L_x and L_y both give zero on an l = 0 state)."

- question: "The expectation value ⟨ψ|Â|ψ⟩ gives the probability-weighted average of all possible measurement outcomes for a system in state |ψ⟩."
  type: true-false
  answer: true
  explanation: "If |ψ⟩ = Σ cₙ|aₙ⟩, then ⟨ψ|Â|ψ⟩ = Σ aₙ|cₙ|², which is exactly a probability-weighted average of the eigenvalues. This is the quantum analog of the classical expected value. The expectation value is not what you observe in a single measurement — that gives one eigenvalue — but rather what you observe as the average over many identically prepared measurements."

- question: "Why does the non-commutativity of position and momentum ([X̂, P̂] = iℏ ≠ 0) imply that a particle cannot have simultaneously definite position and momentum? What would commutativity have implied instead?"
  type: short-answer
  answer: "Non-commuting operators have no shared eigenbasis: no state can be simultaneously an eigenstate of both X̂ and P̂. Any state with definite position is a superposition of momentum eigenstates (and vice versa), so measuring momentum on a state with definite position yields a spread of outcomes — the uncertainty principle. If [X̂, P̂] = 0, the operators would share a common eigenbasis, meaning states could simultaneously have definite position and momentum, and classical determinism would be recovered."
  explanation: "The commutator [X̂, P̂] = iℏ is not just a computational fact — it encodes the physical incompatibility of position and momentum. The Heisenberg uncertainty relation ΔxΔp ≥ ℏ/2 follows directly. This is why quantum mechanics is fundamentally different from classical mechanics: the operators for canonically conjugate variables do not commute, making the classical phase-space picture of definite (x, p) points impossible."
```

## Explainer

In classical mechanics, an observable is just a number — a particle's position, momentum, or energy at any instant. Quantum mechanics replaces these numbers with **operators**: mathematical objects that act on state vectors (kets) to produce new state vectors. The position of a particle is not a fixed number but an operator X̂; its momentum is an operator P̂. This isn't a notational whim — it is forced by the experimental fact that quantum systems don't have definite values until measured, and the act of measurement disturbs the system.

The central constraint is that operators representing physical observables must be **Hermitian** (or self-adjoint): Â = Â†, meaning ⟨φ|Â|ψ⟩ = ⟨ψ|Â|φ⟩*. You need Hermitian operators for two reasons, both rooted in physics. First, Hermitian operators have real eigenvalues — and measurement outcomes must be real numbers, not complex ones. Second, their eigenstates form a complete orthonormal set, so any quantum state can be expanded in them. This is the spectral theorem from linear algebra, now doing real physical work: it guarantees that the eigenstates of any observable form a valid basis for the Hilbert space.

The **eigenvalue equation** Â|aₙ⟩ = aₙ|aₙ⟩ encodes the measurement postulate directly. If the system is in eigenstate |aₙ⟩, a measurement of A yields the definite value aₙ with certainty. If the system is in a superposition |ψ⟩ = Σ cₙ|aₙ⟩, a measurement yields outcome aₙ with probability |cₙ|² = |⟨aₙ|ψ⟩|², and the state collapses to |aₙ⟩ afterward. The **expectation value** ⟨ψ|Â|ψ⟩ = Σ aₙ|cₙ|² is simply the probability-weighted average of all possible outcomes — the quantum analog of a classical average.

Two observables have a complete set of simultaneous eigenstates exactly when their operators **commute**: [Â, B̂] = ÂB̂ − B̂Â = 0. When this commutator is zero, the operators share a common eigenbasis — you can simultaneously know definite values of both A and B. When the commutator is a nonzero multiple of the identity (as it is for position and momentum: [X̂, P̂] = iℏ), no state can have definite values of both simultaneously, and the uncertainty principle follows. For other non-commuting pairs, a few special states can still be eigenstates of both (L_x and L_y both give zero on an l = 0 state), but no complete shared basis exists. The operator structure is therefore not just a bookkeeping device: it encodes which pairs of quantities are compatible and which are fundamentally in tension.
