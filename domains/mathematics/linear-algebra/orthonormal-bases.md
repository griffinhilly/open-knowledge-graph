---
id: orthonormal-bases
title: Orthonormal Bases
domain: mathematics
course: linear-algebra
prerequisites:
- id: orthogonality-in-linear-algebra
  type: hard
- id: basis-and-dimension
  type: hard
builds-toward:
- gram-schmidt-process
- spectral-theorem
tags:
- orthonormal
- ONB
- orthogonal matrix
- coordinates
- Fourier coefficients
stage: formal-systems
status: validated
---

# Orthonormal Bases

## Core Idea
An orthonormal basis (ONB) is a basis in which every vector has unit norm and every pair of distinct vectors is orthogonal. Orthonormal bases make coordinate computation trivial: the coordinate of a vector v with respect to basis vector uᵢ is simply ⟨v, uᵢ⟩. A matrix whose columns form an orthonormal basis is called an orthogonal matrix Q, satisfying QᵀQ = I (so Qᵀ = Q⁻¹). Orthogonal matrices preserve lengths and angles, making them the natural matrices for rotations and reflections. Orthonormal bases are the 'gold standard' basis choice in both theory and computation.

## How It's Best Learned
Verify that QᵀQ = I for rotation matrices and reflection matrices in R². Observe that computing coordinates in an orthonormal basis via dot products is far simpler than solving a linear system as required for non-orthogonal bases.

## Common Misconceptions
- An 'orthogonal matrix' has orthonormal columns, not merely orthogonal ones — the columns must also have unit length.
- Qᵀ = Q⁻¹ only when Q is a square orthogonal matrix; for a non-square matrix with orthonormal columns, QᵀQ = I but QQᵀ ≠ I.
- Students confuse orthogonal sets (merely pairwise perpendicular) with orthonormal bases (perpendicular AND unit length AND spanning).
