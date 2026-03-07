---
id: derivatives-of-exponential-functions
title: Derivatives of Exponential Functions
domain: mathematics
course: calculus-1
prerequisites:
  - id: chain-rule
    type: hard
  - id: exponential-functions-review
    type: hard
builds-toward:
  - derivatives-of-logarithmic-functions
  - differential-equations-intro-separable
tags: [derivatives, exponential]
stage: formal-systems
status: draft
---

# Derivatives of Exponential Functions

## Core Idea
The natural exponential function has the remarkable property that d/dx[e^x] = e^x: it is its own derivative. For a general base, d/dx[b^x] = b^x * ln(b). With the chain rule, d/dx[e^(g(x))] = e^(g(x)) * g'(x). This property makes e^x the most important function in calculus and differential equations, because exponential growth/decay is the solution to dy/dx = ky.

## How It's Best Learned
Motivate by showing that the limit definition yields e^x back. Compare with other bases to see why ln(b) appears. Practice with chain rule applications: e^(3x), e^(-x^2), 2^(sin(x)). Connect to growth/decay problems.

## Common Misconceptions
- Applying the power rule to e^x (it is not x * e^(x-1)).
- Forgetting the chain rule: d/dx[e^(2x)] = 2e^(2x), not e^(2x).
- Confusing d/dx[e^x] with d/dx[x^e] (the latter uses the power rule since e is a constant).
