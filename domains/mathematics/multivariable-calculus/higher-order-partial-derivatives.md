---
id: higher-order-partial-derivatives
title: Higher-Order Partial Derivatives
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: partial-derivatives
  type: hard
- id: higher-order-derivatives
  type: soft
builds-toward:
- second-partials-test
tags:
- second-order
- mixed-partials
- Clairaut
stage: formal-systems
status: validated
---

# Higher-Order Partial Derivatives

## Core Idea
Higher-order partial derivatives are obtained by differentiating partial derivatives with respect to any variable. The second-order mixed partial ∂²f/∂x∂y means 'differentiate first with respect to y, then with respect to x.' Clairaut's theorem states that if the mixed partials are continuous, the order of differentiation does not matter: ∂²f/∂x∂y = ∂²f/∂y∂x. For functions with continuous second-order partials, there are three distinct second-order derivatives: f_xx, f_yy, and f_xy.

## Common Misconceptions
- ∂²f/∂x∂y means differentiate with respect to y first, then x — the notation is read right to left.
- Clairaut's theorem requires continuity of the mixed partials, not just their existence.
- The Hessian matrix collects all second-order partial derivatives and is symmetric when Clairaut's theorem applies.
