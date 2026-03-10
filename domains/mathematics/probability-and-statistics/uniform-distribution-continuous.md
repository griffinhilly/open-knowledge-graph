---
id: uniform-distribution-continuous
title: The Continuous Uniform Distribution
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: continuous-random-variables
  type: hard
tags:
- uniform-distribution
- continuous
- equally-likely
- rectangular-distribution
stage: formal-systems
status: draft
---

# The Continuous Uniform Distribution

## Core Idea
A continuous uniform distribution on [a, b] assigns equal probability density f(x) = 1/(b−a) to every point in the interval and zero elsewhere. Probabilities are computed as areas of rectangles: P(c ≤ X ≤ d) = (d−c)/(b−a). The mean is (a+b)/2 and the variance is (b−a)²/12. Despite its simplicity, the uniform distribution is foundational — uniform random number generators underlie most statistical simulations.

## How It's Best Learned
Use a bus arrival time scenario: a bus comes every 10 minutes. If you arrive at a random time, waiting time is Uniform(0,10). Find the probability of waiting more than 7 minutes — this is straightforward geometry. Emphasize that the rectangular PDF makes all probability computations elementary integrals.

## Common Misconceptions
- Confusing the continuous uniform with the discrete uniform (equal probability at each integer value vs. equal density across a continuous interval).
