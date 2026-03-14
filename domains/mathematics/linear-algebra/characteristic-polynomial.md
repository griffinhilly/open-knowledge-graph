---
id: characteristic-polynomial
title: Characteristic Polynomial and Eigenvalue Computation
domain: mathematics
course: linear-algebra
prerequisites:
- id: linear-transformation-matrix-representation
  type: hard
- id: determinant-computation
  type: hard
builds-toward:
- eigenvalues-eigenvectors-introduction
- diagonalization-similar-matrices
tags:
- characteristic-polynomial
- eigenvalues
stage: formal-systems
status: draft
---

# Characteristic Polynomial and Eigenvalue Computation

## Core Idea
The characteristic polynomial is char(A) = det(A − λI), a polynomial of degree n. Its roots are the eigenvalues of A. For an n×n matrix, the characteristic polynomial has degree n, yielding at most n eigenvalues (counting multiplicity). Cayley-Hamilton theorem: A satisfies its own characteristic equation, char(A) = 0.
