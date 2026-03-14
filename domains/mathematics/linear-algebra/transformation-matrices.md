---
id: transformation-matrices
title: The Standard Matrix of a Linear Transformation
domain: mathematics
course: linear-algebra
prerequisites:
- id: linear-transformations
  type: hard
- id: row-echelon-form
  type: soft
builds-toward:
- matrix-composition
- change-of-basis
- eigenvalues-and-eigenvectors
tags:
- standard matrix
- matrix representation
- basis images
- columns of matrix
stage: formal-systems
status: validated
---

# The Standard Matrix of a Linear Transformation

## Core Idea
Every linear transformation T: Rⁿ → Rᵐ is uniquely determined by where it sends the n standard basis vectors e₁, e₂, …, eₙ. The standard matrix A of T is the m×n matrix whose j-th column is T(eⱼ), so that T(x) = Ax for all x in Rⁿ. This correspondence means matrix multiplication IS the computational model for all linear transformations between Euclidean spaces. Finding the standard matrix requires only computing T on basis vectors, then assembling the results as columns.

## How It's Best Learned
Derive standard matrices for common geometric transformations — rotation by angle θ, reflection across a line, projection onto a subspace — by tracking where e₁ and e₂ land. Then verify by applying the matrix to arbitrary vectors.

## Common Misconceptions
- The columns of the standard matrix are the IMAGES of the basis vectors, not the basis vectors themselves.
- Students sometimes try to 'solve' for A using a system of equations; instead, A is directly assembled from T(e₁), T(e₂), …
- The standard matrix depends on the choice of basis; the 'standard' qualifier means we use the standard basis for both domain and codomain.
