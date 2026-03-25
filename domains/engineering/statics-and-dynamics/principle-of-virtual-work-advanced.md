---
id: principle-of-virtual-work-advanced
title: Principle of Virtual Work and Generalized Forces
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: principle-of-virtual-work-method
  type: hard
- id: generalized-coordinates
  type: hard
- id: virtual-work-method
  type: soft
builds-toward:
- lagrangian-mechanics-overview
tags:
- virtual-work
- energy-methods
- generalized-forces
stage: formal-systems
status: validated
---
# Principle of Virtual Work and Generalized Forces

## Core Idea
The principle of virtual work extends from statics into dynamics when combined with D'Alembert's principle and expressed in generalized coordinates. Generalized forces Qᵢ represent the effective force in each generalized direction, allowing powerful energy-based methods without explicitly solving for constraint forces.

## Questions

```yaml
- question: "What is the key advantage of expressing the principle of virtual work in generalized coordinates rather than Cartesian coordinates?"
  type: multiple-choice
  options:
    - "Generalized coordinates always produce simpler algebraic expressions regardless of the system"
    - "Constraint forces automatically drop out because virtual displacements consistent with constraints do no work for them"
    - "The equations of motion become linear, making them easier to solve numerically"
    - "Generalized coordinates eliminate the need to know the kinetic energy of the system"
  answer: 1
  explanation: "The key advantage is that constraint forces (normal forces, pin reactions, roller reactions at frictionless contacts) do no virtual work for displacements that satisfy the constraints. When virtual displacements are defined to be compatible with the constraints, constraint forces are perpendicular to those displacements and drop out automatically. This means you never need to introduce or solve for constraint forces — only the applied forces (and inertia forces, in dynamics) appear in the equations. This is what makes the method so powerful for multi-degree-of-freedom systems."

- question: "A slider-crank mechanism consists of a rotating crank, a connecting rod, and a piston sliding in a cylinder. How many generalized coordinates are needed to fully describe its configuration?"
  type: multiple-choice
  options:
    - "Three — one for the crank angle, one for the rod angle, and one for the piston position"
    - "One — a single angle (e.g., crank angle) determines the position of every other link"
    - "Two — the crank angle and piston displacement are independently variable"
    - "Six — three translational and three rotational degrees of freedom for each rigid body"
  answer: 1
  explanation: "A slider-crank mechanism has one degree of freedom: specifying the crank angle completely determines the position of the connecting rod and piston through the geometric constraints. Once the crank angle θ is known, the constraint equations give the rod angle and piston displacement uniquely. This is exactly the power of generalized coordinates: they encode the constraints, so only the true independent degrees of freedom appear. Six Cartesian coordinates per body (option D) would over-specify the system; the constraints reduce it to one."

- question: "When the principle of virtual work is formulated in generalized coordinates, the constraint forces (e.g., normal forces at frictionless supports) appear in the generalized force Qᵢ and must be included explicitly."
  type: true-false
  answer: false
  explanation: "Constraint forces at frictionless contacts are perpendicular to the virtual displacements that satisfy the constraints, so they do zero virtual work. When computing the generalized force Qᵢ = ∂(δW)/∂(δqᵢ), only applied forces contribute — constraint forces have already been eliminated by the choice of admissible virtual displacements. This is the fundamental reason for using generalized coordinates: you never need to solve for constraint forces at all, greatly simplifying the equations of motion."

- question: "If a generalized coordinate qᵢ is an angle (measured in radians), the corresponding generalized force Qᵢ must have units of torque (N·m)."
  type: true-false
  answer: true
  explanation: "The generalized force Qᵢ is defined so that Qᵢ δqᵢ has units of energy (Joules = N·m). If δqᵢ is a dimensionless angle in radians, then Qᵢ must have units of N·m (torque) so the product has units of energy. This unit analysis is not arbitrary — it reflects the physical content of the work-energy relationship expressed in generalized coordinates. If qᵢ were a length (meters), Qᵢ would be a force (N). The units of Qᵢ always depend on the units of the corresponding coordinate."

- question: "Explain why constraint forces drop out when virtual work is expressed in generalized coordinates, and why this makes the method powerful for complex systems."
  type: short-answer
  answer: "Virtual displacements in generalized coordinates are defined to be admissible — they satisfy all geometric constraints. Constraint forces (pin reactions, normal forces at frictionless contacts) act perpendicular to the directions allowed by the constraints, so they do zero work for any admissible virtual displacement. Since they contribute nothing to the total virtual work, they never appear in the generalized force Qᵢ. This eliminates the need to solve for constraint forces, reducing an n-body system with many constraints to n decoupled equations of motion in the true degrees of freedom."
  explanation: "For a system with many rigid bodies and constraints, the Newtonian approach requires writing equations for every body and then solving a large system that includes all the internal constraint forces (tensions, normal forces, pin reactions). The virtual work method sidesteps this entirely — by choosing generalized coordinates that respect the constraints, you automatically eliminate those forces from the problem. For a robot arm with 6 joints, for example, this means 6 equations of motion in 6 generalized coordinates rather than equations for dozens of forces and reactions between links."
```

## Explainer

In your earlier study of the principle of virtual work, you applied it to static systems: a system in equilibrium does zero total virtual work for any virtual displacement consistent with its constraints. The power of that method was that constraint forces — reactions at frictionless pins, surfaces, and rollers — do no virtual work, so they drop out automatically. You could solve for unknown forces without ever introducing them. The advanced form keeps this advantage and extends it into dynamics by incorporating **D'Alembert's principle**, which treats inertia forces as if they were applied forces.

**Generalized coordinates** q₁, q₂, ..., qₙ are a minimal set of parameters that completely describe the configuration of a system. For a simple pendulum, one angle θ suffices. For a double pendulum, two angles θ₁ and θ₂. For a slider-crank mechanism, one angle describes the entire configuration. The key property: generalized coordinates automatically encode the system's constraints. When you use θ to describe a pendulum, the constraint that the bob stays on the rod is already built in — you never need to write or enforce it separately. The degrees of freedom n equals the number of generalized coordinates needed.

The **generalized force** Qᵢ associated with coordinate qᵢ is defined so that the total virtual work equals Σᵢ Qᵢ δqᵢ. Note the units: whatever makes Qᵢ δqᵢ have units of energy. If qᵢ is an angle (radians), then Qᵢ must be a torque (N·m). If qᵢ is a length (m), Qᵢ is a force (N). To compute Qᵢ, you differentiate the virtual work of all applied forces with respect to the virtual displacement δqᵢ, holding all other generalized coordinates fixed. This is a systematic procedure that handles any combination of forces, torques, and mixed systems without special cases.

Applying D'Alembert's principle — treating −mᵢaᵢ as an "inertia force" acting on each mass — and combining with the virtual work principle yields the **Lagrange equations of motion**: d/dt(∂T/∂q̇ᵢ) − ∂T/∂qᵢ = Qᵢ, where T is total kinetic energy. These equations require only kinetic energy and generalized forces as inputs, and they automatically produce the correct equations of motion for each degree of freedom. Constraint forces never appear. For conservative forces, Qᵢ = −∂V/∂qᵢ, simplifying further to the standard Lagrangian form L = T − V. This framework is the gateway to Lagrangian mechanics — the same method that governs multi-body robotics, spacecraft dynamics, and analytical mechanics at every level beyond introductory physics.
