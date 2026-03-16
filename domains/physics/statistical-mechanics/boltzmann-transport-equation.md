---
id: boltzmann-transport-equation
title: Boltzmann Transport Equation
domain: physics
course: statistical-mechanics
prerequisites:
- id: kinetic-theory-of-gases
  type: hard
- id: partial-derivatives
  type: hard
builds-toward:
- h-theorem-irreversibility
tags:
- transport
- kinetic-theory
- non-equilibrium
stage: advanced
status: draft
---

# Boltzmann Transport Equation

## Core Idea
The Boltzmann equation ∂f/∂t + v·∇f + F/m·∇_v f = (∂f/∂t)_{coll} describes the evolution of the single-particle distribution f(r,v,t) under external forces F and collisions. The collision term (∂f/∂t)_{coll} is typically approximated as −(f − f^eq)/τ (relaxation-time approximation). It governs viscosity, thermal conductivity, and electrical conductivity in gases and weakly-coupled plasmas.

## Explainer

From kinetic theory, you know that a dilute gas can be described by a **distribution function** f(r, v, t): the density of particles in the six-dimensional phase space of positions and velocities at time t. The Maxwell-Boltzmann distribution f^eq ∝ exp(−mv²/2kT) is the equilibrium form. The Boltzmann transport equation is the dynamical law governing how f evolves when the gas is not in equilibrium — when there are density gradients, temperature gradients, or external forces driving a current.

Think of the left-hand side as a total time derivative of f following a particle's trajectory through phase space. The term ∂f/∂t is the explicit time change at a fixed point. The term **v · ∇f** (spatial streaming) accounts for particles drifting between neighboring positions: if more fast particles are entering a region from the left than leaving on the right, f there will change. The term **(F/m) · ∇_v f** (force streaming) does the same in velocity space: an external force like gravity or an electric field accelerates particles, shifting f toward higher or lower velocities. Together these three terms describe perfectly free flow in phase space — Liouville's theorem says they would sum to zero for a Hamiltonian system with no collisions.

The right-hand side, the **collision term** (∂f/∂t)_{coll}, represents the effect of binary collisions that scatter particles from one velocity to another. In the full Boltzmann collision integral, you sum over all possible in-scattering and out-scattering events weighted by cross-sections — this is where the physics of molecular interactions enters. The **relaxation-time approximation** replaces all this complexity with a single rate: −(f − f^eq)/τ, where τ is a characteristic collision time. The idea is simple: collisions drive f back toward equilibrium, and they do so at a rate 1/τ. This approximation is often good enough to derive Ohm's law, Fourier's law of heat conduction, and Fick's law of diffusion in a unified framework.

The Boltzmann equation occupies a special position in physics because it bridges two levels of description. The microscopic input is particle dynamics and collision cross-sections. The macroscopic output — by taking moments of f multiplied by 1, v, ½mv², and so on — yields the continuity equation, the Navier-Stokes equation, and energy transport. The equation also provides the basis for the H-theorem: Boltzmann showed that a functional of f is monotonically decreasing in time until equilibrium, giving the statistical arrow of time.
