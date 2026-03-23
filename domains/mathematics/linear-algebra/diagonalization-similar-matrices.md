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
status: validated
---

# Diagonalization and Similar Matrices

## Core Idea
A matrix A is diagonalizable if A = PDP⁻¹ where D is diagonal and P has eigenvectors as columns. Diagonalizable iff A has n linearly independent eigenvectors. Similar matrices represent the same transformation in different bases; A and B are similar iff they have the same eigenvalues and can be diagonalized to the same D. Diagonalization simplifies computation of powers Aⁿ and exponentials eᴬ.

## How It's Best Learned
Find eigenvalues and eigenvectors. Build P from eigenvectors as columns; D has eigenvalues on the diagonal. Verify A = PDP⁻¹ by computation. Use diagonal form to compute A¹⁰ easily.

## Questions

```yaml
- question: "A 3×3 matrix A has eigenvalues 2, 2, and 5. Is A necessarily diagonalizable?"
  type: multiple-choice
  options:
    - "Yes — A has real eigenvalues, which is sufficient for diagonalizability"
    - "No — A has a repeated eigenvalue, so it cannot be diagonalized"
    - "It depends — A is diagonalizable if and only if the eigenvalue 2 has two linearly independent eigenvectors"
    - "It depends — A is diagonalizable if and only if the eigenvalue 5 has a non-zero eigenvector"
  answer: 2
  explanation: "The condition for diagonalizability is having n linearly independent eigenvectors, not having distinct eigenvalues. A repeated eigenvalue (here, λ=2 with multiplicity 2) may or may not provide two independent eigenvectors. If it does (geometric multiplicity equals algebraic multiplicity), A is diagonalizable. If it does not (only one independent eigenvector for λ=2), A is not diagonalizable and requires Jordan normal form instead. Option B is the common misconception — repeated eigenvalues do not automatically prevent diagonalization."

- question: "What is the primary computational advantage of diagonalizing a matrix A = PDP⁻¹ before computing A¹⁰⁰?"
  type: multiple-choice
  options:
    - "It reduces the matrix to a smaller size, making storage more efficient"
    - "It allows A¹⁰⁰ = PD¹⁰⁰P⁻¹, where D¹⁰⁰ requires only raising scalar diagonal entries to the 100th power"
    - "It ensures the result has only integer entries, simplifying exact computation"
    - "It converts the problem to solving a system of linear equations, which is faster"
  answer: 1
  explanation: "The key identity is Aⁿ = PDⁿP⁻¹. A diagonal matrix Dⁿ is trivial to compute: just raise each diagonal entry to the n-th power (scalar exponentiation). Without diagonalization, computing A¹⁰⁰ would require 99 matrix multiplications, each O(n³). With diagonalization, it requires computing P and P⁻¹ once, then one multiplication PDⁿP⁻¹. This is the payoff for all the eigenvalue machinery — it reduces matrix exponentiation (hard) to scalar exponentiation (trivial) plus two matrix multiplications."

- question: "If a matrix has a repeated eigenvalue, it cannot be diagonalized."
  type: true-false
  answer: false
  explanation: "This is a common misconception. A matrix is diagonalizable if and only if it has n linearly independent eigenvectors. Distinct eigenvalues guarantee this (since eigenvectors for distinct eigenvalues are always independent), so a matrix with n distinct eigenvalues is always diagonalizable. But a repeated eigenvalue *may* still yield enough independent eigenvectors — the identity matrix I has only one eigenvalue (λ=1, with multiplicity n) yet is perfectly diagonalizable (it's already diagonal). The question is whether the geometric multiplicity (dimension of the eigenspace) equals the algebraic multiplicity (multiplicity as a root of the characteristic polynomial)."

- question: "Two similar matrices A and B, related by B = P⁻¹AP for some invertible P, always have the same eigenvalues because they represent the same linear transformation in different coordinate systems."
  type: true-false
  answer: true
  explanation: "Similarity is a change of basis: A and B describe the same linear transformation, just expressed in different bases (related by P). Since eigenvalues capture the intrinsic scaling behavior of a transformation — not the coordinate system used to describe it — they are invariants of the transformation itself, not of any particular matrix representation. Similar matrices therefore share all eigenvalues, the same characteristic polynomial, the same determinant, and the same trace. This is why diagonalization can be thought of as finding the 'simplest' basis to represent a transformation."

- question: "Explain what it means geometrically that the columns of P are eigenvectors. Why does this choice of P make the factorization A = PDP⁻¹ hold?"
  type: short-answer
  answer: "Each column of P is an eigenvector vᵢ of A, meaning Avᵢ = λᵢvᵢ — A acts on vᵢ purely by scaling (no rotation or mixing). The equation AP = PD expresses this simultaneously for all eigenvectors: multiplying each column by A is the same as multiplying it by its eigenvalue (which is what D does — it scales the i-th column by λᵢ). So PDP⁻¹ applies three steps: convert to eigenvector coordinates (P⁻¹), scale each coordinate by its eigenvalue (D), convert back (P). The composition of these three steps is exactly what A does."
  explanation: "The geometric insight is that eigenvectors are the 'natural axes' of a linear transformation — the directions where the transformation acts simplest (pure scaling). In the eigenvector basis, A looks diagonal because all cross-terms vanish: each basis vector is only scaled, never mixed with others. Diagonalization is just the algebraic expression of this geometric fact. This is also why not every matrix is diagonalizable: if A rotates or shears space in a way that mixes directions, there may not be enough invariant directions (eigenvectors) to form a complete basis."
```

