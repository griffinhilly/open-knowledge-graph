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
stage: expert
status: validated
---

# Fourier Series as Lᵖ Theory

## Core Idea
Viewing L²([0, 2π]) as a Hilbert space with orthonormal basis {e^(inx)}, Fourier series are orthogonal projections. Convergence in L² is automatic by Parseval; pointwise convergence requires additional regularity of f.

## Questions

```yaml
- question: "A student proves that Fourier partial sums Sₙ(f) satisfy ‖f − Sₙ(f)‖₂ → 0 for some f ∈ L²([0, 2π]), then concludes Sₙ(f)(x) → f(x) for every x. What is wrong with this conclusion?"
  type: multiple-choice
  options:
    - "L² convergence of Fourier series is not actually guaranteed for all f ∈ L²; the student's premise is false"
    - "L² convergence means the integral of squared error goes to zero — it says nothing about behavior at individual points; pointwise convergence requires additional smoothness or regularity of f"
    - "Pointwise convergence is weaker than L² convergence, so it would follow automatically if the student's claim were about almost every x"
    - "The conclusion is valid for continuous functions but the student should have verified continuity of f first"
  answer: 1
  explanation: "L² convergence (norm convergence) and pointwise convergence are fundamentally different modes of convergence. A sequence can converge in L² while diverging pointwise at specific x-values — the 'typewriter sequence' of sliding indicator functions is the canonical example. Moreover, L² functions are equivalence classes: they are defined only up to modification on measure-zero sets, so 'the value of f at x' isn't even well-defined as a concept in L². Pointwise convergence requires f to have additional regularity — Hölder continuity, bounded variation, or similar conditions."

- question: "Why is L²([0, 2π]) considered the 'right' space for Fourier analysis compared to L¹([0, 2π])?"
  type: multiple-choice
  options:
    - "L¹ functions cannot be integrated on [0, 2π], making Fourier coefficients undefined in L¹"
    - "L² has an inner product structure that makes Fourier coefficients orthogonal projections and guarantees norm convergence; L¹ lacks an inner product and Fourier series can fail to converge in L¹ norm"
    - "L² contains strictly more functions than L¹ on [0, 2π], making it the more general and powerful space"
    - "Fourier series converge pointwise for L² functions but not for L¹ functions"
  answer: 1
  explanation: "The inner product ⟨f, g⟩ = (1/2π)∫fg̅dx on L² makes the complex exponentials {eⁱⁿˣ} an orthonormal basis, and the Fourier coefficient cₙ = ⟨f, eₙ⟩ is exactly the orthogonal projection of f onto eₙ. Parseval's theorem then says ∑|cₙ|² = ‖f‖² — the infinite-dimensional Pythagorean theorem — and completeness of the system guarantees L² convergence for all f ∈ L². L¹ lacks an inner product, so there's no natural notion of 'projection,' and Fourier series can fail to converge in L¹ norm. The Hilbert space structure of L² is what makes p = 2 so special."

- question: "If f ∈ L²([0, 2π]) and ‖f − Sₙ(f)‖₂ → 0, then the Fourier partial sums Sₙ(f)(x) converge to f(x) for nearly every x ∈ [0, 2π]."
  type: true-false
  answer: false
  explanation: "L² norm convergence does not imply pointwise convergence at every x. L² functions are equivalence classes (defined up to sets of measure zero), so 'the value at x' isn't even well-defined. Pointwise convergence is a separate question that requires f to have additional regularity. Without further hypotheses, you can only conclude that the approximation is good 'on average' in the L² sense — the squared error integrates to zero — but the series may misbehave at particular points."

- question: "In L²([0, 2π]), the Fourier coefficient cₙ = (1/2π) ∫f(x)e⁻ⁱⁿˣ dx is the inner product of f with the nth basis element eₙ(x) = eⁱⁿˣ, and equals the orthogonal projection of f onto that basis direction."
  type: true-false
  answer: true
  explanation: "With the standard inner product ⟨f, g⟩ = (1/2π)∫fg̅ dx on L², we have ⟨f, eₙ⟩ = (1/2π)∫f(x)e⁻ⁱⁿˣ dx = cₙ exactly. This is the projection formula for orthonormal bases in Hilbert spaces. Parseval's theorem — ∑|cₙ|² = ‖f‖² — is then the infinite-dimensional Pythagorean theorem: the squared norm of f equals the sum of squared magnitudes of its projections. The entire Fourier theory in L² is just Hilbert space geometry applied to a concrete function space."

- question: "Why does the Hilbert space structure of L² make Fourier series natural, and what does Parseval's theorem say in abstract Hilbert space terms?"
  type: short-answer
  answer: "L²([0, 2π]) with inner product ⟨f, g⟩ = (1/2π)∫fg̅ dx is a Hilbert space in which the complex exponentials {eⁱⁿˣ} form a complete orthonormal system. A Fourier coefficient cₙ = ⟨f, eₙ⟩ is the coordinate of f in the eₙ direction — the amount of f lying in that basis direction. Parseval's theorem is the infinite-dimensional Pythagorean theorem: ∑|cₙ|² = ‖f‖². This says the squared norm of f equals the sum of squared coordinates, exactly as in finite-dimensional Euclidean space. Completeness of the system then guarantees that the partial sums Sₙ(f) converge to f in L² norm — recovering f from its coordinates — with no additional hypotheses on f beyond f ∈ L²."
  explanation: "The key payoff of the Hilbert space perspective is that it makes Fourier theory a special case of a completely general abstract result. Any Hilbert space with a complete orthonormal basis has the same properties: projections give coordinates, Parseval holds, and the series converges in norm. L² is special only in being the concrete function space where this abstract structure naturally lives for Fourier analysis. This perspective also immediately explains why p = 2 is special — the inner product is a p = 2 feature with no analogue for other values of p."
```

