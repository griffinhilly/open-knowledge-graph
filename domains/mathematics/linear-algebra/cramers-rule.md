---
id: cramers-rule
title: Cramer's Rule for Solving Systems
domain: mathematics
course: linear-algebra
prerequisites:
- id: determinant-properties
  type: hard
- id: systems-of-linear-equations
  type: hard
tags:
- systems
- cramers rule
- determinants
stage: formal-systems
status: draft
---

# Cramer's Rule for Solving Systems

## Core Idea
For a square system Ax = b with det(A) ≠ 0, Cramer's rule gives x_i = det(A_i) / det(A), where A_i is A with column i replaced by b. This provides an explicit formula for solutions but is computationally inefficient compared to Gaussian elimination.

## Explainer

You already know two things that Cramer's rule combines: how to solve a system of linear equations Ax = b, and how to compute the determinant of a matrix. From systems of equations, you know that a square system has a unique solution exactly when det(A) ≠ 0. From determinant properties, you know that the determinant measures how a linear transformation scales volume. Cramer's rule connects these ideas by expressing each solution variable as a ratio of determinants — giving you an explicit formula without any elimination steps.

Here is the rule: to solve Ax = b for x₁, x₂, ..., xₙ, compute x_i = det(A_i) / det(A), where **A_i** is the matrix formed by taking A and replacing column i with the vector b. For a 2×2 system, this is easy to verify by hand. Take the system 2x + y = 5, x + 3y = 7. The coefficient matrix A has det(A) = 2·3 − 1·1 = 5. To find x₁, replace the first column with [5, 7] to get A₁; det(A₁) = 5·3 − 1·7 = 8, so x₁ = 8/5. To find x₂, replace the second column with [5, 7] to get A₂; det(A₂) = 2·7 − 5·1 = 9, so x₂ = 9/5. You can verify these values satisfy both equations.

Why does this work? Here is the geometric intuition. The vector b is a linear combination of the columns of A: b = x₁a₁ + x₂a₂ + ... + xₙaₙ, where aᵢ is column i of A. The matrix A_i replaces column i with b, which can be written as the original matrix A but with column i "contaminated" by the weighted sum. When you take the determinant of A_i, the multilinearity of the determinant isolates the xᵢ coefficient (all other terms vanish because they introduce repeated columns), leaving det(A_i) = xᵢ · det(A). Dividing by det(A) recovers xᵢ.

Cramer's rule is theoretically elegant but **computationally expensive**. Computing a single n×n determinant takes O(n³) work (or O(n!) via cofactor expansion). Cramer's rule requires n+1 determinants, so solving a full n-variable system costs O(n⁴) — far worse than Gaussian elimination's O(n³). For n = 100, that's 100 times more work. In practice, nobody uses Cramer's rule to actually solve large systems. Its value is theoretical: it gives explicit, closed-form expressions for solutions, which are useful when deriving formulas in proofs, studying how solutions depend on parameters, or computing the inverse of a matrix symbolically. You will encounter Cramer's rule again whenever exact symbolic solutions matter more than computational speed.
