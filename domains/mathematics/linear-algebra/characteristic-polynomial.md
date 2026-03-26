---
id: characteristic-polynomial
title: Characteristic Polynomial and Diagonalization
domain: mathematics
course: linear-algebra
prerequisites:
- id: eigenvalues-and-eigenvectors
  type: hard
tags:
- characteristic polynomial
- diagonalization
- eigenvalues
stage: formal-systems
status: validated
---

# Characteristic Polynomial and Diagonalization

## Core Idea
The characteristic polynomial of A is det(A − λI), whose roots are eigenvalues. A matrix is diagonalizable if its eigenvectors form a complete basis. Diagonalizable matrices A satisfy A = PDP^{-1}, where D is diagonal and P is the eigenvector matrix. Similar matrices share eigenvalues and determinant.

## Questions

```yaml
- question: "A 3×3 matrix has characteristic polynomial (λ − 2)(λ − 3)². Which additional fact would guarantee the matrix is diagonalizable?"
  type: multiple-choice
  options:
    - "The eigenspace for λ = 2 is 1-dimensional"
    - "The eigenspace for λ = 3 is 2-dimensional"
    - "The trace of the matrix equals 8"
    - "The determinant of the matrix equals 36"
  answer: 1
  explanation: "Diagonalizability requires that for every eigenvalue, the geometric multiplicity (dimension of the eigenspace) equals the algebraic multiplicity (multiplicity as a root of the characteristic polynomial). Here λ = 2 has algebraic multiplicity 1, so its eigenspace is automatically 1-dimensional — no problem there. The concern is λ = 3 with algebraic multiplicity 2: if its eigenspace is only 1-dimensional, diagonalization fails. Confirming a 2-dimensional eigenspace for λ = 3 ensures geometric = algebraic multiplicity for every eigenvalue. Trace and determinant tell you sums and products of eigenvalues, but nothing about eigenspace dimensions."

- question: "What does the constant term of the characteristic polynomial of an n×n matrix always equal?"
  type: multiple-choice
  options:
    - "The trace of the matrix (sum of diagonal entries)"
    - "The sum of all eigenvalues"
    - "The determinant of the matrix"
    - "The product of the diagonal entries only"
  answer: 2
  explanation: "The characteristic polynomial is p(λ) = det(A − λI). At λ = 0, this becomes det(A − 0) = det(A). So the constant term of p(λ) is always the determinant of A. This gives a useful check: since the constant term also equals the product of all eigenvalues (evaluated at λ = 0), the product of the eigenvalues equals det(A). Similarly, the coefficient of λⁿ⁻¹ is always −tr(A), connecting eigenvalue sums to the trace. These relationships hold even without solving for eigenvalues explicitly."

- question: "Two matrices with the same characteristic polynomial must be similar to each other."
  type: true-false
  answer: false
  explanation: "Similarity implies the same characteristic polynomial — that direction holds. But the converse fails: two matrices can share a characteristic polynomial without being similar. The classic example involves the 2×2 identity matrix I and any diagonalizable matrix with both eigenvalues equal to 1; they have the same characteristic polynomial (λ−1)² but are similar only to I itself. More starkly, [[1,1],[0,1]] and [[1,0],[0,1]] have the same characteristic polynomial (λ−1)² but are not similar (one is diagonalizable, the other is not). The characteristic polynomial is a similarity invariant, but not a complete invariant."

- question: "A square matrix with n distinct eigenvalues is always diagonalizable."
  type: true-false
  answer: true
  explanation: "Eigenvectors corresponding to distinct eigenvalues are always linearly independent. If an n×n matrix has n distinct eigenvalues, it has n linearly independent eigenvectors, which form a basis of ℝⁿ. The columns of P (the eigenvector matrix) are then a complete basis, P is invertible, and A = PDP⁻¹ holds. Note that the converse is false: a matrix can be diagonalizable even with repeated eigenvalues, as long as the geometric multiplicity matches the algebraic multiplicity for each repeated eigenvalue."

- question: "What is the difference between algebraic multiplicity and geometric multiplicity of an eigenvalue, and why does their relationship determine whether a matrix is diagonalizable?"
  type: short-answer
  answer: "The algebraic multiplicity of eigenvalue λ is its multiplicity as a root of the characteristic polynomial det(A − λI). The geometric multiplicity is the dimension of the corresponding eigenspace — the number of linearly independent eigenvectors for that eigenvalue. Geometric multiplicity ≤ algebraic multiplicity always. Diagonalization requires a complete basis of eigenvectors, so you need n total linearly independent eigenvectors. If geometric multiplicity is strictly less than algebraic multiplicity for any eigenvalue, there are not enough eigenvectors to span ℝⁿ, and diagonalization fails."
  explanation: "The matrix [[2,1],[0,2]] illustrates the failure: characteristic polynomial (λ−2)² gives algebraic multiplicity 2, but solving (A−2I)v = 0 yields only a 1-dimensional eigenspace (geometric multiplicity 1). One eigenvector short of a basis means no diagonalization is possible. The matrix is instead similar to a Jordan block — the next topic in the theory of canonical forms."
```

## Explainer

From your study of eigenvalues and eigenvectors, you know that λ is an eigenvalue of A when Av = λv for some nonzero vector v — equivalently, when (A − λI)v = 0 has a nontrivial solution. This happens precisely when A − λI is **singular**, meaning det(A − λI) = 0. The **characteristic polynomial** is simply this determinant written as a function of λ: p(λ) = det(A − λI). Its roots are exactly the eigenvalues of A.

For an n×n matrix, p(λ) is a polynomial of degree n. For a 2×2 matrix [[a,b],[c,d]], p(λ) = (a−λ)(d−λ) − bc = λ² − (a+d)λ + (ad−bc). Notice what appears: the coefficient of λⁿ⁻¹ is always −tr(A) (the **trace**, sum of diagonal entries), and the constant term is always det(A). This means you can read off two important eigenvalue facts without solving anything: the sum of all eigenvalues equals tr(A), and the product of all eigenvalues equals det(A). The characteristic polynomial encodes these global properties as coefficients.

**Diagonalization** asks: can we choose a basis of eigenvectors? If A has n linearly independent eigenvectors v₁, …, vₙ with eigenvalues λ₁, …, λₙ, form the matrix P whose columns are these vectors and D = diag(λ₁, …, λₙ). Then AP = PD (multiply out: AP's i-th column is Avᵢ = λᵢvᵢ = PD's i-th column), so A = PDP⁻¹. This decomposition is powerful because Aᵏ = PDᵏP⁻¹, and raising a diagonal matrix to a power is trivial: just raise each diagonal entry to that power.

Not every matrix is diagonalizable. The obstruction arises when the **geometric multiplicity** (dimension of the eigenspace) is less than the **algebraic multiplicity** (multiplicity as a root of the characteristic polynomial) for some eigenvalue. For instance, the matrix [[2,1],[0,2]] has characteristic polynomial (λ−2)², so λ = 2 has algebraic multiplicity 2, but the eigenspace is only 1-dimensional — there is only one independent eigenvector. No basis of eigenvectors exists, so the matrix is not diagonalizable. Similar matrices (A and B = PAP⁻¹ for invertible P) always share the same characteristic polynomial and therefore the same eigenvalues, trace, and determinant — these are **similarity invariants** that capture intrinsic properties of the linear transformation regardless of which basis you choose.
