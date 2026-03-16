---
id: hilbert-spaces
title: Hilbert Spaces
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: inner-products
  type: hard
- id: banach-spaces
  type: hard
builds-toward:
- orthogonality-hilbert-spaces
tags:
- hilbert-spaces
stage: advanced
status: draft
---

# Hilbert Spaces

## Core Idea
A Hilbert space is a complete inner product space. The inner product induces a norm, and completeness ensures limits exist. L² spaces exemplify Hilbert spaces, which are fundamental in quantum mechanics and harmonic analysis.

## Explainer

You've already studied two structural properties of infinite-dimensional spaces separately: **inner products**, which give you a notion of angle, length, and orthogonality via ⟨u, v⟩; and **Banach spaces**, which are normed spaces where Cauchy sequences converge. A **Hilbert space** unifies both requirements: it is an inner product space whose inner product induces a norm ‖v‖ = √⟨v,v⟩, and in which that norm makes the space complete. Every Cauchy sequence converges to a limit that stays inside the space.

The necessity of completeness becomes vivid with Fourier series. You can approximate a function by taking finite sums of sines and cosines. Each partial sum is a legitimate element of your function space. But as you add more and more terms, the partial sums form a Cauchy sequence — they stabilize — and the limit is the function itself. Without completeness, that limit might not belong to your space, leaving infinite sums as meaningless operations. Hilbert spaces guarantee that these limit operations are safe: infinite superpositions always converge to an element that remains in the space.

The canonical example is **L²(Ω)**, the space of square-integrable functions on a domain Ω. The inner product is ⟨f, g⟩ = ∫_Ω f(x)g(x) dx, which induces the norm ‖f‖² = ∫_Ω |f(x)|² dx — a measure of the total "energy" of a function. L²(Ω) is a Hilbert space, and it is the natural arena for Fourier analysis: sinusoids form an orthonormal basis, every square-integrable function has a convergent Fourier expansion, and Parseval's theorem says the energy of a signal equals the sum of squared Fourier coefficients.

In quantum mechanics, the state of a physical system is a unit vector in a Hilbert space (typically L²(ℝ³)), observable quantities correspond to self-adjoint operators on this space, and the inner product encodes probability amplitudes. The abstract geometry you're studying — orthogonality, projections, basis expansions — governs physical reality at the microscopic scale. This is not a coincidence: the axioms of quantum mechanics were chosen precisely because Hilbert space geometry captures the probabilistic structure of measurement.
