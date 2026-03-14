---
id: alternating-series-test
title: Alternating Series Test
domain: mathematics
course: calculus-2
prerequisites:
  - id: divergence-test
    type: hard
  - id: sequences-convergence
    type: hard
builds-toward:
  - absolute-vs-conditional-convergence
tags: [series, convergence-tests, alternating]
stage: formal-systems
status: validated
---

# Alternating Series Test

## Core Idea
The Alternating Series Test (Leibniz's test) states: if a_n > 0, a_n is decreasing, and lim a_n = 0, then the alternating series sum of (-1)^n * a_n converges. Furthermore, the error from using the Nth partial sum is bounded by the (N+1)th term: |S - S_N| <= a_(N+1). This test handles series that converge because of cancellation between positive and negative terms, even when the series of absolute values diverges.

## How It's Best Learned
Verify the three conditions: alternating signs, decreasing absolute values, limit zero. Visualize partial sums bouncing back and forth, converging to the sum. Apply the alternating series estimation theorem for error bounds. Classic example: the alternating harmonic series sum of (-1)^(n+1)/n = ln(2).

## Common Misconceptions
- Forgetting to check that a_n is decreasing (not just that a_n -> 0).
- Applying the test to non-alternating series.
- Confusing the alternating series test with the divergence test (both check if a_n -> 0, but for different conclusions).
