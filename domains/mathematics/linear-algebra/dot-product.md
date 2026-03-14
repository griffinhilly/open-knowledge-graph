---
id: dot-product
title: Dot Product and Orthogonality
domain: mathematics
course: linear-algebra
prerequisites:
- id: vectors-in-rn-operations
  type: hard
- id: vector-norms
  type: hard
builds-toward:
- linear-transformations-definition
- orthogonality-and-orthonormal-sets
- gram-schmidt-orthogonalization
tags:
- dot-product
- orthogonality
- inner-product
- projection
stage: formal-systems
status: draft
---

# Dot Product and Orthogonality

## Core Idea
The dot product of vectors u and v is u·v = u₁v₁ + u₂v₂ + ... + uₙvₙ, which equals ||u|| ||v|| cos(θ) where θ is the angle between them. Two vectors are orthogonal if their dot product is zero. The dot product enables computing angles, projections, and lengths—fundamental to geometry and optimization.

## How It's Best Learned
Compute dot products algebraically first, then relate the result to geometric angle. Use u·v = 0 to verify orthogonality. Explore the relationship cos(θ) = (u·v)/(||u|| ||v||).

## Common Misconceptions
The dot product is not element-wise multiplication—it's a sum of products. Orthogonality (u·v = 0) does not mean the vectors are perpendicular in everyday language; it's a precise algebraic condition.
