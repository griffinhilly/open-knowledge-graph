---
id: dimension-vector-space
title: Dimension of Vector Spaces
domain: mathematics
course: linear-algebra
prerequisites:
- id: basis-definition
  type: hard
builds-toward:
- rank-nullity-theorem
tags:
- dimension
- vector spaces
- basis
stage: formal-systems
status: draft
---

# Dimension of Vector Spaces

## Core Idea
The dimension of a vector space V, denoted dim(V), is the size of any basis. All bases have equal cardinality. Dimension measures the number of independent coordinates needed. For R^n, dimension is n. Subspaces have dimension ≤ the parent space's dimension.

## Explainer

You learned from the definition of a basis that a basis is a set of vectors that is both linearly independent and spans the space — it is exactly enough to describe every vector in the space without redundancy. **Dimension** is what you get when you count the vectors in a basis. It measures how many truly independent directions exist in the space.

The foundational theorem behind dimension is that all bases of a vector space have the same number of vectors. This is not obvious — a space might seem to admit different bases of different sizes — but the exchange lemma guarantees it can't happen. If B₁ and B₂ are both bases of V, then |B₁| = |B₂|. Because of this, dim(V) is well-defined: you can compute it from any basis and get the same answer. For **ℝⁿ**, the standard basis {e₁, e₂, ..., eₙ} has n vectors, so dim(ℝⁿ) = n. For the space of 2×2 matrices, the standard basis has 4 matrices, so the dimension is 4, even though the space looks different from ℝ⁴.

Think of dimension as the minimum number of numbers needed to uniquely specify any element of the space. In ℝ³, you need exactly 3 coordinates — no more, no less — to pin down a point. A plane through the origin in ℝ³ is a 2-dimensional subspace: you need only 2 coordinates relative to a basis for the plane. A line through the origin is 1-dimensional. The zero vector alone forms the zero subspace, which has no basis and dimension 0. Each of these subspaces requires fewer independent coordinates than the parent space — which is why dimension of a subspace is always ≤ dimension of the full space.

Dimension interacts with the four fundamental subspaces of a matrix in a precise way. The **rank** of a matrix A is the dimension of its column space (equivalently, its row space). The **nullity** is the dimension of the null space. The **rank-nullity theorem** — which you'll prove next — states that rank + nullity = n, where n is the number of columns of A. This is a conservation law for dimensions: the dimensions of the column space and null space always partition the n input dimensions. Understanding dimension as a count of independent directions makes this theorem intuitive rather than mysterious.

The concept scales far beyond ℝⁿ. The space of polynomials of degree ≤ 3 is 4-dimensional (basis: {1, x, x², x³}). The space of continuous functions on [0, 1] is infinite-dimensional — no finite set of functions spans it. Dimension is the single number that classifies a finite-dimensional vector space up to isomorphism: any two vector spaces over the same field with the same dimension are structurally identical. This makes dimension one of the most powerful invariants in all of linear algebra.
