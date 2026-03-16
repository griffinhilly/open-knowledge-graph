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

## Explainer

Every matrix represents a linear transformation — it takes vectors as input and produces new vectors as output, possibly rotating, stretching, or shearing them. Most vectors change direction when multiplied by a matrix. But certain special vectors only get *scaled* — they point in the same direction after the transformation (or exactly the opposite direction). These special vectors are **eigenvectors**, and the scale factor is the corresponding **eigenvalue**. The equation Av = λv captures this precisely: A transforms v, and the result is just v stretched or compressed by λ.

To build intuition, imagine a transformation that stretches space horizontally by a factor of 3 and vertically by a factor of 1 (leaves it unchanged). Any horizontal vector — pointing purely in the x-direction — just gets tripled: Av = 3v, so λ = 3. Any vertical vector is unchanged: Av = 1·v, so λ = 1. These horizontal and vertical directions are the eigenvectors, and 3 and 1 are the eigenvalues. For a more complex matrix, the eigenvectors may point in non-axis-aligned directions, but the idea is the same: they are the directions the transformation considers "pure scaling."

From your study of the characteristic polynomial, you know how to find eigenvalues: solve det(A − λI) = 0. This equation says "for what values of λ does A − λI fail to be invertible?" — equivalently, "for what λ does A − λI have a nontrivial kernel?" When λ is an eigenvalue, the **eigenspace** E_λ = ker(A − λI) is the set of all eigenvectors for that eigenvalue, together with the zero vector. It is always a subspace. Finding it is a null-space computation: row-reduce A − λI and describe the solution set.

The significance of eigenvalues and eigenvectors extends far beyond linear algebra. They are the backbone of matrix diagonalization: if a matrix has enough independent eigenvectors, you can change basis to a coordinate system where the matrix acts as pure scaling along each axis — far easier to compute with. They also appear in differential equations (the modes of a vibrating system are eigenfunctions of the differential operator), in statistics (principal components are eigenvectors of the covariance matrix), in graph theory (the spectrum of a graph's adjacency matrix encodes connectivity properties), and in quantum mechanics (observables have eigenstates). Mastering eigenvectors means gaining a tool that recurs throughout mathematics and its applications.
