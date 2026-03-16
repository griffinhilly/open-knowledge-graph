---
id: characteristic-polynomial
title: Characteristic Polynomial and Diagonalization
domain: mathematics
course: linear-algebra
prerequisites:
- id: eigenvalues-eigenvectors
  type: hard
tags:
- characteristic polynomial
- diagonalization
- eigenvalues
stage: formal-systems
status: draft
---

# Characteristic Polynomial and Diagonalization

## Core Idea
The characteristic polynomial of A is det(A − λI), whose roots are eigenvalues. A matrix is diagonalizable if its eigenvectors form a complete basis. Diagonalizable matrices A satisfy A = PDP^{-1}, where D is diagonal and P is the eigenvector matrix. Similar matrices share eigenvalues and determinant.

## Explainer

From your study of eigenvalues and eigenvectors, you know that λ is an eigenvalue of A when Av = λv for some nonzero vector v — equivalently, when (A − λI)v = 0 has a nontrivial solution. This happens precisely when A − λI is **singular**, meaning det(A − λI) = 0. The **characteristic polynomial** is simply this determinant written as a function of λ: p(λ) = det(A − λI). Its roots are exactly the eigenvalues of A.

For an n×n matrix, p(λ) is a polynomial of degree n. For a 2×2 matrix [[a,b],[c,d]], p(λ) = (a−λ)(d−λ) − bc = λ² − (a+d)λ + (ad−bc). Notice what appears: the coefficient of λⁿ⁻¹ is always −tr(A) (the **trace**, sum of diagonal entries), and the constant term is always det(A). This means you can read off two important eigenvalue facts without solving anything: the sum of all eigenvalues equals tr(A), and the product of all eigenvalues equals det(A). The characteristic polynomial encodes these global properties as coefficients.

**Diagonalization** asks: can we choose a basis of eigenvectors? If A has n linearly independent eigenvectors v₁, …, vₙ with eigenvalues λ₁, …, λₙ, form the matrix P whose columns are these vectors and D = diag(λ₁, …, λₙ). Then AP = PD (multiply out: AP's i-th column is Avᵢ = λᵢvᵢ = PD's i-th column), so A = PDP⁻¹. This decomposition is powerful because Aᵏ = PDᵏP⁻¹, and raising a diagonal matrix to a power is trivial: just raise each diagonal entry to that power.

Not every matrix is diagonalizable. The obstruction arises when the **geometric multiplicity** (dimension of the eigenspace) is less than the **algebraic multiplicity** (multiplicity as a root of the characteristic polynomial) for some eigenvalue. For instance, the matrix [[2,1],[0,2]] has characteristic polynomial (λ−2)², so λ = 2 has algebraic multiplicity 2, but the eigenspace is only 1-dimensional — there is only one independent eigenvector. No basis of eigenvectors exists, so the matrix is not diagonalizable. Similar matrices (A and B = PAP⁻¹ for invertible P) always share the same characteristic polynomial and therefore the same eigenvalues, trace, and determinant — these are **similarity invariants** that capture intrinsic properties of the linear transformation regardless of which basis you choose.
