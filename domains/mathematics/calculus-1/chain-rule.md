---
id: chain-rule
title: Chain Rule
domain: mathematics
course: calculus-1
prerequisites:
- id: product-rule
  type: soft
- id: composition-of-functions
  type: hard
- id: composition-of-functions-advanced
  type: soft
builds-toward:
- implicit-differentiation
- related-rates
- u-substitution
tags:
- derivatives
- rules
- chain-rule
- composition
stage: formal-systems
status: validated
---
# Chain Rule

## Core Idea
The chain rule states that if y = f(g(x)), then dy/dx = f'(g(x)) * g'(x). In Leibniz notation: if y = f(u) and u = g(x), then dy/dx = (dy/du)(du/dx). You differentiate the outer function evaluated at the inner function, then multiply by the derivative of the inner function. The chain rule is arguably the most important derivative rule because composite functions appear everywhere.

## How It's Best Learned
Start with clear identification of the "outer" and "inner" functions. Practice with simple compositions like (3x + 1)^5, sin(x^2), e^(2x). Build up to multi-layer compositions (chain rule applied multiple times). Connect to u-substitution in integration (the chain rule in reverse).

## Common Misconceptions
- Forgetting to multiply by the derivative of the inner function (the most common chain rule error).
- Difficulty identifying the inner and outer functions in complex expressions.
- Not recognizing when the chain rule is needed (any composite function requires it).
