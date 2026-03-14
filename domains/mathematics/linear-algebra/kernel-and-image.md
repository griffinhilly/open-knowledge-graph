---
id: kernel-and-image
title: Kernel and Image of Linear Transformations
domain: mathematics
course: linear-algebra
prerequisites:
- id: linear-transformation-matrix-representation
  type: hard
- id: rank-nullity-theorem
  type: hard
builds-toward:
- linear-transformations-advanced
- least-squares-approximation
tags:
- kernel
- image
- null-space
- column-space
stage: formal-systems
status: draft
---

# Kernel and Image of Linear Transformations

## Core Idea
The kernel ker(T) = {v : T(v) = 0} is the null space of the matrix A. The image im(T) = {T(v) : v ∈ V} is the column space of A. These subspaces determine when T is injective (ker(T) = {0}) or surjective (im(T) = W). The rank-nullity theorem: dim(ker(T)) + dim(im(T)) = dim(domain).

## How It's Best Learned
Compute kernel by solving Ax = 0 (null space). Find image by identifying pivot columns and their span. Relate geometric intuition: kernel is directions that collapse to zero; image is reachable outputs.
