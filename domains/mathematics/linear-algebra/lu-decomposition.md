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

## Explainer

You already know Gaussian elimination: you apply a sequence of row operations to transform a matrix A into upper triangular form U. LU decomposition is the insight that this process doesn't just produce U — it also produces L automatically as a byproduct. Every time you perform an elimination step (subtract a multiple of one row from another), you are recording a **multiplier**. Collect those multipliers into a lower triangular matrix and you have L. The factorization A = LU is simply a way to package the entire elimination process into two matrices.

To see why L has the shape it does, think about what elimination does: to eliminate the entry in row i, column j, you subtract (a_ij / a_jj) times row j from row i. That ratio is the multiplier, and it fills position (i, j) of L — below the diagonal. The diagonal of L is all 1s because each row eliminates itself trivially. The result is that L is lower triangular with 1s on the diagonal, and U is the upper triangular echelon form of A.

The real payoff comes when you need to solve Ax = b for many different right-hand sides b. With Gaussian elimination alone, you must redo O(n³) work for each new b. With LU, you factor once and then solve two cheaper problems: **forward substitution** (Ly = b, solving for y row by row from top to bottom) and **back substitution** (Ux = y, solving for x row by row from bottom to top). Each of these triangular solves costs only O(n²), so once the factorization is in hand, each new right-hand side is solved in O(n²) time. This is why LU is the standard algorithm inside `numpy.linalg.solve`, MATLAB's `\` operator, and virtually every numerical solver.

One important caveat: LU decomposition as described requires that elimination proceeds without any zero pivots appearing. When a zero pivot would appear, you must swap rows before continuing — this introduces a **permutation matrix** P so that the factorization becomes PA = LU rather than A = LU. In practice, even non-zero pivots are swapped when they are very small relative to other entries (partial pivoting), which improves numerical stability. The L and U factors always exist for any invertible matrix after the appropriate row permutations.
