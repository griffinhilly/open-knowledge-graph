---
id: row-space
title: The Row Space of a Matrix
domain: mathematics
course: linear-algebra
prerequisites:
- id: column-space
  type: hard
- id: matrix-transpose-properties
  type: soft
builds-toward:
- rank-and-nullity-theorem
tags:
- row space
- row operations
- RREF rows
- orthogonal complement
- rank
stage: formal-systems
status: draft
---

# The Row Space of a Matrix

## Core Idea
The row space of an m×n matrix A is the span of its row vectors, forming a subspace of Rⁿ. Unlike the column space, the row space IS preserved by elementary row operations, so a basis for the row space can be read directly as the nonzero rows of any row echelon form of A. The dimension of the row space equals the rank of A, confirming that row rank equals column rank — a foundational theorem. The row space and null space of A are orthogonal complements in Rⁿ: every vector in Rⁿ can be uniquely written as the sum of a row-space component and a null-space component.

## How It's Best Learned
Row-reduce A to REF and identify the nonzero rows as a row-space basis. Then verify the rank matches the column rank found from Col(A). Use the orthogonality relationship Nul(A) ⊥ Row(A) to geometrically motivate least squares.

## Common Misconceptions
- Row operations DO preserve the row space (unlike the column space, which row operations change).
- Students assume the row space of A equals the column space of A — they are subspaces of different spaces (Rⁿ vs Rᵐ) and equal only when m = n and A is symmetric.
- The row space basis comes from the RREF rows of A, while the column space basis comes from pivot columns of the ORIGINAL A.
