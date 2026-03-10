---
id: spectral-theorem
title: The Spectral Theorem
domain: mathematics
course: linear-algebra
prerequisites:
- id: symmetric-matrices
  type: hard
- id: diagonalization
  type: hard
- id: orthonormal-bases
  type: hard
tags:
- spectral theorem
- orthogonal diagonalization
- principal axes
- eigendecomposition
- symmetric
stage: formal-systems
status: draft
---

# The Spectral Theorem

## Core Idea
The Spectral Theorem states that every real symmetric matrix A is orthogonally diagonalizable: there exists an orthogonal matrix Q (with Qᵀ = Q⁻¹) and diagonal matrix D such that A = QDQᵀ. The columns of Q are orthonormal eigenvectors of A and D contains the corresponding real eigenvalues. This is stronger than ordinary diagonalization in two ways: the diagonalizing matrix Q is orthogonal (not just invertible), and real eigenvectors always exist. The spectral decomposition A = Σ λᵢuᵢuᵢᵀ writes A as a sum of rank-1 orthogonal projections, one per eigenvalue, revealing the geometric structure of the transformation.

## How It's Best Learned
Orthogonally diagonalize a 2×2 symmetric matrix, verify Q is orthogonal, and reconstruct A = QDQᵀ. Then interpret the eigenvectors as the 'principal axes' of the quadratic form xᵀAx — an ellipse aligned with the eigenvectors.

## Common Misconceptions
- The Spectral Theorem applies to SYMMETRIC matrices; it does not hold for general (non-symmetric) matrices, which may not be diagonalizable or may require complex eigenvectors.
- 'Spectral' refers to the spectrum (set of eigenvalues) of A, not to visible-light spectra.
- Orthogonal diagonalization requires Gram-Schmidt within each eigenspace when an eigenvalue has geometric multiplicity > 1; distinct eigenvalue eigenvectors are already orthogonal but may need normalization.
