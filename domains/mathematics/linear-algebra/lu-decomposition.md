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

## Questions

```yaml
- question: "You need to solve Ax = b for 50 different right-hand-side vectors b, where A is a fixed 500×500 matrix. Compared to running Gaussian elimination 50 separate times, LU decomposition offers what advantage?"
  type: multiple-choice
  options:
    - "LU is faster only for the first solve; subsequent solves cost the same as elimination"
    - "LU performs one O(n³) factorization, then each of the 50 solves costs only O(n²) via forward and back substitution"
    - "Both approaches cost the same total work — LU is only useful when b is unknown in advance"
    - "LU avoids all numerical errors, making it more accurate rather than faster"
  answer: 1
  explanation: "This is the core practical payoff of LU decomposition. Gaussian elimination on a new b costs O(n³) each time because it redoes the entire elimination. LU factors A once at O(n³), then each new b requires only forward substitution (Ly = b, O(n²)) and back substitution (Ux = y, O(n²)). For 50 right-hand sides, LU replaces 50 × O(n³) operations with 1 × O(n³) + 50 × O(n²) — a dramatic saving for large n."

- question: "What does the lower triangular matrix L in an LU decomposition actually store?"
  type: multiple-choice
  options:
    - "The inverse of the upper triangular matrix U"
    - "The row echelon form of A with the pivots on the diagonal"
    - "The multipliers used during Gaussian elimination to zero out below-diagonal entries"
    - "The eigenvalues of A arranged in lower triangular form"
  answer: 2
  explanation: "Each entry ℓᵢⱼ below the diagonal of L is the multiplier used in Gaussian elimination to eliminate the entry in row i, column j: the ratio aᵢⱼ/aⱼⱼ at that elimination step. L is not invented separately — it is produced automatically as a byproduct of elimination. The diagonal of L is all 1s because each row trivially eliminates itself. This is the elegant insight: elimination produces both U (explicitly) and L (via the recorded multipliers) simultaneously."

- question: "LU decomposition always exists for any invertible matrix without requiring row interchanges."
  type: true-false
  answer: false
  explanation: "This is a common misconception. Even invertible matrices can produce a zero pivot during elimination, which requires a row swap before proceeding. When row swaps are needed, the correct factorization is PA = LU, where P is a permutation matrix recording the row swaps. In practice, partial pivoting (swapping rows to place the largest available pivot first) is always used for numerical stability, even when pivots wouldn't be exactly zero. A = LU without P only works for matrices where elimination proceeds with no row swaps."

- question: "Solving the triangular system Ly = b (forward substitution) costs O(n²) operations, which is cheaper than the O(n³) required for full Gaussian elimination on Ax = b."
  type: true-false
  answer: true
  explanation: "A lower triangular system with n unknowns is solved row by row from top to bottom. Each row i requires i–1 multiplications and subtractions (for already-solved variables) plus one division — O(i) operations. Summing over all rows gives O(1 + 2 + ... + n) = O(n²). The same applies to back substitution for U. Full Gaussian elimination, which must also reduce the matrix, costs O(n³). This is why LU's value is realized when the expensive O(n³) factorization is done once and the cheap O(n²) triangular solves handle many right-hand sides."

- question: "Why is LU decomposition more efficient than repeated Gaussian elimination when solving Ax = b for many different vectors b, and what is the role of each factor?"
  type: short-answer
  answer: "LU decomposition separates the expensive part (transforming A, which costs O(n³)) from the cheap part (using the factored form to solve for each b, which costs O(n²)). L records the elimination steps and U is the resulting echelon form. For each new b, forward substitution (Ly = b) reconstructs what b would look like after those same elimination steps, and back substitution (Ux = y) solves the resulting upper triangular system — both at O(n²)."
  explanation: "The key insight is that the structure of A doesn't change across systems with different b vectors. Gaussian elimination re-derives that structure every time. LU captures it once. The factorization is the work; subsequent solves are inexpensive lookups through the stored L and U. This is why numpy.linalg.solve and MATLAB's backslash operator use LU internally — the same factorization is reused even when you only see one call."
```

## Explainer

You already know Gaussian elimination: you apply a sequence of row operations to transform a matrix A into upper triangular form U. LU decomposition is the insight that this process doesn't just produce U — it also produces L automatically as a byproduct. Every time you perform an elimination step (subtract a multiple of one row from another), you are recording a **multiplier**. Collect those multipliers into a lower triangular matrix and you have L. The factorization A = LU is simply a way to package the entire elimination process into two matrices.

To see why L has the shape it does, think about what elimination does: to eliminate the entry in row i, column j, you subtract (a_ij / a_jj) times row j from row i. That ratio is the multiplier, and it fills position (i, j) of L — below the diagonal. The diagonal of L is all 1s because each row eliminates itself trivially. The result is that L is lower triangular with 1s on the diagonal, and U is the upper triangular echelon form of A.

The real payoff comes when you need to solve Ax = b for many different right-hand sides b. With Gaussian elimination alone, you must redo O(n³) work for each new b. With LU, you factor once and then solve two cheaper problems: **forward substitution** (Ly = b, solving for y row by row from top to bottom) and **back substitution** (Ux = y, solving for x row by row from bottom to top). Each of these triangular solves costs only O(n²), so once the factorization is in hand, each new right-hand side is solved in O(n²) time. This is why LU is the standard algorithm inside `numpy.linalg.solve`, MATLAB's `\` operator, and virtually every numerical solver.

One important caveat: LU decomposition as described requires that elimination proceeds without any zero pivots appearing. When a zero pivot would appear, you must swap rows before continuing — this introduces a **permutation matrix** P so that the factorization becomes PA = LU rather than A = LU. In practice, even non-zero pivots are swapped when they are very small relative to other entries (partial pivoting), which improves numerical stability. The L and U factors always exist for any invertible matrix after the appropriate row permutations.
