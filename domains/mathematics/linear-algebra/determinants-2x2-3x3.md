---
id: determinants-2x2-3x3
title: Determinants of 2×2 and 3×3 Matrices
domain: mathematics
course: linear-algebra
prerequisites:
- id: matrix-multiplication
  type: hard
builds-toward:
- determinant-properties
- matrix-inverses
- systems-of-linear-equations
- characteristic-polynomial
tags:
- determinant
- 2x2
- 3x3
- volume
stage: formal-systems
status: draft
---

# Determinants of 2×2 and 3×3 Matrices

## Core Idea
The determinant is a scalar assigned to a square matrix that measures how the matrix scales areas (2D) or volumes (3D). For 2×2: det(A) = ad − bc; for 3×3, it's computed via the rule of Sarrus or cofactor expansion. A nonzero determinant indicates the matrix is invertible.

## Explainer

From matrix multiplication, you know that a matrix transforms vectors — it stretches, rotates, reflects, or shears space. The **determinant** is a single number that captures one crucial aspect of that transformation: by what factor does the matrix scale areas (in 2D) or volumes (in 3D)? If you take a unit square and apply the matrix A, the resulting parallelogram has area equal to |det(A)|. The sign tells you whether the transformation preserved orientation (positive) or flipped it (negative, like a reflection).

For a 2×2 matrix A = [[a, b], [c, d]], the formula is det(A) = ad − bc. Geometrically, think of the two columns as vectors: [a, c] and [b, d]. The determinant is the signed area of the parallelogram they span. The product ad comes from the "main diagonal" contribution and bc from the "anti-diagonal" — you subtract the anti-diagonal because it represents the overlap. If the two column vectors are parallel (one is a multiple of the other), the parallelogram collapses to a line and det(A) = 0.

For a 3×3 matrix, the **cofactor expansion** (also called Laplace expansion) reduces the problem to three 2×2 determinants. Expanding along the first row: det(A) = a₁₁ · M₁₁ − a₁₂ · M₁₂ + a₁₃ · M₁₃, where each Mᵢⱼ is the determinant of the 2×2 matrix obtained by deleting row i and column j. The alternating signs (+ − +) follow the checkerboard pattern of cofactors. The **Rule of Sarrus** is a mnemonic shortcut specific to 3×3 matrices: write the matrix, repeat the first two columns alongside it, sum the three downward diagonals, subtract the three upward diagonals. It gives the same result as cofactor expansion and is faster by hand.

The determinant's most important application is the invertibility test: a square matrix is invertible if and only if its determinant is nonzero. When det(A) = 0, the transformation collapses space — it squashes some direction to zero, which means different inputs map to the same output, making the transformation non-reversible. This connects to everything downstream: Cramer's rule, eigenvalues (via the characteristic polynomial det(A − λI) = 0), and the theory of linear independence. The determinant is the gateway into all of these.
