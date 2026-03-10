---
id: matrix-inverses
title: The Matrix Inverse
domain: mathematics
course: linear-algebra
prerequisites:
- id: row-echelon-form
  type: hard
- id: matrix-operations
  type: hard
builds-toward:
- change-of-basis
- cramers-rule
- least-squares-approximation
- lu-decomposition
tags:
- inverse matrix
- invertible
- nonsingular
- A inverse
- identity matrix
stage: formal-systems
status: draft
---

# The Matrix Inverse

## Core Idea
A square matrix A is invertible (nonsingular) if there exists a matrix A⁻¹ such that AA⁻¹ = A⁻¹A = I, where I is the identity matrix. The inverse can be computed by augmenting A with I and row-reducing until the left side becomes I, at which point the right side is A⁻¹. A matrix is invertible if and only if its RREF is the identity, equivalently if and only if its determinant is nonzero. The inverse allows formal algebraic manipulation of matrix equations and is central to change-of-basis formulas.

## How It's Best Learned
First compute inverses of 2×2 matrices using the explicit formula (ad−bc)⁻¹[[d,−b],[−c,a]), then generalize to 3×3 and larger using the augmented-matrix method. Verify results by multiplying A⁻¹A and checking for I.

## Common Misconceptions
- Students apply A⁻¹ = 1/A, which has no meaning for matrices; the inverse is not scalar division.
- Not every square matrix is invertible — matrices with linearly dependent rows or columns have no inverse.
- For rectangular matrices, left and right inverses may differ; the notion of a two-sided inverse only applies to square matrices.
