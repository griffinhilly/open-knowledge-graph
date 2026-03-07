---
id: mean-value-theorem
title: Mean Value Theorem
domain: mathematics
course: calculus-1
prerequisites:
  - id: continuity-definition
    type: hard
  - id: derivative-as-slope-of-tangent
    type: hard
  - id: rolles-theorem
    type: hard
builds-toward:
  - first-derivative-test
  - lhopitals-rule
tags: [theorems, MVT, existence-theorems]
stage: formal-systems
status: draft
---

# Mean Value Theorem

## Core Idea
The Mean Value Theorem (MVT) states that if f is continuous on [a, b] and differentiable on (a, b), then there exists at least one c in (a, b) where f'(c) = (f(b) - f(a))/(b - a). In other words, there is a point where the instantaneous rate of change equals the average rate of change over the interval. This theorem is the theoretical backbone for many results in calculus, including why zero derivative implies constant function.

## How It's Best Learned
Interpret geometrically: there is a tangent line parallel to the secant line through the endpoints. Verify with specific examples. Apply to prove corollaries: if f'(x) = 0 for all x, then f is constant; if f'(x) > 0, then f is increasing. Emphasize that MVT guarantees existence of c without finding it.

## Common Misconceptions
- Forgetting to verify the hypotheses (continuity on closed interval, differentiability on open interval).
- Confusing MVT with IVT (MVT is about derivatives, IVT is about function values).
- Believing there is exactly one c (there may be multiple).
