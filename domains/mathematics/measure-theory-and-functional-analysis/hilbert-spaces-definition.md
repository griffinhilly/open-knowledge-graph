---
id: hilbert-spaces-definition
title: 'Hilbert Spaces: Definition and Examples'
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: banach-spaces-definition
  type: hard
- id: inner-products
  type: hard
builds-toward:
- orthogonality-and-projections
tags:
- hilbert-spaces
- functional-analysis
stage: advanced
status: draft
---

# Hilbert Spaces: Definition and Examples

## Core Idea
A Hilbert space is a complete normed vector space whose norm comes from an inner product: ‖x‖ = √⟨x,x⟩. Examples include L², ℓ², and ℝⁿ. The inner product structure enables orthogonality and powerful representation theorems.

## Explainer

You already know what a **Banach space** is: a vector space equipped with a norm, where every Cauchy sequence converges — completeness prevents gaps in the space. And you know what an **inner product** is: a function ⟨·,·⟩ that takes two vectors and returns a scalar, satisfying linearity, symmetry, and positive-definiteness. A Hilbert space is the marriage of these two structures: a Banach space whose norm is derived from an inner product via ‖x‖ = √⟨x,x⟩. Not every Banach space has this property — the inner product requirement is an additional constraint that adds rich geometric structure.

The geometric gain is orthogonality. In ℝ² with the standard dot product, you can ask whether two vectors are perpendicular. In a Hilbert space, you can ask the same question about any two elements, even if they are functions rather than finite-dimensional vectors. This is what distinguishes Hilbert spaces from general Banach spaces: the inner product gives you angles, not just distances. The norm tells you how large something is; the inner product tells you how aligned two things are.

The canonical examples cover three regimes of dimension. **ℝⁿ** with the dot product ⟨x,y⟩ = Σxᵢyᵢ is the finite-dimensional case — every student of linear algebra has worked in a Hilbert space. **ℓ²** is the space of infinite sequences (x₁, x₂, x₃, ...) with Σxᵢ² < ∞, with inner product ⟨x,y⟩ = Σxᵢyᵢ; completeness is non-trivial here and must be verified. **L²[a,b]** is the space of square-integrable functions on an interval, with ⟨f,g⟩ = ∫f(x)g(x)dx; this is where Fourier analysis lives, turning a function into a "sum of orthogonal components" just as a vector decomposes along orthogonal axes.

The completeness condition is what makes Hilbert spaces analytically tractable. It guarantees that orthogonal series (like Fourier series) converge within the space, and it underpins the powerful theorems to come — the projection theorem, the Riesz representation theorem, and the existence of orthonormal bases in infinite dimensions. A space without completeness might have orthogonal sequences whose sums drift toward elements that are not in the space, breaking the theory. Hilbert spaces avoid this failure, which is why they are the natural setting for quantum mechanics, signal processing, and much of modern analysis.
