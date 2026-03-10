---
id: diagonalization
title: Diagonalization of Matrices
domain: mathematics
course: linear-algebra
prerequisites:
- id: characteristic-polynomial
  type: hard
- id: change-of-basis
  type: hard
- id: basis-and-dimension
  type: soft
builds-toward:
- spectral-theorem
tags:
- diagonalization
- diagonalizable
- PDP inverse
- eigenbasis
- matrix powers
stage: formal-systems
status: draft
---

# Diagonalization of Matrices

## Core Idea
An n×n matrix A is diagonalizable if there exists an invertible matrix P and a diagonal matrix D such that A = PDP⁻¹. The columns of P are eigenvectors of A and the diagonal entries of D are the corresponding eigenvalues. A is diagonalizable if and only if it has n linearly independent eigenvectors — equivalently, the geometric multiplicity of every eigenvalue equals its algebraic multiplicity. Diagonalization simplifies computations dramatically: Aᵏ = PDᵏP⁻¹ and Dᵏ is trivially computed by raising each diagonal entry to the k-th power.

## How It's Best Learned
Find eigenvectors for each eigenvalue, assemble them as columns of P, write D with eigenvalues on the diagonal, and verify A = PDP⁻¹. Then use diagonalization to compute Aᵏ for large k, where direct multiplication would be prohibitive.

## Common Misconceptions
- Not all matrices are diagonalizable; matrices with repeated eigenvalues and deficient eigenspaces (Jordan blocks) are not.
- The columns of P must be ordered to match the diagonal entries of D — swapping an eigenvector column without swapping the corresponding eigenvalue breaks A = PDP⁻¹.
- Symmetric matrices are always diagonalizable (over R), which is the content of the Spectral Theorem.
