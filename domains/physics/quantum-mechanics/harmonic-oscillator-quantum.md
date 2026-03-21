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
stage: advanced
status: draft
---

# Quantum Harmonic Oscillator

## Core Idea
The quantum harmonic oscillator is exactly solvable via ladder operators a† and a. Energy levels are Eₙ = (n + ½)ℏω with n = 0,1,2,.... The ground state has nonzero energy (zero-point energy), with ladder operators elegantly revealing the algebra without differential equations.

## Questions

```yaml
- question: "A quantum harmonic oscillator is in its ground state |0⟩. A student claims it has zero energy since it contains no quanta of vibration. Which response is correct?"
  type: multiple-choice
  options:
    - "The student is correct — zero quanta means zero energy"
    - "The oscillator has energy E₀ = ½ℏω, because the uncertainty principle forbids both zero position and zero momentum simultaneously"
    - "The oscillator has zero energy only if it is not being measured"
    - "The energy is undefined in the ground state"
  answer: 1
  explanation: "The ground state |0⟩ contains no quanta of vibration (n = 0), but Eₙ = (n + ½)ℏω gives E₀ = ½ℏω ≠ 0. This zero-point energy is not an artifact — it is required by the uncertainty principle. Zero energy would demand simultaneously zero position and zero momentum, violating ΔxΔp ≥ ℏ/2. The classical spring can sit at rest; the quantum oscillator cannot."

- question: "Two quantum harmonic oscillators share the same natural frequency ω but are in eigenstates |n=2⟩ and |n=5⟩. What is the energy difference between them?"
  type: multiple-choice
  options:
    - "2ℏω"
    - "3ℏω"
    - "3.5ℏω"
    - "5ℏω"
  answer: 1
  explanation: "Eₙ = (n + ½)ℏω, so E₅ = 5.5ℏω and E₂ = 2.5ℏω. The difference is 3ℏω — three equally-spaced rungs of the ladder. The zero-point energy cancels in the difference. A common error is computing 5 − 2 = 3 correctly but then mistakenly writing 3.5ℏω by half-counting the zero-point contribution, which already cancels out."

- question: "Applying the lowering operator a to the ground state |0⟩ produces |−1⟩, the state with negative energy E = −½ℏω."
  type: true-false
  answer: false
  explanation: "a|0⟩ = 0 (the null vector), not a new energy eigenstate. The ground state is defined precisely by the condition a|0⟩ = 0 — there is no lower rung. If a|0⟩ yielded |−1⟩, the energy spectrum would extend to negative infinity with no ground state, which is physically impossible for a bound harmonic potential."

- question: "The energy levels of the quantum harmonic oscillator are equally spaced, with any two adjacent levels separated by exactly ℏω regardless of which levels are compared."
  type: true-false
  answer: true
  explanation: "Since Eₙ = (n + ½)ℏω, the difference between consecutive levels is always Eₙ₊₁ − Eₙ = ℏω. This equal spacing is a special property of the harmonic potential — it is not true for, say, the hydrogen atom (where level spacing decreases with n). The equal spacing underlies the use of ladder operators a and a† and is the algebraic foundation for quantum field theory's treatment of particles as excitations."

- question: "Why must the ground state of the quantum harmonic oscillator have nonzero energy, and what would be physically violated if it did not?"
  type: short-answer
  answer: "Zero energy would require simultaneously zero kinetic energy (p = 0) and zero potential energy (x = 0), meaning the particle sits perfectly still at the equilibrium point. This violates the Heisenberg uncertainty principle ΔxΔp ≥ ℏ/2, which forbids exact simultaneous knowledge of position and momentum. The zero-point energy E₀ = ½ℏω represents the minimum irreducible quantum fluctuation consistent with this constraint."
  explanation: "This is the key conceptual difference from a classical oscillator. Classically, the minimum energy is zero (the spring at rest). Quantum mechanically, the uncertainty principle enforces a floor. The same logic applies to every mode of the electromagnetic field in quantum field theory — each mode is a harmonic oscillator with zero-point energy ½ℏω — which sums to the vacuum energy of quantum field theory."
```

## Explainer

The classical harmonic oscillator — a mass on a spring — has energy E = ½kx² + p²/2m that can take any continuous value. The quantum harmonic oscillator, built from the same potential V(x) = ½mω²x², reveals something completely different: energy is quantized in equally spaced steps of ℏω. The elegant way to see this uses the **ladder operators** you already know.

Define a = (mωx̂ + ip̂)/√(2mωℏ) and a† = (mωx̂ − ip̂)/√(2mωℏ). The Hamiltonian then becomes H = ℏω(a†a + ½). The operator N̂ = a†a is the **number operator** — it counts quanta of vibration and has eigenvalues n = 0, 1, 2, 3, .... The energy eigenvalues are Eₙ = (n + ½)ℏω. The factor of ½ is not a rounding artifact — it is the **zero-point energy**, the irreducible ground-state energy even when no quanta are present. Unlike a classical spring that can sit at rest with zero energy, the quantum oscillator cannot stop fluctuating; the uncertainty principle forbids simultaneously zero position and zero momentum, so the ground state must carry energy E₀ = ½ℏω.

The ladder operators earn their name because a†|n⟩ = √(n+1)|n+1⟩ creates an additional quantum (climbs the ladder) while a|n⟩ = √n|n−1⟩ destroys one (descends). Starting from the ground state |0⟩, which satisfies a|0⟩ = 0, you can construct every energy eigenstate by repeated application of a†. This algebraic approach is far more powerful than solving the differential equation directly: it reveals the energy structure without any special functions, and the commutation relation [a, a†] = 1 does all the heavy lifting.

The quantum harmonic oscillator matters far beyond springs. Any smooth potential near its minimum looks parabolic for small oscillations — so this model describes vibrations of diatomic molecules, phonons in crystalline solids, and modes of optical cavities. When you study quantum field theory, a and a† become **photon creation and annihilation operators**: each mode of the electromagnetic field is a quantum harmonic oscillator, and the vacuum (n = 0 for every mode) still carries zero-point fluctuations in every mode. The algebra you master here is literally the algebra of light.
