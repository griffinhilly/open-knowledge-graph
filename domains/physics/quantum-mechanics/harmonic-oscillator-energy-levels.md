---
id: harmonic-oscillator-energy-levels
title: Energy Levels and Eigenstates of the Quantum Harmonic Oscillator
domain: physics
course: quantum-mechanics
prerequisites:
- id: ladder-operators
  type: hard
tags:
- energy-levels
- eigenstates
- spectrum
stage: advanced
status: draft
---

# Energy Levels and Eigenstates of the Quantum Harmonic Oscillator

## Core Idea
Eigenstates |n⟩ with energies E_n = (n + ½)ℏω form an orthonormal basis. The spectrum is equally spaced—unique to quadratic potentials.

## Explainer

From your study of ladder operators, you know that the raising operator â† and lowering operator â act algebraically on energy eigenstates: â†|n⟩ = √(n+1)|n+1⟩ and â|n⟩ = √n|n−1⟩. These relations, together with the requirement that no state can have negative energy (the ladder must have a ground floor), forced the existence of a **ground state** |0⟩ satisfying â|0⟩ = 0. Everything about the energy spectrum follows from this structure, without ever solving a differential equation.

The energy eigenvalue equation gives E_n = (n + ½)ℏω for n = 0, 1, 2, … The factor ½ℏω is the **zero-point energy** — the energy of the ground state. This is a purely quantum effect with no classical analogue. A classical oscillator can sit at the bottom of its potential well with zero kinetic and potential energy. A quantum oscillator cannot: the uncertainty principle forbids simultaneously zero position uncertainty and zero momentum uncertainty, so the particle must always be "jiggling," contributing a residual energy even at absolute zero. The zero-point energy is not a mathematical artifact — it has measurable consequences in the Casimir effect and in the stability of matter.

The **equally spaced spectrum** is the most distinctive feature of the quadratic potential. For a general potential V(x), energy levels are not equally spaced — they bunch together at high energy (as in the hydrogen atom's Rydberg levels) or spread apart in other ways. Only the quadratic potential V = ½mω²x² produces perfectly uniform spacing ℏω between adjacent levels. This is why the quantum harmonic oscillator is so important as a building block: any physical system near a stable equilibrium can be approximated by a quadratic potential (via a Taylor expansion), and the first corrections to its spectrum come from the next terms in that expansion. The harmonic oscillator is not just a toy model — it is the universal first approximation.

The states |n⟩ form a **complete orthonormal basis** for the Hilbert space of the oscillator. Any wavefunction can be expanded in them. A coherent state — the quantum state that most closely resembles a classical oscillating particle — is a Poisson-distributed superposition of these number eigenstates. In quantum field theory, this same algebraic structure reappears: â† creates a particle and â destroys one, so the harmonic oscillator energy levels become the occupation numbers of a quantum field mode. What you are learning here is not just one example — it is the algebraic skeleton underlying bosonic fields throughout all of physics.
