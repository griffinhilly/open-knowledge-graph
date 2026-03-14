---
id: column-space
title: The Column Space of a Matrix
domain: mathematics
course: linear-algebra
prerequisites:
- id: subspaces
  type: hard
- id: span-of-vectors
  type: hard
- id: row-echelon-form
  type: soft
builds-toward:
- rank-and-nullity-theorem
- row-space
- least-squares-approximation
tags:
- column space
- image
- range
- pivot columns
- Ax=b consistency
stage: formal-systems
status: validated
---

# The Column Space of a Matrix

## Core Idea
The column space (image or range) of an m×n matrix A is the span of its column vectors, forming a subspace of Rᵐ. A vector b lies in the column space of A if and only if the system Ax = b is consistent — so the column space is precisely the set of all achievable outputs. A basis for the column space consists of the pivot columns of A (identified from the RREF but taken from the original A, not the RREF). The dimension of the column space is called the rank of A and equals the number of pivot columns.

## How It's Best Learned
Connect column space to system consistency: Ax = b has a solution iff b is in Col(A). Row-reduce the augmented matrix [A|b] and check for inconsistency. For the basis, identify pivot column positions from RREF, then use those columns from the original A.

## Common Misconceptions
- The basis for Col(A) uses pivot columns from the ORIGINAL matrix A, not from the RREF — the row operations change the column space of the resulting matrix.
- Col(A) is a subspace of Rᵐ (the codomain), while Nul(A) is a subspace of Rⁿ (the domain).
- Row operations change which columns are pivots but preserve which columns are in the column space — a subtle distinction students miss.
