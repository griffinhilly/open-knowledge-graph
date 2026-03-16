---
id: determinant-computation
title: Computing Determinants
domain: mathematics
course: linear-algebra
prerequisites:
- id: matrices-definition
  type: hard
builds-toward:
- determinant-properties
- cramers-rule
- eigenvalues-eigenvectors
tags:
- determinants
- computation
- algorithms
stage: formal-systems
status: draft
---

# Computing Determinants

## Core Idea
The determinant of an n × n matrix is a scalar with geometric meaning (signed volume of the parallelepiped spanned by columns). For 2×2: det([a b; c d]) = ad − bc. For larger matrices, use cofactor expansion C_ij = (−1)^{i+j} M_ij or row reduction. det(A) = 0 iff A is singular.

## Explainer

You know from your work with matrices that a matrix represents a linear transformation — it takes a vector and produces a new vector. The **determinant** measures how that transformation scales space. Specifically, the absolute value of the determinant of a 2×2 matrix equals the area of the parallelogram formed by the two column vectors. For a 3×3 matrix, it equals the volume of the parallelepiped formed by the three column vectors. If the determinant is negative, it means the transformation includes a reflection — it reversed the orientation of space. If the determinant is zero, the transformation squashes all of space onto a lower-dimensional subspace (the columns are linearly dependent), which is why det(A) = 0 if and only if A is singular.

For a 2×2 matrix [a b; c d], the formula is simply ad − bc. The geometric intuition: one column is (a, c) and the other is (b, d). The area of the parallelogram they span is the base times the height — computing this gives ad − bc. You can verify: if the two columns are identical, the parallelogram collapses to a line, giving area 0, and indeed ad − bc = ad − ad = 0.

For larger matrices, the two main methods are **cofactor expansion** and **row reduction**. In cofactor expansion, you pick any row or column and expand along it: det(A) = Σ aᵢⱼ · Cᵢⱼ, where the **cofactor** Cᵢⱼ = (−1)^{i+j} · Mᵢⱼ and Mᵢⱼ is the determinant of the (n−1)×(n−1) matrix left after deleting row i and column j. The (−1)^{i+j} factor creates a checkerboard sign pattern (+,−,+,−,…). This reduces an n×n determinant to a sum of (n−1)×(n−1) determinants, applied recursively. For a 3×3 matrix, this means three 2×2 determinants; for 4×4, four 3×3 determinants.

Row reduction is usually faster for larger matrices. The key facts: swapping two rows negates the determinant; multiplying a row by a scalar multiplies the determinant by that scalar; adding a multiple of one row to another leaves the determinant unchanged. By tracking these operations as you row-reduce to upper triangular form, you can compute the determinant as the product of the diagonal entries (times any sign flips from row swaps and any scalars you factored out). This connects the determinant computation directly to Gaussian elimination, which you will use throughout linear algebra — determinants and row reduction are deeply intertwined tools.
