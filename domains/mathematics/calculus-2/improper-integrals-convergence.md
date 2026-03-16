---
id: improper-integrals-convergence
title: Improper Integrals - Convergence
domain: mathematics
course: calculus-2
prerequisites:
- id: limits-at-infinity
  type: hard
- id: fundamental-theorem-of-calculus-part-2
  type: hard
- id: lhopitals-rule
  type: soft
- id: partial-fraction-decomposition-integration
  type: soft
builds-toward:
- integral-test
- comparison-test
tags:
- integration
- improper
- convergence
stage: formal-systems
status: validated
---
# Improper Integrals - Convergence

## Core Idea
An improper integral has either an infinite limit of integration or an integrand with an infinite discontinuity in the interval. It is evaluated as a limit: the integral from a to infinity of f(x) dx = lim(b->infinity) of the integral from a to b of f(x) dx. If this limit exists and is finite, the integral converges; otherwise, it diverges. The p-integral (integral of 1/x^p from 1 to infinity) converges if and only if p > 1, a key benchmark.

## How It's Best Learned
Start with concrete examples: integral of 1/x^2 from 1 to infinity (converges to 1) vs. integral of 1/x from 1 to infinity (diverges). Evaluate by antidifferentiating and taking the limit. Practice both types of impropriety (infinite bounds and discontinuous integrands). Introduce the p-test as a reference point.

## Common Misconceptions
- Evaluating an improper integral without taking a limit (plugging in infinity directly).
- Not recognizing an infinite discontinuity within the interval (e.g., integral of 1/x from -1 to 1 has a discontinuity at 0).
- Confusing convergence of the integral with convergence of the integrand to zero (the integrand can go to zero and the integral still diverge).

## Explainer

The Fundamental Theorem of Calculus tells you how to evaluate ∫ₐᵇ f(x) dx: find an antiderivative and plug in the limits. But this recipe assumes f is continuous on a closed, bounded interval [a, b]. An **improper integral** violates at least one of those conditions — either a limit is ±∞, or the integrand blows up somewhere in the interval. Because you can't "plug in" infinity, you replace the problematic boundary with a parameter and take a limit.

For an infinite upper limit: ∫₁^∞ f(x) dx = lim_{b→∞} ∫₁^b f(x) dx. If the limit exists and is finite, the integral **converges** to that value; otherwise it **diverges**. The **p-integral** ∫₁^∞ 1/xᵖ dx is the benchmark. When p > 1, the antiderivative is x^{1−p}/(1−p), which goes to 0 as x → ∞, giving a finite answer: it converges to 1/(p−1). When p = 1, the antiderivative is ln(x), which grows without bound — diverges. When p < 1, even worse divergence. So the rule is: ∫₁^∞ 1/xᵖ dx converges if and only if p > 1.

The most common error is forgetting that the integrand going to zero is necessary but not sufficient for convergence. The function 1/x → 0 as x → ∞, yet ∫₁^∞ 1/x dx diverges. Intuitively, 1/x shrinks, but it shrinks too slowly — the accumulation outpaces the decay. In contrast, 1/x² shrinks fast enough that the infinite tail has finite total area. The distinction between "slow decay" and "fast decay" is precisely what the p-test captures.

The second type of improper integral involves an integrand with an infinite discontinuity inside the interval. Consider ∫₀¹ 1/√x dx: the integrand blows up at x = 0. Replace the problem boundary with a parameter: lim_{a→0⁺} ∫ₐ¹ 1/√x dx = lim_{a→0⁺} [2√x]ₐ¹ = 2 − 0 = 2, which converges. The key habit is always checking: does the integrand have any discontinuities on the interval, including at the endpoints? A subtle discontinuity buried inside an interval — like 1/x on [−1, 1] — is easy to miss, but naively applying the FTC gives the wrong answer of 0 (when the integral actually diverges).
