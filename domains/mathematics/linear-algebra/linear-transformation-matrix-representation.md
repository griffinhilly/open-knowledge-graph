---
id: linear-transformation-matrix-representation
title: Matrix Representation of Linear Transformations
domain: mathematics
course: linear-algebra
prerequisites:
- id: linear-transformations-definition
  type: hard
- id: basis-and-dimension
  type: hard
builds-toward:
- change-of-basis-matrices
- eigenvalues-eigenvectors-introduction
tags:
- matrix-representation
- coordinates
- bases
stage: formal-systems
status: draft
---

# Matrix Representation of Linear Transformations

## Core Idea
Every linear transformation T: Rⁿ → Rᵐ is represented by an m×n matrix A, where T(x) = Ax. To find A, compute T(eᵢ) for each standard basis vector and place the results as columns. For non-standard bases, the matrix is [T]_B = [T(b₁) ... T(bₙ)]_C in coordinates relative to bases B and C.

## Explainer

The core insight here is beautiful: a linear transformation is completely determined by what it does to any basis. You already know from your study of bases that every vector in Rⁿ can be written uniquely as a linear combination of basis vectors. And you know that linear transformations preserve those combinations — T(αu + βv) = αT(u) + βT(v). Combine these two facts: once you know where T sends each basis vector, you know where T sends every vector. The matrix is just a systematic way of recording that information.

For the standard basis in Rⁿ, this is especially clean. The standard basis vectors are e₁ = (1,0,...,0), e₂ = (0,1,...,0), and so on. To build the matrix for T: Rⁿ → Rᵐ, compute T(e₁), T(e₂), ..., T(eₙ). Each result is a vector in Rᵐ. Arrange them as columns: the first column is T(e₁), the second is T(e₂), and so on. You have your m×n matrix A. To verify it works: any x ∈ Rⁿ can be written as x = x₁e₁ + ... + xₙeₙ, so T(x) = x₁T(e₁) + ... + xₙT(eₙ) = Ax, where Ax is the standard matrix-vector product.

For non-standard bases, the same logic applies but coordinates change. If T maps from a space with basis B to a space with basis C, you compute T applied to each vector in B, then express each result in terms of C. The resulting coordinate vectors become the columns of the **change-of-basis matrix** [T]_B^C. This is the direct application of your prerequisite on basis and dimension: the matrix representation depends entirely on which bases you choose for the domain and codomain.

The payoff is that every theorem about matrices becomes a theorem about linear transformations, and vice versa. Composition of transformations corresponds to matrix multiplication. The rank of the matrix equals the dimension of the image. The nullity equals the dimension of the kernel. The abstract world of transformations and the computational world of matrices are not just analogous — they are literally the same object written in two different notations.
