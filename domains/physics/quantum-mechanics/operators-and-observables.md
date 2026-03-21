---
id: operators-and-observables
title: Operators and Observables
domain: physics
course: quantum-mechanics
prerequisites:
- id: dirac-notation
  type: hard
- id: quantum-postulates
  type: hard
builds-toward:
- commutation-relations
- expectation-values
- time-independent-perturbation-theory
tags:
- observables
- operators
stage: advanced
status: draft
---

# Operators and Observables

## Core Idea
Physical observables correspond to Hermitian operators on Hilbert space. Measuring an observable yields one of its eigenvalues. The expectation value ⟨A⟩ predicts the average measurement result for a given state.

## Questions

```yaml
- question: "A hydrogen atom is prepared in an energy eigenstate. You measure its energy 100 times and get the same value every time. You then measure its position 100 times and get a different value each time. What explains this difference?"
  type: multiple-choice
  options:
    - "Energy measurements are more accurate because the Hamiltonian is a simpler operator"
    - "The position measurement disturbs the energy eigenstate, making energy undefined on subsequent measurements"
    - "The state is an eigenstate of the Hamiltonian, so energy measurements always yield the corresponding eigenvalue; it is not an eigenstate of the position operator, so position outcomes are probabilistic"
    - "The Heisenberg uncertainty principle prevents definite position measurements under any circumstances"
  answer: 2
  explanation: "This is the eigenvalue structure at work. A state |ψ⟩ that is an eigenstate of operator Â satisfies Â|ψ⟩ = λ|ψ⟩, which means measuring A always yields λ with certainty. The energy eigenstate is not an eigenstate of position, so when you expand it in the position eigenbasis, you get a spread of coefficients — each position value can occur with probability |⟨x|ψ⟩|². The observable's operator, not the measurement technique, determines whether outcomes are definite or probabilistic."

- question: "Why must quantum mechanical observables correspond to Hermitian operators specifically, rather than any linear operator on Hilbert space?"
  type: multiple-choice
  options:
    - "Hermitian operators are easier to compute with and have simpler matrix representations"
    - "Hermitian operators guarantee real eigenvalues (so measurement outcomes are real numbers) and a complete orthonormal eigenbasis (so probabilities of all outcomes sum to one) — both physically required"
    - "Only Hermitian operators can be diagonalized, which is necessary for the expectation value formula"
    - "Hermiticity is a historical convention with no deeper physical justification"
  answer: 1
  explanation: "Hermiticity is not a convention — it is forced by physics. Two requirements must hold: (1) measurement outcomes are real numbers, which requires real eigenvalues; (2) the probabilities of all possible outcomes must sum to 1, which requires a complete orthonormal eigenbasis. Both are guaranteed by Hermiticity (specifically by the spectral theorem for Hermitian operators). Non-Hermitian operators can have complex eigenvalues and incomplete eigenbases, neither of which corresponds to a valid measurement process."

- question: "The expectation value ⟨Â⟩ = ⟨ψ|Â|ψ⟩ gives the result you will obtain when you measure observable A on the state |ψ⟩."
  type: true-false
  answer: false
  explanation: "The expectation value is the average over many repeated measurements on identically prepared copies of |ψ⟩, not the result of a single measurement. A single measurement yields one of the eigenvalues of Â, with probability determined by the overlap of |ψ⟩ with the corresponding eigenstate. The expectation value may not even equal any eigenvalue — for example, a spin-½ particle in an equal superposition of |↑⟩ and |↓⟩ has ⟨Ŝz⟩ = 0, but no individual measurement ever returns 0 (only ±ℏ/2)."

- question: "If two observables have operators that commute ([Â, B̂] = 0), then there exist quantum states in which both A and B simultaneously have perfectly definite values."
  type: true-false
  answer: true
  explanation: "Commuting operators share a complete set of simultaneous eigenstates — states that are eigenstates of both operators at once. In such a state, measuring A always yields one specific eigenvalue, and measuring B always yields one specific eigenvalue. This is the formal meaning of 'simultaneously definite values.' When operators do not commute ([Â, B̂] ≠ 0), no simultaneous eigenbasis exists, and no state can have both observables definite at once — the origin of quantum uncertainty relations."

- question: "The position and momentum operators satisfy [x̂, p̂] = iℏ ≠ 0. Explain what this commutation relation implies about simultaneously knowing position and momentum."
  type: short-answer
  answer: "Because x̂ and p̂ do not commute, they share no common eigenstates — no state exists that is simultaneously an eigenstate of both. Any state with definite position (a position eigenstate, sharply peaked in space) is a superposition of infinitely many momentum eigenstates, so its momentum is completely indefinite, and vice versa. The commutator iℏ directly leads to the Heisenberg uncertainty relation ΔxΔp ≥ ℏ/2: the more precisely one quantity is defined (small spread), the more spread-out the other must be. This is not a measurement disturbance effect — it is a structural feature of the operators."
  explanation: "The algebraic relationship [x̂, p̂] = iℏ encodes quantum incompatibility. Commuting operators (like energy and total angular momentum in a spherically symmetric potential) allow simultaneous definite values and obey [Â, B̂] = 0. Non-commuting operators cannot. The nonzero commutator is the mathematical fact from which the uncertainty principle follows — it is the operator algebra, not limitations of measurement apparatus, that prevents simultaneous precision."
```

