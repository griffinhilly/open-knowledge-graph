---
id: matrix-representation-linear-transformations
title: Matrix Representation of Linear Transformations
domain: mathematics
course: linear-algebra
prerequisites:
- id: linear-transformations
  type: hard
- id: matrix-multiplication
  type: hard
builds-toward:
- composition-linear-transformations
- change-of-basis
tags:
- matrix-representation
- basis
- coordinates
stage: formal-systems
status: draft
---

# Matrix Representation of Linear Transformations

## Core Idea
Every linear transformation T: Rⁿ → Rᵐ has a matrix representation [T] whose columns are T(e₁), T(e₂), ..., T(eₙ). Once bases are fixed, the transformation is completely determined by this matrix. Changing bases changes the matrix representation, but the transformation itself is basis-independent.
