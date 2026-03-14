---
id: jordan-normal-form-intro
title: Jordan Normal Form and Generalized Eigenvectors
domain: mathematics
course: linear-algebra
prerequisites:
- id: diagonalization-similar-matrices
  type: hard
builds-toward:
- matrix-exponential
tags:
- jordan-form
- generalized-eigenvectors
- canonical-form
stage: formal-systems
status: draft
---

# Jordan Normal Form and Generalized Eigenvectors

## Core Idea
Not all matrices are diagonalizable. Jordan normal form J is block-diagonal with Jordan blocks (eigenvalue λ on diagonal, 1s on superdiagonal). Every matrix A is similar to its Jordan form: A = PJP⁻¹. Generalized eigenvectors extend eigenvectors to fill out Jordan blocks. Jordan form reveals algebraic and geometric multiplicities and enables computing matrix functions.
