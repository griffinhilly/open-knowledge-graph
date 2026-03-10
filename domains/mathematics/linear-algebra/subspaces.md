---
id: subspaces
title: Subspaces
domain: mathematics
course: linear-algebra
prerequisites:
- id: vector-spaces
  type: hard
builds-toward:
- null-space
- column-space
- basis-and-dimension
- orthogonal-projections
- row-space
tags:
- subspace
- subspace test
- closure
- zero vector
- span
stage: formal-systems
status: draft
---

# Subspaces

## Core Idea
A subspace of a vector space V is a nonempty subset H that is itself a vector space under the same operations. Instead of checking all ten axioms, the subspace test condenses the verification to three conditions: H contains the zero vector, H is closed under addition, and H is closed under scalar multiplication. Equivalently, H is a subspace if and only if it is closed under all linear combinations. Major subspaces associated with a matrix include the null space, column space, and row space, each of which plays a distinct role in understanding the matrix.

## How It's Best Learned
Practice the three-part subspace test on diverse candidates: lines and planes through the origin in R³ are subspaces; lines not through the origin are not. Confirm that a single vector's span always forms a subspace.

## Common Misconceptions
- A subset containing the zero vector is NOT automatically a subspace; it must also be closed under addition and scalar multiplication.
- Lines and planes through the origin in R³ are subspaces; those not through the origin are not (they lack the zero vector).
- The empty set cannot be a subspace because subspaces must contain the zero vector.
