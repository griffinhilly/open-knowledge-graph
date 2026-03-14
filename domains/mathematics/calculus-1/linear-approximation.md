---
id: linear-approximation
title: Linear Approximation
domain: mathematics
course: calculus-1
prerequisites:
  - id: derivative-as-slope-of-tangent
    type: hard
builds-toward:
  - differentials
  - taylor-polynomials
tags: [derivatives, applications, approximation, tangent-line]
stage: formal-systems
status: validated
---

# Linear Approximation

## Core Idea
Linear approximation uses the tangent line at a known point to estimate function values nearby: f(x) is approximately equal to L(x) = f(a) + f'(a)(x - a) for x near a. This is the simplest and most practical consequence of differentiability. It is the foundation for differentials, Newton's method, and Taylor polynomials. The quality of the approximation depends on how close x is to a and how curved the function is.

## How It's Best Learned
Approximate values like sqrt(4.1) by linearizing sqrt(x) at x = 4. Compare the approximation with the true value to see the error. Discuss when the approximation is good (f is nearly linear near a) vs. poor (high curvature).

## Common Misconceptions
- Using a tangent line centered at a point far from the target value.
- Forgetting that the approximation gets worse as you move further from a.
- Confusing linear approximation (one term) with higher-order Taylor approximation.
