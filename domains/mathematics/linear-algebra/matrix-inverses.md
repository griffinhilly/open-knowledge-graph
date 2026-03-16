---
id: matrix-inverses
title: Invertible Matrices and Matrix Inverses
domain: mathematics
course: linear-algebra
prerequisites:
- id: matrix-multiplication
  type: hard
builds-toward:
- systems-of-linear-equations
- rank-nullity-theorem
tags:
- matrices
- inverses
- invertibility
stage: formal-systems
status: draft
---

# Invertible Matrices and Matrix Inverses

## Core Idea
A square matrix A is invertible if there exists A^{-1} such that AA^{-1} = A^{-1}A = I. A matrix is invertible if and only if it has full rank and non-zero determinant. Invertibility is equivalent to being non-singular and having linearly independent rows and columns.

## Explainer

From your study of matrix multiplication, you know that multiplying by a matrix transforms vectors — it can rotate, scale, shear, or project them. The **matrix inverse** is the transformation that undoes this: if A sends vector x to Ax, then A⁻¹ brings it back. The defining condition AA⁻¹ = A⁻¹A = I captures exactly this idea, where the **identity matrix** I is the "do nothing" transformation. Just as the number 1 satisfies a·(1/a) = 1, the inverse matrix satisfies the matrix analog of this equation.

Why does invertibility require the matrix to be square? A non-square matrix maps between spaces of different dimensions — for example, a 2×3 matrix maps ℝ³ into ℝ². No matter how you try to undo it, you can't recover the original three-dimensional information from two-dimensional output. Squareness is necessary for even the possibility of a two-sided inverse. But squareness isn't sufficient: a square matrix that collapses multiple input vectors to the same output (like a projection matrix) cannot be inverted, because you can't tell which input produced which output.

The **determinant** gives a scalar test for this collapse: det(A) = 0 if and only if A fails to be invertible. Geometrically, the determinant measures the factor by which A scales area (in 2D) or volume (in 3D). A determinant of zero means the transformation squashes space down to a lower dimension — exactly the unrecoverable collapse. Full rank — meaning all rows and all columns are linearly independent — is the equivalent algebraic condition: each row and column contributes genuinely new information.

The inverse matters most for solving systems of equations. If Ax = b has a unique solution, it's x = A⁻¹b. In practice, computing A⁻¹ explicitly is expensive and numerically unstable, so algorithms like Gaussian elimination solve Ax = b directly. But the existence of A⁻¹ is what guarantees a unique solution exists in the first place — making invertibility one of the most important properties a matrix can have.
