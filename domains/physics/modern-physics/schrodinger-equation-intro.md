---
id: schrodinger-equation-intro
title: The Schrödinger Equation
domain: physics
course: modern-physics
prerequisites:
- id: wavefunction-and-probability
  type: hard
- id: differential-equations-intro-separable
  type: hard
- id: de-broglie-wavelength
  type: soft
- id: complex-numbers-intro
  type: soft
- id: partial-derivatives
  type: soft
- id: differential-equations-intro
  type: hard
- id: eigenvalues-eigenvectors
  type: hard
- id: eigenvalues-and-eigenvectors
  type: hard
builds-toward:
- particle-in-a-box
- quantum-tunneling
- quantum-numbers
tags:
- quantum
- schrodinger
- hamiltonian
- time-independent
- eigenvalues
stage: advanced
status: validated
---

# The Schrödinger Equation

## Core Idea
The time-independent Schrödinger equation Ĥψ = Eψ governs stationary states: −(ℏ²/2m)d²ψ/dx² + V(x)ψ = Eψ in one dimension. Solutions give the allowed energy levels E and the corresponding wavefunctions ψ for a particle in a potential V(x). The time-dependent form iℏ ∂ψ/∂t = Ĥψ describes how quantum states evolve in time. Schrödinger's equation plays the role for quantum mechanics that Newton's second law plays for classical mechanics — it is the fundamental equation of motion.

## How It's Best Learned
Apply the time-independent equation first to the infinite square well (particle in a box) where V=0 inside. The boundary conditions ψ=0 at walls force the quantization of k, and hence E, making the reason for discrete energy levels transparent.

## Common Misconceptions
- The Schrödinger equation was derived from first principles — it was postulated (motivated by de Broglie's relation); its validity is justified by its successful predictions.
- The potential V in the equation is the same as the classical potential — yes, this is correct and is a central assumption of non-relativistic quantum mechanics.
- The equation only works for one particle — multi-particle Schrödinger equations exist but in a higher-dimensional configuration space.
