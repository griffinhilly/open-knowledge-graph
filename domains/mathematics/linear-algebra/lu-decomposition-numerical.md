---
id: lu-decomposition-numerical
title: LU Decomposition and Forward/Back Substitution
domain: mathematics
course: linear-algebra
prerequisites:
- id: gaussian-elimination-pivoting
  type: hard
- id: lu-decomposition
  type: soft
builds-toward:
- matrix-norms-conditioning
tags:
- lu-decomposition
- forward-substitution
- numerical-methods
stage: formal-systems
status: validated
---
# LU Decomposition and Forward/Back Substitution

## Core Idea
LU decomposition factors A = LU where L is lower triangular (result of Gaussian elimination) and U is upper triangular. To solve Ax = b: first solve Ly = b (forward substitution), then solve Ux = y (back substitution). LU is efficient for multiple right-hand sides and provides cost O(n²) when decomposed once. Pivoting is necessary for stability: PA = LU with permutation P.

## Questions

```yaml
- question: "A numerical library needs to solve Ax = b for the same matrix A but 1,000 different right-hand sides b. What is the computational advantage of LU decomposition over repeated Gaussian elimination?"
  type: multiple-choice
  options:
    - "LU decomposition eliminates the need for pivoting, making all 1,000 solves more accurate"
    - "LU decomposes A once at O(n³) cost, then each of the 1,000 systems requires only O(n²) work via forward/back substitution"
    - "LU reduces each of the 1,000 solves to O(n log n) using binary search on the triangular matrices"
    - "LU stores the solution x directly, so all 1,000 right-hand sides can be solved in O(1)"
  answer: 1
  explanation: "Gaussian elimination costs O(n³) each time you apply it to a new right-hand side. LU decomposition records the elimination work once: the factorization is computed at O(n³) cost, then each new b requires only forward substitution (Ly = Pb, O(n²)) and back substitution (Ux = y, O(n²)). For 1,000 right-hand sides, this saves enormous computation: 1×O(n³) + 1000×O(n²) instead of 1000×O(n³)."

- question: "In the factorization PA = LU, what does the permutation matrix P capture, and why is it needed?"
  type: multiple-choice
  options:
    - "P records the order in which variables were eliminated to make forward substitution more efficient"
    - "P reorders rows so the largest available entry serves as pivot, preventing catastrophic cancellation from near-zero pivots"
    - "P symmetrizes the matrix A so that L and U have equal dimensions"
    - "P is optional — it only improves performance on dense matrices but has no effect on accuracy"
  answer: 1
  explanation: "Partial pivoting reorders rows at each elimination step to place the largest available entry on the diagonal, ensuring pivots are never near zero. Near-zero pivots cause catastrophic cancellation — small numerical errors get amplified enormously when you divide by a tiny number. P records all row swaps. When solving, you apply the same permutation to b (forming Pb) before the triangular solves."

- question: "The lower triangular matrix L in LU decomposition records the multipliers used during Gaussian elimination, with 1s on the diagonal."
  type: true-false
  answer: true
  explanation: "This is exactly what L stores. When Gaussian elimination subtracts a multiple of one row from another to zero out a below-diagonal entry, that multiplier is stored in the corresponding position of L. The diagonal entries of L are 1 (unit lower triangular). The upper triangular matrix U is the final result of elimination — exactly the matrix you would back-substitute through after ordinary Gaussian elimination."

- question: "If LU decomposition of a matrix is computed without pivoting, it is always numerically safe to use those factors to solve any new right-hand side."
  type: true-false
  answer: false
  explanation: "Decomposition without pivoting is numerically unsafe whenever A has small or zero entries in pivot positions. Without pivoting, a near-zero pivot causes division by a very small number during elimination, amplifying floating-point errors catastrophically. The stored L and U factors from such a decomposition will contain large entries that make the triangular solves inaccurate. Partial pivoting (PA = LU) ensures pivots are as large as possible and makes the decomposition numerically stable."

- question: "Once you have the factorization PA = LU, describe in words the two-step process for solving Ax = b for a new right-hand side b."
  type: short-answer
  answer: "First apply the same permutation to b to get b' = Pb. Then solve Ly = b' using forward substitution (work top to bottom, each step using only already-computed values). Then solve Ux = y using back substitution (work bottom to top). The solution x satisfies the original Ax = b."
  explanation: "The key insight is that PAx = Pb is the same as LUx = Pb. Letting y = Ux, you first solve Ly = Pb (forward substitution, O(n²), since L is lower triangular with diagonal 1s), then solve Ux = y (back substitution, O(n²), since U is upper triangular). Both triangular solves go in one direction with no back-tracking — each step uses only values already computed."
```

## Explainer

You already know Gaussian elimination: you apply row operations to transform a matrix into upper triangular form, then back-substitute to find the solution. LU decomposition is nothing more than a systematic way of *recording* those row operations so you can reuse them. When you eliminate below a pivot, you divide one row by a multiplier and subtract. LU decomposition stores those multipliers as entries in a lower triangular matrix **L**. The upper triangular matrix **U** is just the final result of elimination — exactly what you already computed.

The payoff comes when you need to solve Ax = b for *many different right-hand sides* b. Without LU, you'd redo the entire elimination process each time — O(n³) work per system. With LU stored, each new b only requires two triangular solves: first **forward substitution** Ly = b (work left to right, top to bottom, since L is lower triangular), then **back substitution** Ux = y (work right to left, bottom to top, since U is upper triangular). Each triangular solve is O(n²), so you pay O(n³) once and O(n²) for every subsequent right-hand side. This is why LU is the workhorse of linear algebra software libraries.

**Pivoting** is what connects LU to the numerical stability lessons from Gaussian elimination. A zero or very small pivot can cause catastrophic cancellation. Partial pivoting reorders rows so the largest available entry serves as pivot at each step, and this reordering is captured by a **permutation matrix P**. The factorization becomes PA = LU: permute A first, *then* factor. When you solve PAx = Pb, you apply the same permutation to b before running the two triangular solves.

One concrete example clarifies the structure. For a 3×3 system, L looks like a unit lower triangle: 1s on the diagonal, multipliers below. U is whatever upper triangular matrix results. Solving Ly = b means: y₁ = b₁ (free), y₂ = b₂ − L₂₁y₁, y₃ = b₃ − L₃₁y₁ − L₃₂y₂. Each step uses only already-computed values — no back-tracking. Solving Ux = y runs in reverse: x₃ = y₃/U₃₃, x₂ = (y₂ − U₂₃x₃)/U₂₂, x₁ = (y₁ − U₁₂x₂ − U₁₃x₃)/U₁₁. The elegance is that each triangular system has exactly one solution when the diagonal entries are nonzero — and pivoting ensures they are.
