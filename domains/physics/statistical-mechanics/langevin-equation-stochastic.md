---
id: langevin-equation-stochastic
title: Langevin Equation
domain: physics
course: statistical-mechanics
prerequisites:
- id: brownian-motion
  type: hard
- id: newton-second-law
  type: hard
builds-toward:
- fokker-planck-equation
tags:
- stochastic
- dynamics
- noise
stage: advanced
status: draft
---

# Langevin Equation

## Core Idea
The Langevin equation m(dv/dt) = F - γv + ξ(t) describes particle motion with damping and random thermal noise. The friction coefficient γ and noise variance are related through the fluctuation-dissipation theorem, making this equation fundamental to modeling thermal motion, molecular dynamics, and response to external forces.

## Explainer

From your study of Brownian motion, you know that a small particle suspended in a fluid is constantly bombarded by solvent molecules, executing an irregular random walk. The Langevin equation gives that random walk a precise dynamical description by writing down a Newton's second law that explicitly includes both the dissipative and the random aspects of the environment. The equation m dv/dt = F − γv + ξ(t) has three terms: an external force F, a viscous drag −γv proportional to velocity, and a **stochastic force** ξ(t) representing the rapid, uncorrelated kicks from solvent molecules.

The stochastic force ξ(t) is modeled as **Gaussian white noise**: ⟨ξ(t)⟩ = 0 (zero mean, since kicks arrive from all directions equally) and ⟨ξ(t)ξ(t')⟩ = 2γk_BT δ(t − t') (correlations are instantaneous). The key relationship here is that the noise strength 2γk_BT is not a free parameter — it is completely determined by the drag coefficient γ and the temperature T. This is the **fluctuation-dissipation theorem** in its simplest form: the same molecular collisions that cause dissipation (drag) also cause fluctuations (noise), and the ratio between them is set by temperature. You cannot have one without the other: a frictionless fluid would also be noiseless, which would allow the particle to cool below ambient temperature — violating thermodynamics.

Without noise (ξ = 0), the Langevin equation is just exponential velocity decay: v(t) = v₀ e^{−γt/m}, characterized by the **relaxation time** τ = m/γ. For a micron-sized particle in water, τ is on the order of microseconds — very fast. On timescales much longer than τ, the inertial term m dv/dt becomes negligible and the equation reduces to the **overdamped Langevin equation**: γ dx/dt = F + ξ(t). This overdamped limit is the relevant regime for most biological molecular machines, polymer dynamics, and colloidal particles.

Solving the Langevin equation (with F = 0, overdamped) gives the diffusion coefficient D = k_BT/γ — this is the **Einstein relation**, connecting the random-walk diffusion constant to drag and temperature. From D you recover the mean-squared displacement ⟨x²⟩ = 2Dt, which is the signature of Brownian diffusion you already know. The Langevin framework thus unifies the phenomenology of Brownian motion (random walk, diffusion coefficient) with a microscopic dynamical picture, and extends it to handle external forces, confined geometries, and coupled degrees of freedom — the starting point for modern molecular dynamics simulation.
