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
status: draft
---

# Holonomic and Nonholonomic Constraints

## Core Idea
Holonomic constraints can be expressed as equations relating positions (e.g., x² + y² = r² for a particle on a circle) and reduce degrees of freedom algebraically. Nonholonomic constraints involve velocity relationships (e.g., rolling without slipping: v = ωr) and cannot be reduced to position equations alone, requiring more sophisticated analysis methods.

## Explainer

When you studied constrained particle motion, the key insight was that constraints restrict a system's accessible positions — a bead on a wire can't just teleport off the wire. The classification of constraints into **holonomic** and **nonholonomic** types sharpens this idea by asking a deeper question: can the constraint be fully expressed using only coordinates (positions), or does it fundamentally involve velocities in a way that can't be eliminated?

A **holonomic** constraint is one that can be written as f(q₁, q₂, ..., qₙ, t) = 0 — a relationship among the generalized coordinates and time alone. The classic example is a particle confined to a sphere: x² + y² + z² = R². This constraint says nothing about velocities directly; it restricts the *set of accessible positions*. From the system's point of view, a holonomic constraint reduces the number of degrees of freedom by one: a particle in 3D space normally has 3 DOF, but confined to a sphere it has only 2 (it can move anywhere on the surface). You can choose coordinates intrinsic to the sphere (like latitude and longitude) and forget about the constraint entirely — the constraint has been *absorbed* into the coordinate choice. This is why holonomic systems work so naturally with Lagrangian mechanics: the constraint is handled upfront by choosing the right generalized coordinates.

A **nonholonomic** constraint is one that involves velocities and *cannot* be integrated to a position equation. The canonical example is a disk rolling without slipping on a flat surface. The no-slip condition requires that the contact velocity v = ωr at every instant. This looks like a constraint on velocities, but can you integrate it to get a position relationship? You cannot — the disk can reach any position and any heading on the plane despite the constraint, just via different paths. The constraint restricts *allowable motions* (you can't slide sideways), but it doesn't restrict *accessible configurations*. A nonholonomic system has more accessible configurations than the velocity constraints would naively suggest, which is exactly why a car (another nonholonomic system with a steering constraint) can parallel-park: it takes more steps, but any configuration is reachable through a series of allowed motions.

The engineering significance is practical: holonomic systems can be analyzed using Lagrangian mechanics with reduced coordinates and no special treatment of constraints. Nonholonomic systems require additional techniques — Lagrange multipliers, the Gibbs-Appell equations, or nonholonomic mechanics — because the constraint couples velocities without fixing positions. Before attempting to model any mechanical system, classifying its constraints as holonomic or nonholonomic is therefore the first architectural decision: it determines which analytical tools apply and how many genuinely independent degrees of freedom the system possesses.
