---
id: rank-and-nullity-theorem
title: Rank-Nullity Theorem
domain: mathematics
course: linear-algebra
prerequisites:
- id: basis-and-dimension
  type: hard
builds-toward:
  - column-space
tags:
- rank
- nullity
- rank-nullity
- dimension
stage: formal-systems
status: draft
---
# Rank-Nullity Theorem

## Core Idea
For an m × n matrix A: rank(A) + nullity(A) = n, where rank is the dimension of the column space and nullity is the dimension of the null space. Rank equals the number of pivot columns in RREF. This fundamental theorem connects dimension of the domain, kernel, and image of a linear transformation.

## Explainer

Every linear transformation T: ℝⁿ → ℝᵐ takes an n-dimensional space as input. The rank-nullity theorem says something elegant: that input space is divided, without overlap, between two parts — the part that collapses to zero (the null space, with dimension called **nullity**) and the part that survives and contributes to the output (the column space, with dimension called **rank**). These two dimensions must sum to exactly n, the number of columns.

Here's a concrete example. Suppose A is a 3 × 5 matrix. It maps ℝ⁵ to ℝ³. That 5-dimensional input space can't all "make it through" into a 3-dimensional output — some dimensions must collapse. If you row-reduce A and find 3 pivot columns, then rank = 3 and nullity = 2. This means the null space is 2-dimensional: there's a whole 2D plane of input vectors that A maps to zero. Conversely, if only 2 pivot columns appear, rank = 2 and nullity = 3, meaning a 3D subspace of inputs gets annihilated. You identified basis and dimension as prerequisites — rank-nullity is precisely the statement that the dimension of the domain splits between "what survives" and "what dies."

The theorem has immediate practical consequences. A square n × n matrix is invertible if and only if rank = n, which means nullity = 0: nothing maps to zero except zero itself. If rank < n for a square matrix, the null space is nontrivial and the system Ax = b has either no solutions or infinitely many. For a non-square system Ax = b with m equations and n unknowns, the theorem governs what's possible: if rank < n, solutions (if they exist) are not unique; if rank < m, some right-hand sides b cannot be achieved at all.

The pivot-counting interpretation ties everything together. Row reducing A to RREF reveals which columns are pivot columns and which are free columns. Pivot columns correspond to rank — they form a basis for the column space. Free columns, and their count equals nullity, correspond to free variables that parameterize the null space. The rank-nullity theorem is not something you verify after the fact; it's built into the structure of row reduction itself. Counting pivots and counting free variables always gives you two numbers that add up to n.
