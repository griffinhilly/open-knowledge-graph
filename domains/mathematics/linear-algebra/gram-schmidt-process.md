---
id: gram-schmidt-process
title: The Gram-Schmidt Process
domain: mathematics
course: linear-algebra
prerequisites:
- id: orthonormal-bases
  type: hard
- id: linear-independence
  type: hard
builds-toward:
- orthogonal-projections
tags:
- Gram-Schmidt
- orthogonalization
- QR decomposition
- projection
- algorithm
stage: formal-systems
status: draft
---

# The Gram-Schmidt Process

## Core Idea
The Gram-Schmidt process converts any linearly independent set {v₁, v₂, …, vₖ} into an orthonormal set {u₁, u₂, …, uₖ} that spans the same subspace. Each step subtracts from vⱼ its projections onto all previously constructed orthonormal vectors, leaving a residual orthogonal to all previous uᵢ; normalizing the residual yields uⱼ. This process underlies the QR decomposition, where A = QR and Q has orthonormal columns. Gram-Schmidt guarantees that every finite-dimensional subspace has an orthonormal basis.

## How It's Best Learned
Work through the 3D case on a specific independent set, drawing each projection step geometrically. Then verify orthogonality of the result with dot products. Recognize that numerical implementations use a modified Gram-Schmidt for stability.

## Common Misconceptions
- Each step requires projecting onto ALL previously found orthonormal vectors, not just the most recent one.
- Gram-Schmidt fails if the input vectors are linearly dependent — one step will produce a zero vector that cannot be normalized.
- The process produces vectors spanning the same subspace as the input, not a larger or different subspace.
