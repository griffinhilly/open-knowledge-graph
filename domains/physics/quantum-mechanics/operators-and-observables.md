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

## Explainer

In classical physics, an observable is simply a function evaluated on the system's state — position, momentum, and energy are numbers you can read off directly. Quantum mechanics replaces this with a more abstract structure: **observables are operators acting on a Hilbert space**. You already know Dirac notation from your prerequisites, so you recognize that an operator Â maps kets to kets: Â|ψ⟩ produces another ket. Every measurable physical quantity — position, momentum, spin, energy — corresponds to a specific operator, and the relationship between operator and measurement outcome is governed by the eigenvalue problem.

The requirement that observables be **Hermitian** (Â = Â†) is not an arbitrary convention — it is forced by two physical requirements. First, measurement outcomes must be real numbers, and Hermitian operators are guaranteed to have real eigenvalues. Second, all probabilities of measurement outcomes must sum to one, which requires eigenstates to form a complete orthonormal basis. Both conditions are secured by Hermiticity. The position operator x̂ (multiplication by x in position space) and the momentum operator p̂ = −iℏ∂/∂x are both Hermitian. The Hamiltonian Ĥ = p̂²/2m + V(x̂) is Hermitian whenever V is a real-valued function — which guarantees energy eigenvalues are real, as physically required.

The **expectation value** ⟨Â⟩ = ⟨ψ|Â|ψ⟩ is the computational bridge between operator formalism and experiment. It predicts the average result over many identical measurements on identically prepared copies of state |ψ⟩. A single measurement yields eigenvalue λₙ with probability |⟨φₙ|ψ⟩|²; the expectation value is the probability-weighted sum ⟨Â⟩ = Σₙ λₙ|⟨φₙ|ψ⟩|². For a spin-½ particle in state |ψ⟩ = cos(θ/2)|↑⟩ + sin(θ/2)|↓⟩, the expectation value of spin ⟨Ŝz⟩ = (ℏ/2)cosθ — a continuous value, even though each individual measurement returns only ±ℏ/2.

The operator framework pays dividends when considering whether two observables can simultaneously have definite values. If two operators commute ([Â, B̂] = 0), they share a common eigenbasis: states exist that are simultaneously eigenstates of both, meaning both quantities can be known precisely at once. If they do not commute ([Â, B̂] ≠ 0), no common eigenbasis exists and simultaneous precision is bounded. The position and momentum operators satisfy [x̂, p̂] = iℏ, so no state can have definite x and definite p simultaneously. The algebra of operators thus encodes the structure of quantum uncertainty: commutators determine which pairs of observables are compatible, and incompatibility leads directly to the uncertainty relations you will encounter in subsequent topics.
