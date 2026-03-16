---
id: fokker-planck-equation
title: Fokker-Planck Equation
domain: physics
course: statistical-mechanics
prerequisites:
- id: langevin-equation-stochastic
  type: hard
builds-toward:
- master-equation
tags:
- stochastic
- probability
- evolution
stage: advanced
status: draft
---

# Fokker-Planck Equation

## Core Idea
The Fokker-Planck equation describes how the probability distribution P(x,t) evolves under stochastic dynamics. Derived from the Langevin equation, it generalizes the diffusion equation to include drift due to external forces, and appears in many contexts from Brownian motion to population dynamics.

## Explainer

From the Langevin equation, you know how to describe a single stochastic trajectory: the velocity of a Brownian particle satisfies ṁv = −γv + η(t), where γ is friction and η(t) is white noise. But tracking individual trajectories is impractical when you want to know the distribution of outcomes — where a particle is likely to be at time t, given where it started. The **Fokker-Planck equation** describes the evolution of the probability density P(x, t) directly, without following individual trajectories.

The derivation proceeds by asking: how does P(x, t) change over a short time dt? Particles drift deterministically due to external forces, and they spread stochastically due to noise. Both effects can be captured in terms of the first and second moments of the displacement over dt: the **drift coefficient** A(x) = ⟨Δx⟩/dt and the **diffusion coefficient** D(x) = ⟨(Δx)²⟩/(2dt). The Fokker-Planck equation is then ∂P/∂t = −∂/∂x[A(x) P] + ∂²/∂x²[D(x) P]. The first term is a **continuity equation** for probability under drift — if all particles are pushed to the right by a force, the probability density shifts right. The second term is a **diffusion equation** — noise spreads the distribution.

Connecting back to Brownian motion: for a free particle in a fluid (no external force, A = 0, D = k_BT/γ by the fluctuation-dissipation theorem), the Fokker-Planck equation reduces to the ordinary diffusion equation, and an initially sharp distribution broadens as a Gaussian with variance 2Dt. Add a harmonic confining potential V = ½kx², and A(x) = −kx/γ; the distribution relaxes toward a stationary Gaussian centered at x = 0 — the Boltzmann equilibrium distribution P_eq ∝ exp(−V/k_BT). This illustrates a general result: the stationary solution of the Fokker-Planck equation with thermal noise is always the Boltzmann distribution, providing a direct link between stochastic dynamics and equilibrium statistical mechanics.

The Fokker-Planck equation is a **deterministic partial differential equation** for a probability density, even though it describes an inherently random process. This is its great advantage over the Langevin equation: you can use all the tools of PDEs — Green's functions, eigenfunction expansions, numerical methods — to compute distributions, mean first-passage times, escape rates, and correlation functions. Its reach extends far beyond physics: the Black-Scholes equation in finance, the Kolmogorov forward equation in probability theory, and models of neural firing rates and gene expression are all Fokker-Planck equations in disguise.
