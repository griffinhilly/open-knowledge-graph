---
id: telescoping-series
title: Telescoping Series
domain: mathematics
course: calculus-2
prerequisites:
  - id: series-definition-and-partial-sums
    type: hard
  - id: partial-fractions
    type: hard
builds-toward:
  - convergence-test-strategy
tags: [series, telescoping, partial-sums]
stage: formal-systems
status: validated
---

# Telescoping Series

## Core Idea
A telescoping series is one whose partial sums collapse through cancellation, leaving only a few surviving terms. After partial fraction decomposition, the general term has the form f(n) - f(n+1) (or similar), so when you sum, most terms cancel: S_N = f(1) - f(N+1). Taking the limit as N -> infinity gives the exact sum. Telescoping is one of the few methods that yields exact sums for infinite series.

## How It's Best Learned
Decompose 1/(n(n+1)) by partial fractions, write out several terms of the partial sum, observe the cancellation pattern, and find the sum. Practice recognizing series that telescope after algebraic manipulation. Verify by computing partial sums.

## Common Misconceptions
- Not recognizing when a series telescopes (partial fractions are the key step).
- Making errors tracking which terms survive after cancellation.
- Assuming all series with partial fractions telescope (they do not).
