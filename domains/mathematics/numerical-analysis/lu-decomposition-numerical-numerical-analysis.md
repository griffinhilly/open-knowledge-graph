---
id: lu-decomposition-numerical-numerical-analysis
title: LU Decomposition
domain: mathematics
course: numerical-analysis
prerequisites:
- id: gaussian-elimination-with-pivoting
  type: hard
builds-toward:
- condition-number-of-a-matrix
tags:
- lu-decomposition
- matrix-factorization
- linear-solver
stage: advanced
status: draft
---

# LU Decomposition

## Core Idea
LU decomposition factors a matrix as A = LU where L is lower triangular and U is upper triangular. This factorization is obtained via Gaussian elimination and allows efficient solution of multiple systems with the same coefficient matrix A. With partial pivoting, the factorization A = PLU provides numerical stability and is the basis for efficient linear system solvers.

## Explainer

You know Gaussian elimination: apply row operations to reduce an augmented matrix [A|b] to upper triangular form, then back-substitute to solve for x. **LU decomposition** asks: can we record those row operations in a reusable matrix? The answer is yes. Each elimination step — "subtract c times row i from row j" — corresponds to multiplying A on the left by an elementary lower-triangular matrix. If we compose all those operations, the product inverts to give L, a lower-triangular matrix with 1's on the diagonal, such that A = LU where U is the upper-triangular result of elimination.

The practical payoff is immediate. If you need to solve Ax = b for many different right-hand sides b but the same coefficient matrix A — common in simulations, iterative algorithms, and sensitivity analyses — LU decomposition lets you factor A once (an O(n³) operation) and then solve each new system in O(n²) via two triangular solves: forward substitution Ly = b followed by back substitution Ux = y. Triangular systems are solved by sweeping row by row, making each solve trivial after the one-time factorization cost.

**Partial pivoting** is essential for numerical stability. Without it, the algorithm may divide by a very small diagonal entry, amplifying floating-point rounding errors catastrophically. With partial pivoting, before each elimination step we swap the current row with the row below it having the largest absolute value in the current column. This produces the decomposition PA = LU, where P is a **permutation matrix** recording the row swaps. In practice P is stored as a permutation vector, and L and U overwrite A's memory in-place.

LU decomposition underlies most dense linear algebra in practice. Computing the determinant reduces to det(A) = (sign of P) × product of diagonal entries of U. Inverting A is rarely done explicitly; instead, each column of A⁻¹ is found by solving a separate triangular system. The condition number of A — which you'll encounter next — quantifies how sensitive Ax = b is to perturbations in b, and its computation also uses the LU factorization.
