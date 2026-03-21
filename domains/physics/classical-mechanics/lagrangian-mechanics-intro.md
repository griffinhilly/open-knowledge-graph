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

## Questions

```yaml
- question: "A bead slides along a frictionless wire bent into an arbitrary curve. Using Newton's laws requires calculating the normal force at every point. Using Lagrangian mechanics with arc length along the wire as the generalized coordinate:"
  type: multiple-choice
  options:
    - "Also requires calculating the normal force, because all forces must be accounted for in any mechanics approach"
    - "Eliminates the need to calculate the normal force — it is a constraint force that does no work and disappears when the constraint is encoded in the generalized coordinate"
    - "Cannot be used because the bead's motion is constrained to a curve"
    - "Requires more equations than Newton's approach because generalized coordinates are more complex to define"
  answer: 1
  explanation: "Constraint forces (normal forces, string tension) do no work and don't appear in T − V when you choose generalized coordinates that automatically satisfy the constraint. With arc length as the single generalized coordinate, the bead is always on the wire by definition — the constraint is built into the coordinate system. The Euler-Lagrange equation yields the equation of motion directly, with the constraint force never appearing. This is one of the primary practical advantages of the Lagrangian framework."

- question: "The Lagrangian of a system is found to not depend on position x — it only depends on velocity ẋ and time. By Noether's theorem, what is conserved?"
  type: multiple-choice
  options:
    - "Energy, because any system with a well-defined Lagrangian conserves energy"
    - "Angular momentum, because spatial independence always implies rotational symmetry"
    - "Linear momentum in the x-direction, because translational symmetry in x implies momentum conservation"
    - "Nothing — Noether's theorem applies only to time symmetry, not spatial symmetry"
  answer: 2
  explanation: "Noether's theorem states that each continuous symmetry of the Lagrangian corresponds to a conserved quantity. If L doesn't depend on x, the system is invariant under translation in x — and the conserved quantity is linear momentum in the x-direction. Time-translation symmetry → energy; spatial translation symmetry → momentum; rotational symmetry → angular momentum. Option A confuses time-translation symmetry (which conserves energy) with any arbitrary Lagrangian."

- question: "The principle of stationary action states that nature always takes the path that minimizes the action integral."
  type: true-false
  answer: false
  explanation: "Hamilton's principle states that nature takes the path for which the action is stationary — meaning the first variation is zero — not necessarily minimized. The action can be a minimum, a maximum, or a saddle point depending on the system and boundary conditions. 'Principle of least action' is a historical misnomer that persisted; the mathematically correct statement is stationary action. The distinction matters in field theory and for paths near caustics."

- question: "Noether's theorem implies that if a system's Lagrangian has time-translation symmetry (it does not explicitly depend on time), then the system's total energy is conserved."
  type: true-false
  answer: true
  explanation: "Time-translation symmetry — the Lagrangian has the same form regardless of when you observe the system — corresponds via Noether's theorem to conservation of energy. This gives conservation of energy not as an independent empirical fact but as a logical consequence of time symmetry. Systems whose Lagrangians explicitly depend on time (e.g., driven oscillators with time-varying external forces) break time-translation symmetry and do not conserve energy."

- question: "Why does using generalized coordinates make the Lagrangian approach easier to apply to constrained systems than Newton's force-based approach?"
  type: short-answer
  answer: "In Newton's approach, constraints generate unknown forces (normal forces, tension) that must be solved for simultaneously with the equations of motion — introducing extra unknowns and equations. In the Lagrangian approach, you choose generalized coordinates that automatically satisfy the constraints, encoding them in the coordinate system itself. Since constraint forces do no work, they don't appear in T − V, and the Euler-Lagrange equations yield the equations of motion directly in terms of unconstrained degrees of freedom, with constraint forces never entering the calculation."
  explanation: "A pendulum illustrates this perfectly. Newton requires resolving tension along and perpendicular to the rod, setting up two coupled equations, and eliminating the tension. Lagrange uses θ alone as the generalized coordinate (the rod length is constant by constraint), writes T and V in terms of θ and θ̇, and the Euler-Lagrange equation immediately gives mℓ²θ̈ + mgℓ sin θ = 0 — the correct equation of motion with no mention of tension."
```

## Explainer

Your work on Newton's laws approached mechanics through forces: identify all forces acting on a body, sum them to get the net force, and integrate F = ma to get the trajectory. This works beautifully for a single particle in a simple geometry, but it becomes unwieldy fast. A pendulum requires resolving tension along a curved path. A bead constrained to a wire requires computing a constraint force that does no work. A double pendulum requires coupling multiple force equations. Lagrangian mechanics reformulates the same physics using energy rather than force, and the result is a method that handles constraints and complex geometries almost automatically.

The central object is the **Lagrangian** L = T − V: kinetic energy minus potential energy. From your work on conservation of energy, you know that total mechanical energy E = T + V is conserved in many systems. The Lagrangian is the difference, not the sum — a quantity whose integral over time, called the **action** S = ∫L dt, measures something like the "cost" of a trajectory. The **principle of stationary action** (Hamilton's principle) states that nature takes the path for which the action is stationary — not necessarily minimized, but neither increased nor decreased by small variations. Among all the possible paths a system could take between two configurations, the one that actually occurs makes the action stationary. This principle is deep: it reframes physics as a global optimization over trajectories, not a local rule about forces.

Applying calculus of variations to make the action stationary (which is where your work on partial derivatives becomes essential) yields the **Euler–Lagrange equation**: d/dt(∂L/∂q̇) − ∂L/∂q = 0 for each **generalized coordinate** q. The beauty is in what q can be. Instead of being tied to Cartesian coordinates, you can choose any coordinates that naturally describe your system — the angle of a pendulum, the distance along a constrained track, the joint angles of a robot arm. Constraints are handled by simply choosing coordinates that satisfy them from the start, eliminating constraint forces from the problem entirely. For a pendulum, one generalized coordinate (the angle θ) fully describes the system; the Euler–Lagrange equation in θ directly yields the equation of motion without ever mentioning tension.

The deepest result in the Lagrangian framework is **Noether's theorem**: every continuous symmetry of the Lagrangian corresponds to a conserved quantity. If L does not change when you translate the system in time (time-translation symmetry), energy is conserved. If L does not change when you translate in space, momentum is conserved. If L does not change under rotation, angular momentum is conserved. Conservation laws are not separate empirical facts to be discovered one by one — they are consequences of symmetry, and the Lagrangian is the object that makes the symmetry manifest. This is why Lagrangian mechanics is not just a computational convenience but a conceptual reorganization of physics: it reveals the structural reasons why conserved quantities exist.
