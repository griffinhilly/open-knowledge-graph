---
id: linear-transformation-matrix-representation
title: Matrix Representation of Linear Transformations
domain: mathematics
course: linear-algebra
prerequisites:
- id: linear-transformations-definition
  type: hard
- id: basis-and-dimension
  type: hard
builds-toward:
- change-of-basis-matrices
- eigenvalues-eigenvectors-introduction
tags:
- matrix-representation
- coordinates
- bases
stage: formal-systems
status: draft
---

# Matrix Representation of Linear Transformations

## Core Idea
Every linear transformation T: Rⁿ → Rᵐ is represented by an m×n matrix A, where T(x) = Ax. To find A, compute T(eᵢ) for each standard basis vector and place the results as columns. For non-standard bases, the matrix is [T]_B = [T(b₁) ... T(bₙ)]_C in coordinates relative to bases B and C.
