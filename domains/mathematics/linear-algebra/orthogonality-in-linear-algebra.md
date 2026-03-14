---
id: orthogonality-in-linear-algebra
title: Orthogonality
domain: mathematics
course: linear-algebra
prerequisites:
- id: inner-product-spaces
  type: hard
builds-toward:
- orthonormal-bases
- orthogonal-projections
tags:
- orthogonal
- perpendicular
- orthogonal complement
- orthogonal set
stage: formal-systems
status: validated
---

# Orthogonality

## Core Idea
Two vectors u and v in an inner product space are orthogonal if ⟨u,v⟩ = 0. A set of vectors is orthogonal if every pair of distinct vectors in the set is orthogonal, and orthonormal if additionally each vector has unit norm. Orthogonal sets are automatically linearly independent (assuming no zero vectors). The orthogonal complement of a subspace W is the set of all vectors orthogonal to every vector in W; this complement is itself a subspace, and V = W ⊕ W⊥ (direct sum decomposition). Orthogonality is the key geometric tool behind projections and the Gram-Schmidt process.

## How It's Best Learned
Verify orthogonality using dot products in R² and R³ before generalizing. Compute orthogonal complements of lines and planes in R³ by setting up dot product equations. Note that W⊥⊥ = W (taking the complement twice returns the original subspace).

## Common Misconceptions
- Orthogonal does not mean 'in the direction of the axes'; it means perpendicular in the inner product sense.
- Orthogonal sets are linearly independent, but independent sets are NOT necessarily orthogonal.
- In R³, the orthogonal complement of a plane is a line and vice versa — dimension always satisfies dim(W) + dim(W⊥) = n.
