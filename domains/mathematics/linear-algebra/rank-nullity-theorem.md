---
id: rank-nullity-theorem
title: Rank, Nullity, and the Rank-Nullity Theorem
domain: mathematics
course: linear-algebra
prerequisites:
- id: row-echelon-form-rref
  type: hard
- id: basis-and-dimension
  type: soft
builds-toward:
- linear-transformations-definition
- kernel-and-image
- least-squares-approximation
tags:
- rank
- nullity
- dimension
stage: formal-systems
status: draft
---

# Rank, Nullity, and the Rank-Nullity Theorem

## Core Idea
For an m×n matrix A, rank(A) is the number of pivot columns (dimension of column space), and nullity(A) = n − rank(A) (dimension of null space). The rank-nullity theorem states: rank(A) + nullity(A) = n. This fundamental relationship constrains the structure of solutions to Ax = b and underpins the dimension theorem for linear transformations.
