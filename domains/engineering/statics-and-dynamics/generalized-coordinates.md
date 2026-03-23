---
id: generalized-coordinates
title: Generalized Coordinates and Degrees of Freedom
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: holonomic-and-nonholonomic-constraints
  type: hard
builds-toward:
- lagrangian-mechanics-overview
tags:
- coordinates
- constraints
- systems-analysis
stage: formal-systems
status: validated
---

# Generalized Coordinates and Degrees of Freedom

## Core Idea
Rather than tracking all Cartesian coordinates, generalized coordinates (q₁, q₂, ..., qₙ) describe only the independent motions of a system. The number of generalized coordinates equals the degrees of freedom—the minimum number of independent parameters needed to specify the system's configuration completely.

## Questions

```yaml
- question: "A rigid bar connects two particles in 3D space. How many degrees of freedom does this two-particle system have?"
  type: multiple-choice
  options:
    - "6 — three Cartesian coordinates for each particle"
    - "5 — the rigidity constraint (fixed distance between particles) removes one degree of freedom"
    - "4 — the bar removes two degrees of freedom because the particles cannot move independently"
    - "3 — the rigid bar makes the pair equivalent to a single particle"
  answer: 1
  explanation: "Two particles in 3D have 3×2 = 6 Cartesian coordinates. The rigid bar imposes one holonomic constraint: the distance between the particles is fixed, (x₁−x₂)²+(y₁−y₂)²+(z₁−z₂)² = L². This one constraint reduces the DOF by one: 6−1 = 5. The five remaining degrees of freedom correspond to three coordinates for the center of mass plus two angles specifying the bar's orientation. Each holonomic constraint removes exactly one DOF."

- question: "A coin rolls without slipping on a flat surface. The no-slip rolling condition is a non-holonomic constraint. What does this mean for the number of generalized coordinates needed to describe the coin's configuration?"
  type: multiple-choice
  options:
    - "The no-slip condition reduces the number of required generalized coordinates, just like a holonomic constraint would"
    - "The no-slip condition does not reduce the number of generalized coordinates — you still need as many parameters to specify the configuration fully"
    - "The no-slip condition eliminates all constraints on position, since it only affects velocity"
    - "Non-holonomic constraints are ignored in Lagrangian mechanics and never affect generalized coordinate counts"
  answer: 1
  explanation: "The key distinction: holonomic constraints (expressible as f(q,t)=0) reduce the degrees of freedom and thus the number of generalized coordinates needed. Non-holonomic constraints involve velocities in a way that cannot be integrated to a position constraint — they restrict which velocities are accessible at each configuration, but every configuration is still reachable. The coin can reach any position and orientation on the surface; it's just constrained in how it gets there. You still need all generalized coordinates (e.g., (x, y, θ, φ, ψ) for a coin), and the non-holonomic constraint appears as a supplementary condition on the generalized velocities."

- question: "For a simple pendulum of length L, choosing the angle θ as the sole generalized coordinate automatically satisfies the length constraint without needing to impose it separately."
  type: true-false
  answer: true
  explanation: "Choosing θ as the generalized coordinate means writing the position as x = L sin θ, y = −L cos θ. Any value of θ gives a point on the circle of radius L — you cannot represent an off-circle position using θ. The constraint x²+y²=L² is built into the parameterization. This is what 'building in the constraints' means: the generalized coordinate parameterizes only the physically accessible configurations, making the constraint implicit rather than explicit."

- question: "For a system of N particles subject to k holonomic constraints, the degrees of freedom always equals 3N − k, regardless of whether any non-holonomic constraints are also present."
  type: true-false
  answer: false
  explanation: "The formula DOF = 3N − k holds only for holonomic constraints. Non-holonomic constraints (velocity constraints that cannot be integrated to position constraints, like rolling without slipping) restrict the accessible velocity directions but do NOT reduce the number of generalized coordinates needed to specify the configuration. A system with 3N − k holonomic degrees of freedom plus m non-holonomic constraints still requires 3N − k generalized coordinates; the non-holonomic constraints appear separately as constraints on the generalized velocities q̇ᵢ."

- question: "Explain what it means for generalized coordinates to 'build in' the constraints of a system, and why this makes the Lagrangian approach more efficient than applying Newtonian mechanics with explicit constraint forces."
  type: short-answer
  answer: "In Newtonian mechanics, you write equations for all 3N Cartesian coordinates and then add constraint forces (tension, normal forces) to enforce each constraint — resulting in more equations and unknown forces to solve for. Generalized coordinates reparameterize the problem so the configuration space only contains physically accessible states. The constraints are encoded in the parameterization itself: a double pendulum described by angles (θ₁, θ₂) can only reach positions where both arms have fixed length — there is no way to violate the constraint using θ₁ and θ₂ as coordinates. This eliminates the constraint forces from the equations entirely, leaving only DOF equations of motion instead of 3N, and no unknown reaction forces."
  explanation: "The efficiency gain is substantial in complex systems. A robotic arm with 6 joints has 6 generalized coordinates regardless of how many rigid-body constraints are internally imposed; the Lagrangian formulation handles the constraint forces implicitly through the geometry of the configuration space. The tradeoff is that the kinetic energy expression becomes more complex in generalized coordinates, but this is typically far easier to handle than solving the full Newtonian system with explicit constraint forces."
```

## Explainer

In Newtonian mechanics, you naturally describe a particle's position by three Cartesian coordinates (x, y, z). For a system of N particles, that's 3N coordinates. But your prerequisite on holonomic constraints established that each constraint equation restricts the system to a lower-dimensional surface in that 3N-dimensional space. A rigid rod connecting two particles imposes one constraint (fixed distance), reducing 6 coordinates to 5. Holonomic constraints — those expressible as f(q₁, q₂, ..., t) = 0 — each reduce the degrees of freedom by exactly one.

**Generalized coordinates** are a minimal set of independent parameters that completely specify the system's configuration once you've accounted for all constraints. Instead of tracking all Cartesian coordinates and enforcing constraints separately, you reparameterize the problem so that constraints are built in automatically. For a simple pendulum of length L, instead of (x, y) subject to x² + y² = L², you use a single angle θ. For a planar rigid body, instead of the positions of every constituent particle, you use (x_cm, y_cm, θ) — three coordinates, three degrees of freedom. The number of generalized coordinates equals the degrees of freedom: DOF = 3N − (number of independent holonomic constraints).

The freedom to choose generalized coordinates is a genuine advantage. Any smooth parameterization of the configuration space works — joint angles, arc lengths, displacement ratios, normal mode amplitudes. You choose whichever coordinates make the geometry most natural. A double pendulum is far more cleanly described by two joint angles (θ₁, θ₂) than by the Cartesian positions of both pendulum bobs. This flexibility is precisely what makes the Lagrangian mechanics framework — which operates entirely in generalized coordinates — so powerful.

Non-holonomic constraints (those involving velocities that cannot be integrated to position constraints, like a rolling wheel without slipping) do not reduce the degrees of freedom in the same way; the system still requires as many generalized coordinates, but the constraint restricts the accessible velocity directions. This distinction, which you encountered in your prerequisite, is why generalized coordinates are defined through holonomic constraints alone, while non-holonomic constraints appear as supplementary conditions on the generalized velocities q̇ᵢ in the equations of motion.
