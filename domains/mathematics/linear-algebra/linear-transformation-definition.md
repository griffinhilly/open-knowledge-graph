---
id: linear-transformation-definition
title: Linear Transformations and Properties
domain: mathematics
course: linear-algebra
prerequisites:
- id: vector-spaces-definition
  type: hard
builds-toward:
- matrix-representation-linear-map
- kernel-image-rank
tags:
- transformations
- linear maps
- properties
stage: formal-systems
status: draft
---

# Linear Transformations and Properties

## Core Idea
A function T: V → W between vector spaces is linear if T(u + v) = T(u) + T(v) and T(cu) = cT(u) for all vectors u, v and scalar c. Linear transformations preserve vector space structure and can be represented by matrices once bases are chosen. Kernel and image are fundamental subspaces of any linear map.

## Explainer

From your study of vector spaces, you know that a vector space is defined by two operations — addition and scalar multiplication — together with a list of axioms that make them behave predictably. A **linear transformation** is a function between two vector spaces that respects exactly those two operations. When you apply T to a sum, you get the same result as summing the outputs: T(u + v) = T(u) + T(v). When you scale an input first, the output scales by the same factor: T(cu) = cT(u). These two conditions together mean T doesn't distort the underlying algebraic structure — it carries vectors over to the new space in a way that honors how those spaces work.

A useful way to build intuition is through geometry. Consider the transformation T: ℝ² → ℝ² that rotates every vector by 45 degrees. If you rotate u + v, you get the same result as rotating u and v separately and adding them. Scaling a vector then rotating gives the same result as rotating then scaling. Rotation is linear. Now consider a translation — shifting every vector by adding a fixed constant vector b: T(v) = v + b. This fails linearity because T(0) = b ≠ 0; a linear map must always send the zero vector to the zero vector. That's a useful first check: if T doesn't map 0 to 0, it cannot be linear.

The power of linearity is that knowing what T does to a **basis** is enough to determine T completely. If {e₁, e₂, …, eₙ} is a basis for V, then any vector v in V can be written as a linear combination of basis vectors, and linearity forces T(v) to be the corresponding linear combination of T(e₁), T(e₂), …, T(eₙ). This is why linear transformations can be encoded as **matrices**: each column of the matrix is the image of the corresponding basis vector. The matrix is the lookup table for the transformation in those coordinates.

Two subspaces tell you the most important structural facts about T. The **kernel** (or null space) is the set of all inputs that T sends to zero — it measures how "far from injective" T is. If the kernel is just {0}, then T is one-to-one; every input maps to a distinct output. The **image** (or range) is the set of all possible outputs — it measures how much of W the transformation actually covers. The Rank-Nullity theorem, which you'll prove soon, gives the precise relationship between the sizes of these two subspaces: dim(kernel) + dim(image) = dim(V). Understanding a linear transformation means understanding its kernel and image.
