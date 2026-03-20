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
stage: advanced
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

## Explainer

Single-variable differentiation measures how f(x) changes as x varies — f'(x) is the rate of change at each point. For a function of multiple variables like f(x, y), there is no single direction of change: you can vary x, vary y, or move in any diagonal direction. **Partial derivatives** isolate one direction at a time by holding all other variables fixed. The partial derivative ∂f/∂x at a point (a, b) is the rate of change of f as x varies while y is frozen at b — it is the ordinary derivative of the single-variable function g(x) = f(x, b) evaluated at x = a. Nothing structurally new is happening; you are simply reducing a multivariable problem to a single-variable one.

Computation is therefore mechanical: treat every variable except the differentiation variable as a constant, then apply all single-variable rules. For f(x, y) = x² + xy + y², differentiating with respect to x gives ∂f/∂x = 2x + y — the y² term contributes 0 (constant), the x² term gives 2x by the power rule, and xy gives y because y is a constant coefficient. Differentiating with respect to y gives ∂f/∂y = x + 2y — now x is the constant coefficient on the xy term. The curly **∂** notation (not d) is the signal that other variables are held fixed; writing df/dx would imply total differentiation, where y might itself vary with x. These are genuinely different quantities, and the notation enforces the distinction.

Geometrically, ∂f/∂x at a point is the slope of the tangent line to the curve you get by slicing the surface z = f(x, y) with the horizontal plane y = constant. Imagine the surface as a landscape: ∂f/∂x is the slope heading due east, and ∂f/∂y is the slope heading due north. Each partial derivative describes one family of cross-sectional slices. Crucially, knowing both slopes does not fully characterize the surface's behavior in every direction — the surface might rise steeply in a northeast direction even if both partial derivatives are zero at a point. This limitation is what motivates directional derivatives and the gradient, which combine partial derivative information to describe rates of change in arbitrary directions.

The chain rule and product rule apply inside partial derivatives exactly as in single-variable calculus — the key is consistently treating non-differentiated variables as constants throughout. For f = x² sin(y), differentiating with respect to x gives 2x sin(y); sin(y) is just a constant factor. For f = e^(xy), differentiating with respect to x gives ye^(xy) by the chain rule, with y as the constant coefficient in the exponent. Building fluency with these patterns prepares you for higher-order partial derivatives, where you differentiate a partial derivative again with respect to the same or a different variable, and for the multivariable chain rule, where the variables themselves may depend on other parameters.
