---
id: symmetric-matrices
title: Symmetric Matrices and Their Properties
domain: mathematics
course: linear-algebra
prerequisites:
- id: matrix-transpose-properties
  type: hard
- id: eigenvalues-and-eigenvectors
  type: soft
- id: inner-product-spaces
  type: soft
builds-toward:
- spectral-theorem
tags:
- symmetric matrix
- real eigenvalues
- orthogonal eigenvectors
- positive definite
- quadratic form
stage: formal-systems
status: draft
---

# Symmetric Matrices and Their Properties

## Core Idea
A symmetric matrix satisfies Aᵀ = A; equivalently, its (i,j) entry equals its (j,i) entry for all i, j. Symmetric matrices arise naturally from inner products, quadratic forms, and covariance matrices in statistics. Two fundamental properties distinguish them: all eigenvalues of a real symmetric matrix are real, and eigenvectors corresponding to distinct eigenvalues are orthogonal. These properties make symmetric matrices far better behaved than general matrices and are the hypotheses of the Spectral Theorem. A symmetric matrix A is positive definite if xᵀAx > 0 for all nonzero x, equivalent to all eigenvalues being positive.

## How It's Best Learned
Verify that the eigenvalues of specific symmetric 2×2 and 3×3 matrices are real and that eigenvectors for distinct eigenvalues are orthogonal via dot product. Contrast with a non-symmetric matrix having complex eigenvalues (e.g., a rotation matrix).

## Common Misconceptions
- Not all matrices with real eigenvalues are symmetric; symmetry is a sufficient but not necessary condition.
- Positive definite matrices have all positive eigenvalues, but not all symmetric matrices with positive diagonal entries are positive definite.
- Symmetry is a property of the matrix in a fixed basis; it is NOT preserved under arbitrary change of basis.
