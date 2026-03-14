---
id: null-space
title: Null Space and Kernel
domain: mathematics
course: linear-algebra
prerequisites:
- id: subspaces
  type: hard
- id: gaussian-elimination
  type: hard
builds-toward:
- rank-and-nullity-theorem
tags:
- null-space
- kernel
- homogeneous-solutions
stage: formal-systems
status: draft
---

# Null Space and Kernel

## Core Idea
The null space nul(A) is the set of all solutions to Ax = 0, found by Gaussian elimination. It is a subspace and equals the kernel of the linear transformation x ↦ Ax. Nullity(A) is the dimension of nul(A), equal to the number of free variables in RREF.
