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

## Questions

```yaml
- question: "For f(x, y) = x²y + sin(y), what is ∂f/∂x?"
  type: multiple-choice
  options:
    - "2xy + cos(y)"
    - "2xy"
    - "x² + cos(y)"
    - "2xy + x²cos(y)"
  answer: 1
  explanation: "When computing ∂f/∂x, treat y as a constant. For the term x²y: y is a constant coefficient, so ∂/∂x[x²y] = 2xy by the power rule. For the term sin(y): since y is treated as a constant, sin(y) is just a constant, and ∂/∂x[sin(y)] = 0. So ∂f/∂x = 2xy. Option A (adding cos(y)) is the classic error of treating sin(y) as if y were the differentiation variable. Option D applies the product rule as if y were a function of x, which is incorrect when computing partial derivatives."

- question: "A function f(x, y) has ∂f/∂x = 0 and ∂f/∂y = 0 at a point (a, b). What can you conclude about f at that point?"
  type: multiple-choice
  options:
    - "The function has a local maximum at (a, b)"
    - "The function has a local minimum at (a, b)"
    - "The function is completely flat in all directions at (a, b)"
    - "The function has zero rate of change in the x and y directions specifically, but may still change in other directions — further analysis is needed"
  answer: 3
  explanation: "Zero partial derivatives mean the surface has zero slope in the x-direction and y-direction at that point — but this does not rule out change in diagonal directions. The partial derivatives only measure two specific cross-sections of the surface. A saddle point, for example, has zero partial derivatives but is neither a max nor a min, and it changes in diagonal directions. Determining whether a critical point is a max, min, or saddle requires the second derivative test (using the Hessian matrix). This limitation is what motivates the study of directional derivatives and gradients."

- question: "For f(x, y) = x³ + 5y², the partial derivative ∂f/∂y equals 10y, with the x³ term contributing zero."
  type: true-false
  answer: true
  explanation: "When computing ∂f/∂y, x is treated as a constant. The term x³ is a constant (in y), so its partial derivative with respect to y is 0. The term 5y² differentiates normally to give 10y. So ∂f/∂y = 10y. This demonstrates the key mechanical rule: treat every variable except the one you're differentiating with respect to as a constant, then apply standard single-variable differentiation rules."

- question: "The partial derivative ∂f/∂x for a function f(x, y) is the same as the total derivative df/dx."
  type: true-false
  answer: false
  explanation: "These are genuinely different quantities. ∂f/∂x (partial derivative) holds y completely fixed as a constant. df/dx (total derivative) accounts for the possibility that y may itself depend on x — using the chain rule: df/dx = ∂f/∂x + (∂f/∂y)(dy/dx). If y is truly independent of x, they coincide; but in general they differ. The ∂ notation exists precisely to signal this distinction. Writing df/dx when you mean ∂f/∂x leads to incorrect results whenever y is not independent of x."

- question: "Explain geometrically what ∂f/∂x means for a surface z = f(x, y), and why knowing both partial derivatives does not fully describe the surface's behavior in every direction."
  type: short-answer
  answer: "∂f/∂x at a point (a, b) is the slope of the tangent line to the curve you get by slicing the surface z = f(x, y) with the vertical plane y = b — i.e., varying only x while keeping y fixed. Geometrically, if the surface is a landscape, ∂f/∂x is the slope heading due east and ∂f/∂y is the slope heading due north. But the surface can behave very differently in a northeast, diagonal, or any arbitrary direction. Two partial derivatives give you two directional slopes; the gradient gives a complete picture of the steepest ascent direction, and directional derivatives generalize to any direction."
  explanation: "A concrete example: at a saddle point, ∂f/∂x = 0 and ∂f/∂y = 0, yet the function rises in some directions and falls in others. The partial derivatives are insufficient to detect this. This motivates directional derivatives: ∇f · u gives the rate of change in direction u, combining both partial derivatives with the direction vector."
```

## Explainer

Single-variable differentiation measures how f(x) changes as x varies — f'(x) is the rate of change at each point. For a function of multiple variables like f(x, y), there is no single direction of change: you can vary x, vary y, or move in any diagonal direction. **Partial derivatives** isolate one direction at a time by holding all other variables fixed. The partial derivative ∂f/∂x at a point (a, b) is the rate of change of f as x varies while y is frozen at b — it is the ordinary derivative of the single-variable function g(x) = f(x, b) evaluated at x = a. Nothing structurally new is happening; you are simply reducing a multivariable problem to a single-variable one.

Computation is therefore mechanical: treat every variable except the differentiation variable as a constant, then apply all single-variable rules. For f(x, y) = x² + xy + y², differentiating with respect to x gives ∂f/∂x = 2x + y — the y² term contributes 0 (constant), the x² term gives 2x by the power rule, and xy gives y because y is a constant coefficient. Differentiating with respect to y gives ∂f/∂y = x + 2y — now x is the constant coefficient on the xy term. The curly **∂** notation (not d) is the signal that other variables are held fixed; writing df/dx would imply total differentiation, where y might itself vary with x. These are genuinely different quantities, and the notation enforces the distinction.

Geometrically, ∂f/∂x at a point is the slope of the tangent line to the curve you get by slicing the surface z = f(x, y) with the horizontal plane y = constant. Imagine the surface as a landscape: ∂f/∂x is the slope heading due east, and ∂f/∂y is the slope heading due north. Each partial derivative describes one family of cross-sectional slices. Crucially, knowing both slopes does not fully characterize the surface's behavior in every direction — the surface might rise steeply in a northeast direction even if both partial derivatives are zero at a point. This limitation is what motivates directional derivatives and the gradient, which combine partial derivative information to describe rates of change in arbitrary directions.

The chain rule and product rule apply inside partial derivatives exactly as in single-variable calculus — the key is consistently treating non-differentiated variables as constants throughout. For f = x² sin(y), differentiating with respect to x gives 2x sin(y); sin(y) is just a constant factor. For f = e^(xy), differentiating with respect to x gives ye^(xy) by the chain rule, with y as the constant coefficient in the exponent. Building fluency with these patterns prepares you for higher-order partial derivatives, where you differentiate a partial derivative again with respect to the same or a different variable, and for the multivariable chain rule, where the variables themselves may depend on other parameters.
