---
id: fourier-series-lp-theory
title: Fourier Series as Lᵖ Theory
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: bessel-parseval
  type: hard
- id: product-measures-fubini-theorem
  type: soft
tags:
- fourier-analysis
stage: advanced
status: draft
---

# Fourier Series as Lᵖ Theory

## Core Idea
Viewing L²([0, 2π]) as a Hilbert space with orthonormal basis {e^(inx)}, Fourier series are orthogonal projections. Convergence in L² is automatic by Parseval; pointwise convergence requires additional regularity of f.

## Explainer

From Bessel's inequality and Parseval's theorem, you already know that in a Hilbert space, the partial sums of an expansion in an orthonormal basis converge in norm to the original element. The key realization here is that L²([0, 2π]) equipped with the inner product ⟨f, g⟩ = (1/2π) ∫ f(x)g̅(x) dx is precisely such a Hilbert space, and the **complex exponentials** eₙ(x) = eⁱⁿˣ form a complete orthonormal system in it. Fourier series are nothing more than orthogonal projection onto successive terms of this basis.

The Fourier coefficient cₙ = ⟨f, eₙ⟩ = (1/2π) ∫ f(x) e⁻ⁱⁿˣ dx is exactly the projection of f onto the nth basis vector. Parseval's theorem, which you know, tells you that ∑|cₙ|² = ‖f‖² — the squared norm of f equals the sum of squared projections. In Hilbert space language, this is just the infinite-dimensional Pythagorean theorem. Completeness of the exponential system means the partial sums Sₙ(f) converge to f in the L² norm: ‖f − Sₙ(f)‖ → 0. This **L² convergence** is guaranteed for every f ∈ L²([0, 2π]) without additional hypotheses.

The subtlety arises when you ask about **pointwise convergence** — does Sₙ(f)(x) → f(x) for a fixed x? L² convergence says the integral of the squared error goes to zero; it says nothing about individual points. The difference matters because L² functions are equivalence classes: they are defined only up to modification on null sets, so "the value at x" is not even a well-defined concept in L². For pointwise convergence to hold, you need f to have additional smoothness or regularity — Hölder continuity, bounded variation, or similar conditions.

This distinction between L² convergence and pointwise convergence is one of the central lessons of functional analysis. L² is the "right" space for Fourier theory: the inner product structure makes Fourier coefficients natural projections, and completeness guarantees convergence in norm. But the Lᵖ framework also extends to other function spaces. For p ≠ 2, the spaces Lᵖ([0, 2π]) lack an inner product but retain a norm, and convergence of Fourier series in Lᵖ norm is a harder theorem — it holds for 1 < p < ∞ (by the Riesz-Fischer theorem and M. Riesz interpolation) but fails at the endpoints p = 1 and p = ∞. The Hilbert space structure of L² is what makes p = 2 so special and so natural for Fourier analysis.
