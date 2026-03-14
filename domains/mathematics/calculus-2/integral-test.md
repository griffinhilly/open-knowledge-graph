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
