---
id: quantum-chemistry-foundations
title: Quantum Chemistry Foundations
domain: chemistry
course: physical-chemistry
prerequisites:
- id: schrodinger-equation-intro
  type: hard
- id: wavefunction-and-probability
  type: hard
- id: atomic-orbitals
  type: hard
- id: heisenberg-uncertainty-principle
  type: soft
- id: electron-configuration
  type: soft
- id: wave-particle-duality
  type: soft
- id: particle-in-a-box
  type: soft
- id: differential-equations-intro-separable
  type: soft
- id: quantum-mechanics-postulates-core
  type: hard
builds-toward:
- born-oppenheimer-approximation
- hydrogen-atom-wavefunctions
- harmonic-oscillator-molecular-vibrations
tags:
- quantum
- wavefunctions
- operators
- observables
stage: advanced
status: validated
---

# Quantum Chemistry Foundations

## Core Idea
Quantum chemistry applies the postulates of quantum mechanics to chemical systems, treating electrons and nuclei as quantum particles described by wavefunctions. Measurable properties correspond to eigenvalues of Hermitian operators, and the expectation value of an observable is computed as the integral of ψ*Ôψ over all space. The time-independent Schrödinger equation Ĥψ = Eψ is the central equation, with the Hamiltonian operator encoding kinetic and potential energy. Exact solutions exist only for one-electron systems; all multi-electron systems require approximations.

## How It's Best Learned
Start by becoming fluent with operator algebra and bra-ket notation before applying it to chemical systems. Revisit the hydrogen atom solutions from physics and reinterpret them chemically — orbital shapes, nodal surfaces, and energies all follow directly from the wavefunction.

## Common Misconceptions
- Confusing the wavefunction ψ with probability — ψ itself can be negative or complex; |ψ|² is the probability density.
- Thinking operators always commute; non-commuting operators encode the uncertainty principle.
- Assuming quantum chemistry only applies to small systems — it underlies all bonding, spectroscopy, and reactivity.
