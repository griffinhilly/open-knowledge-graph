---
id: characteristic-polynomial
title: Characteristic Polynomial
domain: mathematics
course: linear-algebra
prerequisites:
- id: determinants-2x2-3x3
  type: hard
- id: matrix-multiplication
  type: hard
builds-toward:
- eigenvalues-and-eigenvectors
- diagonalization
tags:
- characteristic-polynomial
- eigenvalues
- determinant
stage: formal-systems
status: draft
---

# Characteristic Polynomial

## Core Idea
The characteristic polynomial of n × n matrix A is p(λ) = det(A − λI), a polynomial of degree n. The eigenvalues of A are the roots of p(λ). By the Cayley–Hamilton theorem, A satisfies its own characteristic equation: p(A) = 0.
