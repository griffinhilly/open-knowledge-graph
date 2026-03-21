---
id: eigenvalues-eigenstates-quantum
title: Eigenvalues and Eigenstates
domain: physics
course: quantum-mechanics
prerequisites:
- id: quantum-operators
  type: hard
- id: eigenvalues-eigenvectors
  type: hard
builds-toward:
- quantum-observables
- hydrogen-atom-quantum
tags:
- linear-algebra
- quantum-mechanics
- eigenvalue-problem
stage: advanced
status: draft
---

# Eigenvalues and Eigenstates

## Core Idea
For an operator Â, an eigenstate |φₙ⟩ satisfies Â|φₙ⟩ = λₙ|φₙ⟩ where λₙ is the eigenvalue. In quantum mechanics, eigenvalues of an observable operator are the only possible measurement outcomes, and eigenstates are states in which the observable has a definite value. The completeness of eigenstates ensures any quantum state can be expanded in eigenbasis.

## Questions

```yaml
- question: "A quantum system is prepared in the state |ψ⟩ = (1/√2)|E₁⟩ + (1/√2)|E₂⟩, a superposition of two energy eigenstates with E₁ ≠ E₂. An energy measurement is performed. What happens?"
  type: multiple-choice
  options:
    - "The system has both energies E₁ and E₂ simultaneously, and both values are registered"
    - "The measurement yields the average energy (E₁ + E₂)/2"
    - "The measurement yields either E₁ or E₂, each with probability 1/2, and the state collapses to the corresponding eigenstate"
    - "The measurement cannot be performed because the state is not an energy eigenstate"
  answer: 2
  explanation: "When a measurement is made in quantum mechanics, the outcome is always one of the operator's eigenvalues — never an intermediate value or simultaneous both. The probability of each outcome is |cₙ|², where cₙ = ⟨Eₙ|ψ⟩. Here c₁ = c₂ = 1/√2, so each eigenvalue has probability |1/√2|² = 1/2. After the measurement, the state collapses to the corresponding eigenstate. Option B (the average) is the expectation value ⟨Ĥ⟩ = (E₁ + E₂)/2, which is a statistical property over many measurements — no single measurement ever yields this intermediate value."

- question: "Why must observables in quantum mechanics correspond to Hermitian operators rather than arbitrary linear operators?"
  type: multiple-choice
  options:
    - "Hermitian operators commute with each other, ensuring that two observables can always be measured simultaneously"
    - "Hermitian operators are computationally easiest to diagonalize in practice"
    - "Hermitian operators guarantee real eigenvalues (so measurement outcomes are real numbers) and orthogonal eigenstates for distinct eigenvalues (so different outcomes correspond to distinguishable states)"
    - "Hermitian operators have non-negative eigenvalues, which ensures that probabilities computed from them are non-negative"
  answer: 2
  explanation: "The two key properties of Hermitian operators (Â = Â†) are: (1) all eigenvalues are real, which is required because physical measurement outcomes are real numbers; (2) eigenstates corresponding to different eigenvalues are orthogonal, which means distinct measurement outcomes correspond to maximally distinguishable quantum states. Option A is wrong — Hermitian operators do not all commute; two Hermitian operators commute if and only if they share a common eigenbasis. Option D is wrong — eigenvalues of Hermitian operators are real but can be negative (e.g., energy eigenvalues can be negative)."

- question: "A quantum system can be in a state that is not an eigenstate of an observable, but any measurement of that observable will still yield one of the eigenvalues."
  type: true-false
  answer: true
  explanation: "This is the Born rule combined with the spectral theorem. Any state |ψ⟩ can be expanded as a superposition of eigenstates: |ψ⟩ = Σₙ cₙ|φₙ⟩. A measurement always yields one of the eigenvalues λₙ with probability |cₙ|², regardless of whether |ψ⟩ is itself an eigenstate. If |ψ⟩ is not an eigenstate, the measurement outcome is probabilistic — but it is always drawn from the set of eigenvalues, never from an intermediate value. This is why the discreteness of atomic spectra is explained by the energy eigenvalues: only these energies are possible outcomes."

- question: "If a quantum state is a superposition of energy eigenstates |E₁⟩ and |E₂⟩, a single energy measurement can yield a value between E₁ and E₂."
  type: true-false
  answer: false
  explanation: "Measurement in quantum mechanics always yields an eigenvalue — never an interpolated or average value. The expectation value ⟨Ĥ⟩ = Σₙ |cₙ|² Eₙ is the statistical average over many measurements, but no individual measurement yields this value unless it happens to equal one of the eigenvalues. This is a fundamental departure from classical physics, where a continuous range of values is typically possible. The discreteness of eigenvalues is what explains discrete atomic spectra: only specific energy transitions (differences between eigenvalues) are possible."

- question: "What is the physical significance of the completeness of eigenstates of a Hermitian operator, and how does it connect to the probability interpretation of quantum measurement?"
  type: short-answer
  answer: "Completeness means the eigenstates of any observable span the full Hilbert space — any quantum state |ψ⟩ can be written as a superposition |ψ⟩ = Σₙ cₙ|φₙ⟩. This is physically significant because it guarantees that a measurement of any observable can always be performed on any state: there is always a well-defined expansion in the eigenbasis. The coefficients cₙ = ⟨φₙ|ψ⟩ are the projections of the state onto each eigenstate, and |cₙ|² gives the probability of obtaining eigenvalue λₙ. Completeness is the mathematical condition that ensures probabilities sum to 1: Σₙ |cₙ|² = ⟨ψ|ψ⟩ = 1."
  explanation: "Without completeness, there could be states that have no expansion in the eigenbasis — states for which the probability interpretation would break down. The spectral theorem for Hermitian operators on Hilbert spaces guarantees completeness, which is why Hermiticity is the physical requirement for observables. Completeness also enables the resolution of the identity Σₙ |φₙ⟩⟨φₙ| = 𝟙, which is the mathematical expression of 'any state can be fully decomposed into measurement outcomes' — the foundation of the Born rule."
```

