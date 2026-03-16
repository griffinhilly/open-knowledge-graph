---
id: orthogonality-and-orthonormal-sets
title: Orthogonality and Orthonormal Bases
domain: mathematics
course: linear-algebra
prerequisites:
- id: inner-product-spaces
  type: hard
builds-toward:
- gram-schmidt-orthogonalization
- orthogonal-projections-least-squares
- spectral-theorem-symmetric
tags:
- orthogonality
- orthonormal
- orthogonal-sets
stage: formal-systems
status: draft
---

# Orthogonality and Orthonormal Bases

## Core Idea
Vectors u and v are orthogonal if ⟨u,v⟩ = 0. An orthogonal set is pairwise orthogonal; an orthonormal set has unit vectors. Orthonormal bases are powerful: coordinates are computed easily ([v]_B = [⟨v,b₁⟩, ..., ⟨v,bₙ⟩]), and the matrix of an orthonormal basis has orthogonal columns.

## Explainer

From your work with inner product spaces, you know that the inner product ⟨u, v⟩ captures a notion of "alignment" between vectors. When ⟨u, v⟩ = 0, two vectors are perfectly non-aligned — knowing the component of a vector along u tells you nothing about its component along v. This is **orthogonality**, and it is the multidimensional generalization of perpendicularity. In ℝ² with the dot product, u ⊥ v exactly when the angle between them is 90°. In abstract inner product spaces the same algebraic condition holds, even when geometry is less visual.

An **orthogonal set** is a collection of vectors that are pairwise orthogonal: every pair has zero inner product. An **orthonormal set** goes one step further — each vector additionally has unit length (‖v‖ = 1). The standard basis {e₁, e₂, e₃} in ℝ³ is the canonical example: dot any two distinct basis vectors and you get 0; each has length 1. The power of orthonormality lies in what it does for coordinates. For any orthonormal basis {b₁, …, bₙ}, the coordinate of a vector v in direction bᵢ is simply ⟨v, bᵢ⟩ — a projection onto that basis vector. This makes decomposing a vector into components effortless: no matrix inversion, no system of equations, just inner products.

This coordinate formula has a striking consequence. If you assemble the basis vectors as columns of a matrix Q, then Qᵀ = Q⁻¹. Such a matrix is called **orthogonal** (somewhat confusingly, even though the columns are orthonormal). Orthogonal matrices preserve lengths and angles under multiplication: ‖Qv‖ = ‖v‖ and ⟨Qu, Qv⟩ = ⟨u, v⟩. Geometrically, they represent rotations and reflections — rigid motions that don't distort the space.

The deeper reason orthonormal bases matter is that they decouple directions. In an arbitrary basis, changing one coordinate might require adjustments to others to maintain consistency. In an orthonormal basis, each direction is completely independent of the others. This decoupling makes orthonormal bases indispensable in projection problems, least-squares fitting, spectral decompositions, and Fourier analysis — all of which reduce complex multidimensional problems to independent one-dimensional calculations along each basis direction.
