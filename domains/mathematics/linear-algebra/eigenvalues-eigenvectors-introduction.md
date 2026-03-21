---
id: eigenvalues-eigenvectors-introduction
title: Eigenvalues and Eigenvectors
domain: mathematics
course: linear-algebra
prerequisites:
- id: characteristic-polynomial
  type: hard
builds-toward:
- diagonalization-similar-matrices
- jordan-normal-form-intro
tags:
- eigenvalues
- eigenvectors
- spectral
stage: formal-systems
status: draft
---

# Eigenvalues and Eigenvectors

## Core Idea
For a square matrix A, an eigenvector is a nonzero vector v with Av = λv for some scalar λ (eigenvalue). Eigenvectors point in directions unchanged by A (only scaled). Eigenvalues are roots of det(A − λI) = 0. Eigenspaces E_λ = ker(A − λI) are subspaces of eigenvectors for each λ. Real matrices may have complex eigenvalues.

## Questions

```yaml
- question: "Which of the following best describes what makes a vector an eigenvector of matrix A?"
  type: multiple-choice
  options:
    - "Its length becomes 1 after multiplication by A"
    - "It points in the same or exactly opposite direction after multiplication by A — it is only scaled, not rotated"
    - "It is orthogonal to every other vector in the space"
    - "It lies in the null space of A, so Av = 0"
  answer: 1
  explanation: "An eigenvector v satisfies Av = λv: multiplying by A scales v by λ but does not change its direction (unless λ < 0, in which case it reverses direction — still a 'scaling'). Option D describes the special case λ = 0, which is a valid eigenvalue but not the general definition. Options A and C describe unrelated geometric properties."

- question: "A matrix A has eigenvalue λ = 0. What does this necessarily imply?"
  type: multiple-choice
  options:
    - "The matrix has no eigenvectors for any eigenvalue"
    - "Every nonzero vector is an eigenvector of A"
    - "The matrix is singular — it has no inverse"
    - "The matrix is the zero matrix"
  answer: 2
  explanation: "If λ = 0 is an eigenvalue, then Av = 0v = 0 for some nonzero v, meaning v is in the null space of A. A matrix with a nontrivial null space is not invertible (singular). This is exactly the condition det(A) = 0, which follows from 0 being a root of det(A − λI) = 0. Options A and B are incorrect; option D is a sufficient but not necessary condition."

- question: "For a given eigenvalue λ, the eigenspace E_λ = ker(A − λI) contains exactly one eigenvector."
  type: true-false
  answer: false
  explanation: "The eigenspace is a subspace, not a single vector. If v is an eigenvector with eigenvalue λ, then so is cv for any nonzero scalar c: A(cv) = cAv = c(λv) = λ(cv). The eigenspace always contains infinitely many eigenvectors (every nonzero vector in the subspace), and may be higher-dimensional if multiple independent eigenvectors share the same eigenvalue. 'The' eigenvector for a given eigenvalue is a common misconception."

- question: "The eigenvectors of a matrix point in directions that are only scaled — not rotated — by the linear transformation."
  type: true-false
  answer: true
  explanation: "This is the defining geometric property of eigenvectors. While most input vectors change direction under a matrix transformation, eigenvectors are special precisely because they maintain their line of action — the transformation only stretches or compresses them by the factor λ (or reverses them if λ < 0). This is why eigenvectors reveal the 'natural axes' of a transformation."

- question: "Why are eigenvalues found by solving det(A − λI) = 0 rather than directly from Av = λv?"
  type: short-answer
  answer: "The equation Av = λv can be rewritten as (A − λI)v = 0. This system has a nonzero solution v only when A − λI fails to be invertible — i.e., when det(A − λI) = 0. If A − λI were invertible, the only solution would be v = 0, which is excluded by definition. So the characteristic equation det(A − λI) = 0 is the condition for eigenvalues to exist, and solving it for λ gives all possible eigenvalues before any eigenvectors are computed."
  explanation: "This connects the definition to the algorithm. You can't solve for v directly without knowing λ, and you can't know λ without first finding when the system has nontrivial solutions. The determinant condition is the bridge: it tells you which values of λ make the system underdetermined (with infinitely many solutions), which are exactly the eigenvalues. Once λ is known, you row-reduce A − λI to find the eigenvectors."
```

## Explainer

Every matrix represents a linear transformation — it takes vectors as input and produces new vectors as output, possibly rotating, stretching, or shearing them. Most vectors change direction when multiplied by a matrix. But certain special vectors only get *scaled* — they point in the same direction after the transformation (or exactly the opposite direction). These special vectors are **eigenvectors**, and the scale factor is the corresponding **eigenvalue**. The equation Av = λv captures this precisely: A transforms v, and the result is just v stretched or compressed by λ.

To build intuition, imagine a transformation that stretches space horizontally by a factor of 3 and vertically by a factor of 1 (leaves it unchanged). Any horizontal vector — pointing purely in the x-direction — just gets tripled: Av = 3v, so λ = 3. Any vertical vector is unchanged: Av = 1·v, so λ = 1. These horizontal and vertical directions are the eigenvectors, and 3 and 1 are the eigenvalues. For a more complex matrix, the eigenvectors may point in non-axis-aligned directions, but the idea is the same: they are the directions the transformation considers "pure scaling."

From your study of the characteristic polynomial, you know how to find eigenvalues: solve det(A − λI) = 0. This equation says "for what values of λ does A − λI fail to be invertible?" — equivalently, "for what λ does A − λI have a nontrivial kernel?" When λ is an eigenvalue, the **eigenspace** E_λ = ker(A − λI) is the set of all eigenvectors for that eigenvalue, together with the zero vector. It is always a subspace. Finding it is a null-space computation: row-reduce A − λI and describe the solution set.

The significance of eigenvalues and eigenvectors extends far beyond linear algebra. They are the backbone of matrix diagonalization: if a matrix has enough independent eigenvectors, you can change basis to a coordinate system where the matrix acts as pure scaling along each axis — far easier to compute with. They also appear in differential equations (the modes of a vibrating system are eigenfunctions of the differential operator), in statistics (principal components are eigenvectors of the covariance matrix), in graph theory (the spectrum of a graph's adjacency matrix encodes connectivity properties), and in quantum mechanics (observables have eigenstates). Mastering eigenvectors means gaining a tool that recurs throughout mathematics and its applications.
