---
id: p-series
title: P-Series
domain: mathematics
course: calculus-2
prerequisites:
  - id: series-definition-and-partial-sums
    type: hard
  - id: improper-integrals-convergence
    type: hard
builds-toward:
  - comparison-test
  - limit-comparison-test
tags: [series, p-series, convergence, benchmark]
stage: formal-systems
status: draft
---

# P-Series

## Core Idea
A p-series is sum from n=1 to infinity of 1/n^p. It converges if p > 1 and diverges if p <= 1. The case p = 1 is the harmonic series, the most famous divergent series. The convergence boundary at p = 1 matches the p-integral test and serves as the primary benchmark for comparison tests. Knowing p-series convergence is essential for all subsequent convergence tests.

## How It's Best Learned
Prove convergence/divergence using the integral test (integral of 1/x^p). Study the harmonic series carefully to understand why terms going to zero is not sufficient for convergence. Use p-series as comparison benchmarks for other series.

## Common Misconceptions
- Believing the harmonic series converges because 1/n -> 0 (this is the classic trap).
- Confusing p-series with geometric series (p-series has n in the base, geometric has n in the exponent).
- Not remembering whether p > 1 converges or diverges (think: the integral of 1/x^2 from 1 to infinity converges).
