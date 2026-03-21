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

## Questions

```yaml
- question: "A student argues: 'The ground state of a quantum harmonic oscillator must have zero energy, just like a classical oscillator at rest at the bottom of its potential well.' What is the fundamental error?"
  type: multiple-choice
  options:
    - "The quantum oscillator has a continuous energy spectrum, so it has no distinct ground state"
    - "The classical analogy is valid for the ground state but breaks down only for excited states"
    - "The uncertainty principle forbids simultaneously zero position uncertainty and zero momentum uncertainty — a quantum particle 'at rest at the bottom' would violate this — so the ground state must have nonzero energy (½ℏω)"
    - "The student is correct: the zero-point energy is a mathematical artifact of the ladder operator formalism and carries no physical significance"
  answer: 2
  explanation: "A classical oscillator can sit motionless at x = 0 with p = 0. A quantum oscillator cannot: zero position uncertainty (Δx = 0) and zero momentum uncertainty (Δp = 0) would violate ΔxΔp ≥ ℏ/2. The particle must 'jiggle,' and this residual motion contributes energy ½ℏω even at absolute zero. The zero-point energy is real — it contributes to the Casimir effect and to why helium remains liquid at atmospheric pressure near absolute zero."

- question: "What makes the equally-spaced energy spectrum (E_n = (n + ½)ℏω) distinctive compared to other quantum bound-state systems?"
  type: multiple-choice
  options:
    - "No other quantum system has discrete energy levels — only the harmonic oscillator does"
    - "The spacing ℏω between adjacent levels is constant for all n, a property unique to the quadratic potential; other potentials produce levels that bunch together or spread apart with increasing n"
    - "The harmonic oscillator has a ground state energy of zero, unlike other systems"
    - "The levels are equally spaced because the potential is symmetric about x = 0, and all symmetric potentials share this property"
  answer: 1
  explanation: "For the hydrogen atom, energy levels go as −13.6/n² eV, bunching toward zero at large n. For an infinite square well, they grow as n². Only the quadratic potential V = ½mω²x² produces constant spacing ℏω between every adjacent pair. This is a consequence of the algebraic structure: the commutation relation [â, â†] = 1 ensures that applying â† always adds exactly one quantum of energy. Symmetry alone does not produce equal spacing — the infinite square well is also symmetric but has non-equal spacing."

- question: "The zero-point energy ½ℏω is a real, physically measurable quantum effect with no classical analogue."
  type: true-false
  answer: true
  explanation: "A classical oscillator can have zero energy (at rest at equilibrium). The quantum zero-point energy ½ℏω is mandated by the uncertainty principle and has measurable consequences: the Casimir effect (vacuum fluctuations between conducting plates), the stability of matter (zero-point motion prevents electrons from collapsing into the nucleus in a classical sense), and the persistence of helium as a liquid at atmospheric pressure near 0 K (zero-point motion prevents crystallization)."

- question: "The algebraic ladder operator approach to the harmonic oscillator is a convenient shortcut but is less rigorous than directly solving the Schrödinger equation with Hermite polynomials."
  type: true-false
  answer: false
  explanation: "Both approaches are fully rigorous and yield identical results. The algebraic approach uses only the commutation relation [â, â†] = 1 and the positivity of energy to derive all eigenvalues and the structure of eigenstates. No approximation is involved. The Hermite polynomial approach solves the differential equation directly and also produces exact results. The algebraic approach is sometimes preferred precisely because it is more transparent about why the spectrum is equally spaced, and because it generalizes directly to quantum field theory."

- question: "Why does the uncertainty principle guarantee that the ground state of a quantum harmonic oscillator must have nonzero energy?"
  type: short-answer
  answer: "If the ground state had zero energy, the particle would be at rest at the bottom of the potential (x = 0, p = 0), meaning both position and momentum would be exactly zero with no uncertainty. This violates the Heisenberg uncertainty principle ΔxΔp ≥ ℏ/2, which requires that if Δp = 0 then Δx = ∞ (and vice versa). The actual ground state is a compromise: it minimizes total energy E = ⟨p²⟩/2m + ½mω²⟨x²⟩ subject to the uncertainty constraint, yielding the minimum possible energy ½ℏω — exactly the zero-point energy."
  explanation: "This can be made quantitative: write E ≥ (Δp)²/2m + ½mω²(Δx)² and use ΔxΔp = ℏ/2 to substitute Δp = ℏ/(2Δx), then minimize over Δx. The minimum is at Δx = √(ℏ/2mω), giving E_min = ½ℏω. The ground state is the state of minimum uncertainty consistent with the commutation relations."
```

## Explainer

From your study of ladder operators, you know that the raising operator â† and lowering operator â act algebraically on energy eigenstates: â†|n⟩ = √(n+1)|n+1⟩ and â|n⟩ = √n|n−1⟩. These relations, together with the requirement that no state can have negative energy (the ladder must have a ground floor), forced the existence of a **ground state** |0⟩ satisfying â|0⟩ = 0. Everything about the energy spectrum follows from this structure, without ever solving a differential equation.

The energy eigenvalue equation gives E_n = (n + ½)ℏω for n = 0, 1, 2, … The factor ½ℏω is the **zero-point energy** — the energy of the ground state. This is a purely quantum effect with no classical analogue. A classical oscillator can sit at the bottom of its potential well with zero kinetic and potential energy. A quantum oscillator cannot: the uncertainty principle forbids simultaneously zero position uncertainty and zero momentum uncertainty, so the particle must always be "jiggling," contributing a residual energy even at absolute zero. The zero-point energy is not a mathematical artifact — it has measurable consequences in the Casimir effect and in the stability of matter.

The **equally spaced spectrum** is the most distinctive feature of the quadratic potential. For a general potential V(x), energy levels are not equally spaced — they bunch together at high energy (as in the hydrogen atom's Rydberg levels) or spread apart in other ways. Only the quadratic potential V = ½mω²x² produces perfectly uniform spacing ℏω between adjacent levels. This is why the quantum harmonic oscillator is so important as a building block: any physical system near a stable equilibrium can be approximated by a quadratic potential (via a Taylor expansion), and the first corrections to its spectrum come from the next terms in that expansion. The harmonic oscillator is not just a toy model — it is the universal first approximation.

The states |n⟩ form a **complete orthonormal basis** for the Hilbert space of the oscillator. Any wavefunction can be expanded in them. A coherent state — the quantum state that most closely resembles a classical oscillating particle — is a Poisson-distributed superposition of these number eigenstates. In quantum field theory, this same algebraic structure reappears: â† creates a particle and â destroys one, so the harmonic oscillator energy levels become the occupation numbers of a quantum field mode. What you are learning here is not just one example — it is the algebraic skeleton underlying bosonic fields throughout all of physics.
