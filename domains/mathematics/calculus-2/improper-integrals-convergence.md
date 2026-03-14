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
