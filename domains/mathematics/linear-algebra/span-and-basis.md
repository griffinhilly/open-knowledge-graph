---
id: span-and-basis
title: Span, Linear Independence, and Basis
domain: mathematics
course: linear-algebra
prerequisites:
- id: vector-subspaces
  type: hard
builds-toward:
- basis-and-dimension
- change-of-basis-matrices
tags:
- span
- linear-independence
- basis
stage: formal-systems
status: draft
---

# Span, Linear Independence, and Basis

## Core Idea
The span of vectors v₁, ..., vₖ is all linear combinations c₁v₁ + ... + cₖvₖ, forming a subspace. Vectors are linearly independent if c₁v₁ + ... + cₖvₖ = 0 only when all cᵢ = 0. A basis is a maximal linearly independent set (or equivalently, a minimal spanning set). Every basis has the same cardinality—the dimension.

## How It's Best Learned
Compute span geometrically in R² and R³ (lines, planes). Check linear independence by row-reducing the matrix of vectors. Build a basis by selecting pivot columns from a spanning set.

## Explainer

You already know that a **subspace** is a subset of Rⁿ closed under addition and scalar multiplication. The concept of span answers the question: given a collection of vectors, what subspace do they generate? The **span** of vectors v₁, …, vₖ is the set of all linear combinations c₁v₁ + c₂v₂ + … + cₖvₖ, where each cᵢ is any real number. In R², the span of a single nonzero vector is a line through the origin. The span of two vectors that point in different directions is all of R² — you can reach any point by choosing the right scalars. If the two vectors point in the same direction, their span is still just a line: one of them adds no new reach.

That last observation motivates **linear independence**. A set of vectors is linearly independent if the only way to combine them to get the zero vector is by setting every coefficient to zero: c₁v₁ + … + cₖvₖ = 0 implies c₁ = c₂ = … = cₖ = 0. Linear independence means no vector in the set is redundant — none can be written as a combination of the others. If one can, you have linear dependence, and removing that vector doesn't shrink the span. Geometrically: two vectors in R² are linearly dependent if and only if they are collinear (parallel or anti-parallel).

A **basis** for a subspace V is a set of vectors that does two things simultaneously: it spans V (you can reach everything in V), and it is linearly independent (there is no redundancy). These are dual requirements: a spanning set might have too many vectors (some redundant), while a linearly independent set might have too few (missing some of V). A basis hits the sweet spot — it is a minimal spanning set and a maximal independent set at the same time. For example, the standard basis vectors e₁ = (1,0,0), e₂ = (0,1,0), e₃ = (0,0,1) form a basis for R³: they span all of R³ and are independent.

The deepest theorem in this area is that **every basis for a subspace has the same number of vectors**. That common count is the **dimension** of the subspace. This is not obvious — it requires proof — but it means dimension is a well-defined property of the subspace, not of the particular basis you chose. R³ has dimension 3; any plane through the origin has dimension 2; any line through the origin has dimension 1; the zero subspace has dimension 0. Dimension captures the "degrees of freedom" in a subspace and will govern nearly every theorem you encounter from here: the rank-nullity theorem, the invertibility of matrices, the structure of solutions to linear systems.
