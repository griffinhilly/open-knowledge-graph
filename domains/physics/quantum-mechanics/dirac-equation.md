---
id: dirac-equation
title: The Dirac Equation
domain: physics
course: quantum-mechanics
prerequisites:
- id: relativistic-quantum-mechanics
  type: hard
- id: pauli-matrices
  type: hard
tags:
- dirac-equation
- relativistic
- spinors
stage: advanced
status: draft
---

# The Dirac Equation

## Core Idea
The Dirac equation (iγᵘ∂ᵤψ − mψ = 0) is the relativistic wave equation for spin-½ fermions. It predicts the electron's g-factor and positrons. Solutions are 4-component spinors; spin emerges as a relativistic effect.

## Explainer

You know the Schrödinger equation and how Pauli matrices represent spin-½ as two-component spinors. The problem Dirac faced was that the Schrödinger equation is not Lorentz-invariant: it is first-order in time but second-order in space, treating time and space asymmetrically. The **Klein-Gordon equation** (∂²ψ/∂t² = ∇²ψ − m²ψ) fixes this by being second-order in both time and space, but it admits negative-energy solutions and a probability density that is not positive-definite — problems that cannot be patched without a fundamentally different approach.

Dirac's insight was to demand an equation that is *first-order in both time and space*, so that the continuity equation automatically gives a positive-definite probability density. To write E = √(p²c² + m²c⁴) as a first-order operator, he needed to "take the square root" of the operator p²c² + m²c⁴ algebraically. He needed matrices α_i and β satisfying anticommutation relations {α_i, α_j} = 2δᵢⱼ and {α_i, β} = 0. Here your knowledge of Pauli matrices becomes essential: these relations cannot be satisfied by 2×2 matrices alone — the minimum size is 4×4. The **gamma matrices** γᵘ are built from Pauli matrices in block form (the Dirac or Weyl representation being two common choices).

The consequence of needing 4×4 matrices is that the wave function must be a **4-component spinor** ψ — this is not an assumption but is forced by the algebra of Lorentz symmetry. The four components split naturally: two correspond to spin-up and spin-down states of the particle, and two to spin-up and spin-down states of the *antiparticle*. Most remarkably, **spin-½ emerges automatically** from Lorentz symmetry — it is not added by hand as in the non-relativistic Pauli theory. This is one of the deepest results in physics: half-integer spin is an inevitable consequence of combining quantum mechanics with special relativity.

The Dirac equation made two spectacular predictions at the time of its discovery. First, the **electron's anomalous magnetic moment**: the Schrödinger–Pauli theory assumes g = 2; the Dirac equation *derives* g = 2 (plus small corrections from quantum electrodynamics) from first principles, with no free parameters. Second, the negative-energy solutions — initially troubling — were reinterpreted as **antiparticles**. Dirac predicted the positron in 1928, before its experimental discovery in 1932. The original "Dirac sea" picture (negative-energy states are all filled, a hole is a positron) has since been superseded by quantum field theory, where positrons are excitations of the electron field; but the core prediction — that every charged fermion has an antiparticle with opposite charge — follows directly from the structure of the equation and has been confirmed for every known fermion.
