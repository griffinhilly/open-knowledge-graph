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
stage: expert
status: validated
---

# Orthonormal Bases in Hilbert Spaces

## Core Idea
An orthonormal system {eᵢ}ᵢ∈ᴵ is orthonormal if ⟨eᵢ, eⱼ⟩ = δᵢⱼ. A maximal orthonormal system (orthonormal basis) has dense span in H. Every separable Hilbert space has a countable orthonormal basis.

## Questions

```yaml
- question: "A student claims: 'If {eᵢ} is an orthonormal basis for Hilbert space H, then every f ∈ H equals a finite sum Σᵢ₌₁ᴺ cᵢeᵢ for some N.' What is wrong with this?"
  type: multiple-choice
  options:
    - "The coefficients cᵢ are not computable in general, so the sum cannot be constructed"
    - "In infinite-dimensional Hilbert spaces, every f equals an INFINITE series Σᵢ cᵢeᵢ that converges in the H-norm — not necessarily a finite sum"
    - "The claim is correct for separable Hilbert spaces but fails for non-separable ones"
    - "f must be written as an integral, not a sum, because the basis may be uncountable"
  answer: 1
  explanation: "This is the key conceptual shift from finite to infinite dimensions. In ℝⁿ, every vector is an exact finite combination of basis vectors. In an infinite-dimensional Hilbert space, 'basis' means the span is DENSE — every vector can be approximated arbitrarily well by finite linear combinations, but the exact representation requires an infinite series converging in norm. The partial sums Σᵢ₌₁ᴺ ⟨f,eᵢ⟩eᵢ approach f in the norm as N → ∞, but no finite N suffices for most f."

- question: "Why does Fourier analysis work — that is, why can every square-integrable function on [0,1] be represented by its Fourier series?"
  type: multiple-choice
  options:
    - "Because the Weierstrass approximation theorem guarantees trigonometric polynomials approximate all continuous functions"
    - "Because the Fourier transform is an invertible operation on L² functions"
    - "Because every L² function can be recovered pointwise from its Fourier coefficients"
    - "Because the trigonometric functions {1, cos(2πnx), sin(2πnx)} form an orthonormal basis for L²([0,1]) — the Fourier expansion IS the basis expansion, with convergence in L² norm"
  answer: 3
  explanation: "Fourier analysis is not analogous to Hilbert space theory — it IS Hilbert space theory applied to L²([0,1]). The inner product ⟨f,g⟩ = ∫₀¹ f(x)g(x)dx makes L² a Hilbert space. The trig functions are orthonormal under this inner product and their span is dense in L², making them an orthonormal basis. The Fourier coefficient ĉₙ = ∫f(x)eₙ(x)dx is exactly ⟨f,eₙ⟩, and f = Σ ⟨f,eₙ⟩eₙ is the basis expansion formula. Convergence is in L² norm, not pointwise."

- question: "An orthonormal system {eᵢ} in a Hilbert space is an orthonormal basis if and mainly if its span equals H — most element of H can be written as a finite linear combination of the eᵢ."
  type: true-false
  answer: false
  explanation: "An orthonormal basis requires that the span is DENSE in H — every element can be approximated arbitrarily well by finite linear combinations, but not necessarily written as a finite combination exactly. 'Span equals H' is the finite-dimensional notion of basis. In infinite-dimensional spaces, the correct condition is density of the span (equivalently, maximality: no unit vector exists that is orthogonal to every element of the set). The expansion f = Σ⟨f,eᵢ⟩eᵢ is an infinite series converging in norm, not a finite sum."

- question: "In a separable Hilbert space, every orthonormal basis is countable."
  type: true-false
  answer: true
  explanation: "Separability means H has a countable dense subset. If the orthonormal basis were uncountable, then for any two distinct basis elements eᵢ, eⱼ, we have ‖eᵢ − eⱼ‖² = ‖eᵢ‖² − 2⟨eᵢ,eⱼ⟩ + ‖eⱼ‖² = 2. So the open balls of radius 1/√2 around each basis element are pairwise disjoint, and each must contain a point from the countable dense subset — requiring uncountably many such points. This contradicts countability. Hence the basis must be countable."

- question: "What is the relationship between Fourier series and orthonormal bases in Hilbert space theory — and why is this not merely an analogy?"
  type: short-answer
  answer: "The Fourier basis {1, cos(2πnx), sin(2πnx)} is literally an orthonormal basis for L²([0,1]) — the Hilbert space of square-integrable functions with inner product ⟨f,g⟩ = ∫f(x)g(x)dx. The trig functions are orthonormal under this inner product, and their span is dense in L² (L² is separable and this system is maximal). The Fourier expansion f = Σcₙeₙ with cₙ = ⟨f,eₙ⟩ is exactly the Hilbert space basis expansion formula. Convergence is in the L² norm. This is not an analogy — Fourier analysis is Hilbert space theory instantiated in L²."
  explanation: "Understanding this relationship clarifies both directions. Hilbert space theory explains WHY Fourier series converge (in L² norm) and represent L² functions exactly. And Fourier analysis is the motivating historical example that guided the development of the abstract theory. Parseval's identity ‖f‖² = Σ|cₙ|² is Bessel's equality for a complete orthonormal system."
```

## Explainer

From finite-dimensional linear algebra, you know the power of an orthonormal basis: every vector can be written as a linear combination of basis vectors, and the coefficients are simply inner products with each basis element. In a Hilbert space — which may be infinite-dimensional — this idea extends, but "basis" now means an infinite collection of vectors and "linear combination" becomes an infinite series that converges in the norm of H.

A set {eᵢ}ᵢ∈ᴵ is an **orthonormal system** if ⟨eᵢ, eⱼ⟩ = δᵢⱼ — each vector has unit length and any two distinct vectors are perpendicular. An orthonormal system is an **orthonormal basis** (or complete orthonormal system) when it is *maximal*: no unit vector exists in H that is perpendicular to every element of the set. Equivalently, the **span of {eᵢ} is dense in H** — every element of H can be approximated arbitrarily well by finite linear combinations of basis elements, even if it cannot be written as a *finite* combination.

The **expansion formula** f = Σᵢ ⟨f, eᵢ⟩ eᵢ holds for every f ∈ H, where the coefficients ĉᵢ = ⟨f, eᵢ⟩ are the **Fourier coefficients** of f with respect to the basis. This is identical in form to coordinate representations in ℝⁿ, except the sum is infinite and its convergence is in the H-norm (not pointwise). The Riesz representation theorem, which you've already studied, is the key tool that makes this work: it guarantees that every continuous linear functional on H is realized as an inner product, and that structure underlies why the basis expansion recovers f exactly.

The statement that every **separable** Hilbert space has a *countable* orthonormal basis is proven in two steps: existence of a maximal orthonormal set (via Zorn's lemma) and countability (from separability — the space has a countable dense subset, so the basis cannot be uncountably large). L²([0,1]) is separable because trigonometric polynomials with rational coefficients are dense; its countable orthonormal basis is the Fourier basis {1, cos(2πnx), sin(2πnx) : n = 1, 2, 3, ...}. This is why Fourier analysis works: the Fourier basis is literally an orthonormal basis for L², and the Fourier expansion is the basis representation.
