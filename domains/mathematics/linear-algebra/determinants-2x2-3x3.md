---
id: determinants-2x2-3x3
title: Computing Determinants (2×2 and 3×3)
domain: mathematics
course: linear-algebra
prerequisites:
- id: matrix-operations
  type: hard
builds-toward:
- cofactor-expansion
- determinant-properties
- eigenvalues-and-eigenvectors
tags:
- determinant
- 2x2
- 3x3
- Sarrus rule
- area
- volume
stage: formal-systems
status: draft
---

# Computing Determinants (2×2 and 3×3)

## Core Idea
The determinant of a square matrix is a scalar that encodes key geometric and algebraic information about the matrix. For a 2×2 matrix [[a,b],[c,d]], det(A) = ad − bc, which equals the signed area of the parallelogram spanned by the row vectors. For 3×3 matrices, the determinant can be computed via the Rule of Sarrus or by expansion along any row or column. A nonzero determinant signals that the matrix is invertible; a zero determinant signals that the rows (or columns) are linearly dependent. The absolute value of the determinant measures the volume scaling factor of the associated linear transformation.

## How It's Best Learned
Memorize the 2×2 formula and derive it geometrically as signed area. For 3×3, master cofactor expansion along the first row, then use the Rule of Sarrus as a checking heuristic. Always verify that a matrix with two identical rows has determinant zero.

## Common Misconceptions
- Students often forget the negative sign in front of the (1,2) cofactor in 3×3 expansion.
- det(A + B) ≠ det(A) + det(B) — the determinant is not linear in the whole matrix, only in each row or column separately.
- A determinant of zero does not mean the matrix is zero; it means the matrix is singular (non-invertible).
