---
id: integrating-factor-method
title: Integrating Factor Method
domain: mathematics
course: differential-equations
prerequisites:
- id: first-order-linear-odes
  type: hard
- id: integration-by-parts
  type: soft
builds-toward:
- variation-of-parameters
- laplace-transform-of-derivatives
tags:
- first-order
- method
- solving
stage: advanced
status: draft
---

# Integrating Factor Method

## Core Idea
The integrating factor method transforms a first-order linear ODE dy/dx + p(x)y = q(x) into an exact equation by multiplying through by μ(x) = e^(∫p(x)dx). This technique converts the left side into the derivative of a product, allowing direct integration to find y.

## How It's Best Learned
Solve several examples where p(x) is constant, then tackle cases where p(x) is more complex. Always verify that μ(x)p(x) equals d/dx[μ(x)].

## Common Misconceptions
- Computing the integrating factor incorrectly by forgetting the constant of integration (the +C must be omitted). - Multiplying only part of the equation by μ(x). - Not recognizing when to use integrating factors versus other methods.
