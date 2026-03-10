---
id: cramers-rule
title: Cramer's Rule
domain: mathematics
course: linear-algebra
prerequisites:
- id: determinant-properties
  type: hard
- id: matrix-inverses
  type: soft
tags:
- Cramer's rule
- determinant solution
- systems of equations
- explicit formula
stage: formal-systems
status: draft
---

# Cramer's Rule

## Core Idea
Cramer's rule gives an explicit formula for the solution of a square linear system Ax = b when A is invertible: the j-th component of the solution is xⱼ = det(Aⱼ)/det(A), where Aⱼ is the matrix formed by replacing the j-th column of A with b. While theoretically elegant — it expresses each variable as a ratio of determinants — Cramer's rule is computationally inefficient for large systems compared to Gaussian elimination. Its main value is in proving theoretical results, deriving formulas for 2×2 and 3×3 systems, and deriving the inverse formula via cofactors.

## How It's Best Learned
Apply Cramer's rule to 2×2 systems and verify against substitution. For 3×3 systems, use it to appreciate why Gaussian elimination is preferred computationally. Observe that Cramer's rule fails (no formula applies) when det(A) = 0.

## Common Misconceptions
- Cramer's rule replaces the j-th COLUMN with b, not the j-th row.
- The rule only applies when det(A) ≠ 0 (unique solution exists); it does not apply to inconsistent or underdetermined systems.
- Students sometimes think Cramer's rule is the standard method for solving systems; in practice it is rarely used computationally beyond 3×3.
