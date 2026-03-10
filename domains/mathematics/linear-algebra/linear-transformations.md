---
id: linear-transformations
title: Linear Transformations
domain: mathematics
course: linear-algebra
prerequisites:
- id: vectors-in-rn
  type: hard
- id: matrix-operations
  type: hard
builds-toward:
- transformation-matrices
- eigenvalues-and-eigenvectors
- matrix-composition
tags:
- linear transformation
- linearity
- kernel
- image
- function between vector spaces
stage: formal-systems
status: draft
---

# Linear Transformations

## Core Idea
A linear transformation T: Rⁿ → Rᵐ is a function between vector spaces satisfying two properties: T(u + v) = T(u) + T(v) (additivity) and T(cu) = cT(u) (homogeneity) for all vectors u, v and scalars c. Every linear transformation from Rⁿ to Rᵐ can be represented as multiplication by an m×n matrix. Geometrically, linear transformations include rotations, reflections, projections, and shears — transformations that map lines through the origin to lines through the origin and preserve the zero vector. The kernel (null space) and image (column space) of a transformation reveal its behavior: injective transformations have trivial kernel, surjective ones have full image.

## How It's Best Learned
Test whether given functions are linear by checking additivity and homogeneity on specific examples. Observe geometric effects of standard 2×2 transformations (rotation by θ, reflection across y = x, projection onto x-axis) before working algebraically.

## Common Misconceptions
- Not every function between Rⁿ and Rᵐ is linear; T(x) = x + b (a translation) is NOT linear because T(0) = b ≠ 0.
- Students sometimes think linearity means 'graphed as a line' — linearity is an algebraic property, not a geometric one in this sense.
- The zero vector must map to the zero vector under any linear transformation.
