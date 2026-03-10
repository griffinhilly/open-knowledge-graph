---
id: null-space
title: The Null Space of a Matrix
domain: mathematics
course: linear-algebra
prerequisites:
- id: subspaces
  type: hard
- id: row-echelon-form
  type: hard
builds-toward:
- rank-and-nullity-theorem
tags:
- null space
- kernel
- homogeneous solution
- Ax=0
- free variables
stage: formal-systems
status: draft
---

# The Null Space of a Matrix

## Core Idea
The null space (kernel) of an m×n matrix A is the set of all vectors x in Rⁿ such that Ax = 0. It is always a subspace of Rⁿ. To find a basis for the null space, row-reduce A to RREF, identify the free variables, and express each basic variable in terms of the free variables; each free variable then generates one basis vector. The dimension of the null space is called the nullity of A and counts the number of free variables in the RREF. The null space measures the 'failure of injectivity' of the linear transformation T(x) = Ax.

## How It's Best Learned
Practice extracting null space basis vectors from RREF by assigning one free variable to 1 and the rest to 0, then reading off the basic variables. Write the general solution as a linear combination of these basis vectors.

## Common Misconceptions
- The null space of A is a subspace of Rⁿ (the domain), not Rᵐ (the codomain).
- A nontrivial null space means the system Ax = b may have infinitely many solutions or no solution — not necessarily one of each.
- Students sometimes confuse the null space with the solution to a specific non-homogeneous system Ax = b; the null space corresponds specifically to b = 0.