## Explainer

From Bessel's inequality and Parseval's theorem, you already know that in a Hilbert space, the partial sums of an expansion in an orthonormal basis converge in norm to the original element. The key realization here is that L²([0, 2π]) equipped with the inner product ⟨f, g⟩ = (1/2π) ∫ f(x)g̅(x) dx is precisely such a Hilbert space, and the **complex exponentials** eₙ(x) = eⁱⁿˣ form a complete orthonormal system in it. Fourier series are nothing more than orthogonal projection onto successive terms of this basis.

The Fourier coefficient cₙ = ⟨f, eₙ⟩ = (1/2π) ∫ f(x) e⁻ⁱⁿˣ dx is exactly the projection of f onto the nth basis vector. Parseval's theorem, which you know, tells you that ∑|cₙ|² = ‖f‖² — the squared norm of f equals the sum of squared projections. In Hilbert space language, this is just the infinite-dimensional Pythagorean theorem. Completeness of the exponential system means the partial sums Sₙ(f) converge to f in the L² norm: ‖f − Sₙ(f)‖ → 0. This **L² convergence** is guaranteed for every f ∈ L²([0, 2π]) without additional hypotheses.

The subtlety arises when you ask about **pointwise convergence** — does Sₙ(f)(x) → f(x) for a fixed x? L² convergence says the integral of the squared error goes to zero; it says nothing about individual points. The difference matters because L² functions are equivalence classes: they are defined only up to modification on null sets, so "the value at x" is not even a well-defined concept in L². For pointwise convergence to hold, you need f to have additional smoothness or regularity — Hölder continuity, bounded variation, or similar conditions.

This distinction between L² convergence and pointwise convergence is one of the central lessons of functional analysis. L² is the "right" space for Fourier theory: the inner product structure makes Fourier coefficients natural projections, and completeness guarantees convergence in norm. But the Lᵖ framework also extends to other function spaces. For p ≠ 2, the spaces Lᵖ([0, 2π]) lack an inner product but retain a norm, and convergence of Fourier series in Lᵖ norm is a harder theorem — it holds for 1 < p < ∞ (by the Riesz-Fischer theorem and M. Riesz interpolation) but fails at the endpoints p = 1 and p = ∞. The Hilbert space structure of L² is what makes p = 2 so special and so natural for Fourier analysis.
