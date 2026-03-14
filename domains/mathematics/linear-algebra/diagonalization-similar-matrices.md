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
