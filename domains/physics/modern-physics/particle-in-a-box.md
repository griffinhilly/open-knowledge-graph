---
id: particle-in-a-box
title: Particle in a Box (Infinite Square Well)
domain: physics
course: modern-physics
prerequisites:
- id: schrodinger-equation-intro
  type: hard
- id: differential-equations-intro
  type: hard
- id: boundary-value-problems-electrostatics
  type: hard
builds-toward:
- quantum-tunneling
- quantum-numbers
- band-theory-intro
tags:
- quantum
- infinite-square-well
- energy-levels
- standing-waves
- zero-point-energy
stage: advanced
status: validated
---

# Particle in a Box (Infinite Square Well)

## Core Idea
A particle confined between rigid walls at x=0 and x=L (where V=0 inside, V=∞ outside) has wavefunctions ψ_n = √(2/L) sin(nπx/L) and quantized energies E_n = n²π²ℏ²/(2mL²) for n = 1, 2, 3, … The lowest allowed energy E₁ > 0 is the zero-point energy — a purely quantum effect arising from the uncertainty principle: confinement in space requires nonzero momentum spread. The model illustrates energy quantization, node structure of wavefunctions, and the role of boundary conditions in selecting allowed states.

## How It's Best Learned
Solve the Schrödinger equation step by step: write down the general solution inside the box, apply boundary conditions to get standing-wave condition kL = nπ, then compute energies. Sketch the first few wavefunctions and probability densities and note the number of nodes.

## Common Misconceptions
- The particle can be at rest at the bottom of the box — the zero-point energy forbids it; E₁ is strictly positive.
- Larger boxes have higher energies — larger L means smaller E_n for fixed n; particles in bigger boxes have lower energy levels.
- The wavefunction outside the box is undefined — it is zero (enforced by infinite potential), and this is what imposes the boundary condition.
