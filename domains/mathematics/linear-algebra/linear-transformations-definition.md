---
id: linear-transformations-definition
title: Linear Transformations and Their Properties
domain: mathematics
course: linear-algebra
prerequisites:
- id: function-notation-review
  type: soft
- id: basis-and-dimension
  type: hard
builds-toward:
- linear-transformation-matrix-representation
- kernel-and-image
tags:
- linear-transformations
- mappings
- functions
stage: formal-systems
status: draft
---

# Linear Transformations and Their Properties

## Core Idea
A linear transformation T: V → W is a function satisfying T(u + v) = T(u) + T(v) and T(cu) = cT(u). Examples: rotation, projection, differentiation, matrix multiplication. Linear transformations preserve vector space structure, making them natural maps between vector spaces. The kernel and image determine injectivity and surjectivity.

## How It's Best Learned
Check linearity carefully: verify both additivity and homogeneity. Explore examples: derivatives T(p) = p', rotations, projections onto a line. Visualize in R² and R³.
