---
id: vector-norms
title: Vector Norms and Magnitude
domain: mathematics
course: linear-algebra
prerequisites:
- id: vectors-in-rn-operations
  type: hard
- id: square-roots-intro
  type: hard
builds-toward:
- dot-product
- orthogonality-and-orthonormal-sets
- matrix-norms
tags:
- vectors
- norms
- magnitude
- distance
stage: formal-systems
status: draft
---

# Vector Norms and Magnitude

## Core Idea
The norm (or magnitude) of a vector is a real number measuring its length, computed as ||v|| = √(v₁² + v₂² + ... + vₙ²). Norms generalize distance to n-dimensional space and satisfy key properties: ||cv|| = |c| ||v|| and the triangle inequality. Unit vectors (norm 1) form the basis for orthonormal sets.

## How It's Best Learned
Start with 2D and 3D visualization of distance formula. Then extend algebraically to R^n. Normalize vectors by dividing by their norm to create unit vectors in the same direction.
