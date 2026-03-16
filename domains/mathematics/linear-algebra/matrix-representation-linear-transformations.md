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

## Explainer

From your study of linear transformations, you know that a linear map T: Rⁿ → Rᵐ is completely determined by what it does to a basis. If you know T(e₁), T(e₂), ..., T(eₙ) — where e₁, ..., eₙ are the standard basis vectors — then for any vector v = c₁e₁ + c₂e₂ + ... + cₙeₙ, linearity gives T(v) = c₁T(e₁) + c₂T(e₂) + ... + cₙT(eₙ). The outputs T(eᵢ) are fixed vectors in Rᵐ, so T(v) is just a specific linear combination of them. The **matrix representation** packages this fact into a single object: the matrix [T] whose columns are exactly T(e₁), T(e₂), ..., T(eₙ).

The connection to matrix multiplication you already know makes this concrete. When you compute [T]v — that is, multiply the matrix [T] by the coordinate vector v = (c₁, c₂, ..., cₙ) — you get exactly c₁·(column 1) + c₂·(column 2) + ... + cₙ·(column n) = c₁T(e₁) + ... + cₙT(eₙ) = T(v). Matrix-vector multiplication *is* linear transformation application. The matrix is just a compact encoding of where the basis vectors land.

Here is how to build the matrix for any transformation: apply T to each standard basis vector one at a time, and write the result as a column. For example, if T: R² → R² rotates vectors 90° counterclockwise, then T(e₁) = T(1,0) = (0,1) and T(e₂) = T(0,1) = (-1,0). Stack these as columns: [T] = [[0, -1], [1, 0]]. You can verify that multiplying this matrix by any (x, y) gives (-y, x), which is exactly the 90° rotation formula.

The deeper point is that the matrix depends on your **choice of basis**, not on the transformation itself. If you choose a different basis for Rⁿ or Rᵐ, the same transformation T gets a different matrix. The transformation is a geometric object — a rule for moving vectors — while the matrix is a coordinate description of that rule. This distinction becomes critical when you study change of basis: you will learn how to translate between matrix representations as you switch coordinate systems, always describing the same underlying transformation. For now, the key insight is that fixing a basis makes abstract transformations concrete: every linear map becomes a matrix, and every matrix is a linear map.
