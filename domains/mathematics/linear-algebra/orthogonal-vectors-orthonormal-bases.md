---
id: orthogonal-vectors-orthonormal-bases
title: Orthogonal Vectors and Orthonormal Bases
domain: mathematics
course: linear-algebra
prerequisites:
- id: inner-product-spaces
  type: hard
- id: basis-definition
  type: hard
builds-toward:
- gram-schmidt-process
tags:
- orthogonal
- orthonormal
- bases
stage: formal-systems
status: draft
---

# Orthogonal Vectors and Orthonormal Bases

## Core Idea
Vectors u and v are orthogonal if ⟨u, v⟩ = 0. An orthonormal set has pairwise orthogonal unit vectors. An orthonormal basis enables simple coordinates: v = Σ⟨v, e_i⟩e_i. Orthonormal bases are numerically stable and reveal structure clearly.

## Explainer

The inner product you already know measures geometric alignment: ⟨u, v⟩ = ‖u‖‖v‖cosθ. Two vectors are **orthogonal** when ⟨u, v⟩ = 0 — they point in completely independent directions, sharing nothing. Think of the standard x- and y-axes: how far east you travel tells you nothing about how far north you've gone. Orthogonality formalizes this geometric independence in any inner product space.

An **orthonormal set** adds the requirement that each vector has length 1: ⟨eᵢ, eᵢ⟩ = 1, and ⟨eᵢ, eⱼ⟩ = 0 for i ≠ j. The standard basis {e₁, e₂, e₃} of R³ is the canonical example — three unit vectors along the coordinate axes, perfectly perpendicular to each other. But orthonormal sets appear in every inner product space, including spaces of functions where ⟨f, g⟩ = ∫f(x)g(x)dx.

The power of an orthonormal basis is the coordinate formula it enables. With a general basis, finding the coordinates of a vector v requires solving a system of equations — a potentially messy computation where the basis vectors' mutual interactions must be disentangled. With an orthonormal basis {e₁, ..., eₙ}, this collapses entirely: v = Σ⟨v, eᵢ⟩eᵢ. Each coefficient ⟨v, eᵢ⟩ is simply the projection of v onto eᵢ — one dot product, readable directly. You can compute each component independently, without the others interfering.

This independence is the structural advantage orthonormal bases provide throughout linear algebra and analysis. Errors in one component do not propagate to others (numerical stability). Each coefficient has a direct geometric meaning as the "amount of v in the eᵢ direction." When you study the Gram-Schmidt process next, you will learn to *construct* an orthonormal basis from any linearly independent set — transforming a messy basis into a clean one by systematically removing the components each new vector shares with the previous ones.
