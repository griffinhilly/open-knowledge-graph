---
id: characteristic-polynomial
title: The Characteristic Polynomial
domain: mathematics
course: linear-algebra
prerequisites:
- id: eigenvalues-and-eigenvectors
  type: hard
- id: cofactor-expansion
  type: soft
builds-toward:
- diagonalization
- spectral-theorem
tags:
- characteristic polynomial
- characteristic equation
- algebraic multiplicity
- geometric multiplicity
- trace
stage: formal-systems
status: validated
---

# The Characteristic Polynomial

## Core Idea
The characteristic polynomial of an n×n matrix A is p(λ) = det(A − λI), a degree-n polynomial in λ whose roots are the eigenvalues of A. By the Fundamental Theorem of Algebra, A has exactly n eigenvalues (counted with algebraic multiplicity) in the complex numbers. The algebraic multiplicity of an eigenvalue λ₀ is its multiplicity as a root of p(λ); the geometric multiplicity is the dimension of its eigenspace. The geometric multiplicity is always at most the algebraic multiplicity, and A is diagonalizable if and only if these multiplicities agree for every eigenvalue.

## How It's Best Learned
Practice computing characteristic polynomials for 2×2 and 3×3 matrices, factoring them to find eigenvalues, and then finding eigenspaces. Notice that the trace of A equals the sum of eigenvalues and det(A) equals their product.

## Common Misconceptions
- The characteristic polynomial is det(A − λI), not det(λI − A) — the sign convention varies by textbook, but the roots are the same.
- A repeated eigenvalue (algebraic multiplicity > 1) does not always yield multiple independent eigenvectors — you must check geometric multiplicity separately.
- An n×n matrix always has a degree-n characteristic polynomial, but may have fewer than n distinct real eigenvalues.
