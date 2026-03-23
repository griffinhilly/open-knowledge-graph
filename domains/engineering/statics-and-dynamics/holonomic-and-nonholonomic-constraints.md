---
id: holonomic-and-nonholonomic-constraints
title: Holonomic and Nonholonomic Constraints
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: constrained-particle-motion
  type: soft
builds-toward:
- generalized-coordinates
- lagrangian-mechanics-overview
tags:
- constraints
- mechanics
- systems-analysis
stage: formal-systems
status: validated
---

# Holonomic and Nonholonomic Constraints

## Core Idea
Holonomic constraints can be expressed as equations relating positions (e.g., x² + y² = r² for a particle on a circle) and reduce degrees of freedom algebraically. Nonholonomic constraints involve velocity relationships (e.g., rolling without slipping: v = ωr) and cannot be reduced to position equations alone, requiring more sophisticated analysis methods.

## Questions

```yaml
- question: "A disk rolls without slipping on a flat surface. Despite the no-slip condition v = ωr constraining velocity at every instant, which statement about accessible configurations is correct?"
  type: multiple-choice
  options:
    - "The disk can only reach configurations along straight lines, since rolling constrains it to forward motion"
    - "The disk can reach any position and heading on the plane, via sufficiently complex rolling paths"
    - "The disk's heading is permanently linked to its initial orientation and cannot change freely"
    - "The velocity constraint reduces accessible configurations just as a holonomic constraint would"
  answer: 1
  explanation: "This is the central insight about nonholonomic constraints: they restrict *instantaneous* allowable motions but do NOT restrict which configurations are accessible. The disk can reach any position and any heading on the plane — it just takes longer paths (like parallel parking a car). The constraint prevents sideways sliding at each instant, but does not remove any configuration from the reachable set. Option D reflects the classic misconception that velocity constraints reduce accessible configurations the same way position constraints do."

- question: "A particle is constrained to remain on a sphere of radius R (x² + y² + z² = R²). How does this holonomic constraint change the system?"
  type: multiple-choice
  options:
    - "It adds a degree of freedom, enabling surface-specific motion that wasn't possible in free space"
    - "It reduces the particle's DOF from 3 to 2 and allows the constraint to be absorbed into the coordinate choice"
    - "It reduces the particle's DOF from 3 to 2, but the constraint must still be retained as a Lagrange multiplier"
    - "It has no effect on DOF since the particle still exists in 3D space"
  answer: 1
  explanation: "A holonomic constraint f(q, t) = 0 reduces DOF by exactly one. A free particle in 3D has 3 DOF; confined to a sphere, it has 2. Crucially, because the constraint is a position equation, it can be *absorbed* into the coordinate choice: you can work entirely in intrinsic surface coordinates (like latitude/longitude) and forget about the constraint equation entirely. This is the key practical advantage of holonomic constraints — they simplify analysis by reducing the problem's dimensionality. Nonholonomic constraints cannot be absorbed this way."

- question: "A nonholonomic constraint limits which configurations a system can ever reach."
  type: true-false
  answer: false
  explanation: "This is the central misconception about nonholonomic constraints. A nonholonomic constraint restricts *instantaneous allowable velocities* — at each moment, certain directions of motion are forbidden. But because the constraint doesn't fix positions, the system can still reach any configuration in its full configuration space by taking appropriate (possibly complex) paths. The rolling disk and the car are canonical examples: both can reach any position and heading on the plane despite their nonholonomic velocity constraints."

- question: "A holonomic constraint can always be used to eliminate one generalized coordinate from the Lagrangian, simplifying the equations of motion."
  type: true-false
  answer: true
  explanation: "This is the practical advantage of holonomic constraints: because they are algebraic equations relating coordinates, you can solve for one coordinate in terms of the others and substitute, reducing the number of independent variables by one. The constraint disappears into the coordinate choice. Nonholonomic constraints (velocity constraints that cannot be integrated to position equations) cannot be handled this way — they require Lagrange multipliers or specialized techniques because no coordinates can be eliminated."

- question: "A car has a nonholonomic steering constraint — it cannot slide sideways at any instant. Does this mean there are parking spots it cannot reach? Explain why or why not, and what this reveals about nonholonomic constraints."
  type: short-answer
  answer: "No — a car can reach any parking spot despite its nonholonomic constraint. The constraint limits instantaneous motions (no sideways sliding) but not accessible configurations. Through sequences of allowed forward, reverse, and turning maneuvers (like parallel parking), any position and orientation is reachable. This reveals that nonholonomic constraints restrict the *paths* through configuration space, not the *set of reachable configurations* — a key distinction from holonomic constraints, which genuinely remove configurations from the accessible set."
  explanation: "This is what makes nonholonomic systems richer and more complex than holonomic ones. A ball on a sphere is genuinely restricted to the sphere — it cannot leave the surface. But a car on a flat plane can reach every point and every heading, despite its steering constraint. The constraint shapes the geometry of paths but doesn't shrink the configuration space. This is why nonholonomic systems require special treatment: you cannot simply reduce coordinates as with holonomic constraints, because no configurations have been removed."
```

## Explainer

When you studied constrained particle motion, the key insight was that constraints restrict a system's accessible positions — a bead on a wire can't just teleport off the wire. The classification of constraints into **holonomic** and **nonholonomic** types sharpens this idea by asking a deeper question: can the constraint be fully expressed using only coordinates (positions), or does it fundamentally involve velocities in a way that can't be eliminated?

A **holonomic** constraint is one that can be written as f(q₁, q₂, ..., qₙ, t) = 0 — a relationship among the generalized coordinates and time alone. The classic example is a particle confined to a sphere: x² + y² + z² = R². This constraint says nothing about velocities directly; it restricts the *set of accessible positions*. From the system's point of view, a holonomic constraint reduces the number of degrees of freedom by one: a particle in 3D space normally has 3 DOF, but confined to a sphere it has only 2 (it can move anywhere on the surface). You can choose coordinates intrinsic to the sphere (like latitude and longitude) and forget about the constraint entirely — the constraint has been *absorbed* into the coordinate choice. This is why holonomic systems work so naturally with Lagrangian mechanics: the constraint is handled upfront by choosing the right generalized coordinates.

A **nonholonomic** constraint is one that involves velocities and *cannot* be integrated to a position equation. The canonical example is a disk rolling without slipping on a flat surface. The no-slip condition requires that the contact velocity v = ωr at every instant. This looks like a constraint on velocities, but can you integrate it to get a position relationship? You cannot — the disk can reach any position and any heading on the plane despite the constraint, just via different paths. The constraint restricts *allowable motions* (you can't slide sideways), but it doesn't restrict *accessible configurations*. A nonholonomic system has more accessible configurations than the velocity constraints would naively suggest, which is exactly why a car (another nonholonomic system with a steering constraint) can parallel-park: it takes more steps, but any configuration is reachable through a series of allowed motions.

The engineering significance is practical: holonomic systems can be analyzed using Lagrangian mechanics with reduced coordinates and no special treatment of constraints. Nonholonomic systems require additional techniques — Lagrange multipliers, the Gibbs-Appell equations, or nonholonomic mechanics — because the constraint couples velocities without fixing positions. Before attempting to model any mechanical system, classifying its constraints as holonomic or nonholonomic is therefore the first architectural decision: it determines which analytical tools apply and how many genuinely independent degrees of freedom the system possesses.
