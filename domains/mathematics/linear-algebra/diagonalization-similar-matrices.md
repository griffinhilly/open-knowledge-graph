---
id: diagonalization-similar-matrices
title: Diagonalization and Similar Matrices
domain: mathematics
course: linear-algebra
prerequisites:
- id: eigenvalues-eigenvectors-introduction
  type: hard
- id: change-of-basis-matrices
  type: hard
builds-toward:
- jordan-normal-form-intro
- spectral-theorem-symmetric
tags:
- diagonalization
- similar-matrices
- canonical-form
stage: formal-systems
status: draft
---

# Diagonalization and Similar Matrices

## Core Idea
A matrix A is diagonalizable if A = PDP⁻¹ where D is diagonal and P has eigenvectors as columns. Diagonalizable iff A has n linearly independent eigenvectors. Similar matrices represent the same transformation in different bases; A and B are similar iff they have the same eigenvalues and can be diagonalized to the same D. Diagonalization simplifies computation of powers Aⁿ and exponentials eᴬ.

## How It's Best Learned
Find eigenvalues and eigenvectors. Build P from eigenvectors as columns; D has eigenvalues on the diagonal. Verify A = PDP⁻¹ by computation. Use diagonal form to compute A¹⁰ easily.

## Explainer

From eigenvalues and eigenvectors, you know that the equation Av = λv identifies special directions — **eigenvectors** — where a matrix acts purely by scaling. From change-of-basis, you know that the same linear transformation looks different in different coordinate systems, and that P and P⁻¹ convert between them. **Diagonalization** combines these two ideas: it asks whether there exists a basis made entirely of eigenvectors, because in that basis, the transformation looks perfectly simple — a diagonal matrix.

Here is the mechanism. If A has n linearly independent eigenvectors v₁, …, vₙ with eigenvalues λ₁, …, λₙ, build the matrix P whose columns are those eigenvectors. Then A = PDP⁻¹, where D is the diagonal matrix with λ₁, …, λₙ on the diagonal. To see why: AP = PD expresses the fact that multiplying each eigenvector by A is the same as multiplying it by its eigenvalue. Read the factorization as three steps: P⁻¹ converts a vector from standard coordinates into eigenvector coordinates; D scales each eigenvector-coordinate by its eigenvalue; P converts back to standard coordinates. The whole trip is equivalent to one application of A.

The payoff is **computing powers**. A diagonal matrix Dⁿ is trivial — just raise each diagonal entry to the n-th power. So Aⁿ = PDⁿP⁻¹ reduces matrix exponentiation (hard in general) to scalar exponentiation plus two matrix multiplications. This is essential in applications like Markov chains (where you need Aⁿ for large n), differential equations (where matrix exponentials eᴬᵗ appear), and PageRank (where you iterate a transition matrix to convergence). Without diagonalization, computing A¹⁰⁰ would require 99 matrix multiplications; with it, it requires one.

Two matrices A and B are **similar** (B = P⁻¹AP for some invertible P) when they represent the same linear transformation expressed in different bases. Similar matrices share all eigenvalues, the same determinant, the same trace, and the same characteristic polynomial. If A is diagonalizable, every matrix similar to A is also diagonalizable with the same diagonal form D. A matrix is diagonalizable if and only if it has n linearly independent eigenvectors — a sufficient condition is having n *distinct* eigenvalues, but repeated eigenvalues may or may not provide enough independent eigenvectors. When they don't, the best available form is the Jordan normal form, which you'll encounter next.
