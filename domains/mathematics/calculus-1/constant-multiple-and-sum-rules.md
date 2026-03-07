---
id: constant-multiple-and-sum-rules
title: Constant Multiple and Sum/Difference Rules
domain: mathematics
course: calculus-1
prerequisites:
  - id: power-rule
    type: hard
builds-toward:
  - product-rule
  - antiderivatives
tags: [derivatives, rules, linearity]
stage: formal-systems
status: draft
---

# Constant Multiple and Sum/Difference Rules

## Core Idea
The constant multiple rule says d/dx[c*f(x)] = c*f'(x): constants factor out of derivatives. The sum/difference rule says d/dx[f(x) +/- g(x)] = f'(x) +/- g'(x): derivatives distribute over addition and subtraction. Together, these express the linearity of differentiation. Combined with the power rule, they allow you to differentiate any polynomial term by term.

## How It's Best Learned
Derive from the limit definition (constants factor out of limits, limit of a sum is sum of limits). Practice differentiating polynomials term by term. Emphasize that this only works for sums, not products or compositions (those need the product rule and chain rule).

## Common Misconceptions
- Trying to apply the sum rule to products: d/dx[f*g] is not f'*g'.
- Forgetting to differentiate constant terms (their derivative is zero, not the constant itself).
- Not recognizing that these rules together mean differentiation is a linear operation.