## Explainer

From eigenvalues and eigenvectors, you know that the equation Av = λv identifies special directions — **eigenvectors** — where a matrix acts purely by scaling. From change-of-basis, you know that the same linear transformation looks different in different coordinate systems, and that P and P⁻¹ convert between them. **Diagonalization** combines these two ideas: it asks whether there exists a basis made entirely of eigenvectors, because in that basis, the transformation looks perfectly simple — a diagonal matrix.

Here is the mechanism. If A has n linearly independent eigenvectors v₁, …, vₙ with eigenvalues λ₁, …, λₙ, build the matrix P whose columns are those eigenvectors. Then A = PDP⁻¹, where D is the diagonal matrix with λ₁, …, λₙ on the diagonal. To see why: AP = PD expresses the fact that multiplying each eigenvector by A is the same as multiplying it by its eigenvalue. Read the factorization as three steps: P⁻¹ converts a vector from standard coordinates into eigenvector coordinates; D scales each eigenvector-coordinate by its eigenvalue; P converts back to standard coordinates. The whole trip is equivalent to one application of A.

The payoff is **computing powers**. A diagonal matrix Dⁿ is trivial — just raise each diagonal entry to the n-th power. So Aⁿ = PDⁿP⁻¹ reduces matrix exponentiation (hard in general) to scalar exponentiation plus two matrix multiplications. This is essential in applications like Markov chains (where you need Aⁿ for large n), differential equations (where matrix exponentials eᴬᵗ appear), and PageRank (where you iterate a transition matrix to convergence). Without diagonalization, computing A¹⁰⁰ would require 99 matrix multiplications; with it, it requires one.

Two matrices A and B are **similar** (B = P⁻¹AP for some invertible P) when they represent the same linear transformation expressed in different bases. Similar matrices share all eigenvalues, the same determinant, the same trace, and the same characteristic polynomial. If A is diagonalizable, every matrix similar to A is also diagonalizable with the same diagonal form D. A matrix is diagonalizable if and only if it has n linearly independent eigenvectors — a sufficient condition is having n *distinct* eigenvalues, but repeated eigenvalues may or may not provide enough independent eigenvectors. When they don't, the best available form is the Jordan normal form, which you'll encounter next.
