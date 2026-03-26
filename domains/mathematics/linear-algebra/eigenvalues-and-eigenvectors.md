---
id: eigenvalues-and-eigenvectors
title: Eigenvalues and Eigenvectors
domain: mathematics
course: linear-algebra
prerequisites:
- id: determinant-properties
  type: hard
- id: linear-transformations
  type: hard
builds-toward:
- diagonalization
tags:
- eigenvalues
- eigenvectors
- invariant
stage: formal-systems
status: validated
---

# Eigenvalues and Eigenvectors

## Core Idea
For matrix A, scalar λ is an eigenvalue if Av = λv has a nonzero solution v (an eigenvector). Eigenvectors span the eigenspace E_λ = nul(A − λI). Eigenvalues reveal how A stretches directions; they are invariant under similarity transformations and determine the dynamics of matrix iteration.

## Questions

```yaml
- question: "Matrix A has eigenvector v with eigenvalue λ = -2. What happens to v when multiplied by A?"
  type: multiple-choice
  options: ["v is rotated 180° with no scaling", "v is reversed in direction and doubled in length", "v is unchanged", "v is projected onto a coordinate axis"]
  answer: 1
  explanation: "Av = -2v means v is scaled by -2: the negative sign flips the direction (180° reversal) and the magnitude 2 doubles the length. The key insight is that eigenvectors are only scaled — never rotated off their line — and the eigenvalue encodes both direction (sign) and magnitude of that scaling."

- question: "If v is an eigenvector of A with eigenvalue λ, then the vector 5v is also an eigenvector of A with the same eigenvalue λ."
  type: true-false
  answer: true
  explanation: "A(5v) = 5(Av) = 5(λv) = λ(5v), so 5v satisfies the eigenvector equation with the same λ. Eigenvectors are not unique — any nonzero scalar multiple is also an eigenvector. The eigenspace E_λ = nul(A − λI) captures all of them as a subspace."

- question: "What is the geometric meaning of an eigenvector of a matrix transformation?"
  type: short-answer
  answer: "An eigenvector lies on a line through the origin that the transformation maps to itself — the vector is only stretched or flipped, never rotated off that line."
  explanation: "Most vectors get both scaled and rotated by a matrix. Eigenvectors are the special directions that remain on the same line after the transformation — only their length (and possibly direction sign) changes. This makes them the 'skeleton' that reveals the matrix's fundamental behavior."
```

## Explainer

Most linear transformations scramble vectors — they change both direction and length. But every square matrix has special directions it simply scales, never rotates. These are the eigenvectors. If Av = λv for a nonzero vector v, then multiplying v by A just multiplies it by the scalar λ (the eigenvalue). The vector "survives" the transformation unchanged in direction.

You already know how to find eigenvalues from the characteristic polynomial: solve det(A − λI) = 0. Each root λ is an eigenvalue. Once you have λ, you find its eigenvectors by solving (A − λI)v = 0 — that is, finding the null space of (A − λI). This null space is the eigenspace E_λ. It can be one-dimensional (a line of eigenvectors through the origin) or higher-dimensional if multiple independent vectors satisfy the equation.

Eigenvalues tell you how the matrix stretches along each eigendirection. A positive eigenvalue λ > 1 stretches; 0 < λ < 1 compresses; λ < 0 flips direction and scales; λ = 0 collapses the eigenvector to zero, which signals that A is singular. In applied settings — Google's PageRank, principal component analysis, quantum mechanics, and population dynamics — the largest eigenvalue and its eigenvector describe the dominant long-run behavior of a system under repeated matrix application.

One subtlety: eigenvalues are determined by the characteristic polynomial (so they are fixed properties of A), but eigenvectors are not unique. Any nonzero scalar multiple of an eigenvector is also an eigenvector with the same eigenvalue. The eigenspace captures the entire family. This is why we talk about eigenspaces rather than individual eigenvectors — the direction matters, not the specific vector.

Eigenvalues and eigenvectors unlock diagonalization: if A has n linearly independent eigenvectors, it can be written as A = PDP⁻¹ where D is diagonal with eigenvalues on the diagonal. This makes repeated matrix multiplication trivial (Aⁿ = PDⁿP⁻¹) and is the foundation for efficient algorithms in differential equations, Markov chains, and matrix exponentiation.
