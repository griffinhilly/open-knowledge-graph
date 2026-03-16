---
id: uniform-convergence-power-series
title: Uniform Convergence of Power Series
domain: mathematics
course: real-analysis
prerequisites:
- id: weierstrass-m-test
  type: hard
- id: power-series
  type: soft
tags:
- power-series
- uniform-convergence
- analytic
stage: advanced
status: draft
---

# Uniform Convergence of Power Series

## Core Idea
A power series ∑aₙ(x - c)ⁿ converges uniformly on any closed interval inside its interval of convergence. This justifies term-by-term differentiation and integration of power series, making them the foundation of analytic functions. The uniform convergence follows from the Weierstrass M-Test applied to majorizing geometric series.

## Explainer

A power series ∑aₙ(x − c)ⁿ looks like an infinite polynomial, and you want to treat it like one: differentiate term by term, integrate term by term, substitute x into the series and get a meaningful value. But an infinite sum of functions is a limit — a limit of partial sums Sₙ(x) = ∑ₖ₌₀ⁿ aₖ(x−c)ᵏ — and you know that limits and operations like differentiation don't automatically commute. The question is: when can you treat a power series exactly like a polynomial for purposes of integration and differentiation?

The answer comes from the **Weierstrass M-Test**, which you already know. On any closed interval [c−r, c+r] strictly inside the interval of convergence, you can bound each term: |aₙ(x−c)ⁿ| ≤ |aₙ|rⁿ for all x in the interval. Call Mₙ = |aₙ|rⁿ. Since r is strictly less than the radius of convergence, the series ∑Mₙ = ∑|aₙ|rⁿ converges — it is dominated by a convergent geometric-like series. The Weierstrass M-Test then guarantees that ∑aₙ(x−c)ⁿ converges uniformly on [c−r, c+r]. The key word is "closed interval strictly inside" — uniformity can fail at the boundary, which is why you must stay strictly interior.

Once you have uniform convergence on compact subintervals, all the interchange theorems apply. You can integrate term by term: ∫∑aₙ(x−c)ⁿ dx = ∑∫aₙ(x−c)ⁿ dx = ∑aₙ(x−c)ⁿ⁺¹/(n+1). You can differentiate term by term: d/dx ∑aₙ(x−c)ⁿ = ∑naₙ(x−c)ⁿ⁻¹. Both operations produce a new power series with the same radius of convergence. This means that on the interior of its disk of convergence, a power series can be differentiated infinitely many times, and each derivative is again a power series. Functions representable by power series are called **analytic functions** — the most well-behaved class in analysis.

This result is the gateway to understanding functions like sin(x), cos(x), and eˣ as infinite polynomials that you can manipulate term by term. When you learned that sin(x) = x − x³/6 + x⁵/120 − ···, you were implicitly using this theorem: the series converges uniformly on any bounded interval, so you can integrate it to get the series for −cos(x), differentiate it to get the series for cos(x), and multiply two such series to get new identities. Every formula involving Taylor series manipulation rests on this foundation.
