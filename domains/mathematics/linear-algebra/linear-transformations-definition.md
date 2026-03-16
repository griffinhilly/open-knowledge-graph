---
id: linear-transformations-definition
title: Linear Transformations and Their Properties
domain: mathematics
course: linear-algebra
prerequisites:
- id: function-notation-review
  type: soft
- id: basis-and-dimension
  type: hard
builds-toward:
- linear-transformation-matrix-representation
- kernel-and-image
tags:
- linear-transformations
- mappings
- functions
stage: formal-systems
status: draft
---

# Linear Transformations and Their Properties

## Core Idea
A linear transformation T: V → W is a function satisfying T(u + v) = T(u) + T(v) and T(cu) = cT(u). Examples: rotation, projection, differentiation, matrix multiplication. Linear transformations preserve vector space structure, making them natural maps between vector spaces. The kernel and image determine injectivity and surjectivity.

## How It's Best Learned
Check linearity carefully: verify both additivity and homogeneity. Explore examples: derivatives T(p) = p', rotations, projections onto a line. Visualize in R² and R³.

## Explainer

A linear transformation is a function with special structure — it respects the two core operations of a vector space: addition and scalar multiplication. From your work with bases and dimensions, you know that a vector space is characterized by these operations. A linear transformation T: V → W preserves them, meaning T(u + v) = T(u) + T(v) and T(cu) = cT(u). This is called **linearity** — two conditions that together say "T doesn't disturb the algebraic structure of V." Together, the two conditions imply T(c₁u + c₂v) = c₁T(u) + c₂T(v), meaning T preserves any linear combination.

Consider rotation in R² by angle θ. If you rotate two vectors and add, or add first and then rotate, you get the same result — rotation is linear. Now consider the function T(v) = v + c for some fixed nonzero c (a **translation**). T(u + v) = u + v + c, but T(u) + T(v) = (u + c) + (v + c) = u + v + 2c. These differ, so translations are not linear. A quick check: linear transformations must always map 0 to 0. Setting u = v = 0 in the additivity condition gives T(0) = T(0 + 0) = T(0) + T(0), so T(0) = 0. If a function doesn't map 0 to 0, it's immediately disqualified.

Here is the most powerful consequence of linearity, connecting directly back to your prerequisite on basis and dimension. Once you know where T sends every basis vector, you know T completely. If {v₁, v₂, ..., vₙ} is a basis for V, then any vector v = c₁v₁ + ... + cₙvₙ, and linearity forces T(v) = c₁T(v₁) + ... + cₙT(vₙ). Specifying T on a finite set — the basis — determines T on all of V. This is why, in the next topic, you will represent T by a matrix: the columns of that matrix are exactly the images of the basis vectors.

Two subspaces characterize every linear transformation. The **kernel** of T is ker(T) = {v ∈ V : T(v) = 0} — the set of all inputs that collapse to zero. The **image** of T is im(T) = {T(v) : v ∈ V} — the set of all outputs. The kernel measures how much T "collapses": if ker(T) = {0}, then T is injective (no two inputs produce the same output). The image measures how much of W T reaches: if im(T) = W, then T is surjective. Both are subspaces, and their dimensions are linked by the rank-nullity theorem — a direct generalization of ideas you already know from column space and null space in matrix algebra.
