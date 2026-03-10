---
id: rank-and-nullity-theorem
title: Rank, Nullity, and the Rank-Nullity Theorem
domain: mathematics
course: linear-algebra
prerequisites:
- id: basis-and-dimension
  type: hard
- id: null-space
  type: hard
- id: column-space
  type: hard
- id: row-space
  type: soft
builds-toward:
- least-squares-approximation
tags:
- rank
- nullity
- rank-nullity theorem
- fundamental theorem
- dimensions
stage: formal-systems
status: draft
---

# Rank, Nullity, and the Rank-Nullity Theorem

## Core Idea
The rank of a matrix A is the dimension of its column space (= dimension of its row space), and the nullity is the dimension of its null space. The Rank-Nullity Theorem states that for any m×n matrix A: rank(A) + nullity(A) = n, where n is the number of columns. This elegant result shows that the column count is partitioned between the 'productive' dimensions (rank, where inputs map to nonzero outputs) and the 'wasted' dimensions (nullity, where inputs map to zero). It immediately implies that for square n×n matrices, A is invertible if and only if rank(A) = n (nullity 0).

## How It's Best Learned
Verify the theorem numerically on several matrices of various ranks. Then use it diagnostically: if you know the rank from row reduction, you immediately know the nullity without separately computing the null space.

## Common Misconceptions
- Rank is the number of PIVOT rows (equivalently columns), not the total number of rows or columns.
- For a non-square m×n matrix, rank ≤ min(m, n); the theorem constrains nullity via n, not m.
- Row rank = column rank is a theorem requiring proof — it is not obvious that these two counts must agree.
