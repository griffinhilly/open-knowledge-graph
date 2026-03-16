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

## Explainer

You already know that a linear transformation T respects addition and scalar multiplication. This means T is completely determined by an extremely small amount of information: where it sends each basis vector. If you know T(e₁), T(e₂), …, T(eₙ), you can compute T on any input — because any vector x can be written as a linear combination of the standard basis vectors, and linearity does the rest.

The **standard matrix** turns this observation into a concrete recipe. Assemble the images T(e₁), T(e₂), …, T(eₙ) as the columns of a matrix A. Then for any input vector x = [x₁, x₂, …, xₙ]ᵀ, the matrix-vector product Ax automatically produces T(x). You can verify this: Ax equals x₁ times column 1 plus x₂ times column 2 plus … — exactly x₁T(e₁) + x₂T(e₂) + … = T(x₁e₁ + x₂e₂ + …) = T(x). The matrix multiplication you learned is precisely the mechanism that re-assembles the transformation from its column instructions.

To find the standard matrix for any geometric transformation, you need only track where the basis vectors e₁ = [1,0]ᵀ and e₂ = [0,1]ᵀ land. For a counterclockwise rotation by angle θ: e₁ maps to [cos θ, sin θ]ᵀ and e₂ maps to [−sin θ, cos θ]ᵀ. These become the columns of the rotation matrix. No equations to solve — just compute T on the two basis vectors and read off the columns directly.

The word "standard" is critical: this construction uses the standard basis for both the input space ℝⁿ and the output space ℝᵐ. Change the basis, and the same transformation T would have a different matrix representation. The standard matrix is the special case where both coordinate systems use the natural axes. When you later study change of basis, you will see how to convert between matrix representations as the coordinate system changes — but all of it rests on this foundational idea that a linear transformation is nothing more than its action on basis vectors.
