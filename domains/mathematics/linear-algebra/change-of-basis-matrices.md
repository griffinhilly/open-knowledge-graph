---
id: change-of-basis-matrices
title: Change of Basis and Coordinate Transformations
domain: mathematics
course: linear-algebra
prerequisites:
- id: linear-transformation-matrix-representation
  type: hard
- id: matrix-inverses-computation
  type: hard
builds-toward:
- eigenvalues-eigenvectors-introduction
- diagonalization-similar-matrices
tags:
- change-of-basis
- coordinates
- transformations
stage: formal-systems
status: draft
---

# Change of Basis and Coordinate Transformations

## Core Idea
If B and C are two bases for Rⁿ, the change-of-basis matrix P_C←B converts coordinates from B to C: [v]_C = P_C←B [v]_B. The matrix P has C-coordinates of B-basis vectors as columns. If A represents T in the standard basis, then A' = P⁻¹AP represents T relative to basis B, where P = [B]. Similar matrices represent the same transformation in different bases.
