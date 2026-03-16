---
id: column-space
title: Column Space and Row Space
domain: mathematics
course: linear-algebra
prerequisites:
- id: subspaces
  type: hard
- id: span-of-vectors
  type: hard
builds-toward:
- least-squares-approximation
tags:
- column-space
- row-space
- image
stage: formal-systems
status: draft
---

# Column Space and Row Space

## Core Idea
The column space col(A) is the span of the columns of A; it equals the image of the linear transformation x ↦ Ax. The row space row(A) is the span of the rows of A, equal to col(Aᵀ). Both are fundamental subspaces determined by A; rank(A) is the dimension of each.

## Explainer

From your prerequisite on span of vectors, you know that the span of a set of vectors is all linear combinations of those vectors — it is the smallest subspace containing them all. The **column space** of a matrix A, written col(A), applies this idea directly: take the columns of A as your set of vectors and form their span. If A is m × n, its columns are vectors in ℝᵐ, so col(A) is a subspace of ℝᵐ. From your subspaces prerequisite, you know this span is guaranteed to be a subspace: it contains the zero vector and is closed under addition and scalar multiplication.

The geometric interpretation is the most important thing to understand. Multiplying A by a vector x computes a linear combination of the columns of A, where the entries of x are the coefficients. So the set of all vectors Ax, as x ranges over all of ℝⁿ, is exactly col(A). This means **col(A) is the image of the linear transformation** T(x) = Ax — the set of all outputs the transformation can possibly produce. The equation Ax = b has a solution if and only if b is in col(A). Geometrically: b must lie in the space that A's columns can reach.

The **row space** row(A) is the span of the rows of A, viewed as vectors in ℝⁿ. Equivalently, it is the column space of Aᵀ. A crucial fact: row reduction preserves the row space but can change the column space. When you row-reduce A to its echelon form, the nonzero rows of the echelon form span the same row space as the original rows of A. The pivot columns of A (not the echelon form) form a basis for the column space. This asymmetry is a source of many student errors — do not take the pivot columns from the reduced form and declare them a basis for col(A); go back to the original matrix.

The **rank** of A is defined as the dimension of the column space, and it equals the dimension of the row space — these two numbers always agree, a non-obvious theorem. The rank counts the number of pivot columns (or pivot rows) after row reduction. Together with the rank-nullity theorem, which you will use extensively in least-squares approximation, rank organizes all four fundamental subspaces of a matrix: the column space, the row space, the null space, and the left null space. Understanding which space a given vector belongs to — and why — is the unifying question of linear algebra.
