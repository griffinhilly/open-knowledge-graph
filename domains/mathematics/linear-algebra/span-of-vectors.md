---
id: span-of-vectors
title: Span and Linear Combinations
domain: mathematics
course: linear-algebra
prerequisites:
- id: vector-spaces
  type: hard
builds-toward:
- basis-and-dimension
- column-space
tags:
- span
- linear-combination
- closure
stage: formal-systems
status: draft
---

# Span and Linear Combinations

## Core Idea
The span of vectors v₁, ..., vₖ is the set of all linear combinations c₁v₁ + ... + cₖvₖ where cᵢ ∈ ℝ. Span is a subspace, the smallest containing all given vectors. The columns of a matrix A span the column space; row vectors span the row space.

## Explainer

From your study of vector spaces, you know that vectors can be added and scaled by real numbers. Now ask a natural question: starting from a small collection of vectors, what is the full set of vectors you can construct just using those two operations? The answer is the **span**. Given vectors v₁, v₂, ..., vₖ, a **linear combination** is any expression c₁v₁ + c₂v₂ + ... + cₖvₖ where the cᵢ are arbitrary real numbers. The span is the set of all such linear combinations — every vector you can reach by stretching, shrinking, and adding your starting collection.

Geometry gives the clearest intuition. A single nonzero vector v in ℝ³ spans a line through the origin: { tv : t ∈ ℝ }. Two vectors that are not parallel span a plane through the origin. Three vectors that don't all lie in a common plane span all of ℝ³. In each case, the span is the "flat space" that contains the given vectors and is closed under linear combinations. You cannot escape it without introducing a new vector that points in a direction not already expressible in terms of the others.

The span of any set of vectors is always a **subspace** of the ambient vector space. You can verify the two closure conditions directly: if u and w are both linear combinations of v₁, ..., vₖ, then so is u + w (just add the coefficients), and so is cu for any scalar c. Span is also the *smallest* subspace containing all of v₁, ..., vₖ — any subspace containing those vectors must contain all their linear combinations. Adding more vectors to the spanning set can only maintain or enlarge the span, never shrink it.

The connection to matrices ties everything together. For a matrix A, the **column space** is exactly the span of its column vectors. When you write the linear system Ax = b, you are asking whether b can be expressed as a linear combination of the columns of A — that is, whether b lies in the span of those columns. This reframes the question of solvability entirely: "does b lie in the column space?" becomes the central question of linear systems, leading directly to the concepts of basis and dimension.
