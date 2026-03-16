---
id: basis-definition
title: Basis of a Vector Space
domain: mathematics
course: linear-algebra
prerequisites:
- id: span-spanning-set
  type: hard
- id: linear-independence
  type: hard
builds-toward:
- dimension-vector-space
- rank-nullity-theorem
tags:
- basis
- vector spaces
- linear combinations
stage: formal-systems
status: draft
---

# Basis of a Vector Space

## Core Idea
A basis of a vector space V is a linearly independent spanning set. Every vector in V has a unique representation as a linear combination of basis vectors. A space with a finite basis has dimension equal to the number of basis vectors. Different bases have equal size.

## Explainer

Your two prerequisites give you the two halves of the basis definition. A **spanning set** is a set of vectors from which you can reach every vector in the space by taking linear combinations — it's big enough to cover everything. A **linearly independent** set is one in which no vector is redundant — none can be written as a combination of the others. A **basis** is a set that is both at once: big enough to span, lean enough to be independent. It is the "just right" set — neither too small nor too large.

Why does independence matter if you already have a spanning set? Suppose you span ℝ² with three vectors: (1,0), (0,1), and (1,1). You can reach every point in the plane, but (1,1) is redundant — it's already the sum of the first two. That redundancy has a cost: the representation of any vector as a linear combination is no longer unique. The vector (2,3) could be written as 2(1,0) + 3(0,1) + 0(1,1), or as 1(1,0) + 3(0,1) + 1(1,1) − something, or infinitely many ways. A basis eliminates this ambiguity: with a basis, every vector has **exactly one** representation as a linear combination of basis vectors.

The standard example in ℝ³ is the **standard basis**: e₁ = (1,0,0), e₂ = (0,1,0), e₃ = (0,0,1). These three vectors are clearly independent (none is a combination of the others) and clearly span ℝ³ (any (a,b,c) = ae₁ + be₂ + ce₃). The coefficients (a,b,c) are simply the coordinates — a fact that feels obvious here but generalizes powerfully to abstract vector spaces where "coordinates" only make sense relative to a chosen basis.

A fundamental theorem says all bases of a finite-dimensional vector space have the same number of vectors. That number is the **dimension** of the space. ℝ³ has dimension 3; the space of polynomials of degree ≤ 2 has dimension 3 (basis: {1, x, x²}); a line through the origin has dimension 1. Dimension is a property of the space itself, not of any particular basis. This invariance is what makes dimension a meaningful concept, and it flows directly from the uniqueness-of-representation property that a basis guarantees.
