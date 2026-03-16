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
status: draft
---

# Generalized Coordinates and Degrees of Freedom

## Core Idea
Rather than tracking all Cartesian coordinates, generalized coordinates (q₁, q₂, ..., qₙ) describe only the independent motions of a system. The number of generalized coordinates equals the degrees of freedom—the minimum number of independent parameters needed to specify the system's configuration completely.

## Explainer

In Newtonian mechanics, you naturally describe a particle's position by three Cartesian coordinates (x, y, z). For a system of N particles, that's 3N coordinates. But your prerequisite on holonomic constraints established that each constraint equation restricts the system to a lower-dimensional surface in that 3N-dimensional space. A rigid rod connecting two particles imposes one constraint (fixed distance), reducing 6 coordinates to 5. Holonomic constraints — those expressible as f(q₁, q₂, ..., t) = 0 — each reduce the degrees of freedom by exactly one.

**Generalized coordinates** are a minimal set of independent parameters that completely specify the system's configuration once you've accounted for all constraints. Instead of tracking all Cartesian coordinates and enforcing constraints separately, you reparameterize the problem so that constraints are built in automatically. For a simple pendulum of length L, instead of (x, y) subject to x² + y² = L², you use a single angle θ. For a planar rigid body, instead of the positions of every constituent particle, you use (x_cm, y_cm, θ) — three coordinates, three degrees of freedom. The number of generalized coordinates equals the degrees of freedom: DOF = 3N − (number of independent holonomic constraints).

The freedom to choose generalized coordinates is a genuine advantage. Any smooth parameterization of the configuration space works — joint angles, arc lengths, displacement ratios, normal mode amplitudes. You choose whichever coordinates make the geometry most natural. A double pendulum is far more cleanly described by two joint angles (θ₁, θ₂) than by the Cartesian positions of both pendulum bobs. This flexibility is precisely what makes the Lagrangian mechanics framework — which operates entirely in generalized coordinates — so powerful.

Non-holonomic constraints (those involving velocities that cannot be integrated to position constraints, like a rolling wheel without slipping) do not reduce the degrees of freedom in the same way; the system still requires as many generalized coordinates, but the constraint restricts the accessible velocity directions. This distinction, which you encountered in your prerequisite, is why generalized coordinates are defined through holonomic constraints alone, while non-holonomic constraints appear as supplementary conditions on the generalized velocities q̇ᵢ in the equations of motion.
