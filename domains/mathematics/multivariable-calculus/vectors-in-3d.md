---
id: vectors-in-3d
title: Vectors in Three-Dimensional Space
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: vectors-in-rn
  type: hard
- id: dot-product
  type: hard
- id: cross-product
  type: hard
builds-toward:
- vector-valued-functions
- functions-of-several-variables
- cylindrical-coordinates
- vector-fields
tags:
- vectors
- 3d
- cross-product
- dot-product
- geometry
stage: formal-systems
status: draft
---

# Vectors in Three-Dimensional Space

## Core Idea
Vectors in three-dimensional space are ordered triples (x, y, z) representing magnitude and direction in ℝ³. The dot product measures projection and angle between vectors, while the cross product produces a vector perpendicular to both operands with magnitude equal to the area of the parallelogram they span. The right-hand rule determines the orientation of the cross product. These two products are the fundamental tools for all geometric reasoning in 3D calculus.

## How It's Best Learned
Students who have seen vectors in ℝ² should focus on what is genuinely new in ℝ³: the cross product has no 2D analogue, and spatial intuition requires deliberate practice. Draw diagrams in perspective. Practice computing cross products using the determinant formula and verify using the geometric definition. Problems involving normal vectors to planes cement both products simultaneously.

## Common Misconceptions
- The cross product is not commutative: a × b = −(b × a).
- The cross product is only defined in ℝ³ (and ℝ⁷); it does not generalize to arbitrary dimensions.
- |a · b| ≤ |a||b| with equality only when vectors are parallel; students often confuse when equality holds.
- The cross product of two parallel vectors is the zero vector, not zero (the scalar).
