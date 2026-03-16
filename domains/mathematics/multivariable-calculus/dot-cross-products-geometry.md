---
id: dot-cross-products-geometry
title: 'Dot and Cross Products: Geometry and Computation'
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: vectors-in-3d
  type: hard
- id: cross-product-3d
  type: soft
- id: dot-product
  type: soft
builds-toward:
- equations-lines-planes
- curl-and-divergence
tags:
- dot-product
- cross-product
- orthogonality
- area
stage: formal-systems
status: draft
---

# Dot and Cross Products: Geometry and Computation

## Core Idea
The dot product u·v = u₁v₁ + u₂v₂ + u₃v₃ measures alignment (equals |u||v|cos(θ)); it is zero when vectors are orthogonal. The cross product u × v produces a vector perpendicular to both, with magnitude |u||v|sin(θ) equal to the area of the parallelogram they span.

## Explainer

You know from vectors in 3D that a vector has both magnitude and direction. The dot and cross products are tools for extracting geometric relationships between two vectors — and they each answer a different geometric question.

The **dot product** u · v = |u||v|cos θ asks: how much do u and v point in the same direction? If θ = 0° they are perfectly aligned and u · v = |u||v|. If θ = 90° they are perpendicular and u · v = 0. If θ > 90° they point away from each other and u · v < 0. The algebraic formula u₁v₁ + u₂v₂ + u₃v₃ computes this purely from components with no trigonometry needed — the connection to cos θ is the geometric interpretation. The most common application is testing **orthogonality**: two vectors are perpendicular if and only if their dot product is zero. The dot product also computes projections: the component of u along v is (u · v)/|v|, which is exactly how much of u lies in the direction of v.

The **cross product** u × v answers a different question: what direction is perpendicular to both u and v, and how large is the "area" they span? The result is a new vector, not a scalar. Its direction is given by the right-hand rule (curl the fingers from u toward v; the thumb points in the direction of u × v), and its magnitude |u||v|sin θ equals the area of the parallelogram with sides u and v. When u and v are parallel (θ = 0°), sin θ = 0 and the cross product is the zero vector — there is no well-defined perpendicular direction and the parallelogram has zero area. The cross product is anti-commutative: u × v = −(v × u). Reversing the order flips the orientation of the perpendicular direction.

These two products connect throughout multivariable calculus. Equations of planes use the normal vector found by a cross product of two vectors lying in the plane. Torque in physics is a cross product. The divergence theorem and Stokes' theorem involve both in their derivations. A concrete way to build intuition: for the standard basis vectors i, j, k, verify that i × j = k, j × k = i, k × i = j — the cyclic pattern — and that i · j = 0, i · i = 1. Every other dot and cross product calculation is an extension of these base cases via the component formula.
