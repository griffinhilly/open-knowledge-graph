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

## Questions

```yaml
- question: "A student wants to find the standard matrix for T: ℝ² → ℝ² defined by T(x, y) = (2x + y, x − 3y). What is the correct procedure?"
  type: multiple-choice
  options:
    - "Compute T(1, 0) = (2, 1) and T(0, 1) = (1, −3); assemble these as the columns of A"
    - "Solve the system Ax = T(x) for A using row reduction on sample inputs"
    - "Find vectors that A maps to e₁ and e₂ and use those as rows"
    - "Average T's output over many random inputs to estimate A's entries"
  answer: 0
  explanation: "The standard matrix is assembled directly from the images of the basis vectors as columns — no equation solving required. T(e₁) = T(1, 0) = (2, 1) becomes column 1; T(e₂) = T(0, 1) = (1, −3) becomes column 2. This works because linearity guarantees T(x) = x₁·T(e₁) + x₂·T(e₂), which is exactly what Ax computes."

- question: "The standard matrix of a 90° counterclockwise rotation is [[0, −1], [1, 0]]. Why is the first column [0, 1]ᵀ rather than [1, 0]ᵀ?"
  type: multiple-choice
  options:
    - "Because e₁ = [1, 0]ᵀ maps to [0, 1]ᵀ under a 90° counterclockwise rotation, and columns encode where basis vectors go"
    - "Because [1, 0]ᵀ is reserved for identity matrices and cannot appear as a rotation column"
    - "Because columns of a rotation matrix must always be perpendicular to the rows"
    - "Because rows encode where basis vectors go; the first row therefore cannot match e₁"
  answer: 0
  explanation: "Column j of the standard matrix is T(eⱼ). Rotating e₁ = [1, 0]ᵀ by 90° counterclockwise produces [0, 1]ᵀ — that becomes column 1. Rotating e₂ = [0, 1]ᵀ produces [−1, 0]ᵀ — that becomes column 2. The common mistake in option D (rows encode basis images) would produce the transpose, which represents a different transformation."

- question: "The standard matrix of a linear transformation is independent of what basis you use for the input and output spaces."
  type: true-false
  answer: false
  explanation: "The 'standard' qualifier specifically means the standard basis is used for both domain and codomain — that's what makes it standard. Use a different basis and the same transformation T has a different matrix representation. The study of change of basis is precisely about converting between these representations. Basis-independence would mean every transformation has only one matrix, which is false."

- question: "To construct the standard matrix of T: ℝⁿ → ℝᵐ, you should evaluate T on most vector in ℝⁿ."
  type: true-false
  answer: false
  explanation: "You only need T evaluated on the n standard basis vectors e₁, …, eₙ. By linearity, any vector x = x₁e₁ + ··· + xₙeₙ gives T(x) = x₁T(e₁) + ··· + xₙT(eₙ), which the matrix product Ax reproduces automatically. The entire transformation on an infinite domain is encoded in just n basis images — this is the power of linearity."

- question: "Why is it sufficient to know T(e₁), T(e₂), …, T(eₙ) to completely determine a linear transformation T: ℝⁿ → ℝᵐ?"
  type: short-answer
  answer: "Any vector x ∈ ℝⁿ decomposes as x = x₁e₁ + ··· + xₙeₙ. Linearity then gives T(x) = x₁T(e₁) + ··· + xₙT(eₙ). Knowing T on the basis vectors determines T on every linear combination of them — which is every vector in ℝⁿ."
  explanation: "This is the fundamental theorem behind the standard matrix. A linear transformation is completely and uniquely determined by its values on a basis, because linearity 'extends' those values to all of ℝⁿ without ambiguity. The matrix is just the data structure that packages the n basis images so that Ax replicates the extension automatically."
```

## Explainer

You already know that a linear transformation T respects addition and scalar multiplication. This means T is completely determined by an extremely small amount of information: where it sends each basis vector. If you know T(e₁), T(e₂), …, T(eₙ), you can compute T on any input — because any vector x can be written as a linear combination of the standard basis vectors, and linearity does the rest.

The **standard matrix** turns this observation into a concrete recipe. Assemble the images T(e₁), T(e₂), …, T(eₙ) as the columns of a matrix A. Then for any input vector x = [x₁, x₂, …, xₙ]ᵀ, the matrix-vector product Ax automatically produces T(x). You can verify this: Ax equals x₁ times column 1 plus x₂ times column 2 plus … — exactly x₁T(e₁) + x₂T(e₂) + … = T(x₁e₁ + x₂e₂ + …) = T(x). The matrix multiplication you learned is precisely the mechanism that re-assembles the transformation from its column instructions.

To find the standard matrix for any geometric transformation, you need only track where the basis vectors e₁ = [1,0]ᵀ and e₂ = [0,1]ᵀ land. For a counterclockwise rotation by angle θ: e₁ maps to [cos θ, sin θ]ᵀ and e₂ maps to [−sin θ, cos θ]ᵀ. These become the columns of the rotation matrix. No equations to solve — just compute T on the two basis vectors and read off the columns directly.

The word "standard" is critical: this construction uses the standard basis for both the input space ℝⁿ and the output space ℝᵐ. Change the basis, and the same transformation T would have a different matrix representation. The standard matrix is the special case where both coordinate systems use the natural axes. When you later study change of basis, you will see how to convert between matrix representations as the coordinate system changes — but all of it rests on this foundational idea that a linear transformation is nothing more than its action on basis vectors.
