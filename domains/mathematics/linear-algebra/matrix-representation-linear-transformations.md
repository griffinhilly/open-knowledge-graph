---
id: matrix-representation-linear-transformations
title: Matrix Representation of Linear Transformations
domain: mathematics
course: linear-algebra
prerequisites:
- id: linear-transformations
  type: hard
- id: matrix-multiplication
  type: hard
builds-toward:
- composition-linear-transformations
- change-of-basis
tags:
- matrix-representation
- basis
- coordinates
stage: formal-systems
status: draft
---

# Matrix Representation of Linear Transformations

## Core Idea
Every linear transformation T: Rⁿ → Rᵐ has a matrix representation [T] whose columns are T(e₁), T(e₂), ..., T(eₙ). Once bases are fixed, the transformation is completely determined by this matrix. Changing bases changes the matrix representation, but the transformation itself is basis-independent.

## Questions

```yaml
- question: "To find the matrix representation of T: R³ → R², you compute T(e₁) = (2,1), T(e₂) = (0,3), T(e₃) = (−1,2). What is [T]?"
  type: multiple-choice
  options:
    - "A 3×2 matrix with rows (2,1), (0,3), (−1,2)"
    - "A 2×3 matrix with columns (2,1), (0,3), (−1,2)"
    - "A 2×3 matrix with rows (2,1), (0,3), (−1,2)"
    - "A 3×2 matrix with columns (2,1), (0,3), (−1,2)"
  answer: 1
  explanation: "The matrix [T] for T: Rⁿ → Rᵐ is an m×n matrix whose *columns* are T(e₁), T(e₂), ..., T(eₙ). Here n=3, m=2, so [T] is 2×3. The outputs T(eᵢ) go in as columns, not rows — because matrix-vector multiplication [T]v computes c₁·(col 1) + c₂·(col 2) + ... which equals T(v) only when the columns are the T(eᵢ). Placing outputs as rows (options A and C) is the most common error when building the matrix from scratch."

- question: "The same linear transformation T is represented by matrix A in one basis and matrix B in a different basis. What does this imply?"
  type: multiple-choice
  options:
    - "A and B represent different transformations — each matrix defines a unique map"
    - "One of A or B must be wrong; a transformation has only one correct matrix"
    - "A and B are both valid representations of the same geometric transformation; the matrix depends on the choice of basis"
    - "A and B must be equal because the transformation itself is basis-independent"
  answer: 2
  explanation: "The transformation is a geometric object — a rule for moving vectors — while the matrix is a coordinate description of that rule. Choosing different bases gives different coordinate descriptions of the same underlying map. A and B are related by a change-of-basis formula but describe the same transformation, just as the same physical vector has different coordinate representations in different coordinate systems. Option D confuses the transformation (basis-independent) with its matrix representation (basis-dependent)."

- question: "If you know how a linear transformation acts on every vector in Rⁿ, you can always find its matrix by computing T(v) for every possible vector v."
  type: true-false
  answer: false
  explanation: "You only need to compute T on a basis — the n standard basis vectors e₁, ..., eₙ. Linearity then completely determines T on every other vector: if v = c₁e₁ + ... + cₙeₙ, then T(v) = c₁T(e₁) + ... + cₙT(eₙ). Computing T on infinitely many vectors is unnecessary. This is one of the most powerful consequences of linearity: a linear map is completely determined by finitely much data."

- question: "The matrix [T] whose columns are T(e₁), ..., T(eₙ) encodes the transformation in a basis-independent way."
  type: true-false
  answer: false
  explanation: "The matrix representation *depends on* the choice of basis. [T] as constructed with columns T(e₁), ..., T(eₙ) uses the standard basis for Rⁿ and Rᵐ — those are specific choices. With different bases, the same transformation T yields a different matrix. The transformation itself is basis-independent (it is a geometric map), but its matrix representation is not. This is precisely why 'change of basis' is a meaningful operation: you are translating between different coordinate descriptions of the same abstract map."

- question: "Why does matrix-vector multiplication [T]v compute exactly T(v)? Explain in terms of what the columns of [T] represent."
  type: short-answer
  answer: "Any vector v = (c₁, ..., cₙ) can be written as c₁e₁ + ... + cₙeₙ. By linearity, T(v) = c₁T(e₁) + ... + cₙT(eₙ). Matrix-vector multiplication [T]v computes exactly this: c₁ times column 1 plus c₂ times column 2, etc. Since the columns of [T] are defined to be T(e₁), T(e₂), ..., T(eₙ), the result is T(v). Matrix multiplication is not an arbitrary rule — it is the encoding of 'apply a linear transformation to a coordinate vector.'"
  explanation: "This connection reveals why matrix multiplication was defined the way it was: to make function application correspond to matrix multiplication. Understanding this makes matrix algebra feel inevitable rather than arbitrary, and it is the foundation for why composition of linear transformations corresponds to matrix multiplication (composing two maps = multiplying two matrices)."
```

## Explainer

From your study of linear transformations, you know that a linear map T: Rⁿ → Rᵐ is completely determined by what it does to a basis. If you know T(e₁), T(e₂), ..., T(eₙ) — where e₁, ..., eₙ are the standard basis vectors — then for any vector v = c₁e₁ + c₂e₂ + ... + cₙeₙ, linearity gives T(v) = c₁T(e₁) + c₂T(e₂) + ... + cₙT(eₙ). The outputs T(eᵢ) are fixed vectors in Rᵐ, so T(v) is just a specific linear combination of them. The **matrix representation** packages this fact into a single object: the matrix [T] whose columns are exactly T(e₁), T(e₂), ..., T(eₙ).

The connection to matrix multiplication you already know makes this concrete. When you compute [T]v — that is, multiply the matrix [T] by the coordinate vector v = (c₁, c₂, ..., cₙ) — you get exactly c₁·(column 1) + c₂·(column 2) + ... + cₙ·(column n) = c₁T(e₁) + ... + cₙT(eₙ) = T(v). Matrix-vector multiplication *is* linear transformation application. The matrix is just a compact encoding of where the basis vectors land.

Here is how to build the matrix for any transformation: apply T to each standard basis vector one at a time, and write the result as a column. For example, if T: R² → R² rotates vectors 90° counterclockwise, then T(e₁) = T(1,0) = (0,1) and T(e₂) = T(0,1) = (-1,0). Stack these as columns: [T] = [[0, -1], [1, 0]]. You can verify that multiplying this matrix by any (x, y) gives (-y, x), which is exactly the 90° rotation formula.

The deeper point is that the matrix depends on your **choice of basis**, not on the transformation itself. If you choose a different basis for Rⁿ or Rᵐ, the same transformation T gets a different matrix. The transformation is a geometric object — a rule for moving vectors — while the matrix is a coordinate description of that rule. This distinction becomes critical when you study change of basis: you will learn how to translate between matrix representations as you switch coordinate systems, always describing the same underlying transformation. For now, the key insight is that fixing a basis makes abstract transformations concrete: every linear map becomes a matrix, and every matrix is a linear map.