## Explainer

In classical physics, an observable is simply a function evaluated on the system's state — position, momentum, and energy are numbers you can read off directly. Quantum mechanics replaces this with a more abstract structure: **observables are operators acting on a Hilbert space**. You already know Dirac notation from your prerequisites, so you recognize that an operator Â maps kets to kets: Â|ψ⟩ produces another ket. Every measurable physical quantity — position, momentum, spin, energy — corresponds to a specific operator, and the relationship between operator and measurement outcome is governed by the eigenvalue problem.

The requirement that observables be **Hermitian** (Â = Â†) is not an arbitrary convention — it is forced by two physical requirements. First, measurement outcomes must be real numbers, and Hermitian operators are guaranteed to have real eigenvalues. Second, all probabilities of measurement outcomes must sum to one, which requires eigenstates to form a complete orthonormal basis. Both conditions are secured by Hermiticity. The position operator x̂ (multiplication by x in position space) and the momentum operator p̂ = −iℏ∂/∂x are both Hermitian. The Hamiltonian Ĥ = p̂²/2m + V(x̂) is Hermitian whenever V is a real-valued function — which guarantees energy eigenvalues are real, as physically required.

The **expectation value** ⟨Â⟩ = ⟨ψ|Â|ψ⟩ is the computational bridge between operator formalism and experiment. It predicts the average result over many identical measurements on identically prepared copies of state |ψ⟩. A single measurement yields eigenvalue λₙ with probability |⟨φₙ|ψ⟩|²; the expectation value is the probability-weighted sum ⟨Â⟩ = Σₙ λₙ|⟨φₙ|ψ⟩|². For a spin-½ particle in state |ψ⟩ = cos(θ/2)|↑⟩ + sin(θ/2)|↓⟩, the expectation value of spin ⟨Ŝz⟩ = (ℏ/2)cosθ — a continuous value, even though each individual measurement returns only ±ℏ/2.

The operator framework pays dividends when considering whether two observables can simultaneously have definite values. If two operators commute ([Â, B̂] = 0), they share a common eigenbasis: states exist that are simultaneously eigenstates of both, meaning both quantities can be known precisely at once. If they do not commute ([Â, B̂] ≠ 0), no common eigenbasis exists and simultaneous precision is bounded. The position and momentum operators satisfy [x̂, p̂] = iℏ, so no state can have definite x and definite p simultaneously. The algebra of operators thus encodes the structure of quantum uncertainty: commutators determine which pairs of observables are compatible, and incompatibility leads directly to the uncertainty relations you will encounter in subsequent topics.
