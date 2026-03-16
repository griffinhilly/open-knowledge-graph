---
id: symmetric-matrices-properties
title: Symmetric Matrices and the Spectral Theorem
domain: mathematics
course: linear-algebra
prerequisites:
- id: diagonalization-similar-matrices
  type: hard
builds-toward:
- positive-definite-matrices
- spectral-theorem-symmetric
tags:
- symmetric-matrices
- spectral-theorem
stage: formal-systems
status: draft
---

# Symmetric Matrices and the Spectral Theorem

## Core Idea
A matrix A is symmetric if Aᵀ = A. Symmetric matrices have real eigenvalues and orthogonal eigenvectors (even with repeated eigenvalues). The spectral theorem states: a symmetric matrix A is diagonalizable by an orthogonal matrix Q, so A = QΛQᵀ where Λ is diagonal and Qᵀ = Q⁻¹. This provides a canonical form for quadratic forms and symmetric bilinear forms.

## Explainer

From your study of diagonalization, you know that a general matrix A is diagonalizable as A = PΛP⁻¹ only when it has enough linearly independent eigenvectors, and the change-of-basis matrix P need not be orthogonal or even well-conditioned. **Symmetric matrices** — those satisfying Aᵀ = A — enjoy a far stronger result: they are *always* diagonalizable, with real eigenvalues, and their eigenvectors can always be chosen to be mutually orthogonal. This is not a coincidence but a deep structural consequence of the symmetry condition.

Why real eigenvalues? Suppose λ is a (potentially complex) eigenvalue of a symmetric matrix A with eigenvector v. Working through the algebra using conjugate transposes, the symmetry condition Aᵀ = A forces λ = λ̄, meaning λ must be real. Why orthogonal eigenvectors? If v and w are eigenvectors for *distinct* eigenvalues λ ≠ μ, the symmetry condition forces v · w = 0. Even for repeated eigenvalues, the **Gram-Schmidt process** can always produce an orthogonal basis within each eigenspace — a luxury not available for general matrices where eigenspaces may not span the full space.

The **spectral theorem** packages these facts into the decomposition A = QΛQᵀ, where Q is an **orthogonal matrix** (Qᵀ = Q⁻¹, meaning the columns form an orthonormal basis) and Λ is diagonal with the real eigenvalues on the diagonal. The word "spectral" refers to the spectrum — the set of eigenvalues — and the theorem says every symmetric matrix is completely described by its eigenvalues and an orthonormal eigenbasis. This is the cleanest possible diagonalization: instead of P⁻¹ being expensive to compute, here P⁻¹ = Pᵀ, making the decomposition both numerically stable and interpretable.

The payoff appears immediately in quadratic forms. An expression like 3x² − 2xy + 5y² can be written as **x**ᵀA**x** for a symmetric matrix A. The spectral theorem lets you rotate coordinates (via Q) to eliminate the cross term, revealing the quadratic form as a pure sum of squares in the new coordinates. The eigenvalues of A tell you whether the form is always positive, always negative, or mixed-sign — a classification that appears throughout geometry, optimization (second-derivative tests), and statistics (covariance matrices, principal component analysis).
