---
id: geometric-sequences-and-series
title: Geometric Sequences and Series
domain: mathematics
course: algebra-2
prerequisites:
  - id: arithmetic-sequences-and-series
    type: soft
  - id: exponential-functions-and-graphs
    type: hard
builds-toward:
  - sigma-notation
  - binomial-theorem
  - infinite-series
tags: [sequences, series, geometric, common-ratio]
stage: abstract-reasoning
status: draft
---

# Geometric Sequences and Series

## Core Idea
A geometric sequence has a constant ratio r between consecutive terms: a_n = a_1 * r^(n-1). The sum of the first n terms (geometric series) is S_n = a_1 * (1 - r^n)/(1 - r) for r != 1. If |r| < 1, the infinite geometric series converges to S = a_1/(1 - r). Geometric sequences model exponential growth and decay. The infinite series formula is foundational for calculus and finance.

## How It's Best Learned
Identify common ratios in sequences. Derive the finite sum formula by multiplying S_n by r and subtracting. Explore the infinite series by examining what happens as n grows when |r| < 1. Apply to compound interest, bouncing balls, and repeating decimals as infinite geometric series.

## Common Misconceptions
- Confusing common difference (arithmetic) with common ratio (geometric).
- Using the sum formula when r = 1 (division by zero; the sum is simply n*a_1).
- Applying the infinite series formula when |r| >= 1 (the series diverges).
- Sign errors in the sum formula when r is negative.
