---
id: lebesgue-integral
title: Lebesgue Integral (Full Construction)
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: simple-functions-approximation
  type: hard
builds-toward:
- riemann-lebesgue-comparison
- product-measures-fubini-theorem
tags:
- integration
stage: advanced
status: draft
---

# Lebesgue Integral (Full Construction)

## Core Idea
The Lebesgue integral is defined for simple functions as ∫s dμ = Σ aᵢμ(Eᵢ), extended to non-negative measurable functions by monotone supremum, then to general functions via positive and negative parts. This construction unifies and extends Riemann integration.

## Explainer

From your work with simple functions, you know that a **simple function** takes only finitely many values: s(x) = a₁ on set E₁, a₂ on E₂, ..., aₙ on Eₙ, where these sets partition the domain. You can think of a simple function as a step function where the steps need not be intervals — they can be any measurable sets. The Lebesgue integral of such a function is defined by the obvious formula: ∫s dμ = Σ aᵢ · μ(Eᵢ). Each term is the height of a step times the measure (size) of the set where that step occurs. This is the entire foundation — everything else is a careful limit process built on this base.

To integrate a **non-negative measurable function** f, you approximate it from below by simple functions. The key idea: for any such f, there is an increasing sequence of simple functions sₙ with sₙ(x) ↑ f(x) pointwise. The integral of f is defined as the supremum of the integrals of all such approximating simple functions: ∫f dμ = sup{∫s dμ : s simple, 0 ≤ s ≤ f}. Because the approximating functions increase to f, and their integrals are already defined, this supremum captures the "total area" under f — even if f is unbounded or has complicated discontinuities. The Monotone Convergence Theorem then guarantees that this limit behaves as expected.

For a **general measurable function** f (which may be positive, negative, or both), write f = f⁺ - f⁻ where f⁺(x) = max(f(x), 0) is the positive part and f⁻(x) = max(-f(x), 0) is the negative part. Both f⁺ and f⁻ are non-negative, so they are already integrable by the construction above. Then ∫f dμ = ∫f⁺ dμ - ∫f⁻ dμ, provided at least one of these is finite. If both are finite, f is called **Lebesgue integrable**, and we write f ∈ L¹(μ).

The power of this construction becomes clear when you compare it to Riemann integration. The Riemann integral partitions the *domain* into subintervals and sums widths times heights. The Lebesgue integral partitions the *range* into value bands and sums values times the measure of the preimage. This inversion is why Lebesgue handles badly-discontinuous functions that Riemann cannot: the measure of a set of discontinuities matters, not the structure of those discontinuities as a subset of the x-axis. The construction through simple functions, monotone limits, and positive/negative splitting is the full, rigorous answer to the question: what does it mean to integrate a general measurable function?
