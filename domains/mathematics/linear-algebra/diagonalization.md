---
id: diagonalization
title: Diagonalization
domain: mathematics
course: linear-algebra
prerequisites:
- id: eigenvalues-and-eigenvectors
  type: hard
- id: basis-and-dimension
  type: hard
- id: change-of-basis
  type: soft
builds-toward:
- least-squares-approximation
tags:
- diagonalization
- similarity
- powers
- exponentials
stage: formal-systems
status: validated
---

# Diagonalization

## Core Idea
Matrix A is diagonalizable if A = PDP⁻¹ where D is diagonal and P's columns are eigenvectors of A. Diagonalization simplifies computation: Aⁿ = PDⁿP⁻¹. An n × n matrix is diagonalizable iff it has n linearly independent eigenvectors, guaranteed if all eigenvalues are distinct.

## Questions

```yaml
- question: "A 4×4 matrix A has been diagonalized as A = PDP⁻¹. A colleague says computing A¹⁰⁰ requires multiplying A by itself 100 times. What is the correct approach?"
  type: multiple-choice
  options:
    - "Multiply A by itself 100 times — diagonalization only helps for A²"
    - "Compute PD¹⁰⁰P⁻¹, where D¹⁰⁰ is found by raising each diagonal entry to the 100th power"
    - "Raise each entry of A to the 100th power"
    - "Raise each eigenvalue to the 100th power to get the eigenvalues of A¹⁰⁰, but the full matrix cannot be recovered"
  answer: 1
  explanation: "The key payoff of diagonalization is Aⁿ = PDⁿP⁻¹. Since D is diagonal, Dⁿ is trivial — just raise each diagonal entry to the nth power. This reduces 100 full matrix multiplications to raising scalars to a power, then doing two matrix multiplications (with P and P⁻¹). Option D is close to true but incomplete — it correctly identifies the eigenvalues of A¹⁰⁰ but doesn't reconstruct the full matrix."

- question: "Which condition is sufficient (but not necessary) to guarantee that an n × n matrix A is diagonalizable?"
  type: multiple-choice
  options:
    - "All n eigenvalues of A are distinct (no repeated eigenvalues)"
    - "A is invertible (nonzero determinant)"
    - "A is upper triangular"
    - "A has all positive eigenvalues"
  answer: 0
  explanation: "Distinct eigenvalues guarantee diagonalizability because eigenvectors from distinct eigenvalues are always linearly independent, so you automatically get n linearly independent eigenvectors to form the columns of P. This condition is sufficient but not necessary — a matrix can still be diagonalizable with repeated eigenvalues, provided each eigenvalue's geometric multiplicity equals its algebraic multiplicity. Invertibility and triangular structure do not imply diagonalizability."

- question: "A matrix with a repeated eigenvalue can seldom be diagonalized."
  type: true-false
  answer: false
  explanation: "This is a common misconception. Repeated eigenvalues do not automatically prevent diagonalization. What matters is whether the geometric multiplicity of each eigenvalue (the dimension of its eigenspace) equals its algebraic multiplicity (how many times it appears as a root of the characteristic polynomial). If these match for every eigenvalue, the matrix is diagonalizable even with repeats. A non-diagonalizable example with a repeated eigenvalue is [[1,1],[0,1]] — its eigenspace for λ = 1 has dimension 1, but λ = 1 has algebraic multiplicity 2."

- question: "If A = PDP⁻¹ where D is diagonal with entries λ₁, λ₂, …, λₙ, then A¹⁰ = PD¹⁰P⁻¹ where D¹⁰ has entries λ₁¹⁰, λ₂¹⁰, …, λₙ¹⁰."
  type: true-false
  answer: true
  explanation: "This follows directly from the algebra of the factorization. A² = (PDP⁻¹)(PDP⁻¹) = PD(P⁻¹P)DP⁻¹ = PD²P⁻¹, because P⁻¹P = I. By induction, Aⁿ = PDⁿP⁻¹. For a diagonal matrix, raising it to a power just raises each diagonal entry to that power — there are no off-diagonal interactions. This is precisely what makes diagonalization computationally powerful."

- question: "Explain in your own words why diagonalizing a matrix makes computing its powers far more efficient."
  type: short-answer
  answer: "Diagonalization rewrites A = PDP⁻¹ where D is diagonal. Powers simplify as Aⁿ = PDⁿP⁻¹. Raising a diagonal matrix to a power is trivial — just raise each diagonal entry (an eigenvalue) to the nth power. This replaces n−1 full matrix multiplications with scalar exponentiation plus two fixed matrix multiplications."
  explanation: "The key is that P and P⁻¹ cancel in the middle during repeated multiplication: (PDP⁻¹)(PDP⁻¹) = PD(P⁻¹P)DP⁻¹ = PD²P⁻¹. Once you see this cancellation, the formula Aⁿ = PDⁿP⁻¹ follows immediately. The deeper insight: in the eigenvector basis, A acts by simple scaling — each basis vector gets multiplied by its eigenvalue. Repeated application just multiplies the scale factors, which is why powers are trivial in this basis."
```

## Explainer

From your work with eigenvalues and eigenvectors, you know that a vector **v** is an eigenvector of matrix A if Av = λv — multiplying by A just scales **v** by the eigenvalue λ. Diagonalization asks: what if *all* our basis vectors were eigenvectors? Then the matrix would be incredibly easy to work with, because it would just scale each coordinate independently.

Here is the construction. Suppose A is n × n and you can find n linearly independent eigenvectors **v₁, v₂, …, vₙ** with eigenvalues λ₁, λ₂, …, λₙ. Build matrix **P** by placing these eigenvectors as columns: P = [**v₁** | **v₂** | … | **vₙ**]. Build diagonal matrix **D** by placing the corresponding eigenvalues on the diagonal: D = diag(λ₁, λ₂, …, λₙ). Then A = PDP⁻¹. To verify: PDP⁻¹**vᵢ** = PD(**eᵢ**) = P(λᵢ**eᵢ**) = λᵢ**vᵢ** = A**vᵢ**, where **eᵢ** are standard basis vectors. The matrix P is the **change-of-basis** matrix from your basis of eigenvectors back to the standard basis.

The payoff is computation. Squaring A naively requires multiplying two full matrices. But A² = (PDP⁻¹)(PDP⁻¹) = PD²P⁻¹, and D² just squares the diagonal entries. More generally, **Aⁿ = PDⁿP⁻¹**, and Dⁿ is trivial: just raise each diagonal entry to the nth power. This turns computing the 100th power of a matrix from a nightmare into three multiplications. The same trick extends to matrix exponentials: e^(At) = Pe^(Dt)P⁻¹, which is the key to solving systems of differential equations.

The condition for diagonalizability is that A has **n linearly independent eigenvectors** — enough to form a full basis. This is guaranteed when all n eigenvalues are *distinct* (no repeated eigenvalues), because eigenvectors from distinct eigenvalues are always linearly independent. When eigenvalues repeat, diagonalizability is not guaranteed — you need to check whether the **geometric multiplicity** (dimension of the eigenspace) equals the **algebraic multiplicity** (number of times the eigenvalue appears as a root of the characteristic polynomial) for each eigenvalue. If any eigenspace is "too small," A is not diagonalizable — though it may still have a Jordan normal form, the closest diagonal-like structure available.
