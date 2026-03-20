---
id: orthogonality-and-projections
title: Orthogonality and Orthogonal Projections
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: hilbert-spaces-definition
  type: hard
builds-toward:
- riesz-representation-hilbert
- orthonormal-bases-in-hilbert
tags:
- hilbert-spaces
- projections
stage: advanced
status: draft
---

# Orthogonality and Orthogonal Projections

## Core Idea
Vectors x and y in a Hilbert space are orthogonal if ⟨x,y⟩ = 0. For a closed convex set K, there is a unique nearest point. Orthogonal projection onto a closed subspace M is the linear operator P_M: H → M projecting each x to the nearest point in M.

## Explainer

Your study of Hilbert spaces gave you a complete inner product space: a vector space equipped with ⟨·,·⟩ satisfying linearity, symmetry, and positive-definiteness, and complete with respect to the induced norm ||x|| = √⟨x,x⟩. The inner product does something coordinate geometry does not — it defines angles. Two vectors are **orthogonal** when ⟨x, y⟩ = 0, the algebraic condition capturing a 90-degree angle. In ℝ² this is familiar; the power of Hilbert space theory is that the same condition works for spaces of functions. Two functions f and g in L²[0,1] are orthogonal when ∫₀¹ f(x)g(x) dx = 0 — the integral of their product vanishes.

The **projection theorem** is the central result of this topic. Let M be a closed subspace of a Hilbert space H (closed meaning it contains its own limit points). For any x ∈ H, there is a unique element P_M x ∈ M that minimizes the distance ||x - m|| over all m ∈ M. This nearest point is the **orthogonal projection** of x onto M. The intuition from ℝ²: drop a perpendicular from a point to a line — where it lands is the closest point on the line, and the perpendicular segment is the error. This exact geometric picture generalizes without change to any Hilbert space, including infinite-dimensional ones.

The error vector x - P_M x is always orthogonal to M: ⟨x - P_M x, m⟩ = 0 for every m ∈ M. This **orthogonality condition** characterizes the projection uniquely, and it is often the most useful way to compute P_M x in practice. The projection operator P_M: H → H is linear, **idempotent** (P_M² = P_M — projecting twice is the same as projecting once), and **self-adjoint** (⟨P_M x, y⟩ = ⟨x, P_M y⟩). The idempotence expresses that once you're already in M, projection doesn't move you. Self-adjointness is the abstract version of the geometric symmetry of perpendicularity.

Orthogonal projections are the engine behind several major constructions. Least-squares solutions to overdetermined systems are projections of the target vector onto a column space. Fourier series decompose a function as a sum of projections onto subspaces spanned by sine and cosine functions — the coefficients are inner products precisely because projection onto a one-dimensional subspace spanned by a unit vector e is just ⟨x, e⟩e. The direct sum decomposition H = M ⊕ M⊥ — every element uniquely splits into a component in M and a component orthogonal to M — is the cornerstone of the Riesz representation theorem and the spectral theory of self-adjoint operators that lie ahead.
