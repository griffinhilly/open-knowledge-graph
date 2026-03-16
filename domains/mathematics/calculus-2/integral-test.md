---
id: integral-test
title: Integral Test
domain: mathematics
course: calculus-2
prerequisites:
  - id: improper-integrals-convergence
    type: hard
  - id: divergence-test
    type: hard
builds-toward:
  - comparison-test
  - p-series
tags: [series, convergence-tests, integral-test]
stage: formal-systems
status: validated
---

# Integral Test

## Core Idea
The Integral Test states that if f(x) is positive, continuous, and decreasing for x >= 1, and a_n = f(n), then the series sum of a_n and the improper integral of f(x) from 1 to infinity either both converge or both diverge. The test does not give the sum, only the convergence behavior. It is used to prove the p-series convergence criterion and to estimate series sums via integral bounds.

## How It's Best Learned
Visualize the connection: the series is a left Riemann sum for the integral (or vice versa). Apply to prove p-series convergence/divergence. Practice checking the three conditions (positive, continuous, decreasing). Use the integral remainder estimate to bound the error of partial sums.

## Common Misconceptions
- Applying the integral test when f is not eventually decreasing.
- Believing the integral gives the exact sum of the series (it only matches convergence/divergence behavior).
- Confusing the integral test with evaluating the series by integration.

## Explainer

You already know two things this test connects: improper integrals (summing continuous area to infinity) and infinite series (summing discrete terms). The integral test says these two summation processes share the same fate — either both converge or both diverge — when the terms come from a function that is positive, continuous, and decreasing.

The geometric picture makes this clear. Suppose f is a decreasing positive function and aₙ = f(n). Draw the graph of f and superimpose rectangles of width 1 centered at each integer. The rectangle at n has height f(n) = aₙ, so its area equals the n-th term of the series. Now compare the rectangles to the area under the curve. Because f is decreasing, each rectangle between n and n+1 lies either above or below the curve, depending on which edge you use. If the rectangle height is f(n), the rectangle is above the curve on [n, n+1], so the series is an **overestimate** of the integral. If you use f(n+1) instead, it is an underestimate. Sandwiching the integral between two shifted versions of the series shows that the integral and the series differ by at most a finite amount — so they share the same convergence behavior.

The three conditions matter. If f is not **positive**, the comparison to area breaks down. If f is not **continuous**, the Riemann sum interpretation fails. If f is not **decreasing**, the rectangle-to-curve comparison can reverse, and the integral no longer bounds the series in a useful way. In practice, "eventually decreasing" is enough — behavior at finitely many early terms does not affect convergence.

The integral test's most important application is the **p-series**: the series Σ 1/nᵖ converges if and only if p > 1. Using f(x) = 1/xᵖ, the improper integral ∫₁^∞ 1/xᵖ dx equals 1/(p−1) when p > 1 (converges) and diverges when p ≤ 1. The integral test carries this result directly to the series. The p-series criterion then becomes a benchmark for the comparison tests you will study next — when you encounter a new series, asking "does it behave like 1/nᵖ for some p?" is often the first diagnostic step.
