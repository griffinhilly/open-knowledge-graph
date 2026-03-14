---
id: eigenvalues-eigenvectors-introduction
title: Eigenvalues and Eigenvectors
domain: mathematics
course: linear-algebra
prerequisites:
- id: characteristic-polynomial
  type: hard
builds-toward:
- diagonalization-similar-matrices
- jordan-normal-form-intro
tags:
- eigenvalues
- eigenvectors
- spectral
stage: formal-systems
status: draft
---

# Eigenvalues and Eigenvectors

## Core Idea
For a square matrix A, an eigenvector is a nonzero vector v with Av = λv for some scalar λ (eigenvalue). Eigenvectors point in directions unchanged by A (only scaled). Eigenvalues are roots of det(A − λI) = 0. Eigenspaces E_λ = ker(A − λI) are subspaces of eigenvectors for each λ. Real matrices may have complex eigenvalues.
