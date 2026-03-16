---
id: matrix-norms-conditioning
title: Matrix Norms and Condition Numbers
domain: mathematics
course: linear-algebra
prerequisites:
- id: singular-value-decomposition
  type: hard
- id: vector-norms
  type: hard
builds-toward:
- iterative-methods-linear-systems
tags:
- matrix-norms
- conditioning
- numerical-stability
stage: formal-systems
status: draft
---

# Matrix Norms and Condition Numbers

## Core Idea
Matrix norms measure matrix size; common ones are the operator norm ||A||₂ = σ_max(A), Frobenius norm ||A||_F = √(Σᵢⱼ Aᵢⱼ²), and max norm ||A||_∞. The condition number κ(A) = ||A|| ||A⁻¹|| quantifies sensitivity of Ax = b to perturbations: small relative errors in b lead to large relative errors in x when κ is large. κ = σ_max/σ_min for SVD.

## Explainer

You already know that a **vector norm** measures the size of a vector — it gives you a single number capturing how "big" a vector is. A **matrix norm** extends this idea to linear transformations. The most geometrically meaningful one is the **operator norm** (or spectral norm), ||A||₂, which asks: over all unit vectors u, what is the largest ||Au|| can be? In other words, what is the maximum factor by which the matrix stretches any input? From your study of the SVD, you know this answer immediately — it is σ_max, the largest singular value. The matrix is at most that many times bigger than any input it acts on.

The **Frobenius norm** takes a different approach: it treats the matrix as a long vector of all its entries and computes the ordinary Euclidean length. It is computationally simpler and appears often in optimization and statistics, but it does not have a clean geometric interpretation as "maximum stretch." The connection to the SVD is still elegant: ||A||_F = √(σ₁² + σ₂² + ··· + σₙ²), the square root of the sum of squared singular values.

Now for the central concept: the **condition number** κ(A) = ||A|| · ||A⁻¹||. To understand what it measures, consider solving Ax = b. Suppose b is perturbed slightly — say by measurement noise — giving you b̃ = b + δb. The solution shifts to x̃ = A⁻¹b̃. How large can the relative error ||δx||/||x|| be relative to the relative perturbation ||δb||/||b||? The answer is bounded by κ(A). A condition number of 10 means errors in b can be amplified by at most a factor of 10. A condition number of 10⁸ means tiny relative errors in b can become enormous relative errors in x — the system is numerically **ill-conditioned**.

Using the SVD, the condition number has a beautiful form: κ₂(A) = σ_max/σ_min. Think about what this means geometrically. The SVD shows that A stretches space by σ_max in one direction and σ_min in another. A⁻¹ must "undo" those stretches, so it compresses by σ_max and stretches by 1/σ_min. A matrix with very unequal singular values — one enormous direction and one nearly-zero direction — has a huge condition number. Geometrically, this means the matrix nearly collapses space in some direction; recovering the original vector from the output requires extreme amplification, making the problem numerically fragile. When σ_min is nearly zero, the matrix is nearly singular and κ → ∞.
