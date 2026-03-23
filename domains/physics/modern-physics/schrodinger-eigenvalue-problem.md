---
id: schrodinger-eigenvalue-problem
title: Time-Independent Schrödinger Equation and Eigenvalues
domain: physics
course: modern-physics
prerequisites:
- id: uncertainty-principle-derivation
  type: hard
- id: schrodinger-equation-intro
  type: soft
builds-toward:
- hydrogen-quantum-mechanics
tags:
- quantum
- schrödinger
- eigenstates
stage: advanced
status: validated
---

# Time-Independent Schrödinger Equation and Eigenvalues

## Core Idea
The time-independent Schrödinger equation Ĥφ = Eφ determines allowed energies (eigenvalues) and stationary states (eigenfunctions). Solutions exist only for discrete energy levels in bound systems. Each eigenstate φₙ has a definite energy Eₙ and does not change shape over time (up to a global phase factor e^(−iEₙt/ℏ)).

## Questions

```yaml
- question: "Why do bound quantum systems have discrete energy levels rather than a continuous range of allowed energies?"
  type: multiple-choice
  options:
    - "The Heisenberg uncertainty principle directly prohibits energies between allowed values"
    - "Physicists assume quantization and build it into the Schrödinger equation as a postulate"
    - "Normalizable solutions satisfying physical boundary conditions exist only for a discrete set of eigenvalues"
    - "The wave function collapses to discrete values during measurement"
  answer: 2
  explanation: "Quantization is not assumed — it falls out of the mathematics. The time-independent Schrödinger equation Ĥφ = Eφ has solutions for any energy E, but most of those solutions blow up at infinity or fail to satisfy the boundary conditions (e.g., φ = 0 at hard walls, φ → 0 as r → ∞). Only for a discrete set of energies Eₙ do normalizable solutions exist. Between the allowed energies, there are simply no physically acceptable solutions. This is the deep reason quantization is real and not just a modeling assumption."

- question: "A particle is in stationary state Ψ(x,t) = φₙ(x)e^(−iEₙt/ℏ). What does the probability density |Ψ(x,t)|² look like at two different times t₁ and t₂?"
  type: multiple-choice
  options:
    - "It oscillates between two different distributions as the phase rotates"
    - "It is identical at both times — the probability distribution does not change"
    - "It slowly spreads out over time as the wave function disperses"
    - "It collapses to a point when the energy is measured at t₂"
  answer: 1
  explanation: "|Ψ(x,t)|² = |φₙ(x)e^(−iEₙt/ℏ)|² = |φₙ(x)|²·|e^(−iEₙt/ℏ)|² = |φₙ(x)|², because the magnitude of any complex exponential e^(iθ) is 1. The time-dependent phase factor cancels when you take the modulus squared, leaving a probability distribution that is identical at every time. 'Stationary' means the probabilities don't change — not that the particle is frozen or that the wave function isn't oscillating."

- question: "Energy quantization in bound quantum systems is a physical assumption that must be imposed on the Schrödinger equation from outside."
  type: true-false
  answer: false
  explanation: "This is the key insight: quantization is a mathematical consequence, not an additional physical assumption. When you solve Ĥφ = Eφ and require that solutions be normalizable and satisfy boundary conditions, you find that acceptable solutions exist only for a discrete set of energies. The mathematics forces quantization on you. This is why the eigenvalue approach is so powerful — it derives the energy spectrum rather than assuming it."

- question: "In a stationary state, measuring the particle's energy multiple times always yields the same result: the eigenvalue Eₙ."
  type: true-false
  answer: true
  explanation: "A stationary state is by definition an eigenstate of the Hamiltonian with eigenvalue Eₙ. From the measurement postulate of quantum mechanics, measuring an observable on an eigenstate of that observable always returns the eigenvalue with certainty. This is in contrast to a superposition state, where energy measurements yield different eigenvalues probabilistically. Stationary states have perfectly definite energy — zero uncertainty in energy, consistent with the energy-time uncertainty relation (a stationary state has a definite frequency and therefore a definite energy)."

- question: "Explain why a 'stationary state' does not mean the particle is at rest or that nothing is happening physically."
  type: short-answer
  answer: "A stationary state is one where the probability distribution |Ψ(x,t)|² does not change over time. The wave function itself is still evolving — it picks up the phase factor e^(−iEₙt/ℏ), which oscillates in time. The particle is still moving (it has kinetic energy), but the probability of finding it in any region remains constant. 'Stationary' refers to time-independence of probabilities, not of the wave function or the particle's motion."
  explanation: "The confusion arises because 'stationary' sounds like 'stopped.' But the Schrödinger equation shows the wave function always evolves as Ψ(x,t) = φ(x)e^(−iEt/ℏ). In a stationary state, this phase factor is global — it multiplies the entire wave function — so when you compute |Ψ|², it cancels. If the particle were actually at rest, it would have zero momentum and zero kinetic energy, which the uncertainty principle rules out for confined particles."
```

## Explainer

The time-independent Schrödinger equation is an **eigenvalue problem**: given the Hamiltonian operator Ĥ (which encodes all the energies in the system), find the special functions φ and numbers E such that Ĥφ = Eφ. You already know this structure from linear algebra — an eigenvector of a matrix is a vector that the matrix stretches or contracts without rotating. Here, φ is the eigenfunction and E is the eigenvalue, but the "matrix" is a differential operator acting on wave functions. The uncertainty principle you studied earlier tells you that a particle in a box cannot have zero energy; the eigenvalue structure explains exactly which energies are allowed.

The most important feature of bound systems is **quantization**: solutions to Ĥφ = Eφ satisfying physical boundary conditions (φ → 0 as r → ∞, or φ = 0 at hard walls) exist only for a discrete set of energies E₁, E₂, E₃, .... This is not assumed — it falls out of the mathematics. Between the allowed energies there are simply no normalizable solutions. A particle in a one-dimensional box of length L, for example, has energies Eₙ = n²π²ℏ²/(2mL²), a sequence that grows as n². Each integer n labels one stationary state.

A **stationary state** is not a state where nothing happens — the particle still moves. It is a state where the probability distribution |φ(x)|² does not change in time. When you attach the full time dependence, the state is Ψ(x,t) = φ(x)e^(−iEt/ℏ). The exponential phase factor oscillates in time, but because probability involves |Ψ|² = |φ|², the phase cancels and the density is constant. That is what "stationary" means: time-independent probabilities. If a particle is not in an eigenstate — say it starts as a superposition of φ₁ and φ₂ — then the two phase factors oscillate at different frequencies and their interference produces a probability density that oscillates in time.

The physical meaning of eigenvalues comes into focus when you think about measurement. From the postulates of quantum mechanics (which this course leads toward), a measurement of energy on a stationary state always returns exactly Eₙ — the eigenvalue — with certainty. On a superposition state, the measurement randomly returns one of the eigenvalues, with probability given by the squared coefficient of each eigenstate in the expansion. The eigenvalue spectrum is therefore the complete menu of possible measurement outcomes. Solving the eigenvalue problem for a given Hamiltonian — a box, a harmonic oscillator, or eventually a hydrogen atom — is the central computational task of quantum mechanics.
