---
id: bessel-parseval
title: Bessel's Inequality and Parseval's Identity
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: riesz-representation-theorem-hilbert
  type: hard
- id: orthonormal-bases
  type: hard
builds-toward:
- fourier-series-lp-theory
tags:
- hilbert-spaces
stage: advanced
status: draft
---

# Bessel's Inequality and Parseval's Identity

## Core Idea
For an orthonormal sequence (eₙ), Bessel's inequality states Σ|⟨x, eₙ⟩|² ≤ ‖x‖². If the sequence is a complete orthonormal basis, Parseval's identity holds: Σ|⟨x, eₙ⟩|² = ‖x‖².

## Explainer

From orthonormal bases in finite-dimensional linear algebra, you know that if {u₁, ..., uₙ} is an ONB for ℝⁿ, then any vector v can be written as v = Σ⟨v, uᵢ⟩uᵢ and the Pythagorean theorem gives ‖v‖² = Σ|⟨v, uᵢ⟩|². Now suppose you're in a Hilbert space — an infinite-dimensional inner product space that is complete — and you have a countably infinite **orthonormal sequence** (eₙ). The **Fourier coefficients** ⟨x, eₙ⟩ measure how much of the vector x lies along each basis direction, just as in the finite case.

**Bessel's inequality** says that the sum of squared Fourier coefficients never exceeds ‖x‖²: Σ|⟨x, eₙ⟩|² ≤ ‖x‖². The proof is elegant: form the partial sum Sₙ = Σᵢ₌₁ⁿ ⟨x, eᵢ⟩eᵢ (the projection of x onto the span of the first n basis vectors) and use the Pythagorean theorem on the orthogonal decomposition x = Sₙ + (x − Sₙ). Since ‖x − Sₙ‖² ≥ 0, we get ‖x‖² = ‖Sₙ‖² + ‖x − Sₙ‖² ≥ ‖Sₙ‖² = Σᵢ₌₁ⁿ|⟨x, eᵢ⟩|². The inequality survives as n → ∞. Bessel says the orthonormal sequence captures *at most* all of the "energy" of x.

**Parseval's identity** is the equality case: Σ|⟨x, eₙ⟩|² = ‖x‖². This holds precisely when the orthonormal sequence is a **complete orthonormal basis** — one that spans a dense subspace, meaning every vector in the Hilbert space can be approximated arbitrarily well by finite linear combinations of the basis vectors. Completeness ensures the remainder ‖x − Sₙ‖ → 0 as n → ∞, so no energy is "left over." The Riesz representation theorem (your prerequisite) guarantees that the bounded linear functionals on a Hilbert space are exactly the inner products with fixed vectors, which is the machinery that makes this convergence rigorous.

The physical and applied interpretation is that of energy conservation. In signal processing, x is a signal, the eₙ are frequency components, and ⟨x, eₙ⟩ are the amplitudes. Parseval says the total energy computed in the time domain (‖x‖²) equals the total energy computed in the frequency domain (Σ|⟨x, eₙ⟩|²). This equality is the foundation of Fourier analysis: it is what lets you work with coefficients instead of functions, confident that no information is lost in the representation.
