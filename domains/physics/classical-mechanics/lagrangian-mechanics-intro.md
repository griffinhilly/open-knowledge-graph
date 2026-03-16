---
id: lagrangian-mechanics-intro
title: Lagrangian Mechanics (Introduction)
domain: physics
course: classical-mechanics
prerequisites:
- id: conservation-of-energy
  type: hard
- id: work-and-energy
  type: hard
- id: partial-derivatives
  type: hard
- id: lagrange-multipliers
  type: soft
builds-toward:
- hamiltonian-mechanics-intro
tags:
- lagrangian
- formalism
- mechanics
- equations-of-motion
stage: formal-systems
status: draft
---

# Lagrangian Mechanics (Introduction)

## Core Idea
Lagrangian mechanics reformulates Newton's laws using L = T − V (kinetic minus potential energy) and the principle of stationary action. The Euler–Lagrange equation d/dt(∂L/∂ẋ) − ∂L/∂x = 0 yields equations of motion without explicitly calculating forces or accelerations. This powerful approach naturally incorporates constraints via generalized coordinates and reveals symmetries that lead to conservation laws.

## Explainer

Your work on Newton's laws approached mechanics through forces: identify all forces acting on a body, sum them to get the net force, and integrate F = ma to get the trajectory. This works beautifully for a single particle in a simple geometry, but it becomes unwieldy fast. A pendulum requires resolving tension along a curved path. A bead constrained to a wire requires computing a constraint force that does no work. A double pendulum requires coupling multiple force equations. Lagrangian mechanics reformulates the same physics using energy rather than force, and the result is a method that handles constraints and complex geometries almost automatically.

The central object is the **Lagrangian** L = T − V: kinetic energy minus potential energy. From your work on conservation of energy, you know that total mechanical energy E = T + V is conserved in many systems. The Lagrangian is the difference, not the sum — a quantity whose integral over time, called the **action** S = ∫L dt, measures something like the "cost" of a trajectory. The **principle of stationary action** (Hamilton's principle) states that nature takes the path for which the action is stationary — not necessarily minimized, but neither increased nor decreased by small variations. Among all the possible paths a system could take between two configurations, the one that actually occurs makes the action stationary. This principle is deep: it reframes physics as a global optimization over trajectories, not a local rule about forces.

Applying calculus of variations to make the action stationary (which is where your work on partial derivatives becomes essential) yields the **Euler–Lagrange equation**: d/dt(∂L/∂q̇) − ∂L/∂q = 0 for each **generalized coordinate** q. The beauty is in what q can be. Instead of being tied to Cartesian coordinates, you can choose any coordinates that naturally describe your system — the angle of a pendulum, the distance along a constrained track, the joint angles of a robot arm. Constraints are handled by simply choosing coordinates that satisfy them from the start, eliminating constraint forces from the problem entirely. For a pendulum, one generalized coordinate (the angle θ) fully describes the system; the Euler–Lagrange equation in θ directly yields the equation of motion without ever mentioning tension.

The deepest result in the Lagrangian framework is **Noether's theorem**: every continuous symmetry of the Lagrangian corresponds to a conserved quantity. If L does not change when you translate the system in time (time-translation symmetry), energy is conserved. If L does not change when you translate in space, momentum is conserved. If L does not change under rotation, angular momentum is conserved. Conservation laws are not separate empirical facts to be discovered one by one — they are consequences of symmetry, and the Lagrangian is the object that makes the symmetry manifest. This is why Lagrangian mechanics is not just a computational convenience but a conceptual reorganization of physics: it reveals the structural reasons why conserved quantities exist.
