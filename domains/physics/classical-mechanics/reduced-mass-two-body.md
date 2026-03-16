---
id: reduced-mass-two-body
title: Reduced Mass and Two-Body Problems
domain: physics
course: classical-mechanics
prerequisites:
- id: center-of-mass-motion
  type: hard
- id: two-body-collision-center-of-mass
  type: soft
- id: polar-coordinates
  type: hard
builds-toward:
- central-force-motion-analysis
- orbital-mechanics
tags:
- two-body
- effective-systems
- kinematics
stage: formal-systems
status: draft
---

# Reduced Mass and Two-Body Problems

## Core Idea
The two-body problem can be reduced to a one-body problem using the reduced mass μ = m₁m₂/(m₁+m₂). The relative motion evolves as if a single particle of mass μ moves in the central force, while the center of mass moves uniformly.

## Explainer

From **center-of-mass motion** you know that a system's center of mass moves as though all external force acts on a single point with total mass M = m₁ + m₂. And from work in **polar coordinates** you can describe a particle's position and velocity in the plane without Cartesian coordinates. Reduced mass combines these ideas to make two mutually interacting bodies mathematically equivalent to one body orbiting a fixed point.

The key insight is a change of variables. Instead of tracking positions r₁ and r₂ of each body in some fixed reference frame, describe the system by two new quantities: the **center-of-mass position** R = (m₁r₁ + m₂r₂)/(m₁+m₂), and the **relative position** r = r₁ − r₂. The separation vector r tells you where body 1 is relative to body 2 — the quantity that actually determines the gravitational (or spring, or Coulomb) force between them. When you rewrite the two coupled equations of motion in terms of R and r, they decouple exactly into two independent equations: the center of mass accelerates only due to external forces (and moves at constant velocity in an isolated system), and the relative coordinate evolves as if it were a single particle with **reduced mass** μ = m₁m₂/(m₁+m₂) subject to the mutual interaction force.

The formula for μ has a useful limiting form. If one body is much more massive than the other — say m₂ ≫ m₁ — then μ ≈ m₁. The lighter body effectively orbits a stationary heavy body, which is the one-body idealization you already know (Earth orbiting the Sun, or a satellite orbiting Earth). But when the masses are comparable — as in a binary star system — neither body is approximately fixed. Without the reduced mass, you would need to solve two coupled differential equations simultaneously; with it, you reduce to the exact same one-body problem but with μ replacing the orbiting mass. For two equal masses m, μ = m/2: the relative motion behaves as if a particle of half the mass orbits at the full separation distance.

In **polar coordinates**, the equation of motion for r with central force F(r) becomes identical in form to the one-body Kepler problem: μr̈ = F(r)r̂ + (angular momentum terms). All the Kepler orbit shapes — circles, ellipses, parabolas, hyperbolas — carry over exactly, and conservation of energy and angular momentum apply to the relative coordinate. The total kinetic energy splits cleanly: T = ½MV² (center-of-mass motion) + ½μṙ² (relative motion). This decomposition is not an approximation — it is an exact coordinate transformation. It is why the two-body problem has a complete analytical solution while the three-body problem generally does not: with three bodies, no such clean separation into independent equations exists.
