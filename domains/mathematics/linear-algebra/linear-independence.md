---
id: linear-independence
title: Linear Independence
domain: mathematics
course: linear-algebra
prerequisites:
- id: span-of-vectors
  type: hard
- id: row-echelon-form
  type: soft
builds-toward:
- basis-and-dimension
- gram-schmidt-process
- rank-and-nullity-theorem
tags:
- linear independence
- linear dependence
- trivial solution
- redundancy
stage: formal-systems
status: draft
---

# Linear Independence

## Core Idea
A set of vectors {v₁, v₂, …, vₖ} is linearly independent if the only solution to c₁v₁ + c₂v₂ + … + cₖvₖ = 0 is the trivial solution c₁ = c₂ = … = cₖ = 0. A set is linearly dependent if some nontrivial combination equals zero, meaning at least one vector is expressible as a combination of the others (it is 'redundant'). To test independence, form the matrix with the vectors as columns and row-reduce: independence holds if and only if every column is a pivot column (no free variables). More vectors than dimensions guarantees dependence.

## How It's Best Learned
Visualize linear dependence in R² and R³: two vectors are dependent when they're parallel; three vectors in R² are always dependent. Confirm algebraically by setting up the homogeneous system and row-reducing.

## Common Misconceptions
- Linear independence is about the homogeneous equation Ac = 0 having only the trivial solution, not about whether Ax = b has a solution.
- Two nonzero vectors are linearly dependent if and only if one is a scalar multiple of the other — this does not generalize cleanly to three or more vectors.
- Any set containing the zero vector is automatically linearly dependent (the zero vector can be 'removed' as redundant).
