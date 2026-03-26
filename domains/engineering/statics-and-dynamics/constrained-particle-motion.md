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
status: validated
---

# Constrained Particle Motion and Constraint Forces

## Core Idea
When a particle is constrained to move along a surface or curve, constraint forces (like normal forces or tensions) develop to enforce the constraint. These forces are perpendicular to the allowed motion and do no work. Applying Newton's second law with constraint force directions simplifies the analysis by reducing unknowns.

## Questions

```yaml
- question: "A bead slides along a smooth circular wire loop in a vertical plane. You apply Newton's second law in normal-tangential (n-t) coordinates. In which equation does the wire's normal force N appear?"
  type: multiple-choice
  options:
    - "In both the normal and tangential equations, because it keeps the bead on the loop and accelerates it"
    - "Only in the normal equation (ΣFₙ = mv²/r), not in the tangential equation"
    - "Only in the tangential equation, because the normal force changes the bead's speed"
    - "It does not appear at all in either equation for a smooth (frictionless) constraint"
  answer: 1
  explanation: "The constraint force (normal force from the wire) acts perpendicular to the bead's motion — in the normal direction. In n-t coordinates, the normal direction carries the centripetal acceleration mv²/r, and N appears there as the primary unknown. In the tangential direction, only forces with a tangential component drive tangential acceleration (dv/dt). Since N is purely normal, it has zero tangential projection and vanishes from the tangential equation entirely. This separation is the computational payoff of aligning coordinates with the constraint geometry."

- question: "A particle is sliding along a curved ramp and at some point the normal force N from the ramp becomes zero. What happens next?"
  type: multiple-choice
  options:
    - "The particle continues along the ramp surface, now supported entirely by friction"
    - "The particle instantaneously stops and reverses direction"
    - "The particle leaves the ramp surface and follows a free trajectory (e.g., projectile motion)"
    - "The particle accelerates along the ramp because the constraint force no longer opposes motion"
  answer: 2
  explanation: "N = 0 is the leaving condition. A surface can only push (not pull) — the normal force keeps the particle on the surface by pushing inward toward the center of curvature. When the geometry and speed require a 'pulling' normal force, the surface cannot provide it, and the particle separates. Setting N = 0 in the normal equation and solving for speed or angle gives the critical departure condition. After leaving, the particle follows a free trajectory governed only by gravity and other applied forces."

- question: "Constraint forces such as normal forces and string tensions do no work on the particles they constrain."
  type: true-false
  answer: true
  explanation: "Work equals force times displacement in the direction of the force. Constraint forces are always perpendicular to the direction of motion (that is precisely what it means to 'constrain' a path — the force enforces the geometry without driving motion along it). Since the angle between force and displacement is 90°, the dot product F·ds = 0, and no work is done. This is why work-energy methods can ignore constraint forces entirely — they cancel out of the energy accounting."

- question: "A particle constrained to move along a surface will generally remain on the surface as long as the constraint force is acting."
  type: true-false
  answer: false
  explanation: "Constraint forces maintain contact only when they are compressive (surface pushing) or tensile in the correct direction (string pulling). When the required constraint force reverses sign — a surface would need to pull the particle, or the speed exceeds what centripetal balance allows — the physical constraint fails. The particle leaves the surface at the instant N = 0. This is why checking the sign of N throughout the motion is essential: if it ever goes negative, the particle has already left the constrained path."

- question: "Why can work-energy methods bypass the need to solve for constraint forces, even though those forces appear as unknowns in Newton's second law equations?"
  type: short-answer
  answer: "Constraint forces are always perpendicular to the particle's displacement (velocity direction). Work equals F·Δs, and a force perpendicular to displacement does zero work. Since constraint forces do no work, they contribute nothing to the work-energy equation W_net = ΔKE. You can therefore compute kinetic energy changes from applied forces alone, finding speeds directly without ever calculating the constraint force."
  explanation: "This is why work-energy methods are so powerful for curved-path problems — you often want the speed at a particular location and don't need the normal force. Newton's second law gives you the normal force (useful if you need to know whether the particle stays on the surface or want the reaction magnitude); work-energy gives you the speed directly. The two methods are complementary: use Newton's law when you need forces, use work-energy when you need kinematics."
```

## Explainer

From your study of curvilinear kinematics, you know how to describe a particle's position, velocity, and acceleration along a curved path using normal-tangential (n-t) or polar coordinates. Constrained particle motion is where that kinematic description meets Newton's second law from rigid-body kinetics: the constraint geometry tells you the *form* of the acceleration, and the forces tell you its *magnitude*.

The key conceptual shift is recognizing that **constraint forces** are passive — they don't drive the motion, they enforce the geometry. When a bead slides along a wire, the wire's normal force keeps the bead on track without contributing to its speed. When a ball rolls in a bowl, the normal force from the bowl surface always points toward the center of curvature. These forces appear in your free-body diagram and must be solved for, but their direction is determined by the geometry of the constraint, not by the physics of the applied forces. This is why the n-t coordinate system is so powerful: in the normal direction, the constraint force appears as the primary unknown, while in the tangential direction, it vanishes completely, leaving only the applied tangential force to produce tangential acceleration.

Consider a particle moving along a circular track. In the normal direction, Newton's second law gives N − mg·cosθ = m·v²/r, where N is the normal force, v is the speed, and r is the radius. In the tangential direction, mg·sinθ = m·(dv/dt). Notice that N doesn't appear in the tangential equation at all — the constraint force does no work because it's perpendicular to motion. This separation of directions is the computational payoff of choosing coordinates aligned with the constraint geometry rather than using x-y components, where the constraint force would appear in both equations.

A critical insight you need to carry forward: a constraint force can become zero or even negative (tension goes to zero, or a surface can only push, not pull). When the normal force N = 0, the particle leaves the surface — this is the **leaving condition**, and finding it requires setting N = 0 in the normal equation and solving for the speed or angle at that instant. This condition determines, for example, when a ball leaves a curved ramp or when a roller coaster car would need seatbelts. Always check the sign of your constraint force: if it implies the surface must pull the particle (and it can't), the particle has already lost contact.

As you move into more complex problems — systems of particles, rolling bodies, or energy methods — the concept of constraints reappears in each context. Constraints reduce the degrees of freedom in a system, but they also introduce unknown forces. Work-energy methods (your next topic) cleverly bypass solving for constraint forces entirely by exploiting the fact that they do no work, giving you velocities directly from energy accounting without ever finding N.