## Explainer

You already know from linear algebra that for a matrix M, an eigenvector v satisfies Mv = λv — the vector is unchanged in direction by the operation, only scaled by the eigenvalue λ. In quantum mechanics, this algebraic relationship becomes the central fact about measurement. An **eigenstate** |φₙ⟩ of operator Â satisfies Â|φₙ⟩ = λₙ|φₙ⟩, and the eigenvalue λₙ is the only value you can ever obtain when measuring A in that state. This is the sharpest form of a quantum prediction: perfect certainty about a measurement outcome is equivalent to being in an eigenstate.

Why must observables have real eigenvalues? Because measured quantities must be real numbers. You know from the prerequisite on quantum operators that observables correspond to **Hermitian** operators (Â = Â†). A fundamental theorem guarantees that Hermitian operators have real eigenvalues and that eigenstates belonging to distinct eigenvalues are orthogonal: ⟨φₘ|φₙ⟩ = δₘₙ. Orthogonality is physically essential — two distinct measurement outcomes must correspond to distinguishable states, and inner product zero means maximally distinguishable in quantum mechanics.

The real power of eigenstates comes from **completeness**: the eigenstates of any Hermitian operator span the Hilbert space. Any quantum state |ψ⟩ can be written as |ψ⟩ = Σₙ cₙ|φₙ⟩ where cₙ = ⟨φₙ|ψ⟩. This is just the projection decomposition you know from linear algebra, now applied to states. When you measure A in state |ψ⟩, the probability of obtaining λₙ is |cₙ|², and the state collapses to |φₙ⟩. The squared inner products give the Born rule; the eigenbasis provides the framework in which probabilities are computed.

A concrete example: the Hamiltonian Ĥ is the energy operator. Its eigenstates |Eₙ⟩ satisfy Ĥ|Eₙ⟩ = Eₙ|Eₙ⟩ — these are the **stationary states**, states of definite energy. For the hydrogen atom, the energy eigenvalues are Eₙ = −13.6/n² eV with n = 1, 2, 3, ... The discreteness of these eigenvalues is why atomic spectra consist of sharp lines: only these specific energy values are possible, so only photons with energies equal to differences between levels can be emitted or absorbed. Any general state of the hydrogen atom is a superposition of energy eigenstates, and an energy measurement collapses it to one of them with probability |cₙ|².
