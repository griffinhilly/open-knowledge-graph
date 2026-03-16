---
id: rank-nullity-theorem
title: Rank-Nullity Theorem
domain: mathematics
course: linear-algebra
prerequisites:
- id: kernel-image-rank
  type: hard
- id: dimension-vector-space
  type: hard
tags:
- rank-nullity
- dimensions
- linear transformations
stage: formal-systems
status: draft
---

# Rank-Nullity Theorem

## Core Idea
For a linear transformation T: V → W with V finite-dimensional: dim(V) = rank(T) + nullity(T), where rank(T) = dim(im(T)) and nullity(T) = dim(ker(T)). For an m × n matrix A: rank(A) + nullity(A) = n. This fundamental relation connects the sizes of key subspaces.

## Explainer

From your prerequisites, you know that a linear transformation T: V → W has two fundamental subspaces: the **kernel** (or null space) ker(T), which consists of all vectors that T sends to zero, and the **image** im(T), which consists of all outputs T can produce. The rank-nullity theorem says these two subspaces account for all of V together: their dimensions sum exactly to dim(V).

Think of T as sorting the input space V into two populations. One population — the kernel — gets "erased" by T, collapsing to the zero vector. The other population carries information forward into the image. The theorem says the total dimension of V is just the size of what gets erased (nullity) plus the size of what survives (rank). Nothing is counted twice, and nothing is missed. This is a conservation law for dimension.

For a concrete example, take a linear map T: ℝ⁵ → ℝ³ represented by a 3 × 5 matrix. The input space has dimension 5. Suppose T has rank 3 — its image fills all of ℝ³. Then the rank-nullity theorem tells you immediately that nullity = 5 − 3 = 2: there is a 2-dimensional subspace of ℝ⁵ that T crushes to zero. You can verify this by row-reducing the matrix and finding the free variables. Each free variable corresponds to a dimension in the kernel. The count always works out.

A useful consequence is that T can never be injective (one-to-one) if the domain has higher dimension than the codomain — the kernel must be nontrivial, so distinct inputs must collide. Conversely, T can never be surjective (onto) if the codomain has higher dimension than the domain — the image can't have dimension exceeding dim(V). The rank-nullity theorem thus immediately constrains which linear maps can be injective, surjective, or bijective, making it one of the most used tools in linear algebra for reasoning about solvability of linear systems.
