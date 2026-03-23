---
id: quantum-postulates
title: Postulates of Quantum Mechanics
domain: physics
course: quantum-mechanics
prerequisites:
- id: wavefunction-and-probability
  type: hard
- id: hilbert-space-formalism
  type: hard
builds-toward:
- born-rule-and-measurement
- operators-and-observables
- identical-particles-exchange
tags:
- foundations
- postulates
stage: advanced
status: validated
---

# Postulates of Quantum Mechanics

## Core Idea
The postulates specify that states live in Hilbert space, observables are Hermitian operators, measurement outcomes are eigenvalues, and time evolution follows the Schrödinger equation. Together these form the axiomatic foundation distinguishing quantum from classical mechanics.

## Questions

```yaml
- question: "A quantum system is in the state |ψ⟩ = (3/5)|a₁⟩ + (4/5)|a₂⟩, where |a₁⟩ and |a₂⟩ are eigenstates of observable Â with eigenvalues 2 and 5. What is the probability of measuring the value 5?"
  type: multiple-choice
  options:
    - "4/5 — the coefficient of the eigenstate corresponding to eigenvalue 5"
    - "16/25 — the square of the coefficient of the eigenstate corresponding to eigenvalue 5"
    - "1/2 — since there are only two eigenstates, each is equally likely"
    - "7/5 — the weighted average of the two eigenvalues"
  answer: 1
  explanation: "By the Born rule (Postulate 3), the probability of obtaining eigenvalue aₙ is |cₙ|² — the square of the coefficient, not the coefficient itself. The coefficient of |a₂⟩ is 4/5, so the probability is (4/5)² = 16/25. Option (a) is the classic error: confusing the probability amplitude (the coefficient) with the probability (its squared modulus). Option (d) gives the expectation value, which is the average outcome over many measurements, not the probability of any specific outcome."

- question: "Why must quantum mechanical observables be represented specifically by Hermitian operators, rather than general linear operators?"
  type: multiple-choice
  options:
    - "Because Hermitian operators are computationally simpler and have well-defined matrix representations"
    - "Because Hermitian operators always commute with each other, ensuring measurement outcomes are consistent"
    - "Because Hermitian operators have real eigenvalues, and measurement outcomes must be real numbers"
    - "Because Hermitian operators preserve the norm of any state vector, ensuring probability is conserved"
  answer: 2
  explanation: "The requirement of Hermiticity comes directly from physics: when you measure a physical quantity (position, energy, spin), the result must be a real number. Hermitian operators have the mathematical property that all their eigenvalues are real. Non-Hermitian operators can have complex eigenvalues, which cannot represent physical measurement outcomes. Note: norm preservation (option d) is the property of *unitary* operators, which govern time evolution — a separate and equally important requirement."

- question: "According to the postulates of quantum mechanics, the time evolution of a quantum state between measurements is fundamentally probabilistic."
  type: true-false
  answer: false
  explanation: "Between measurements, quantum states evolve deterministically and continuously according to the Schrödinger equation (Postulate 4): iℏ d|ψ⟩/dt = Ĥ|ψ⟩. This evolution is unitary and completely predictable given the initial state and Hamiltonian. Probability only enters at the moment of measurement (Postulate 3), where the Born rule governs which eigenvalue is obtained. The deep puzzle of quantum mechanics is precisely this tension: deterministic evolution between measurements, probabilistic discontinuous collapse at measurement."

- question: "After a measurement yields eigenvalue aₙ, an immediate second measurement of the same observable on the same system will yield aₙ again with certainty."
  type: true-false
  answer: true
  explanation: "This follows directly from the collapse postulate (Postulate 3). Upon measuring observable Â and obtaining eigenvalue aₙ, the state collapses to the corresponding eigenstate |aₙ⟩. Since this state is an eigenstate of Â with eigenvalue aₙ, a second measurement immediately after will find the system in |aₙ⟩ with coefficient 1, giving probability |1|² = 1. This repeatability of immediately successive measurements is an experimentally verified consequence of the postulates and distinguishes quantum measurement from classical statistical sampling."

- question: "What is the conceptual tension between Postulate 3 (measurement and collapse) and Postulate 4 (Schrödinger time evolution), and why is this tension philosophically significant?"
  type: short-answer
  answer: "Postulate 4 says the quantum state evolves continuously and deterministically via the Schrödinger equation — given |ψ(t₀)⟩ and Ĥ, the state at any future time is exactly determined. Postulate 3 says measurement causes a discontinuous, probabilistic collapse to an eigenstate — which eigenstate you get is fundamentally random. These two dynamics are inconsistent: a measuring apparatus is itself a physical system subject to Schrödinger evolution, yet the postulates describe it as causing collapse. The theory provides no rule for when 'collapse' occurs versus 'evolution.' This is the quantum measurement problem, and resolving it (or arguing it needs no resolution) is the project of quantum interpretations: Copenhagen, many-worlds, pilot wave, relational, and others."
  explanation: "This tension is not a technical detail — it goes to the heart of what quantum mechanics says about reality. Does the wavefunction represent physical reality or just our knowledge? Does measurement create the outcome or reveal a pre-existing one? The postulates are operationally complete (they predict every experimental result) but ontologically silent on these questions."
```

