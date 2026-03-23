---
id: quantum-operators-eigenvalues
title: Quantum Operators and Eigenvalues
domain: physics
course: modern-physics
prerequisites:
- id: probability-amplitude-interpretation
  type: hard
builds-toward:
- classical-limit-correspondence
- uncertainty-relation-measurements
tags:
- quantum-mechanics
- operators
stage: advanced
status: validated
---

# Quantum Operators and Eigenvalues

## Core Idea
In quantum mechanics, physical observables (position, momentum, energy) are represented by Hermitian operators. When an operator Â acts on an eigenstate |ψ⟩, it returns the same state multiplied by a scalar eigenvalue: Â|ψ⟩ = a|ψ⟩. The eigenvalue is the unique result obtained when measuring the observable on that eigenstate; the set of all eigenvalues of an operator comprises the possible measurement outcomes.

## How It's Best Learned
Learn the position and momentum operators in 1D: x̂ and p̂ = −iℏ d/dx. Apply them to simple wavefunctions and eigenstates; compute expectation values for particles in boxes.

## Common Misconceptions
- Operators are not numbers; they are mathematical objects that transform states.
- Eigenvalues of Hermitian operators are always real, but eigenstates are generally complex.
- The eigenvalue equation Âψ = aψ holds only for eigenstates, not arbitrary states.

## Questions

```yaml
- question: "A particle is in the state ψ = (1/√2)(ψ₁ + ψ₂), where ψ₁ and ψ₂ are energy eigenstates with eigenvalues E₁ and E₂. What result will a single measurement of energy yield?"
  type: multiple-choice
  options:
    - "The average energy (E₁ + E₂)/2, since the particle is equally in both states"
    - "Either E₁ or E₂, with equal probability 1/2 each, and the state collapses to the corresponding eigenstate"
    - "Both E₁ and E₂ simultaneously, since the particle is in a superposition of both"
    - "An undefined result, because the energy operator cannot act on a superposition state"
  answer: 1
  explanation: "A superposition state does not have a definite energy — this is the foundational departure from classical mechanics. A single measurement yields exactly one eigenvalue (either E₁ or E₂) with probabilities determined by the squared amplitudes of the coefficients. With equal coefficients 1/√2, each outcome has probability (1/√2)² = 1/2. After measurement, the state collapses to the corresponding eigenstate. Option A describes the expectation value ⟨E⟩ = (E₁ + E₂)/2 — the average over many measurements — which is not the result of any single measurement."

- question: "Which property of Hermitian operators is essential for ensuring that quantum mechanical observables yield physically meaningful measurement outcomes?"
  type: multiple-choice
  options:
    - "Hermitian operators have a finite number of eigenvalues, making the set of possible outcomes discrete and countable"
    - "The eigenvalues of Hermitian operators are always real numbers, consistent with measurement results being real"
    - "Hermitian operators commute with each other, allowing simultaneous measurement of all observables"
    - "Hermitian operators always have normalized eigenstates, making probability calculations straightforward"
  answer: 1
  explanation: "Physical measurements always yield real numbers. A Hermitian operator Â satisfies Â† = Â, which guarantees all its eigenvalues are real. This is why physical observables — position, momentum, energy — must be represented by Hermitian operators. Option C is incorrect: Hermitian operators do *not* in general commute (the canonical non-commutation is [x̂, p̂] = iℏ), and non-commuting observables cannot be simultaneously measured with certainty. Option A is false: many Hermitian operators (like position) have continuous, not discrete, spectra."

- question: "The momentum operator p̂ = −iℏ ∂/∂x returns a definite momentum value when applied to any normalizable wavefunction."
  type: true-false
  answer: false
  explanation: "The eigenvalue equation p̂ψ = pψ holds only for eigenstates of p̂ — functions of the form e^{ikx} with definite momentum ℏk. For a general superposition wavefunction, applying p̂ does not return a scalar multiple of the same function; it returns a different function. What can be extracted for a general state is a probability distribution over momentum eigenvalues, not a single definite value. The common misconception is that applying an operator to any state yields an eigenvalue; in fact, eigenvalues arise only for eigenstates."

- question: "Eigenstates of a Hermitian operator corresponding to different eigenvalues are mutually orthogonal."
  type: true-false
  answer: true
  explanation: "This is the orthogonality theorem for Hermitian operators: if Âψ_a = aψ_a and Âψ_b = bψ_b with a ≠ b, then ⟨ψ_a | ψ_b⟩ = 0. The proof follows directly from the Hermitian property. This orthogonality is physically meaningful: eigenstates with different eigenvalues represent mutually exclusive measurement outcomes. It also ensures that eigenstates form an orthogonal basis for the Hilbert space, so any state can be uniquely expanded as a sum of eigenstates with squared coefficients giving the probability distribution for measurement outcomes."

- question: "Why must physical observables in quantum mechanics be represented by Hermitian operators? What two properties of Hermitian operators make them physically appropriate?"
  type: short-answer
  answer: "Two properties: (1) Real eigenvalues — measurements always yield real numbers, so the operator representing an observable must have real eigenvalues; Hermitian operators (Â = Â†) guarantee this. (2) Orthogonal eigenstates — eigenstates with different eigenvalues are orthogonal, forming a basis for the space of states. This means any state can be decomposed into eigenstates with coefficients whose squares give probabilities, making the Born rule well-defined. A non-Hermitian operator could have complex eigenvalues or non-orthogonal eigenstates, both of which are unphysical for a measurable observable."
  explanation: "The Hermitian requirement is not just mathematical convenience — it is physically necessary. Real eigenvalues match the reality of what measuring instruments register. Orthogonal eigenstates allow a consistent probability interpretation: if outcomes A and B are distinct measurement results, the corresponding states must be orthogonal so their probabilities add correctly without interference. The entire probability structure of quantum mechanics depends on this orthogonality. Hermiticity is what makes the Hilbert space formalism match the physical requirements of measurement."
```

