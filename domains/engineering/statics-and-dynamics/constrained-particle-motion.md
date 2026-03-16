---
id: constrained-particle-motion
title: Constrained Particle Motion and Constraint Forces
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: kinematics-particles-curvilinear
  type: hard
- id: rigid-body-kinetics-force-acceleration
  type: hard
tags:
- constraints
- constraint-forces
- normal-force
- tension
stage: formal-systems
status: draft
---

# Constrained Particle Motion and Constraint Forces

## Core Idea
When a particle is constrained to move along a surface or curve, constraint forces (like normal forces or tensions) develop to enforce the constraint. These forces are perpendicular to the allowed motion and do no work. Applying Newton's second law with constraint force directions simplifies the analysis by reducing unknowns.

## Explainer

From your study of curvilinear kinematics, you know how to describe a particle's position, velocity, and acceleration along a curved path using normal-tangential (n-t) or polar coordinates. Constrained particle motion is where that kinematic description meets Newton's second law from rigid-body kinetics: the constraint geometry tells you the *form* of the acceleration, and the forces tell you its *magnitude*.

The key conceptual shift is recognizing that **constraint forces** are passive — they don't drive the motion, they enforce the geometry. When a bead slides along a wire, the wire's normal force keeps the bead on track without contributing to its speed. When a ball rolls in a bowl, the normal force from the bowl surface always points toward the center of curvature. These forces appear in your free-body diagram and must be solved for, but their direction is determined by the geometry of the constraint, not by the physics of the applied forces. This is why the n-t coordinate system is so powerful: in the normal direction, the constraint force appears as the primary unknown, while in the tangential direction, it vanishes completely, leaving only the applied tangential force to produce tangential acceleration.

Consider a particle moving along a circular track. In the normal direction, Newton's second law gives N − mg·cosθ = m·v²/r, where N is the normal force, v is the speed, and r is the radius. In the tangential direction, mg·sinθ = m·(dv/dt). Notice that N doesn't appear in the tangential equation at all — the constraint force does no work because it's perpendicular to motion. This separation of directions is the computational payoff of choosing coordinates aligned with the constraint geometry rather than using x-y components, where the constraint force would appear in both equations.

A critical insight you need to carry forward: a constraint force can become zero or even negative (tension goes to zero, or a surface can only push, not pull). When the normal force N = 0, the particle leaves the surface — this is the **leaving condition**, and finding it requires setting N = 0 in the normal equation and solving for the speed or angle at that instant. This condition determines, for example, when a ball leaves a curved ramp or when a roller coaster car would need seatbelts. Always check the sign of your constraint force: if it implies the surface must pull the particle (and it can't), the particle has already lost contact.

As you move into more complex problems — systems of particles, rolling bodies, or energy methods — the concept of constraints reappears in each context. Constraints reduce the degrees of freedom in a system, but they also introduce unknown forces. Work-energy methods (your next topic) cleverly bypass solving for constraint forces entirely by exploiting the fact that they do no work, giving you velocities directly from energy accounting without ever finding N.
