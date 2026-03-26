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
stage: formal-systems
status: validated
---

# LU Decomposition

## Core Idea
LU decomposition factors a matrix as A = LU where L is lower triangular and U is upper triangular. This factorization is obtained via Gaussian elimination and allows efficient solution of multiple systems with the same coefficient matrix A. With partial pivoting, the factorization A = PLU provides numerical stability and is the basis for efficient linear system solvers.

## Questions

```yaml
- question: "You need to solve Ax = b for 1,000 different right-hand side vectors b, using the same coefficient matrix A. Which approach is most computationally efficient?"
  type: multiple-choice
  options:
    - "Run Gaussian elimination 1,000 times, once per right-hand side"
    - "Compute A⁻¹ explicitly, then multiply each b by A⁻¹"
    - "Factor A = LU once, then solve Ly = b and Ux = y for each new b"
    - "Use iterative methods like conjugate gradient for each right-hand side"
  answer: 2
  explanation: "LU decomposition's key advantage is amortizing the expensive O(n³) factorization over many cheap O(n²) triangular solves. Each new right-hand side requires only a forward substitution (Ly = b) and a back substitution (Ux = y), both O(n²). Option A repeats the full O(n³) work 1,000 times. Option B explicitly inverting A is rarely done in practice — it also costs O(n³) and introduces additional numerical error."

- question: "Why is partial pivoting essential for numerical stability in LU decomposition?"
  type: multiple-choice
  options:
    - "It reduces the number of arithmetic operations from O(n³) to O(n² log n)"
    - "It prevents small diagonal entries from acting as divisors, which would amplify floating-point rounding errors"
    - "It ensures L and U are both orthogonal matrices, improving conditioning"
    - "It allows the factorization to be computed without storing L separately from U"
  answer: 1
  explanation: "At each step of Gaussian elimination, we divide by the diagonal entry (the pivot). If that pivot is very small due to the ordering of rows, we divide by nearly zero, catastrophically amplifying any rounding error. Partial pivoting swaps the current row with the row having the largest absolute value in that column, ensuring the divisor is as large as possible and bounding the amplification of errors. The result is the factorization PA = LU where P records the swaps."

- question: "LU decomposition should be recomputed from scratch whenever the right-hand side vector b changes."
  type: true-false
  answer: false
  explanation: "This is the central practical advantage of LU decomposition: the factorization depends only on A, not on b. Once A = LU (or PA = LU) is computed, any number of right-hand sides can be solved using only O(n²) triangular solves. The factorization is reused; only the forward and back substitution steps (Ly = b, then Ux = y) change when b changes."

- question: "In PA = LU decomposition, the permutation matrix P records the row swaps performed during partial pivoting."
  type: true-false
  answer: true
  explanation: "Partial pivoting reorders the rows of A to place the largest-magnitude entry in the pivot position before each elimination step. These reorderings are captured by the permutation matrix P (stored in practice as a permutation vector). The factored form is PA = LU: if you first permute A's rows according to P, the result factors cleanly into lower and upper triangular matrices L and U."

- question: "Why are triangular systems (lower- or upper-triangular) particularly easy to solve, and how does this relate to why LU decomposition is useful?"
  type: short-answer
  answer: "A triangular system can be solved by sweeping row by row: in a lower-triangular system, each equation has one new unknown and all others already known (forward substitution); in an upper-triangular system, the same logic applies in reverse (back substitution). Each row requires O(n) arithmetic, giving O(n²) total. LU decomposition converts any square system into two triangular systems (Ly = b and Ux = y). Since the expensive part — the O(n³) factorization — is done once and reused, solving new right-hand sides costs only O(n²) each time."
  explanation: "The practical power of LU decomposition rests entirely on this O(n²) solve cost. Dense linear systems arise constantly in simulations, sensitivity analysis, and optimization, often requiring many solves with the same matrix. The LU factorization is the standard approach in production linear algebra libraries (LAPACK's dgesv) precisely because it separates the expensive, reusable work (factoring A) from the cheap, repeated work (solving for each b)."
```

## Explainer

You know Gaussian elimination: apply row operations to reduce an augmented matrix [A|b] to upper triangular form, then back-substitute to solve for x. **LU decomposition** asks: can we record those row operations in a reusable matrix? The answer is yes. Each elimination step — "subtract c times row i from row j" — corresponds to multiplying A on the left by an elementary lower-triangular matrix. If we compose all those operations, the product inverts to give L, a lower-triangular matrix with 1's on the diagonal, such that A = LU where U is the upper-triangular result of elimination.

The practical payoff is immediate. If you need to solve Ax = b for many different right-hand sides b but the same coefficient matrix A — common in simulations, iterative algorithms, and sensitivity analyses — LU decomposition lets you factor A once (an O(n³) operation) and then solve each new system in O(n²) via two triangular solves: forward substitution Ly = b followed by back substitution Ux = y. Triangular systems are solved by sweeping row by row, making each solve trivial after the one-time factorization cost.

**Partial pivoting** is essential for numerical stability. Without it, the algorithm may divide by a very small diagonal entry, amplifying floating-point rounding errors catastrophically. With partial pivoting, before each elimination step we swap the current row with the row below it having the largest absolute value in the current column. This produces the decomposition PA = LU, where P is a **permutation matrix** recording the row swaps. In practice P is stored as a permutation vector, and L and U overwrite A's memory in-place.

LU decomposition underlies most dense linear algebra in practice. Computing the determinant reduces to det(A) = (sign of P) × product of diagonal entries of U. Inverting A is rarely done explicitly; instead, each column of A⁻¹ is found by solving a separate triangular system. The condition number of A — which you'll encounter next — quantifies how sensitive Ax = b is to perturbations in b, and its computation also uses the LU factorization.
