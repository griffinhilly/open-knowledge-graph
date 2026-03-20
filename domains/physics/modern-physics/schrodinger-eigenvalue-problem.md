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
status: draft
---

# Time-Independent Schrödinger Equation and Eigenvalues

## Core Idea
The time-independent Schrödinger equation Ĥφ = Eφ determines allowed energies (eigenvalues) and stationary states (eigenfunctions). Solutions exist only for discrete energy levels in bound systems. Each eigenstate φₙ has a definite energy Eₙ and does not change shape over time (up to a global phase factor e^(−iEₙt/ℏ)).

## Explainer

The time-independent Schrödinger equation is an **eigenvalue problem**: given the Hamiltonian operator Ĥ (which encodes all the energies in the system), find the special functions φ and numbers E such that Ĥφ = Eφ. You already know this structure from linear algebra — an eigenvector of a matrix is a vector that the matrix stretches or contracts without rotating. Here, φ is the eigenfunction and E is the eigenvalue, but the "matrix" is a differential operator acting on wave functions. The uncertainty principle you studied earlier tells you that a particle in a box cannot have zero energy; the eigenvalue structure explains exactly which energies are allowed.

The most important feature of bound systems is **quantization**: solutions to Ĥφ = Eφ satisfying physical boundary conditions (φ → 0 as r → ∞, or φ = 0 at hard walls) exist only for a discrete set of energies E₁, E₂, E₃, .... This is not assumed — it falls out of the mathematics. Between the allowed energies there are simply no normalizable solutions. A particle in a one-dimensional box of length L, for example, has energies Eₙ = n²π²ℏ²/(2mL²), a sequence that grows as n². Each integer n labels one stationary state.

A **stationary state** is not a state where nothing happens — the particle still moves. It is a state where the probability distribution |φ(x)|² does not change in time. When you attach the full time dependence, the state is Ψ(x,t) = φ(x)e^(−iEt/ℏ). The exponential phase factor oscillates in time, but because probability involves |Ψ|² = |φ|², the phase cancels and the density is constant. That is what "stationary" means: time-independent probabilities. If a particle is not in an eigenstate — say it starts as a superposition of φ₁ and φ₂ — then the two phase factors oscillate at different frequencies and their interference produces a probability density that oscillates in time.

The physical meaning of eigenvalues comes into focus when you think about measurement. From the postulates of quantum mechanics (which this course leads toward), a measurement of energy on a stationary state always returns exactly Eₙ — the eigenvalue — with certainty. On a superposition state, the measurement randomly returns one of the eigenvalues, with probability given by the squared coefficient of each eigenstate in the expansion. The eigenvalue spectrum is therefore the complete menu of possible measurement outcomes. Solving the eigenvalue problem for a given Hamiltonian — a box, a harmonic oscillator, or eventually a hydrogen atom — is the central computational task of quantum mechanics.
