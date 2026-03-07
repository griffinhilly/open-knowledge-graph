---
id: concavity-and-inflection-points
title: Concavity and Inflection Points
domain: mathematics
course: calculus-1
prerequisites:
  - id: first-derivative-test
    type: hard
builds-toward:
  - second-derivative-test
  - curve-sketching
tags: [derivatives, concavity, inflection, graphing]
stage: formal-systems
status: draft
---

# Concavity and Inflection Points

## Core Idea
A function is concave up where f''(x) > 0 (the graph curves upward, like a cup) and concave down where f''(x) < 0 (the graph curves downward, like a cap). An inflection point is where the concavity changes. Concavity provides information the first derivative cannot: while f' tells you whether the function is increasing or decreasing, f'' tells you whether the rate of change is accelerating or decelerating.

## How It's Best Learned
Compute f'', find where it is zero or undefined, and build a sign chart. Identify intervals of concave up/down and locate inflection points. Practice on polynomials, then on functions involving trig and exponentials. Connect to physical interpretation: concave up = velocity increasing = acceleration positive.

## Common Misconceptions
- Assuming f''(c) = 0 guarantees an inflection point (concavity must actually change, e.g., f(x) = x^4 has f''(0) = 0 but no inflection point).
- Confusing concavity with increasing/decreasing.
- Believing inflection points are always where f'' = 0 (they can occur where f'' is undefined).
