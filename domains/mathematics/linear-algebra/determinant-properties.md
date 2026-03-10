---
id: determinant-properties
title: Properties of Determinants
domain: mathematics
course: linear-algebra
prerequisites:
- id: cofactor-expansion
  type: hard
- id: gaussian-elimination
  type: soft
builds-toward:
- cramers-rule
- eigenvalues-and-eigenvectors
tags:
- determinant properties
- multiplicativity
- row operations
- invertibility
- det(AB)
stage: formal-systems
status: draft
---

# Properties of Determinants

## Core Idea
Determinants satisfy powerful algebraic properties that make them tractable for large matrices. The three elementary row operations affect det as follows: swapping two rows negates det; multiplying a row by scalar k multiplies det by k; adding a multiple of one row to another leaves det unchanged. Crucially, det(AB) = det(A)det(B), so the determinant is multiplicative. Also, det(Aᵀ) = det(A), meaning row and column expansions give the same answer. A matrix is invertible if and only if its determinant is nonzero, and det(A⁻¹) = 1/det(A) when A is invertible.

## How It's Best Learned
Use row operations to reduce a matrix to triangular form, tracking how each operation changes the determinant, then multiply the diagonal entries. This combines Gaussian elimination with determinant theory and is far more efficient than cofactor expansion for larger matrices.

## Common Misconceptions
- det(A + B) ≠ det(A) + det(B) — this is a persistent and dangerous misconception.
- det(kA) = kⁿ det(A) for an n×n matrix, NOT k·det(A); every row is scaled by k.
- Adding a multiple of one row to another does NOT change the determinant — students frequently think it does.