## Explainer

You already know that quantum states are wavefunctions with probabilistic interpretations — from your study of the wavefunction and the Born rule — and that the mathematical arena for quantum mechanics is a Hilbert space of square-integrable functions, with inner products and orthonormal bases. The postulates of quantum mechanics assemble these ingredients into a complete logical framework that tells you exactly how to predict measurement outcomes and how systems evolve. They are not derived from anything deeper (at least within standard quantum mechanics); they are the axioms from which everything else follows.

**Postulate 1: State representation.** The complete description of a quantum system at any time is a normalized vector |ψ⟩ in a Hilbert space. This is already familiar to you — it is the wavefunction recast in Dirac notation. The key word is "complete": the state contains everything that can in principle be known about the system. There are no hidden variables, no additional information that a more complete theory would supply (within this framework). Two states that differ only by a global phase factor e^{iθ}|ψ⟩ represent the same physical state.

**Postulate 2: Observables as operators.** Every measurable physical quantity — position, momentum, energy, spin — is represented by a **Hermitian operator** acting on the Hilbert space. The requirement that the operator be Hermitian (equal to its own conjugate transpose) guarantees that its eigenvalues are real numbers, which is necessary since measurement outcomes must be real. From your Hilbert space work, you know that Hermitian operators have a complete set of orthonormal eigenvectors that span the space. **Postulate 3: Measurement.** When you measure an observable Â, the only possible outcomes are its eigenvalues aₙ. If the system is in state |ψ⟩ = Σcₙ|aₙ⟩, the probability of obtaining aₙ is |cₙ|² — the Born rule you already know. After the measurement, the state **collapses** to the corresponding eigenstate |aₙ⟩. This is the most philosophically contested postulate, but operationally it is the one that connects the mathematical formalism to experimental results.

**Postulate 4: Time evolution.** Between measurements, a closed quantum system evolves deterministically according to the **Schrödinger equation**: iℏ d|ψ⟩/dt = Ĥ|ψ⟩, where Ĥ is the Hamiltonian operator. This is the quantum analogue of Newton's second law — it specifies how the state changes in time. The evolution is **unitary** (it preserves the norm of the state and hence total probability), reflecting the fact that probability is conserved when no measurement occurs. Together, these four postulates define the rules of the game: state preparation sets |ψ⟩, Schrödinger evolution propagates it, and measurement extracts real numbers from it while collapsing the state. The tension between the deterministic evolution between measurements and the probabilistic collapse during measurement is the heart of the quantum measurement problem — and the starting point for every interpretation of quantum mechanics you will encounter later.
