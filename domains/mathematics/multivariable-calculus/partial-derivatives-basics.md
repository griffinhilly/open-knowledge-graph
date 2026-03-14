---
id: partial-derivatives-basics
title: Partial Derivatives
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: partial-derivatives
  type: hard
- id: continuity-multivariable
  type: soft
builds-toward:
- higher-order-partial-derivatives
- directional-derivatives
tags:
- derivatives
- rates-of-change
stage: formal-systems
status: draft
---

# Partial Derivatives

## Core Idea
The partial derivative ∂f/∂x measures how f changes when x varies while y (and other variables) are held constant. For f(x, y), compute ∂f/∂x by treating y as a constant and differentiating normally.

## How It's Best Learned
Start with f(x,y) = x² + xy + y². Compute ∂f/∂x = 2x + y and ∂f/∂y = x + 2y. Interpret geometrically as slopes of tangent lines to cross-sections.

## Common Misconceptions
Writing ∂f/∂x as df/dx; the notation ∂ signals that other variables are held fixed.
Forgetting to apply chain rule or product rule within partial derivatives.
