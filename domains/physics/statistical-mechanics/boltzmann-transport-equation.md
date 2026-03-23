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
stage: expert
status: validated
---

# Boltzmann Transport Equation

## Core Idea
The Boltzmann equation ∂f/∂t + v·∇f + F/m·∇_v f = (∂f/∂t)_{coll} describes the evolution of the single-particle distribution f(r,v,t) under external forces F and collisions. The collision term (∂f/∂t)_{coll} is typically approximated as −(f − f^eq)/τ (relaxation-time approximation). It governs viscosity, thermal conductivity, and electrical conductivity in gases and weakly-coupled plasmas.

## Questions

```yaml
- question: "In the Boltzmann equation, the spatial streaming term v·∇f appears on the left side. A student claims this term represents how collisions redistribute particle velocities. Why is this wrong?"
  type: multiple-choice
  options:
    - "The v·∇f term actually represents quantum tunneling between energy levels"
    - "v·∇f is purely kinematic — it describes particles drifting between adjacent positions due to their velocity, with no collisions involved"
    - "v·∇f accounts for the external force accelerating particles in velocity space"
    - "The term is negligible compared to the collision integral and can be dropped for dense gases"
  answer: 1
  explanation: "The left side of the BTE describes free streaming in phase space: v·∇f accounts for particles moving between neighboring positions (spatial drift), while (F/m)·∇_v f accounts for particles accelerating through velocity space under external forces. Collisions are entirely on the right side — the collision term (∂f/∂t)_coll. The student's error conflates the two physically distinct mechanisms. Without the collision term, the left side alone would describe a collisionless gas, with f conserved along trajectories by Liouville's theorem."

- question: "In the relaxation-time approximation, the collision term is written as −(f − f^eq)/τ. What physical picture does this model capture?"
  type: multiple-choice
  options:
    - "The random impulsive force a single particle receives during a binary collision"
    - "The exact binary collision integral, summed over all particle pairs and scattering angles"
    - "The net effect of all collisions: driving f back toward the equilibrium distribution at rate 1/τ"
    - "The external force that accelerates particles to their equilibrium drift velocity"
  answer: 2
  explanation: "The relaxation-time approximation replaces the full Boltzmann collision integral — which integrates over all possible binary collision partners, velocities, and scattering cross-sections — with a single phenomenological rate: collisions collectively push f toward f^eq at a rate 1/τ. This sacrifices microscopic detail for tractability, but it correctly captures the physics of thermalization: collisions tend to erase deviations from equilibrium. Despite its simplicity, it correctly yields Ohm's law, Fourier's law of heat conduction, and Fick's law of diffusion."

- question: "The Boltzmann transport equation is designed for systems that are not in thermodynamic equilibrium — the Maxwell-Boltzmann distribution is a special limiting solution, not the general case."
  type: true-false
  answer: true
  explanation: "The equilibrium distribution f^eq ∝ exp(−mv²/2kT) is the steady-state solution when the left side (streaming) is zero and the collision term drives f to f^eq. The BTE's purpose is precisely to describe how f evolves when there are density gradients, temperature gradients, or external forces — all non-equilibrium conditions. This makes the BTE the foundational equation of non-equilibrium statistical mechanics, bridging microscopic particle dynamics to macroscopic transport phenomena."

- question: "The Boltzmann transport equation provides a complete microscopic description of every particle's individual trajectory in the gas."
  type: true-false
  answer: false
  explanation: "The BTE is a mesoscopic, statistical equation: f(r,v,t) is the phase-space density, not the position or velocity of any individual particle. It describes the collective statistical evolution of an ensemble of particles — averaging over microscopic fluctuations. The actual trajectory of a given particle is not tracked. This is why the BTE is an intermediate-level description, more coarse-grained than molecular dynamics (which tracks individual particles) but more detailed than macroscopic fluid equations (which have already averaged over velocity space)."

- question: "Why does the left-hand side of the Boltzmann equation represent a total time derivative of f along a particle's trajectory in phase space, and what does the equation reduce to if there is no collision term?"
  type: short-answer
  answer: "Each particle's trajectory in phase space carries it through position space at rate v = dr/dt and through velocity space at rate dv/dt = F/m. The total rate of change of f along this trajectory is df/dt = ∂f/∂t + v·∇_r f + (F/m)·∇_v f — the sum of the explicit time change and the two streaming terms. Without the collision term, this total derivative equals zero: Liouville's theorem states that for a Hamiltonian system, phase-space density is conserved along trajectories (the gas is incompressible in phase space). The collision term is the source/sink that breaks this conservation by scattering particles between trajectories, driving the gas toward equilibrium."
  explanation: "This framing — left side = streaming/free flow, right side = collisions — is the physical heart of the BTE. It separates deterministic single-particle dynamics (left) from stochastic many-body interactions (right), making the equation tractable while retaining the essential physics of both."
```

## Explainer

From kinetic theory, you know that a dilute gas can be described by a **distribution function** f(r, v, t): the density of particles in the six-dimensional phase space of positions and velocities at time t. The Maxwell-Boltzmann distribution f^eq ∝ exp(−mv²/2kT) is the equilibrium form. The Boltzmann transport equation is the dynamical law governing how f evolves when the gas is not in equilibrium — when there are density gradients, temperature gradients, or external forces driving a current.

Think of the left-hand side as a total time derivative of f following a particle's trajectory through phase space. The term ∂f/∂t is the explicit time change at a fixed point. The term **v · ∇f** (spatial streaming) accounts for particles drifting between neighboring positions: if more fast particles are entering a region from the left than leaving on the right, f there will change. The term **(F/m) · ∇_v f** (force streaming) does the same in velocity space: an external force like gravity or an electric field accelerates particles, shifting f toward higher or lower velocities. Together these three terms describe perfectly free flow in phase space — Liouville's theorem says they would sum to zero for a Hamiltonian system with no collisions.

The right-hand side, the **collision term** (∂f/∂t)_{coll}, represents the effect of binary collisions that scatter particles from one velocity to another. In the full Boltzmann collision integral, you sum over all possible in-scattering and out-scattering events weighted by cross-sections — this is where the physics of molecular interactions enters. The **relaxation-time approximation** replaces all this complexity with a single rate: −(f − f^eq)/τ, where τ is a characteristic collision time. The idea is simple: collisions drive f back toward equilibrium, and they do so at a rate 1/τ. This approximation is often good enough to derive Ohm's law, Fourier's law of heat conduction, and Fick's law of diffusion in a unified framework.

The Boltzmann equation occupies a special position in physics because it bridges two levels of description. The microscopic input is particle dynamics and collision cross-sections. The macroscopic output — by taking moments of f multiplied by 1, v, ½mv², and so on — yields the continuity equation, the Navier-Stokes equation, and energy transport. The equation also provides the basis for the H-theorem: Boltzmann showed that a functional of f is monotonically decreasing in time until equilibrium, giving the statistical arrow of time.
