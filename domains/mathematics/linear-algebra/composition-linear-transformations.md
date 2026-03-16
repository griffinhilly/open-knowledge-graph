---
id: composition-linear-transformations
title: Composition of Linear Transformations
domain: mathematics
course: linear-algebra
prerequisites:
- id: matrix-representation-linear-transformations
  type: hard
builds-toward:
- eigenvalues-and-eigenvectors
- diagonalization
tags:
- composition
- matrix-multiplication
- invertible
stage: formal-systems
status: draft
---

# Composition of Linear Transformations

## Core Idea
The composition of linear transformations S ∘ T is linear, and its matrix representation is the product [S][T]. Invertible transformations form a group under composition (the general linear group GL_n). Composition of matrices directly corresponds to sequential application of transformations.

## Explainer

From your work on **matrix representations of linear transformations**, you know that every linear transformation T: ℝⁿ → ℝᵐ can be represented by a matrix [T], and applying T to a vector v is the same as computing [T]v. Now suppose you have two linear transformations: T: ℝⁿ → ℝᵐ and S: ℝᵐ → ℝᵖ. The **composition** S ∘ T maps ℝⁿ → ℝᵖ by first applying T, then applying S: (S ∘ T)(v) = S(T(v)). The central fact of this topic is that the matrix of S ∘ T is the product [S][T]. This is not a definition — it's a theorem, and it explains why matrix multiplication is defined the way it is.

To see why the formula is right, trace through what happens to a basis vector eⱼ. First, T sends eⱼ to the j-th column of [T]. Then S sends that vector to [S] times the j-th column of [T] — which is the j-th column of [S][T]. Since the matrix of S ∘ T is determined by where it sends basis vectors, and those columns match the columns of [S][T], the matrices are equal. Matrix multiplication is defined precisely so that this correspondence holds. This is why the product [S][T] is computed by taking dot products of rows of [S] with columns of [T] — it's encoding how the two successive transformations interact on each coordinate.

Order matters. S ∘ T means "do T first, then S" — but the matrix product is written [S][T], with [S] on the left. This reversal (the last transformation written first) is a persistent source of confusion. Think of it this way: if you read a composition from right to left, you get the temporal order of operations. The same applies to reading matrix products: [A][B][C]v means apply C first, then B, then A.

When a transformation T is **invertible** — meaning there exists T⁻¹ with T⁻¹ ∘ T = identity — the corresponding matrix [T] is invertible, and [T⁻¹] = [T]⁻¹. The collection of all invertible n×n matrices (equivalently, invertible linear transformations on ℝⁿ) forms a structure called the **general linear group** GL_n under matrix multiplication. "Group" here means: composition of two invertible maps is invertible, composition is associative, the identity map is an element, and every element has an inverse. This group structure is what makes linear algebra interact with symmetry and geometry — rotations, reflections, and shears all live in GL_n, and composing them corresponds to multiplying their matrices.
