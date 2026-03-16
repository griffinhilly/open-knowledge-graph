---
id: harmonic-oscillator-quantum
title: Quantum Harmonic Oscillator
domain: physics
course: quantum-mechanics
prerequisites:
- id: ladder-operators
  type: hard
- id: schrodinger-equation-intro
  type: hard
builds-toward:
- zero-point-energy
- coherent-states
tags:
- oscillator
- exactly-solvable
stage: abstract-reasoning
status: draft
---

# Quantum Harmonic Oscillator

## Core Idea
The quantum harmonic oscillator is exactly solvable via ladder operators a† and a. Energy levels are Eₙ = (n + ½)ℏω with n = 0,1,2,.... The ground state has nonzero energy (zero-point energy), with ladder operators elegantly revealing the algebra without differential equations.

## Explainer

The classical harmonic oscillator — a mass on a spring — has energy E = ½kx² + p²/2m that can take any continuous value. The quantum harmonic oscillator, built from the same potential V(x) = ½mω²x², reveals something completely different: energy is quantized in equally spaced steps of ℏω. The elegant way to see this uses the **ladder operators** you already know.

Define a = (mωx̂ + ip̂)/√(2mωℏ) and a† = (mωx̂ − ip̂)/√(2mωℏ). The Hamiltonian then becomes H = ℏω(a†a + ½). The operator N̂ = a†a is the **number operator** — it counts quanta of vibration and has eigenvalues n = 0, 1, 2, 3, .... The energy eigenvalues are Eₙ = (n + ½)ℏω. The factor of ½ is not a rounding artifact — it is the **zero-point energy**, the irreducible ground-state energy even when no quanta are present. Unlike a classical spring that can sit at rest with zero energy, the quantum oscillator cannot stop fluctuating; the uncertainty principle forbids simultaneously zero position and zero momentum, so the ground state must carry energy E₀ = ½ℏω.

The ladder operators earn their name because a†|n⟩ = √(n+1)|n+1⟩ creates an additional quantum (climbs the ladder) while a|n⟩ = √n|n−1⟩ destroys one (descends). Starting from the ground state |0⟩, which satisfies a|0⟩ = 0, you can construct every energy eigenstate by repeated application of a†. This algebraic approach is far more powerful than solving the differential equation directly: it reveals the energy structure without any special functions, and the commutation relation [a, a†] = 1 does all the heavy lifting.

The quantum harmonic oscillator matters far beyond springs. Any smooth potential near its minimum looks parabolic for small oscillations — so this model describes vibrations of diatomic molecules, phonons in crystalline solids, and modes of optical cavities. When you study quantum field theory, a and a† become **photon creation and annihilation operators**: each mode of the electromagnetic field is a quantum harmonic oscillator, and the vacuum (n = 0 for every mode) still carries zero-point fluctuations in every mode. The algebra you master here is literally the algebra of light.
