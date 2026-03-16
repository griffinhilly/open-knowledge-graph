---
id: change-of-basis-matrices
title: Change of Basis and Coordinate Transformations
domain: mathematics
course: linear-algebra
prerequisites:
- id: linear-transformation-matrix-representation
  type: hard
- id: matrix-inverses-computation
  type: hard
builds-toward:
- eigenvalues-eigenvectors-introduction
- diagonalization-similar-matrices
tags:
- change-of-basis
- coordinates
- transformations
stage: formal-systems
status: draft
---

# Change of Basis and Coordinate Transformations

## Core Idea
If B and C are two bases for Rⁿ, the change-of-basis matrix P_C←B converts coordinates from B to C: [v]_C = P_C←B [v]_B. The matrix P has C-coordinates of B-basis vectors as columns. If A represents T in the standard basis, then A' = P⁻¹AP represents T relative to basis B, where P = [B]. Similar matrices represent the same transformation in different bases.

## Explainer

From your prerequisites, you know that a **linear transformation** can be represented as a matrix — but only once you fix a basis. The matrix depends on which basis you use. The same transformation looks different in different coordinate systems, just as the same city can be described by different GPS coordinate systems. **Change of basis** is the translation dictionary between those coordinate systems.

Here's the concrete setup. Suppose B = {b₁, b₂} is a basis for ℝ², and a vector v has B-coordinates [v]_B = (3, 1) — meaning v = 3b₁ + b₂. To express v in the standard basis, multiply the B-coordinates by the matrix whose columns are b₁ and b₂. This matrix is sometimes written P or [B]. To go the other direction — from standard coordinates to B-coordinates — multiply by P⁻¹. This is why **matrix inverses** are a hard prerequisite: the reverse conversion requires the inverse to exist, which is guaranteed when B is a basis (the columns are linearly independent, so the matrix is invertible).

Now consider how a linear transformation T is affected. If A is the matrix of T in the standard basis, then to work with T using B-coordinates you must: convert from B to standard (multiply by P), apply T (multiply by A), then convert back to B (multiply by P⁻¹). The combined operation is P⁻¹AP. This is called the matrix of T **relative to basis B**, often written A'. The relationship A' = P⁻¹AP defines **matrix similarity** — two matrices are similar if one can be obtained from the other by this conjugation. Similar matrices represent the same linear transformation; they only differ in the choice of coordinate system.

The real power of change of basis is revealed by **diagonalization**, which you'll study next. Many transformations become diagonal matrices in a cleverly chosen basis — and diagonal matrices are trivial to work with (powers, exponentials, eigenvalue computations all become entry-wise operations). The eigenvectors of T form exactly this special basis. So the sequence of ideas is: find eigenvalues and eigenvectors → form P from eigenvectors → compute A' = P⁻¹AP → get a diagonal matrix that represents the same transformation far more simply. Change of basis is the bridge from a complicated matrix to its simplest equivalent form.
