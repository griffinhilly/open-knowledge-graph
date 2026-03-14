---
id: basis-and-dimension
title: Basis and Dimension of Vector Spaces
domain: mathematics
course: linear-algebra
prerequisites:
- id: span-and-basis
  type: hard
builds-toward:
- change-of-basis-matrices
- linear-transformations-definition
- rank-nullity-theorem
tags:
- basis
- dimension
stage: formal-systems
status: draft
---

# Basis and Dimension of Vector Spaces

## Core Idea
Every finite-dimensional vector space has a basis, and all bases have the same size—the dimension dim(V). A set of n linearly independent vectors in an n-dimensional space is a basis. Dimension is additive: dim(U + W) = dim(U) + dim(W) − dim(U ∩ W). Coordinates relative to a basis provide an isomorphism with Rⁿ.

## How It's Best Learned
Find bases for familiar spaces: {1, x, x²} for polynomials of degree ≤ 2 (dim = 3); standard basis eᵢ for Rⁿ (dim = n). Use row reduction to find basis for column/null space.
