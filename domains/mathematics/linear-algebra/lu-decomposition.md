---
id: lu-decomposition
title: LU Decomposition
domain: mathematics
course: linear-algebra
prerequisites:
- id: gaussian-elimination
  type: hard
- id: matrix-inverses
  type: soft
tags:
- LU decomposition
- LU factorization
- lower triangular
- upper triangular
- factorization
stage: formal-systems
status: validated
---

# LU Decomposition

## Core Idea
LU decomposition factors a square matrix A into a product A = LU where L is lower triangular (with 1s on the diagonal) and U is upper triangular. The U factor is the row echelon form of A, and L records the multipliers used in Gaussian elimination. Once computed, LU decomposition allows efficient solution of Ax = b for multiple right-hand sides b: first solve Ly = b (forward substitution), then Ux = y (back substitution), each taking O(n²) time rather than O(n³) for full elimination. LU decomposition is the practical workhorse for numerical linear algebra.

## How It's Best Learned
Perform Gaussian elimination on a matrix while recording multipliers in a separate L matrix. Verify that LU = A. Then solve two or three linear systems with different b vectors using the same LU factorization to appreciate the computational savings.

## Common Misconceptions
- LU decomposition does not always exist without row pivoting; matrices requiring row swaps during elimination need a permutation matrix P so that PA = LU.
- L records the NEGATIVES of the multipliers used to eliminate; a sign error here breaks the factorization.
- LU factorization is not the same as diagonalization; it factors A into triangular matrices, not into diagonal form.
