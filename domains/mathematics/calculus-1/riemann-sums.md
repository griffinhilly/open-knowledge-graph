---
id: riemann-sums
title: Riemann Sums
domain: mathematics
course: calculus-1
prerequisites:
  - id: sequences-and-series-review
    type: soft
  - id: basic-integration-rules
    type: soft
builds-toward:
  - definite-integral-definition
tags: [integration, Riemann-sums, area, approximation]
stage: formal-systems
status: draft
---

# Riemann Sums

## Core Idea
A Riemann sum approximates the area under a curve by dividing the region into n rectangles and summing their areas. The width of each rectangle is Delta_x = (b - a)/n, and the height is f(x_i*) for some sample point x_i* in each subinterval (left endpoint, right endpoint, or midpoint). As n increases, the approximation improves. The limit of the Riemann sum as n approaches infinity defines the definite integral.

## How It's Best Learned
Compute Riemann sums by hand for small n (3, 4, 5 rectangles) to see the approximation improve. Visualize the rectangles on a graph. Compare left, right, and midpoint sums. Observe that for increasing functions, left sums underestimate and right sums overestimate.

## Common Misconceptions
- Confusing the number of rectangles n with the width Delta_x.
- Not understanding that Riemann sums are approximations, not exact values (until the limit).
- Believing that left/right/midpoint sums always give different limits (they all converge to the same integral).
