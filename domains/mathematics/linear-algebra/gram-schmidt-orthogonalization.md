---
id: gram-schmidt-orthogonalization
title: Gram-Schmidt Process and QR Decomposition
domain: mathematics
course: linear-algebra
prerequisites:
- id: orthogonality-and-orthonormal-sets
  type: hard
builds-toward:
- orthogonal-projections-least-squares
- least-squares-approximation
tags:
- gram-schmidt
- orthogonalization
- qr-decomposition
stage: formal-systems
status: draft
---

# Gram-Schmidt Process and QR Decomposition

## Core Idea
The Gram-Schmidt process converts a linearly independent set {v₁, ..., vₖ} into an orthonormal set by iteratively projecting out previously computed directions. It produces vectors u₁, u₂, ... where uᵢ is perpendicular to all u₁, ..., uᵢ₋₁. QR decomposition writes A = QR where Q has orthonormal columns and R is upper triangular, computed via Gram-Schmidt. This is numerically superior to solving normal equations.

## Explainer

From your prerequisite on orthogonality, you know that an **orthonormal set** of vectors is one where every vector has unit length and every pair of distinct vectors is perpendicular. Working in an orthonormal basis is computationally ideal: projections become dot products, and coordinates are computed without solving any systems. The Gram-Schmidt process answers the question: given any linearly independent set of vectors, how do you replace them with an orthonormal set that spans the same space?

The core idea is **iterative projection and subtraction**. Start with v₁: normalize it to get u₁ = v₁/‖v₁‖. Now take v₂: it has some component in the direction of u₁ and some component perpendicular to u₁. The component in the u₁ direction is (v₂ · u₁)u₁ — the projection of v₂ onto u₁. Subtract this out: v₂ − (v₂ · u₁)u₁ is the part of v₂ that is perpendicular to u₁. Normalize this residual to get u₂. Now u₁ and u₂ are orthonormal and span the same plane as v₁ and v₂. For v₃, subtract its projections onto both u₁ and u₂, leaving the component perpendicular to both, then normalize. Each step "peels off" the contributions of previously computed directions, leaving a new direction orthogonal to all of them. The order matters — you process the original vectors in sequence, and each new orthonormal vector is built from the residual after removing all earlier influences.

The process produces a set {u₁, ..., uₖ} where span{u₁, ..., uᵢ} = span{v₁, ..., vᵢ} at every step — the orthonormal basis agrees with the original basis at each prefix. This is the key structural property: you're not just finding any orthonormal basis for the whole space; you're finding one that progressively refines through the same subspaces as the original vectors. This structure is exactly what **QR decomposition** captures. If A is a matrix whose columns are v₁, ..., vₖ, then Gram-Schmidt produces Q (columns are u₁, ..., uₖ — orthonormal) and R (upper triangular — encodes how each vᵢ decomposes in terms of the u₁, ..., uᵢ directions). The entry Rᵢⱼ records the projection coefficient of vⱼ onto uᵢ, which is why R is upper triangular: when processing vⱼ, you only subtract projections onto u₁, ..., uⱼ₋₁.

QR decomposition is numerically preferred over the **normal equations** approach to least squares (Aᵀ A x = Aᵀ b) because forming Aᵀ A squares the condition number of A — it amplifies numerical errors. Solving via QR avoids squaring the condition number and is more stable when columns of A are nearly linearly dependent. This is why most numerical libraries (NumPy, LAPACK) use QR-based algorithms rather than normal equations for least-squares problems. The Gram-Schmidt process is the conceptual foundation, but in practice **modified Gram-Schmidt** or **Householder reflections** are used instead, because they maintain orthogonality more reliably under floating-point arithmetic — small rounding errors in classical Gram-Schmidt accumulate and make the resulting vectors gradually lose their perpendicularity.
