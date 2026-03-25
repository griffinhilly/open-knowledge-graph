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
  type: hard
- id: partial-derivatives
  type: soft
- id: differential-equations-intro
  type: hard
- id: eigenvalues-eigenvectors
  type: hard
- id: eigenvalues-and-eigenvectors
  type: hard
- id: matrix-operations
  type: hard
- id: separation-variables-pde
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

## Questions

```yaml
- question: "In the time-independent Schrödinger equation Ĥψ = Eψ, what kind of mathematical problem is this?"
  type: multiple-choice
  options: ["A differential equation with initial conditions", "An eigenvalue equation where E is the eigenvalue and ψ is the eigenfunction", "A linear system of algebraic equations", "A variational optimization problem"]
  answer: 1
  explanation: "Ĥψ = Eψ is exactly the form of an eigenvalue equation: applying the operator Ĥ to ψ returns a scalar multiple E of ψ. The allowed energy levels E are eigenvalues and the corresponding wavefunctions ψ are eigenfunctions of the Hamiltonian operator. This is why linear algebra and eigenvalues are prerequisites."

- question: "The Schrödinger equation was derived from more fundamental principles, just as Newton's second law can be derived from conservation of momentum."
  type: true-false
  answer: false
  explanation: "The Schrödinger equation is a postulate of quantum mechanics — it was not derived from deeper principles but was proposed by Schrödinger, motivated partly by de Broglie's wave-particle duality. Its justification is empirical: it predicts experimental outcomes with extraordinary accuracy. This is analogous to Newton's second law, which is also a postulate, not a derivation."

- question: "What is the physical role of the potential energy function V(x) in the time-independent Schrödinger equation, and why does changing it change the allowed energy levels?"
  type: short-answer
  answer: "V(x) describes the force environment the particle inhabits (e.g., a box, a harmonic well, a Coulomb potential). Changing V(x) changes the Hamiltonian operator Ĥ, which changes its eigenvalues, so different potentials yield different discrete energy spectra."
  explanation: "The Hamiltonian is Ĥ = −(ℏ²/2m)d²/dx² + V(x). The kinetic part is fixed for a given mass, but V(x) varies by physical situation. The boundary conditions imposed by V(x) (e.g., ψ = 0 at infinite walls) force the wavefunction to satisfy constraints that only discrete values of E can satisfy — this is the origin of energy quantization."
```

## Explainer

From your prerequisite work on wavefunctions, you know that a quantum particle is described not by a definite position and momentum but by a wavefunction ψ whose squared magnitude gives a probability distribution. The Schrödinger equation is the dynamical law that governs how ψ behaves — it is the quantum analogue of Newton's F = ma, telling you how the state of a system evolves.

The time-independent form, Ĥψ = Eψ, applies to stationary states — situations where the probability distribution |ψ|² does not change in time. Written out explicitly in one dimension, it reads −(ℏ²/2m) d²ψ/dx² + V(x)ψ = Eψ. The first term is the kinetic energy operator acting on ψ; V(x)ψ is the potential energy term. Together they form the Hamiltonian operator Ĥ. You have studied eigenvalue equations in linear algebra: Ĥψ = Eψ is exactly that structure, where E is the eigenvalue and ψ is the eigenfunction. The boundary conditions imposed by the physical setup (for example, the wavefunction must go to zero at the walls of a box) restrict which values of E are mathematically allowed — and those allowed values are the quantized energy levels of the system.

It is essential to know that the Schrödinger equation was postulated, not derived. Schrödinger was motivated by de Broglie's idea that particles have wavelengths, and he sought a wave equation that would reproduce the correct energy-momentum relationships. The equation's validity rests entirely on its predictive success: it correctly reproduces atomic spectra, molecular bond lengths, and countless other experimental results. This is philosophically different from, say, deriving kinematic equations from calculus; here the equation is foundational.

The time-dependent form, iℏ ∂ψ/∂t = Ĥψ, generalizes the equation to non-stationary states. When the Hamiltonian has no explicit time dependence, you can separate variables and reduce to the time-independent equation — a technique from partial differential equations you have already studied. Solutions of the time-dependent equation are superpositions of stationary states, each oscillating at a frequency proportional to its energy E/ℏ.

The power of the Schrödinger equation becomes vivid in simple model systems. For the infinite square well (particle in a box), applying boundary conditions ψ = 0 at x = 0 and x = L forces the allowed wavelengths to be integer multiples of L/2, giving discrete energies E_n ∝ n². This is the mechanism of quantization made transparent: not an arbitrary rule, but a consequence of requiring the wavefunction to satisfy boundary conditions. You will use exactly this analysis when you study the particle-in-a-box next.
