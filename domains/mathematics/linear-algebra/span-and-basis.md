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