## Explainer

From the probability amplitude interpretation, you know that the wavefunction ψ(x) encodes probability: |ψ(x)|² dx is the probability of finding the particle in a small interval around x. But the wavefunction also encodes information about momentum, energy, and every other observable — it just takes more work to extract it. **Quantum operators** are the machinery that extracts this information. Each physical observable is paired with a specific operator that "questions" the wavefunction about that quantity.

The key example is momentum. Classically, momentum is just the number p = mv. Quantum mechanically, momentum is represented by the operator p̂ = −iℏ ∂/∂x. This operator does not multiply ψ by a number; it *differentiates* it. Apply p̂ to the wavefunction ψ(x) = e^{ikx} and you get: −iℏ (ik) e^{ikx} = ℏk · e^{ikx}. The result is the *same* wavefunction multiplied by the scalar ℏk. This is the **eigenvalue equation** p̂ψ = pψ, with eigenvalue p = ℏk. The function e^{ikx} is an **eigenstate** of momentum with a definite momentum ℏk — if you measure the momentum of a particle in this state, you will always get exactly ℏk, with certainty. The eigenvalue is the measurement outcome.

What happens when the particle is *not* in a momentum eigenstate? Any normalizable wavefunction can be expanded as a superposition of eigenstates: ψ(x) = ∫ c(k) e^{ikx} dk. Each term e^{ikx} has a definite momentum ℏk, and |c(k)|² is proportional to the probability that a measurement yields that particular momentum. The operator p̂ does not return a single number when it acts on a superposition; instead, measurement causes the state to **collapse** to one eigenstate, with the corresponding eigenvalue as the outcome. Before measurement, only the probability distribution over eigenvalues is defined. This is the fundamental departure from classical mechanics: not all states have definite values for all observables simultaneously.

The requirement that operators be **Hermitian** (self-adjoint: Â† = Â) guarantees two essential properties. First, all eigenvalues of a Hermitian operator are *real numbers* — which they must be, since measurements yield real values. Second, eigenstates belonging to *different* eigenvalues are mutually **orthogonal**: ⟨ψ_a | ψ_b⟩ = 0 if a ≠ b. This orthogonality means the eigenstates form an independent "basis" for all possible states — you can decompose any state into a sum of eigenstates, and the expansion coefficients directly give the probability distribution for measurement outcomes. The position operator x̂ (which simply multiplies by x), the momentum operator p̂, and the Hamiltonian Ĥ (which represents total energy) are the foundational Hermitian operators from which all of quantum mechanics is built.
