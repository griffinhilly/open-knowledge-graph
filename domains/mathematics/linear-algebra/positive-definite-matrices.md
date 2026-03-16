---
id: positive-definite-matrices
title: Positive Definite Matrices
domain: mathematics
course: linear-algebra
prerequisites:
- id: symmetric-matrices-properties
  type: hard
builds-toward:
- least-squares-approximation
tags:
- positive-definite
- quadratic-forms
stage: formal-systems
status: draft
---

# Positive Definite Matrices

## Core Idea
A symmetric matrix A is positive definite if xᵀAx > 0 for all nonzero x. Equivalently, all eigenvalues are positive. Positive definite matrices are invertible, have a unique Cholesky decomposition A = LLᵀ, and define a valid inner product. The normal equations AᵀAx = Aᵀb have a unique solution when A has full column rank (AᵀA is positive definite).

## Explainer

The expression xᵀAx is called a **quadratic form**. For a 2×2 symmetric matrix, it produces an expression like ax₁² + 2bx₁x₂ + cx₂², a bowl-shaped or saddle-shaped surface when graphed. Positive definiteness means this surface is always bowl-shaped — it opens upward and has a unique minimum at the origin. Every other point is strictly higher. This geometric picture is the heart of the concept: a positive definite matrix defines a "shape" on space that behaves like a generalized squared length, always positive except at the origin.

You know from your study of symmetric matrices that symmetric matrices have real eigenvalues and orthogonal eigenvectors. The connection between eigenvalues and positive definiteness is direct: since A is symmetric, any vector x can be written in terms of eigenvectors, and xᵀAx becomes a sum of terms λᵢ(vᵢ · x)². For this sum to be positive for all nonzero x, every eigenvalue λᵢ must be positive. This gives the equivalence: **positive definite** ↔ **all eigenvalues positive**. Negative eigenvalues produce saddle-shaped quadratic forms; zero eigenvalues produce degenerate forms that collapse along some direction.

The **Cholesky decomposition** A = LLᵀ, where L is a lower triangular matrix with positive diagonal entries, is the computational signature of positive definiteness. It is the matrix analogue of writing a positive number as a square: just as 9 = 3², a positive definite matrix factors as A = LLᵀ. This decomposition exists if and only if A is positive definite, making it both a test and a tool. Numerically, Cholesky decomposition is twice as efficient as LU decomposition for symmetric positive definite systems, which is why recognizing positive definiteness matters in practice.

The most important application is in least-squares problems. When you have an overdetermined system Ax = b with more equations than unknowns, you seek the best approximate solution via the normal equations AᵀAx = Aᵀb. The matrix AᵀA is always symmetric, and it is positive definite whenever A has full column rank (no redundant columns). Positive definiteness of AᵀA guarantees these normal equations have a unique solution — the unique least-squares minimizer. Without full rank, AᵀA is only positive *semi*-definite, and solutions are no longer unique.
