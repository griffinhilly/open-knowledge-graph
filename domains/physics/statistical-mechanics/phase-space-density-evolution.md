---
id: phase-space-density-evolution
title: Phase Space Density and the Liouville Equation
domain: physics
course: statistical-mechanics
prerequisites:
- id: liouville-theorem
  type: hard
- id: statistical-ensembles-intro
  type: hard
builds-toward:
- boltzmann-equation-kinetic
- fokker-planck-equation
tags:
- evolution
- dynamics
- phase-space
stage: advanced
status: draft
---

# Phase Space Density and the Liouville Equation

## Core Idea
The Liouville equation describes temporal evolution of probability density in phase space under Hamiltonian dynamics. As a fundamental equation of motion for statistical ensembles, it serves as the parent equation from which the Boltzmann equation (for gases with collisions) and Fokker-Planck equation (for stochastic processes) can be derived.

## Explainer

From your study of the Liouville theorem, you know that phase space volume is conserved under Hamiltonian dynamics — the flow of system points through phase space is incompressible, like the flow of an ideal fluid. The **Liouville equation** takes this conservation law and turns it into a differential equation for the probability density ρ(q, p, t) itself. Just as the continuity equation ∂ρ/∂t + ∇·J = 0 describes conservation of charge density in space, the Liouville equation ∂ρ/∂t + {ρ, H} = 0 describes conservation of probability density in phase space, where {ρ, H} is the Poisson bracket.

The Poisson bracket is the natural language for Hamiltonian mechanics: {f, g} = Σᵢ (∂f/∂qᵢ)(∂g/∂pᵢ) − (∂f/∂pᵢ)(∂g/∂qᵢ). For the Liouville equation, it computes the total time derivative of ρ along a phase-space trajectory. Setting this equal to zero means that the probability density is constant along trajectories — if you follow a cloud of phase-space points as they evolve under Hamilton's equations, the density of the cloud does not change. This is the exact, microscopic statement of ensemble evolution.

The connection to statistical ensembles is direct. An ensemble is a collection of conceptual copies of the system with different initial conditions, distributed according to ρ(q, p, 0). As time passes, each copy evolves according to Hamilton's equations, and the density evolves according to the Liouville equation. Equilibrium ensembles — microcanonical, canonical — correspond to stationary solutions where ∂ρ/∂t = 0, meaning ρ must Poisson-commute with H. Any function of H alone, such as the Boltzmann factor e^(−βH), satisfies this and thus describes an equilibrium ensemble.

The Liouville equation is exact but also intractable for a macroscopic system with ~10²³ degrees of freedom — you cannot track ρ in full 6N-dimensional phase space. The path to the Boltzmann equation involves integrating out all but one or two particle positions and momenta to get reduced distribution functions. When you apply the BBGKY hierarchy and make the **molecular chaos assumption** (that two particles' velocities are uncorrelated before a collision), the infinite hierarchy truncates and you recover the Boltzmann equation with its collision integral. The Fokker-Planck equation follows a different simplification, projecting the dynamics onto a slow, coarse-grained degree of freedom coupled to a noisy environment. Both are approximations derived from the exact Liouville equation, which remains the fundamental law of classical statistical mechanics.
