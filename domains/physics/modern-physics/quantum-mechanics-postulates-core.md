---
id: quantum-mechanics-postulates-core
title: Core Postulates of Quantum Mechanics
domain: physics
course: modern-physics
prerequisites:
- id: wave-particle-duality-observations
  type: hard
- id: classical-limit-correspondence
  type: soft
builds-toward:
- schrodinger-equation-time-dependent
- probability-amplitude-interpretation
tags:
- quantum-foundations
- postulates
stage: advanced
status: validated
---
# Core Postulates of Quantum Mechanics

## Core Idea
Quantum mechanics is built on five key postulates: (1) A quantum system is described by a state vector in Hilbert space, (2) Observables correspond to Hermitian operators, (3) Measurement outcomes are eigenvalues of operators, (4) Measurement collapses the state into an eigenstate, (5) Time evolution is governed by the Schrödinger equation. These postulates form the mathematical foundation for all quantum mechanical calculations and predictions.

## Questions

```yaml
- question: "Before a measurement is made, a quantum particle is in a superposition of two energy eigenstates. According to the postulates, what determines the possible outcomes when energy is measured?"
  type: multiple-choice
  options:
    - "The average (expectation) value of the energy operator."
    - "The eigenvalues of the Hamiltonian operator corresponding to those eigenstates."
    - "The amplitude of the highest-energy eigenstate in the superposition."
    - "The energy of the particle at the moment just before measurement."
  answer: 1
  explanation: "Postulate 3 states that the possible outcomes of measuring an observable are the eigenvalues of the corresponding Hermitian operator. For energy, that operator is the Hamiltonian H. The actual outcome of any single measurement will be one of these eigenvalues; the probabilities of each are given by Born's rule (the squared moduli of the expansion coefficients). The expectation value is the average over many measurements, not a possible single outcome."

- question: "Before measurement, a quantum particle in superposition is 'really' in one definite eigenstate — we just don't know which one. The measurement merely reveals a pre-existing value."
  type: true-false
  answer: false
  explanation: "This is the hidden-variable interpretation, which contradicts the standard (Copenhagen) reading of the postulates. According to the postulates, the state vector IS the complete description of the system — there is no hidden underlying state. Bell's theorem and experiments (Aspect et al.) rule out local hidden-variable theories. The superposition is physically real, not merely a statement of ignorance. Measurement causes a genuine change (collapse) to an eigenstate, not a revelation of a pre-existing value."

- question: "Why must quantum mechanical observables correspond to Hermitian operators rather than arbitrary linear operators?"
  type: short-answer
  answer: "Hermitian operators have real eigenvalues, which is required because measurement outcomes must be real numbers (we can't measure an imaginary energy). Hermitian operators also have orthogonal eigenstates, which allows any state to be expanded uniquely in terms of them. Both properties are essential for the postulates to be physically consistent."
  explanation: "A non-Hermitian operator could have complex eigenvalues, which would correspond to unmeasurable complex-valued physical quantities. The mathematical requirement of Hermiticity is exactly what ensures the physical requirement of real-valued measurement outcomes. Hermitian operators also guarantee a complete orthonormal basis of eigenstates, enabling Born rule calculations."
```

## Explainer

Classical mechanics describes a system by specifying the positions and momenta of all its parts at each moment. Quantum mechanics replaces this picture entirely: a system is described not by a list of definite values but by a *state vector* |ψ⟩ living in a Hilbert space — an abstract vector space equipped with an inner product. The state vector encodes all the probabilistic information about what would happen if you measured any observable. Before measurement, many observables simply do not have definite values; the system is genuinely in a superposition.

The second postulate assigns a Hermitian operator to every observable quantity — position, momentum, energy, spin. The requirement of Hermiticity is not arbitrary: Hermitian operators have real eigenvalues (so that measurement outcomes are real numbers) and a complete set of orthonormal eigenstates (so that any state can be written as a superposition of them). The Hamiltonian H is the energy operator; position and momentum have their own operators that satisfy a canonical commutation relation, [x̂, p̂] = iℏ, which encodes the uncertainty principle.

The third and fourth postulates govern measurement. When you measure an observable, the only possible outcomes are the operator's eigenvalues. Which eigenvalue you actually get is random — governed by Born's rule: the probability of getting eigenvalue λ_n is |⟨n|ψ⟩|², the squared modulus of the inner product between the state and the corresponding eigenstate. Immediately after the measurement, the state *collapses* to that eigenstate (Postulate 4). This is a discontinuous, nonlinear change — fundamentally different from the smooth time evolution described by the Schrödinger equation, and the source of much philosophical debate about what measurement physically means.

The fifth postulate covers everything between measurements: time evolution is governed by the Schrödinger equation, iℏ d|ψ⟩/dt = H|ψ⟩. This is linear, deterministic, and reversible. If you know the state at time t₀, you can calculate it at any later time with no randomness — until a measurement occurs. The tension between this smooth unitary evolution and the abrupt collapse of measurement is the heart of the quantum measurement problem, which remains an active philosophical and foundational issue.

Coming from wave-particle duality, you have already seen that quantum entities behave differently depending on how they are measured. These postulates make that precise: the state vector is not a wave or a particle but a mathematical object encoding the probabilities of all possible measurement outcomes. What the state vector "really is" — whether it describes objective reality, our knowledge, or something else — is debated by interpretations of quantum mechanics (Copenhagen, Many-Worlds, Bohmian mechanics). But regardless of interpretation, the postulates give an unambiguous algorithm for calculating experimental predictions, and they match experiment to extraordinary precision.
