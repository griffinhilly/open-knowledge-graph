---
id: eigenvalues-and-eigenvectors
title: Eigenvalues and Eigenvectors
domain: mathematics
course: linear-algebra
prerequisites:
- id: linear-transformations
  type: hard
- id: determinant-properties
  type: hard
- id: null-space
  type: soft
- id: transformation-matrices
  type: soft
builds-toward:
- characteristic-polynomial
- diagonalization
- spectral-theorem
tags:
- eigenvalue
- eigenvector
- eigenspace
- Av = lambda v
- characteristic
stage: formal-systems
status: validated
---
# Eigenvalues and Eigenvectors

## Core Idea
An eigenvector of a square matrix A is a nonzero vector v such that Av = λv for some scalar λ called the eigenvalue. Geometrically, eigenvectors are directions that the transformation stretches or shrinks (by factor λ) without rotating. To find eigenvalues, solve det(A − λI) = 0 (the characteristic equation); to find eigenvectors for a given λ, find the null space of (A − λI). The eigenspace for eigenvalue λ is the subspace Nul(A − λI). Eigenvalues and eigenvectors are central to applications including differential equations, data compression (PCA), and quantum mechanics.

## How It's Best Learned
Compute eigenvalues and eigenvectors for 2×2 matrices first; verify that Av = λv holds for each eigenvector. Then build intuition for what each eigenvalue means geometrically (λ > 1 stretches, 0 < λ < 1 shrinks, λ < 0 flips, λ = 0 projects to zero).

## Common Misconceptions
- An eigenvector must be NONZERO by definition; the zero vector satisfies Av = λv trivially for any λ.
- A matrix can have complex eigenvalues even if all its entries are real — this occurs for rotation matrices, for example.
- Different eigenvalues always have linearly independent eigenvectors; the same eigenvalue may have multiple linearly independent eigenvectors (forming an eigenspace of dimension > 1).
