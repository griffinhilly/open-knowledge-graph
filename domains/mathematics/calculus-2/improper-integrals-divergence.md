---
id: improper-integrals-divergence
title: Improper Integrals - Divergence and Comparison
domain: mathematics
course: calculus-2
prerequisites:
  - id: improper-integrals-convergence
    type: hard
builds-toward:
  - comparison-test
tags: [integration, improper, divergence, comparison]
stage: formal-systems
status: validated
---

# Improper Integrals - Divergence and Comparison

## Core Idea
When an improper integral cannot be evaluated directly (no closed-form antiderivative), comparison tests determine convergence or divergence without computing the integral. The Direct Comparison Test says: if 0 <= f(x) <= g(x) and the integral of g converges, then the integral of f converges; if the integral of f diverges, so does the integral of g. The Limit Comparison Test uses lim f(x)/g(x) to draw the same conclusions more flexibly.

## How It's Best Learned
Build a library of known benchmarks (p-integrals, exponential decay). Practice bounding unfamiliar integrands above or below by known ones. Use the Limit Comparison Test when direct comparison is difficult. Emphasize that comparison only works for non-negative functions.

## Common Misconceptions
- Comparing in the wrong direction (bounding a convergent integral above by a divergent one proves nothing).
- Forgetting that comparison tests require non-negative integrands.
- Confusing the comparison test for integrals with the comparison test for series (same logic, different context).
