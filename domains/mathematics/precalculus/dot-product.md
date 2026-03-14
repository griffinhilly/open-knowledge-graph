---
id: dot-product
title: Dot Product
domain: mathematics
course: precalculus
prerequisites:
  - id: vector-operations
    type: hard
  - id: law-of-cosines
    type: soft
builds-toward:
  - work-as-integral
tags: [vectors, dot-product, orthogonality]
stage: formal-systems
status: validated
---

# Dot Product

## Core Idea
The dot product of two vectors u = (u1, u2) and v = (v1, v2) is u * v = u1*v1 + u2*v2, a scalar (not a vector). Geometrically, u * v = |u| |v| cos(theta), where theta is the angle between them. The dot product measures how much two vectors point in the same direction. It is zero when vectors are perpendicular (orthogonal), positive when they point similarly, and negative when they point oppositely.

## How It's Best Learned
Compute dot products algebraically, then verify with the geometric formula. Use the dot product to find angles between vectors, check orthogonality, and compute projections. Connect to work in physics (W = F * d) and to the Law of Cosines.

## Common Misconceptions
- Expecting the dot product to produce a vector (it produces a scalar).
- Forgetting that the geometric formula requires the angle between the vectors, not a reference angle.
- Confusing dot product with cross product (which exists in 3D and produces a vector).
