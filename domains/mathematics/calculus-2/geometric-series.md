---
id: geometric-series
title: Geometric Series
domain: mathematics
course: calculus-2
prerequisites:
  - id: series-definition-and-partial-sums
    type: hard
  - id: sequences-and-series-review
    type: hard
builds-toward:
  - power-series
  - radius-and-interval-of-convergence
tags: [series, geometric, convergence]
stage: formal-systems
status: draft
---

# Geometric Series

## Core Idea
A geometric series has the form sum from n=0 to infinity of a*r^n = a/(1 - r), converging if and only if |r| < 1. It is the most important series because it has a known closed-form sum, serves as a benchmark for comparison tests, and is the basis for power series and Taylor series. The partial sum formula S_N = a(1 - r^N)/(1 - r) shows exactly how the series converges.

## How It's Best Learned
Derive the partial sum formula by multiplying S_N by r and subtracting. Take the limit as N -> infinity to get the infinite sum. Practice identifying geometric series in various forms (e.g., sum of (2/3)^n, sum of (-1)^n / 4^n). Apply to repeating decimals and real-world scenarios.

## Common Misconceptions
- Applying the formula when |r| >= 1 (the series diverges in this case).
- Off-by-one errors on the starting index (the formula changes if the series starts at n = 1 vs. n = 0).
- Not recognizing a geometric series when it is written in a non-standard form.
