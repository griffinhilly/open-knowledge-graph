---
id: gaussian-elimination-method
title: Gaussian Elimination and Row Reduction
domain: mathematics
course: linear-algebra
prerequisites:
- id: linear-systems-notation
  type: hard
builds-toward:
- row-echelon-form-rref
- gaussian-elimination-pivoting
- rank-nullity-theorem
tags:
- gaussian-elimination
- row-operations
- solving-systems
stage: formal-systems
status: draft
---

# Gaussian Elimination and Row Reduction

## Core Idea
Gaussian elimination transforms an augmented matrix [A | b] via row operations (row swap, row scaling, row addition) into row echelon form, then back-substitution solves the system. Row operations preserve the solution set, making the system equivalent but simpler to solve. Computational cost is O(n³) for an n×n system.
