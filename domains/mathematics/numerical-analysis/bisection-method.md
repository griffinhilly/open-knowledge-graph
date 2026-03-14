---
id: bisection-method
title: Bisection Method for Root Finding
domain: mathematics
course: numerical-analysis
prerequisites:
- id: intermediate-value-theorem
  type: hard
builds-toward:
- order-of-convergence
tags:
- root-finding
- bisection
- convergence
stage: abstract-reasoning
status: draft
---

# Bisection Method for Root Finding

## Core Idea
The bisection method finds roots by repeatedly halving an interval where the function changes sign, guaranteed by the intermediate value theorem. Each iteration halves the remaining uncertainty, achieving linear convergence. Although slow, bisection is robust and requires only continuity and an initial sign change, with no derivatives or special tuning needed.

## How It's Best Learned
Implement bisection for simple functions like x³ - 2 = 0, tracking how the interval shrinks with each iteration and observing linear error reduction.

## Common Misconceptions
- Thinking bisection is fast just because it converges reliably; convergence is slow compared to faster methods.
- Assuming bisection works without locating an initial sign change; finding such an interval is the user's responsibility.
