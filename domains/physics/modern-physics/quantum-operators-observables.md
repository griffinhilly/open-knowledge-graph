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

## Questions

```yaml
- question: "An electron is in the state ψ = (1/√2)ψ₁ + (1/√2)ψ₂, where ψ₁ and ψ₂ are momentum eigenstates with eigenvalues p₁ and p₂. What is the electron's momentum before measurement?"
  type: multiple-choice
  options:
    - "The average (p₁ + p₂)/2 — the superposition represents a definite momentum equal to the mean of the eigenvalues"
    - "Either p₁ or p₂, with probability 1/2 each — there is no definite momentum before measurement, only a probability distribution"
    - "Zero — the two momentum components cancel because the coefficients are equal"
    - "Both p₁ and p₂ simultaneously — quantum mechanics allows particles to have multiple definite values at once"
  answer: 1
  explanation: "In quantum mechanics, a superposition state does not have a definite value for an observable unless it is an eigenstate of the corresponding operator. Before measurement, the electron's momentum is genuinely indefinite — not merely unknown. The Born rule tells us that measurement returns p₁ with probability 1/2 and p₂ with probability 1/2. Option A gives the expectation value (average over many measurements) but this is not the pre-measurement momentum. Option D gestures at superposition correctly but 'simultaneously' is misleading — each individual measurement returns exactly one definite eigenvalue."

- question: "Why is it physically essential that every observable quantity in quantum mechanics be represented by a Hermitian operator?"
  type: multiple-choice
  options:
    - "Because only Hermitian operators can be applied to complex-valued wavefunctions"
    - "Because Hermitian operators always commute with each other, ensuring observables can be measured simultaneously"
    - "Because Hermitian operators guarantee real eigenvalues, and every measurement outcome must be a real number"
    - "Because Hermitian operators preserve the norm of the wavefunction, ensuring probability is conserved"
  answer: 2
  explanation: "When you measure momentum, energy, or position, the result is always a real number — you cannot measure a complex energy. A Hermitian operator is self-adjoint (∫ψ*(Âφ)dx = ∫(Âψ)*φ dx), and this property guarantees all eigenvalues are real. If observables were represented by non-Hermitian operators, eigenvalues could be complex, giving unphysical measurement outcomes. Note: Option B is false (Hermitian operators do not generally commute — non-commuting Hermitian operators represent complementary observables like position and momentum). Option D describes unitary operators."

- question: "The momentum operator p̂ = −iℏ∂/∂x acts on a wavefunction by multiplying it by the particle's current momentum value, analogous to how the position operator multiplies by x."
  type: true-false
  answer: false
  explanation: "The position operator x̂ acts by multiplication: x̂ψ(x) = xψ(x). The momentum operator is fundamentally different — it acts by differentiation: p̂ψ(x) = −iℏ ∂ψ/∂x. This derivative structure captures the quantum connection between momentum and spatial variation: a wavefunction oscillating rapidly in space has high momentum, just as a short-wavelength wave carries high frequency. The eigenfunctions of p̂ are plane waves e^{ipx/ℏ}, not delta functions. The multiplicative structure of x̂ versus the differential structure of p̂ is exactly why they satisfy the canonical commutation relation [x̂, p̂] = iℏ rather than commuting."

- question: "If a quantum system is in an eigenstate of the Hamiltonian Ĥ with eigenvalue E, every measurement of the system's energy will return E with certainty."
  type: true-false
  answer: true
  explanation: "This is the defining property of an eigenstate: Ĥψ = Eψ means ψ contains only one energy component. Expanding in the energy eigenbasis, all coefficients cₙ are zero except one (c_k = 1), so the Born rule assigns probability |c_k|² = 1 to measuring E_k and probability 0 to all other energies. These are stationary states — their probability distributions for all observables are time-independent. A general superposition state Σcₙψₙ does NOT have a definite energy and will yield different eigenvalues on different measurements with probabilities |cₙ|²."

- question: "Explain what happens to a quantum state when a measurement is made, using the operator/eigenfunction framework. How do the expansion coefficients determine the probability of each outcome?"
  type: short-answer
  answer: "Before measurement, a general state ψ is expanded in the eigenbasis of the observable's operator: ψ = Σcₙψₙ, where Âψₙ = aₙψₙ. The Born rule states that measuring observable A returns eigenvalue aₙ with probability |cₙ|². The measurement collapses the superposition — after returning eigenvalue aₙ, the state is now the corresponding eigenstate ψₙ. The expansion coefficients cₙ encode how much of each eigenstate the original wavefunction contained, and their squared magnitudes give the probability distribution over possible outcomes. Measuring does not reveal a pre-existing value; it collapses a genuine indefiniteness into one definite eigenvalue."
  explanation: "The key insight is that measurement is not passive revelation of a pre-existing fact — it is an interaction that projects the state onto an eigenstate. The operator defines what is measured, eigenfunctions define the possible definite-value states, and the decomposition of ψ in the eigenbasis determines the probability distribution. Every quantum calculation — energy levels, selection rules, expectation values — flows from this framework."
```

## Explainer

In classical physics, an observable like momentum is just a number you can read off — it has a definite value at every moment. Quantum mechanics replaces this with a more subtle picture: an **operator** is a mathematical instruction that acts on the wavefunction, and the possible measurement outcomes are the **eigenvalues** of that operator. Think of an operator as a question you ask the quantum state. The eigenvalues are the only answers the state is allowed to give.

You already know the wavefunction ψ(x,t) as a probability amplitude. The **position operator** x̂ is the simplest possible operator — it just multiplies the wavefunction by x. So x̂ψ = xψ. The **momentum operator** p̂ = −iℏ∂/∂x is more interesting: it differentiates ψ with respect to position. This derivative structure captures the deep connection between momentum and spatial variation — a particle whose wavefunction oscillates rapidly in space has high momentum, just as a short-wavelength wave carries high frequency. The factor −iℏ ensures the resulting eigenvalues are real numbers.

**Hermitian operators** are a special class: they are self-adjoint, meaning ∫ψ*(Âφ)dx = ∫(Âψ)*φ dx. Why does this matter? Because Hermitian operators always have real eigenvalues. Since measurement outcomes must be real numbers (you can't measure a complex energy), every physical observable must be represented by a Hermitian operator. The **Hamiltonian** Ĥ = p̂²/2m + V(x) is Hermitian, so it produces real energies. Its eigenvalue equation Ĥψ_n = E_n ψ_n defines the **energy eigenstates** — the stationary states you found when solving the Schrödinger equation.

The eigenfunction picture unifies everything. If ψ happens to be an eigenfunction of operator Â with eigenvalue a, then measuring A on that state will always return a with certainty. But a general wavefunction is a superposition of eigenfunctions: ψ = Σ c_n ψ_n, and measurement returns eigenvalue a_n with probability |c_n|². This is the Born rule applied to operators. The act of measurement collapses the superposition to the corresponding eigenstate. The operator formalism thus gives quantum measurement a precise mathematical structure: operators define what you can measure, eigenfunctions define the definite-value states, and the expansion coefficients determine the probabilities. Every calculation in quantum mechanics — energy levels, selection rules, expectation values — flows from this framework.
