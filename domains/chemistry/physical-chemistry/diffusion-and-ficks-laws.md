---
id: diffusion-and-ficks-laws
title: Diffusion and Fick's Laws
domain: chemistry
course: physical-chemistry
prerequisites:
- id: transport-phenomena-gases
  type: hard
- id: differential-equations-intro-separable
  type: soft
- id: partial-derivatives
  type: soft
- id: kinetic-theory-of-gases
  type: soft
- id: diffusion-and-ficks-laws
  type: hard
tags:
- Ficks-laws
- diffusion-coefficient
- random-walk
- concentration-gradient
- Stokes-Einstein
stage: advanced
status: validated
---

# Diffusion and Fick's Laws

## Core Idea
Fick's first law states that the diffusion flux J = −D(∂c/∂x) is proportional to the concentration gradient, with diffusion coefficient D. Fick's second law ∂c/∂t = D(∂²c/∂x²) describes how concentration profiles evolve in time, with Gaussian spreading: ⟨x²⟩ = 2Dt for one-dimensional diffusion. The diffusion coefficient for a gas scales as D ∝ T^(3/2)/p from kinetic theory; for a sphere in a liquid, the Stokes-Einstein equation gives D = kT/(6πηr), connecting diffusion to viscosity η and solute radius r. Self-diffusion, mutual diffusion, and tracer diffusion coefficients are distinct but related through the Onsager reciprocal relations.

## How It's Best Learned
Solve the diffusion equation analytically for a point source and verify ⟨x²⟩ = 2Dt. Use the Stokes-Einstein equation to estimate the size of proteins from measured diffusion coefficients (a technique used in DLS).

## Common Misconceptions
- Confusing Fick's first law (steady-state flux) with Fick's second law (time-dependent concentration change); the first applies to steady-state, the second to transient diffusion.
- Thinking diffusion only applies to gases; the Stokes-Einstein equation and Fick's laws describe diffusion in liquids and solutions equally well.
