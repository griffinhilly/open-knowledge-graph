---
id: quantum-operators-observables
title: Quantum Operators and Observables
domain: physics
course: modern-physics
prerequisites:
- id: wavefunction-probability-density
  type: hard
builds-toward:
- expectation-values-quantum
tags:
- quantum
- operators
- measurement
stage: advanced
status: draft
---

# Quantum Operators and Observables

## Core Idea
Physical observables (position, momentum, energy) are represented by Hermitian operators acting on wavefunctions. Position operator: x̂ψ = xψ. Momentum operator: p̂ψ = −iℏ∂ψ/∂x. Hamiltonian Ĥ represents total energy. Eigenvalues of operators are the possible measurement outcomes; eigenfunctions are states of definite value.

## Explainer

In classical physics, an observable like momentum is just a number you can read off — it has a definite value at every moment. Quantum mechanics replaces this with a more subtle picture: an **operator** is a mathematical instruction that acts on the wavefunction, and the possible measurement outcomes are the **eigenvalues** of that operator. Think of an operator as a question you ask the quantum state. The eigenvalues are the only answers the state is allowed to give.

You already know the wavefunction ψ(x,t) as a probability amplitude. The **position operator** x̂ is the simplest possible operator — it just multiplies the wavefunction by x. So x̂ψ = xψ. The **momentum operator** p̂ = −iℏ∂/∂x is more interesting: it differentiates ψ with respect to position. This derivative structure captures the deep connection between momentum and spatial variation — a particle whose wavefunction oscillates rapidly in space has high momentum, just as a short-wavelength wave carries high frequency. The factor −iℏ ensures the resulting eigenvalues are real numbers.

**Hermitian operators** are a special class: they are self-adjoint, meaning ∫ψ*(Âφ)dx = ∫(Âψ)*φ dx. Why does this matter? Because Hermitian operators always have real eigenvalues. Since measurement outcomes must be real numbers (you can't measure a complex energy), every physical observable must be represented by a Hermitian operator. The **Hamiltonian** Ĥ = p̂²/2m + V(x) is Hermitian, so it produces real energies. Its eigenvalue equation Ĥψ_n = E_n ψ_n defines the **energy eigenstates** — the stationary states you found when solving the Schrödinger equation.

The eigenfunction picture unifies everything. If ψ happens to be an eigenfunction of operator Â with eigenvalue a, then measuring A on that state will always return a with certainty. But a general wavefunction is a superposition of eigenfunctions: ψ = Σ c_n ψ_n, and measurement returns eigenvalue a_n with probability |c_n|². This is the Born rule applied to operators. The act of measurement collapses the superposition to the corresponding eigenstate. The operator formalism thus gives quantum measurement a precise mathematical structure: operators define what you can measure, eigenfunctions define the definite-value states, and the expansion coefficients determine the probabilities. Every calculation in quantum mechanics — energy levels, selection rules, expectation values — flows from this framework.
