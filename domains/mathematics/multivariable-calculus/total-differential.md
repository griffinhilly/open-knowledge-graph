---
id: total-differential
title: Total Differential and Linear Approximation
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: partial-derivatives
  type: hard
- id: differentiability-multivariate
  type: hard
builds-toward:
- tangent-planes-linear-approximation
- chain-rule-multivariable
tags:
- total-differential
- approximation
- exactness
stage: formal-systems
status: validated
---

# Total Differential and Linear Approximation

## Core Idea
The total differential df = (∂f/∂x)dx + (∂f/∂y)dy represents the change in a differentiable function f when x and y change by small amounts dx and dy. It defines the best linear approximation to f near a point.

## Questions

```yaml
- question: "You want to estimate how f(x, y) = xy² changes when x goes from 3 to 3.02 and y goes from 2 to 1.99. You know ∂f/∂x = y² = 4 and ∂f/∂y = 2xy = 12 at (3, 2). Which expression gives the correct total differential approximation?"
  type: multiple-choice
  options:
    - "Δf ≈ (∂f/∂x)(∂f/∂y) = 4 · 12 = 48"
    - "Δf ≈ (∂f/∂x)Δx + (∂f/∂y)Δy = 4(0.02) + 12(−0.01) = −0.04"
    - "Δf ≈ (∂f/∂x)Δx = 4(0.02) = 0.08, since only x changes enough to matter"
    - "Δf ≈ (∂f/∂y)Δy = 12(−0.01) = −0.12, since y's percentage change is larger"
  answer: 1
  explanation: "The total differential sums all variable contributions: df = (∂f/∂x)dx + (∂f/∂y)dy. With Δx = 0.02 and Δy = −0.01: Δf ≈ 4(0.02) + 12(−0.01) = 0.08 − 0.12 = −0.04. You cannot drop one term based on which change is 'larger' — both partial derivatives contribute independently. Options A, C, and D all represent common errors: multiplying partials, or using only one term."

- question: "The total differential df of a function f(x, y) at a point is best described as:"
  type: multiple-choice
  options:
    - "The exact change in f when x and y each change by specific amounts"
    - "The rate at which f increases in the direction of steepest ascent"
    - "The best linear approximation to the change in f for simultaneous small changes in x and y"
    - "The product of the two partial derivatives ∂f/∂x and ∂f/∂y"
  answer: 2
  explanation: "The total differential is an approximation, not an exact change — the true change Δf and the differential df differ by higher-order terms that shrink faster than the displacement. 'Best linear approximation' is precise: df is exact to first order, meaning the error |Δf − df|/|(Δx, Δy)| → 0 as the displacement goes to zero. Option B describes the gradient direction; option D is not a standard concept."

- question: "In the total differential df = (∂f/∂x)dx + (∂f/∂y)dy, the quantities dx and dy are independent variables that can represent arbitrary (small) changes in x and y."
  type: true-false
  answer: true
  explanation: "This is subtle but important: dx and dy in the total differential are not fixed increments — they are free variables representing an arbitrary direction of displacement. This is what makes df a linear map on displacements (a 1-form), not a specific number. Only when you substitute specific values Δx and Δy do you get a numerical approximation to Δf."

- question: "If a function f(x, y) has partial derivatives ∂f/∂x and ∂f/∂y at a point, then the total differential df = (∂f/∂x)dx + (∂f/∂y)dy is guaranteed to be a valid linear approximation to Δf near that point."
  type: true-false
  answer: false
  explanation: "Existence of partial derivatives is not sufficient for differentiability. A function can have both partial derivatives at a point yet fail to be differentiable there — meaning the total differential does not accurately approximate the change in all directions. Differentiability (the stronger condition) requires that Δf equals df plus an error term that is o(|(Δx, Δy)|). This is why multivariable differentiability is defined separately from the existence of partial derivatives."

- question: "Explain why the total differential sums the partial derivative contributions rather than, say, taking the larger one or multiplying them."
  type: short-answer
  answer: "Each partial derivative measures the rate of change due to one variable alone, holding the other fixed. When both variables change simultaneously, their first-order contributions to Δf are additive and independent: the change due to Δx is approximately (∂f/∂x)Δx, and the change due to Δy is approximately (∂f/∂y)Δy. The cross-term ΔxΔy is second-order and negligible for small displacements. Summation correctly captures all first-order contributions; taking just one term would ignore part of the change, and multiplying them has no geometric meaning."
  explanation: "This additivity is exactly the linearity of the best linear approximation. Near any differentiable point, f behaves locally like a plane, and the plane's height change is a linear (additive) function of the displacements in x and y. The total differential is the equation of that tangent plane, expressed in terms of the displacement variables dx and dy."
```

## Explainer

From single-variable calculus, you know that the derivative f'(a) gives the slope of the tangent line, and the linear approximation f(a + Δx) ≈ f(a) + f'(a)Δx tells you how much f changes when x changes by a small amount Δx. The **total differential** is the precise multivariable generalization. For a function f(x, y), your prerequisite knowledge of partial derivatives gives you ∂f/∂x (rate of change with x fixed y) and ∂f/∂y (rate of change with x fixed). The total differential df = (∂f/∂x)dx + (∂f/∂y)dy combines both into a single expression that accounts for simultaneous changes in both variables.

The key insight is that **dx and dy are independent variables** in the differential — they represent arbitrary (small) changes in x and y, not specific increments. Given a specific displacement (Δx, Δy), the approximation becomes Δf ≈ (∂f/∂x)Δx + (∂f/∂y)Δy. This is the **best linear approximation** to the change in f: it is exact to first order, meaning the error |Δf − df| shrinks faster than the magnitude of the displacement |(Δx, Δy)| as the displacement goes to zero. This is precisely what differentiability means in the multivariate setting — your other prerequisite — and distinguishes it from merely having partial derivatives.

A concrete example: suppose f(x, y) = x²y and you want to estimate f(2.01, 2.98) without computing it exactly. Near (2, 3): ∂f/∂x = 2xy = 12, ∂f/∂y = x² = 4, f(2, 3) = 12. So Δf ≈ 12(0.01) + 4(−0.02) = 0.12 − 0.08 = 0.04, giving f ≈ 12.04. The actual value is (2.01)²(2.98) ≈ 12.04, confirming the approximation. Each partial derivative isolates the contribution of one variable; the total differential sums the contributions linearly.

The total differential extends naturally to more variables: df = (∂f/∂x)dx + (∂f/∂y)dy + (∂f/∂z)dz, and to **exact differentials** — expressions P dx + Q dy that equal the differential of some function f, which requires ∂P/∂y = ∂Q/∂x. This exactness condition connects directly to conservative vector fields and path independence in line integrals. The total differential is also the foundation for the multivariable **chain rule**: if x and y both depend on a parameter t, then df/dt = (∂f/∂x)(dx/dt) + (∂f/∂y)(dy/dt) — literally the total differential divided by dt, with each term recording how f changes through one path of influence.
