---
id: eigenvalues-eigenvectors
title: Eigenvalues and Eigenvectors
domain: mathematics
course: linear-algebra
prerequisites:
- id: determinant-properties
  type: hard
- id: linear-transformation-definition
  type: hard
builds-toward:
- characteristic-polynomial
tags:
- eigenvalues
- eigenvectors
- spectral
stage: formal-systems
status: draft
---

# Eigenvalues and Eigenvectors

## Core Idea
An eigenvector x of a matrix A is a non-zero vector such that Ax = λx for some scalar λ (the eigenvalue). Geometrically, A stretches x by factor λ without changing direction. Eigenvalues are roots of the characteristic polynomial. Eigenvectors form eigenspaces and reveal matrix structure.

## Questions

```yaml
- question: "A 2×2 matrix A has eigenvector v = [1, 0]ᵀ with eigenvalue 3. Which of the following must be true?"
  type: multiple-choice
  options: ["The matrix A equals 3I", "Multiplying A by [1, 0]ᵀ gives [3, 0]ᵀ", "The matrix A rotates [1, 0]ᵀ by 3 degrees", "The determinant of A is 3"]
  answer: 1
  explanation: "By definition, Av = λv, so A[1, 0]ᵀ = 3[1, 0]ᵀ = [3, 0]ᵀ. A does not need to equal 3I — that would require every vector to be an eigenvector with eigenvalue 3. The determinant of A equals the product of all its eigenvalues, not just one of them."

- question: "If λ = 0 is an eigenvalue of matrix A, then A is invertible."
  type: true-false
  answer: false
  explanation: "An eigenvalue of 0 means there exists a nonzero vector v such that Av = 0v = 0, placing v in the null space of A. A matrix with a nontrivial null space has determinant 0 and is therefore not invertible. The eigenvalue λ = 0 is precisely the indicator that A is singular."

- question: "Explain geometrically what it means for a vector to be an eigenvector of a linear transformation."
  type: short-answer
  answer: "An eigenvector is a direction that the transformation preserves — it only stretches or compresses the vector along the same line through the origin without rotating it off that line."
  explanation: "Most vectors get both stretched and rotated by a linear transformation. Eigenvectors are the special directions where no rotation occurs — they lie along invariant lines of the transformation. This geometric view reveals why eigenvectors expose the 'skeleton' of what a transformation is doing."
```

## Explainer

From your study of linear transformations, you know that a matrix A represents a transformation of space: it can stretch, compress, reflect, shear, or rotate vectors. Most vectors get moved in complicated ways — they end up pointing in a completely different direction after multiplication. But some special vectors are not rotated at all. They might get scaled or flipped, but they remain on the same line through the origin. These are the eigenvectors, and the scaling factors are the eigenvalues.

Formally, v is an eigenvector of A with eigenvalue λ if Av = λv. The equation says: applying the transformation to v just scales v by the factor λ. If λ = 2, the vector doubles in length but points the same way. If λ = −1, it flips direction but stays on the same line. If λ = 0, v collapses to zero — which means A sends a nonzero vector to zero, so A is singular (not invertible). This connects directly to what you learned about determinants: det(A) = 0 exactly when A has a zero eigenvalue.

To find eigenvalues, rearrange Av = λv to (A − λI)v = 0. For this to have a nonzero solution v (eigenvectors must be nonzero by definition), the matrix (A − λI) must be singular, meaning its determinant is zero. So the eigenvalues are the solutions to det(A − λI) = 0, the characteristic polynomial. For a 2×2 matrix this yields a quadratic; for an n×n matrix, a degree-n polynomial. Once you have an eigenvalue λ, finding the eigenvectors means solving the linear system (A − λI)v = 0 — the set of all solutions forms the eigenspace for λ, a subspace of the domain.

A key practical point: eigenvalues do not tell you the direction independently — different matrices can share an eigenvalue but have different eigenvectors. The eigenvalue measures the magnitude of stretching along the eigenvector direction; you need both pieces together. If a matrix has n linearly independent eigenvectors, you can decompose any vector in the space as a combination of them, making repeated applications of A (like computing A¹⁰⁰) dramatically easier: each eigenvector component just gets scaled by the eigenvalue raised to the power.

Eigenvalues and eigenvectors reach far beyond the linear algebra course. In statistics, principal component analysis uses the eigenvectors of a covariance matrix to find the directions of maximum variance. In physics, quantum mechanics is built on eigenvalue equations where physical observables correspond to operators and measured values are eigenvalues. In graph theory and web search, the dominant eigenvector of a connectivity matrix encodes relative importance (PageRank). Understanding the concept geometrically — invariant directions under a transformation — is the foundation for all of these applications.
