---
id: positive-definite-matrices
title: Positive Definite Matrices
domain: mathematics
course: linear-algebra
prerequisites:
- id: symmetric-matrices
  type: hard
builds-toward:
- least-squares-approximation
tags:
- positive-definite
- quadratic-forms
stage: formal-systems
status: validated
---

# Positive Definite Matrices

## Core Idea
A symmetric matrix A is positive definite if xᵀAx > 0 for all nonzero x. Equivalently, all eigenvalues are positive. Positive definite matrices are invertible, have a unique Cholesky decomposition A = LLᵀ, and define a valid inner product. The normal equations AᵀAx = Aᵀb have a unique solution when A has full column rank (AᵀA is positive definite).

## Questions

```yaml
- question: "A student checks that a symmetric matrix A is invertible (det A ≠ 0) and concludes it must be positive definite. Why is this wrong?"
  type: multiple-choice
  options:
    - "It is correct — invertible symmetric matrices are always positive definite"
    - "Invertibility only rules out zero eigenvalues; a matrix with negative eigenvalues is invertible but not positive definite"
    - "Invertibility and positive definiteness are unrelated and neither implies the other"
    - "Positive definite matrices are never invertible because xᵀAx = 0 would have no solution"
  answer: 1
  explanation: "Positive definiteness requires all eigenvalues to be strictly positive. Invertibility only requires that no eigenvalue is zero. A symmetric matrix with eigenvalues {3, −2} is invertible (neither is zero) but not positive definite (one is negative) — it produces a saddle-shaped quadratic form, not a bowl. The correct test checks the sign of all eigenvalues, or equivalently verifies xᵀAx > 0 for all nonzero x. Invertibility is necessary but far from sufficient for positive definiteness."

- question: "Which of the following is the correct characterization? A symmetric matrix A is positive definite if and only if…"
  type: multiple-choice
  options:
    - "A is invertible and has positive diagonal entries"
    - "xᵀAx > 0 for all nonzero vectors x (equivalently, all eigenvalues are strictly positive)"
    - "The determinant of A is positive"
    - "A has an LU factorization with positive diagonal entries in U"
  answer: 1
  explanation: "The definition (xᵀAx > 0 for all nonzero x) and the eigenvalue condition (all eigenvalues positive) are equivalent and together constitute the correct characterization. Option A fails: diagonal entries can be positive while some eigenvalues are negative (off-diagonal entries can force negative eigenvalues). Option C fails: a 4×4 matrix with eigenvalues {2, 2, 2, −3} has positive determinant (product = 24) but is not positive definite. Option D describes LU factorization, not Cholesky (A = LLᵀ), and applies to a much broader class."

- question: "The matrix AᵀA (formed from any real matrix A with more rows than columns) is typically positive definite."
  type: true-false
  answer: false
  explanation: "AᵀA is always symmetric and positive semidefinite (xᵀAᵀAx = ‖Ax‖² ≥ 0), but it is only positive definite when A has full column rank. If A has a nontrivial null space — some nonzero x with Ax = 0 — then xᵀAᵀAx = 0 for that x, violating strict positivity. This matters for least-squares: AᵀA guarantees a unique minimizer exactly when it is positive definite, i.e., when A has full column rank with no redundant columns."

- question: "A positive definite matrix A defines a quadratic form xᵀAx that produces a bowl-shaped surface opening upward, with its unique minimum at the origin."
  type: true-false
  answer: true
  explanation: "This is the geometric heart of positive definiteness. xᵀAx > 0 for all nonzero x means every point except the origin lies strictly above zero — the surface is a bowl (an upward-opening paraboloid for 2×2 matrices). This geometry directly motivates why positive definite matrices appear in optimization: they guarantee a unique global minimum, making systems like the normal equations in least squares well-posed with a unique solution."

- question: "What is the Cholesky decomposition, what does it require, and why is its existence equivalent to positive definiteness?"
  type: short-answer
  answer: "The Cholesky decomposition factors a matrix as A = LLᵀ, where L is lower triangular with positive diagonal entries. It exists if and only if A is symmetric and positive definite. The decomposition is the matrix analogue of writing a positive number as a square (9 = 3²): just as a positive number has a real square root, a positive definite matrix has this 'square root' factorization. If any step of the Cholesky algorithm requires taking the square root of a non-positive number, the matrix is not positive definite."
  explanation: "The Cholesky decomposition serves as both a test and a computational tool. Its existence certificates positive definiteness, and it is roughly twice as efficient as LU decomposition for solving symmetric positive definite linear systems — which is why identifying positive definiteness matters practically in scientific computing, not just theoretically."
```

## Explainer

The expression xᵀAx is called a **quadratic form**. For a 2×2 symmetric matrix, it produces an expression like ax₁² + 2bx₁x₂ + cx₂², a bowl-shaped or saddle-shaped surface when graphed. Positive definiteness means this surface is always bowl-shaped — it opens upward and has a unique minimum at the origin. Every other point is strictly higher. This geometric picture is the heart of the concept: a positive definite matrix defines a "shape" on space that behaves like a generalized squared length, always positive except at the origin.

You know from your study of symmetric matrices that symmetric matrices have real eigenvalues and orthogonal eigenvectors. The connection between eigenvalues and positive definiteness is direct: since A is symmetric, any vector x can be written in terms of eigenvectors, and xᵀAx becomes a sum of terms λᵢ(vᵢ · x)². For this sum to be positive for all nonzero x, every eigenvalue λᵢ must be positive. This gives the equivalence: **positive definite** ↔ **all eigenvalues positive**. Negative eigenvalues produce saddle-shaped quadratic forms; zero eigenvalues produce degenerate forms that collapse along some direction.

The **Cholesky decomposition** A = LLᵀ, where L is a lower triangular matrix with positive diagonal entries, is the computational signature of positive definiteness. It is the matrix analogue of writing a positive number as a square: just as 9 = 3², a positive definite matrix factors as A = LLᵀ. This decomposition exists if and only if A is positive definite, making it both a test and a tool. Numerically, Cholesky decomposition is twice as efficient as LU decomposition for symmetric positive definite systems, which is why recognizing positive definiteness matters in practice.

The most important application is in least-squares problems. When you have an overdetermined system Ax = b with more equations than unknowns, you seek the best approximate solution via the normal equations AᵀAx = Aᵀb. The matrix AᵀA is always symmetric, and it is positive definite whenever A has full column rank (no redundant columns). Positive definiteness of AᵀA guarantees these normal equations have a unique solution — the unique least-squares minimizer. Without full rank, AᵀA is only positive *semi*-definite, and solutions are no longer unique.
