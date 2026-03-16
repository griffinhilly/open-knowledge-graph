---
id: lu-decomposition-numerical
title: LU Decomposition and Forward/Back Substitution
domain: mathematics
course: linear-algebra
prerequisites:
- id: gaussian-elimination-pivoting
  type: hard
builds-toward:
- matrix-norms-conditioning
tags:
- lu-decomposition
- forward-substitution
- numerical-methods
stage: formal-systems
status: draft
---

# LU Decomposition and Forward/Back Substitution

## Core Idea
LU decomposition factors A = LU where L is lower triangular (result of Gaussian elimination) and U is upper triangular. To solve Ax = b: first solve Ly = b (forward substitution), then solve Ux = y (back substitution). LU is efficient for multiple right-hand sides and provides cost O(n²) when decomposed once. Pivoting is necessary for stability: PA = LU with permutation P.

## Explainer

You already know Gaussian elimination: you apply row operations to transform a matrix into upper triangular form, then back-substitute to find the solution. LU decomposition is nothing more than a systematic way of *recording* those row operations so you can reuse them. When you eliminate below a pivot, you divide one row by a multiplier and subtract. LU decomposition stores those multipliers as entries in a lower triangular matrix **L**. The upper triangular matrix **U** is just the final result of elimination — exactly what you already computed.

The payoff comes when you need to solve Ax = b for *many different right-hand sides* b. Without LU, you'd redo the entire elimination process each time — O(n³) work per system. With LU stored, each new b only requires two triangular solves: first **forward substitution** Ly = b (work left to right, top to bottom, since L is lower triangular), then **back substitution** Ux = y (work right to left, bottom to top, since U is upper triangular). Each triangular solve is O(n²), so you pay O(n³) once and O(n²) for every subsequent right-hand side. This is why LU is the workhorse of linear algebra software libraries.

**Pivoting** is what connects LU to the numerical stability lessons from Gaussian elimination. A zero or very small pivot can cause catastrophic cancellation. Partial pivoting reorders rows so the largest available entry serves as pivot at each step, and this reordering is captured by a **permutation matrix P**. The factorization becomes PA = LU: permute A first, *then* factor. When you solve PAx = Pb, you apply the same permutation to b before running the two triangular solves.

One concrete example clarifies the structure. For a 3×3 system, L looks like a unit lower triangle: 1s on the diagonal, multipliers below. U is whatever upper triangular matrix results. Solving Ly = b means: y₁ = b₁ (free), y₂ = b₂ − L₂₁y₁, y₃ = b₃ − L₃₁y₁ − L₃₂y₂. Each step uses only already-computed values — no back-tracking. Solving Ux = y runs in reverse: x₃ = y₃/U₃₃, x₂ = (y₂ − U₂₃x₃)/U₂₂, x₁ = (y₁ − U₁₂x₂ − U₁₃x₃)/U₁₁. The elegance is that each triangular system has exactly one solution when the diagonal entries are nonzero — and pivoting ensures they are.
