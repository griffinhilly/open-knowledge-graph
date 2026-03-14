---
id: u-substitution
title: U-Substitution
domain: mathematics
course: calculus-1
prerequisites:
- id: chain-rule
  type: hard
- id: fundamental-theorem-of-calculus-part-2
  type: hard
- id: differentials
  type: soft
- id: basic-integration-rules
  type: soft
builds-toward:
- integration-by-parts
- trigonometric-substitution
tags:
- integration
- techniques
- u-substitution
stage: formal-systems
status: validated
---
# U-Substitution

## Core Idea
U-substitution is the integration counterpart of the chain rule. If the integrand has the form f(g(x)) * g'(x), substituting u = g(x), du = g'(x) dx transforms the integral into the simpler integral of f(u) du. This is the most commonly used integration technique. For definite integrals, you must also change the bounds from x-values to u-values.

## How It's Best Learned
Start by identifying the inner function u and checking that its derivative (or a constant multiple) appears in the integrand. Practice recognizing the pattern. Work through many examples with increasing complexity. Emphasize changing bounds for definite integrals (or converting back to x before evaluating).

## Common Misconceptions
- Forgetting to convert dx to du (or introducing a missing constant incorrectly).
- Not changing the limits of integration when doing definite integrals with substitution.
- Choosing the wrong u (a good u simplifies the integral; a bad choice makes it worse).
