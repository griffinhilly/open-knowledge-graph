---
id: implicit-differentiation
title: Implicit Differentiation
domain: mathematics
course: calculus-1
prerequisites:
  - id: chain-rule
    type: hard
  - id: derivative-notation
    type: hard
builds-toward:
  - related-rates
tags: [derivatives, implicit, techniques]
stage: formal-systems
status: draft
---

# Implicit Differentiation

## Core Idea
Implicit differentiation finds dy/dx when y is defined implicitly by an equation like x^2 + y^2 = 25, rather than explicitly as y = f(x). The technique treats y as a function of x and applies the chain rule: every time you differentiate a term containing y, you multiply by dy/dx. Then solve algebraically for dy/dx. This extends calculus to curves that are not functions, like circles and ellipses.

## How It's Best Learned
Start with curves whose explicit form is known (e.g., the circle x^2 + y^2 = 25, solve for y, differentiate, then compare with implicit result). Progress to equations that cannot be solved for y. Emphasize the chain rule as the key mechanism: d/dx[y^2] = 2y * dy/dx.

## Common Misconceptions
- Forgetting to multiply by dy/dx when differentiating terms containing y.
- Treating y as a constant instead of a function of x.
- Getting lost in the algebra when solving for dy/dx in complex equations.
