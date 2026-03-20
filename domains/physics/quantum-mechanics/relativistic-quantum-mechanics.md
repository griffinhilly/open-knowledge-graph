---
id: relativistic-quantum-mechanics
title: Relativistic Quantum Mechanics
domain: physics
course: quantum-mechanics
prerequisites:
- id: dirac-notation
  type: hard
builds-toward:
- dirac-equation
tags:
- relativistic-qm
- special-relativity
stage: formal-systems
status: draft
---

# Relativistic Quantum Mechanics

## Core Idea
Schrödinger equation is not Lorentz covariant. The Klein-Gordon (spin-0) and Dirac (spin-½) equations are relativistically invariant. Negative-energy solutions interpret as antiparticles, naturally leading to quantum field theory.

## Explainer

The Schrödinger equation treats time and space asymmetrically: it has a first derivative in time but second derivatives in space. Under a Lorentz boost — a change to a moving reference frame — this asymmetry breaks the equation's form, which means it cannot describe particles moving at relativistic speeds. The requirement of **Lorentz covariance** demands that the equation take the same form in all inertial frames, so the derivatives in time and space must appear symmetrically. The simplest relativistic equation uses the energy-momentum relation E² = (pc)² + (mc²)² and replaces E → iℏ∂/∂t and **p** → −iℏ∇ to get an equation with second derivatives in both space and time.

The result is the **Klein-Gordon equation**: (□ + m²c²/ℏ²)φ = 0, where □ is the d'Alembert operator. This works for spin-0 particles like pions. But it has a problem: the conserved current density can be negative, which would mean negative probability — physically nonsensical. More deeply, the Klein-Gordon equation has solutions with both positive and negative energy, and there is no simple way to discard the negative-energy solutions while keeping a complete set of states.

Dirac approached the problem differently. He required an equation **linear** in both space and time derivatives, of the form (iℏγ^μ ∂_μ − mc)ψ = 0. For this to be consistent with the relativistic energy-momentum relation, the coefficients γ^μ cannot be ordinary numbers — they must be 4×4 matrices, now called **Dirac matrices**. The wave function ψ becomes a four-component spinor. Two components represent spin-up and spin-down for positive energy, and two components represent spin-up and spin-down for negative energy. This doubling is not a defect; it is a prediction: for every particle, there exists an **antiparticle** with the same mass but opposite charge. The positron, discovered in 1932, confirmed this prediction.

The negative-energy sea interpretation (filled Dirac sea) was Dirac's original resolution, but it only works for fermions and becomes unwieldy. The modern understanding is that the correct framework is **quantum field theory**, where both positive- and negative-energy solutions are reinterpreted: the positive-energy modes are particle creation operators and the negative-energy modes are antiparticle annihilation operators. Relativistic quantum mechanics — Klein-Gordon and Dirac equations — works as a one-particle approximation when particle creation is suppressed, but the deeper truth is a field theory. This is where your Dirac notation and operator formalism become indispensable: the full machinery carries over directly into quantum field theory.
