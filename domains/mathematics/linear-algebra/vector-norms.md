---
id: vector-norms
title: Vector Norms and Magnitude
domain: mathematics
course: linear-algebra
prerequisites:
- id: vectors-in-rn-operations
  type: hard
- id: square-roots-intro
  type: hard
builds-toward:
- dot-product
- orthogonality-and-orthonormal-sets
- matrix-norms
tags:
- vectors
- norms
- magnitude
- distance
stage: formal-systems
status: draft
---

# Vector Norms and Magnitude

## Core Idea
The norm (or magnitude) of a vector is a real number measuring its length, computed as ||v|| = √(v₁² + v₂² + ... + vₙ²). Norms generalize distance to n-dimensional space and satisfy key properties: ||cv|| = |c| ||v|| and the triangle inequality. Unit vectors (norm 1) form the basis for orthonormal sets.

## How It's Best Learned
Start with 2D and 3D visualization of distance formula. Then extend algebraically to R^n. Normalize vectors by dividing by their norm to create unit vectors in the same direction.

## Explainer

You already know how to work with vectors in ℝⁿ — adding them, scaling them, working with their components. The **norm** gives you the one thing that's been missing: a way to measure how *long* a vector is. In ℝ² and ℝ³ you've likely seen this as the distance formula from the origin: if v = (3, 4), its length is √(3² + 4²) = √25 = 5. The norm simply extends this to any number of dimensions: for v = (v₁, v₂, ..., vₙ), we define **||v|| = √(v₁² + v₂² + ... + vₙ²)**. This is called the Euclidean norm or L2 norm.

The norm satisfies three properties that any reasonable notion of "length" should have. First, ||v|| ≥ 0, with equality only when v is the zero vector — a nonzero displacement always has positive length. Second, scaling: **||cv|| = |c| ||v||**, so doubling a vector doubles its length and negating it doesn't change the length (the absolute value of the scalar is what matters, not its sign). Third, the **triangle inequality**: ||u + v|| ≤ ||u|| + ||v||. This is the geometric fact that the straight-line path is never longer than the two-leg detour — a constraint that turns out to be essential in more abstract settings.

One immediate application is **normalization**: given any nonzero vector v, the vector v/||v|| has norm 1 and points in exactly the same direction as v. This is called a **unit vector**. Unit vectors let you separate "direction" from "magnitude" — useful whenever you care about orientation without caring about scale (as in defining orthonormal bases). The standard basis vectors e₁ = (1, 0, ..., 0), e₂ = (0, 1, ..., 0), and so on are the canonical unit vectors in ℝⁿ.

The norm also gives you distance between two vectors: d(u, v) = ||u − v||, the length of the displacement vector from v to u. This distance formula underpins nearest-neighbor algorithms, error measurements in least squares, and convergence criteria throughout analysis. When you move to inner product spaces and orthogonality, you'll see that the Euclidean norm is derived from the dot product via ||v|| = √(v · v) — so norms and inner products are tightly linked.
