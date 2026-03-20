---
id: orthonormal-bases-in-hilbert
title: Orthonormal Bases in Hilbert Spaces
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: riesz-representation-hilbert
  type: hard
builds-toward:
- bessel-inequality-parseval-identity
tags:
- hilbert-spaces
- orthonormal-bases
stage: advanced
status: draft
---

# Orthonormal Bases in Hilbert Spaces

## Core Idea
An orthonormal system {eᵢ}ᵢ∈ᴵ is orthonormal if ⟨eᵢ, eⱼ⟩ = δᵢⱼ. A maximal orthonormal system (orthonormal basis) has dense span in H. Every separable Hilbert space has a countable orthonormal basis.

## Explainer

From finite-dimensional linear algebra, you know the power of an orthonormal basis: every vector can be written as a linear combination of basis vectors, and the coefficients are simply inner products with each basis element. In a Hilbert space — which may be infinite-dimensional — this idea extends, but "basis" now means an infinite collection of vectors and "linear combination" becomes an infinite series that converges in the norm of H.

A set {eᵢ}ᵢ∈ᴵ is an **orthonormal system** if ⟨eᵢ, eⱼ⟩ = δᵢⱼ — each vector has unit length and any two distinct vectors are perpendicular. An orthonormal system is an **orthonormal basis** (or complete orthonormal system) when it is *maximal*: no unit vector exists in H that is perpendicular to every element of the set. Equivalently, the **span of {eᵢ} is dense in H** — every element of H can be approximated arbitrarily well by finite linear combinations of basis elements, even if it cannot be written as a *finite* combination.

The **expansion formula** f = Σᵢ ⟨f, eᵢ⟩ eᵢ holds for every f ∈ H, where the coefficients ĉᵢ = ⟨f, eᵢ⟩ are the **Fourier coefficients** of f with respect to the basis. This is identical in form to coordinate representations in ℝⁿ, except the sum is infinite and its convergence is in the H-norm (not pointwise). The Riesz representation theorem, which you've already studied, is the key tool that makes this work: it guarantees that every continuous linear functional on H is realized as an inner product, and that structure underlies why the basis expansion recovers f exactly.

The statement that every **separable** Hilbert space has a *countable* orthonormal basis is proven in two steps: existence of a maximal orthonormal set (via Zorn's lemma) and countability (from separability — the space has a countable dense subset, so the basis cannot be uncountably large). L²([0,1]) is separable because trigonometric polynomials with rational coefficients are dense; its countable orthonormal basis is the Fourier basis {1, cos(2πnx), sin(2πnx) : n = 1, 2, 3, ...}. This is why Fourier analysis works: the Fourier basis is literally an orthonormal basis for L², and the Fourier expansion is the basis representation.
