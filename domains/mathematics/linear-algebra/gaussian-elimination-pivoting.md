---
id: gaussian-elimination-pivoting
title: Gaussian Elimination with Partial Pivoting
domain: mathematics
course: linear-algebra
prerequisites:
- id: gaussian-elimination-method
  type: hard
builds-toward:
- lu-decomposition-numerical
- matrix-norms-conditioning
tags:
- numerical-stability
- pivoting
- gaussian-elimination
stage: formal-systems
status: draft
---

# Gaussian Elimination with Partial Pivoting

## Core Idea
Partial pivoting swaps rows to place the largest entry in the pivot position before elimination, reducing rounding errors in floating-point arithmetic. Without pivoting, small pivots can amplify errors in subsequent operations. Pivoting is essential for numerical stability and is standard in computational practice.

## Explainer

You know Gaussian elimination: systematically use row operations to reduce a matrix to upper triangular form, then back-substitute to find the solution. On paper with exact arithmetic, it works perfectly. But computers store numbers in **floating-point** format with finite precision — every number is rounded to about 15-16 significant digits. This rounding is usually harmless, but Gaussian elimination without care can turn tiny rounding errors into massive ones. The fix is **partial pivoting**.

Here's the problem. Suppose your current pivot — the leading entry you're eliminating with — is 0.0001, and another entry in the same column is 500. To eliminate the 500, you multiply the pivot row by 500/0.0001 = 5,000,000 and subtract. You've just amplified any rounding error in the pivot row by a factor of 5 million. The result can have errors so large that your "solution" is completely wrong. The size of this amplification is related to the **multiplier**: if the multiplier is large, errors grow; if it's small (≤ 1), errors stay controlled.

**Partial pivoting** prevents this by swapping rows before each elimination step. Before using entry (k, k) as the pivot, scan all the entries below it in column k and find the largest one in absolute value. Swap that row up to position k. Now the pivot is the largest available entry in its column, so every multiplier in this step has absolute value ≤ 1. Errors don't get amplified — they stay bounded. The only cost is bookkeeping: you record the row swaps in a permutation matrix P so you can reconstruct that you solved PA = LU rather than A = LU directly.

A small example shows the difference clearly. Solving the system [0.001, 1; 1, 1] × [x; y] = [1; 2] without pivoting: divide row 2 by 0.001 to eliminate, producing a multiplier of 1000 that amplifies floating-point noise. With pivoting: swap rows first so the pivot is 1 (the larger entry), multiplier becomes 0.001, and the elimination is numerically clean. The final answers match analytically but diverge significantly in floating-point.

Every serious numerical linear algebra library — LAPACK, NumPy, MATLAB — applies partial pivoting by default when solving Ax = b. It's not optional engineering caution; it's the reason direct solvers work reliably in practice. Understanding pivoting also prepares you for **LU decomposition with permutation matrices** (PA = LU), where the same row-swapping logic is formalized into a factorization that can be reused to solve systems with multiple right-hand sides efficiently.
