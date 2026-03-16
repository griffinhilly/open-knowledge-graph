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

## Explainer

From your work on orthogonality and bases, you know two ideas separately: vectors can be perpendicular to each other (orthogonality), and a basis is a linearly independent spanning set. An **orthonormal basis** (ONB) combines both properties at once and adds a normalization condition: every basis vector has length exactly 1, and every pair of distinct basis vectors is perpendicular. The standard basis {e₁, e₂, e₃} in ℝ³ is the simplest example — unit vectors along each axis, mutually perpendicular.

The great computational payoff of an ONB is coordinate extraction via inner products. Recall that with a general basis, finding coordinates requires solving a linear system. With an ONB {u₁, u₂, ..., uₙ}, the coordinate of any vector v with respect to uᵢ is simply the inner product ⟨v, uᵢ⟩. No system-solving required — just n dot products. This works because orthogonality eliminates all cross-terms: when you expand v in the basis and take the inner product with uᵢ, every term involving a different basis vector drops to zero. The formula v = ⟨v, u₁⟩u₁ + ⟨v, u₂⟩u₂ + ... + ⟨v, uₙ⟩uₙ is one of the most useful formulas in linear algebra.

When the column vectors of a square matrix Q form an ONB, something remarkable happens: QᵀQ = I, so Qᵀ = Q⁻¹. This means you can invert Q just by transposing it — no row reduction needed. Such matrices are called **orthogonal matrices**. Geometrically, they represent transformations that preserve lengths and angles: ‖Qv‖ = ‖v‖ and ⟨Qu, Qv⟩ = ⟨u, v⟩. Every rotation and reflection is an orthogonal matrix. This length-preservation property is what makes orthogonal matrices the natural choice for representing rigid motions and for numerically stable computations.

The standard basis is one ONB, but there are infinitely many others. Any rotation of the standard basis produces another ONB. This flexibility is central to applications: in Fourier analysis, the sines and cosines form an ONB for function spaces; in data analysis (PCA), you find an ONB aligned with the directions of maximum variance. The Gram-Schmidt process (your next topic) provides the algorithm for constructing an ONB from any linearly independent set. Once you have it, coordinates become dot products, inverses become transposes, and the geometry of the space becomes transparent.
