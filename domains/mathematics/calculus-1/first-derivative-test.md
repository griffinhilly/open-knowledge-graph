---
id: first-derivative-test
title: First Derivative Test
domain: mathematics
course: calculus-1
prerequisites:
  - id: mean-value-theorem
    type: soft
  - id: chain-rule
    type: hard
builds-toward:
  - curve-sketching
  - optimization-problems
tags: [derivatives, applications, extrema, increasing-decreasing]
stage: formal-systems
status: draft
---

# First Derivative Test

## Core Idea
The first derivative test classifies critical points (where f'(c) = 0 or f'(c) is undefined) as local maxima, local minima, or neither. If f' changes from positive to negative at c, then f has a local maximum at c. If f' changes from negative to positive, it is a local minimum. If f' does not change sign, c is neither (like x^3 at x = 0). The test works by analyzing the sign of f' on intervals determined by critical points.

## How It's Best Learned
Find critical points by setting f'(x) = 0 and identifying where f' is undefined. Build a sign chart for f' across the intervals. Determine increasing/decreasing behavior. Classify each critical point by the sign change pattern.

## Common Misconceptions
- Assuming f'(c) = 0 always means there is a local extremum (x^3 at 0 is a counterexample).
- Forgetting to check where f' is undefined (these are also critical points).
- Only checking the sign at one point per interval instead of determining the sign throughout.
