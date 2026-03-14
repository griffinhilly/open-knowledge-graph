---
id: differentials
title: Differentials
domain: mathematics
course: calculus-1
prerequisites:
  - id: linear-approximation
    type: hard
  - id: derivative-notation
    type: hard
builds-toward:
  - u-substitution
tags: [derivatives, differentials, approximation]
stage: formal-systems
status: validated
---

# Differentials

## Core Idea
If y = f(x), the differential dy = f'(x) dx represents the change in y along the tangent line for a small change dx in x. While the actual change in y is Delta_y = f(x + dx) - f(x), the differential dy approximates it: dy is approximately equal to Delta_y when dx is small. Differentials formalize the Leibniz notation and are used in error estimation, integration by substitution, and differential equations.

## How It's Best Learned
Compare Delta_y (actual change along the curve) with dy (change along the tangent line) graphically and numerically. Practice computing differentials: if y = x^3, then dy = 3x^2 dx. Apply to error propagation: if a measurement has error dx, estimate the error in a computed quantity.

## Common Misconceptions
- Confusing dy with Delta_y (dy is the linear approximation to the actual change).
- Treating dx as zero (it is small but nonzero).
- Not understanding the relationship between differentials and the chain rule / u-substitution.
