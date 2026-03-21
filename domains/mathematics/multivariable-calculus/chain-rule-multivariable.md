---
id: chain-rule-multivariable
title: Chain Rule for Multivariable Functions
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: partial-derivatives
  type: hard
- id: chain-rule
  type: hard
builds-toward:
- implicit-differentiation
- directional-derivatives-gradient
tags:
- chain-rule
- composition
- derivatives
stage: formal-systems
status: draft
---

# Chain Rule for Multivariable Functions

## Core Idea
If f(x, y) has continuous partials and x = x(t), y = y(t), then df/dt = (∂f/∂x)(dx/dt) + (∂f/∂y)(dy/dt). For compositions like f(g(x, y), h(x, y)), the chain rule tracks how changes propagate through each layer.

## Questions

```yaml
- question: "f(x, y) = xy, where x(t₀) = 4, y(t₀) = 5, dx/dt|_{t₀} = 3, and dy/dt|_{t₀} = 2. What is df/dt at t₀?"
  type: multiple-choice
  options:
    - "6 — the product of the two rates of change"
    - "8 — only the contribution from the y-branch"
    - "15 — only the contribution from the x-branch"
    - "23 — the sum of both partial-derivative contributions"
  answer: 3
  explanation: "By the multivariable chain rule, df/dt = (∂f/∂x)(dx/dt) + (∂f/∂y)(dy/dt) = y·3 + x·2 = 5·3 + 4·2 = 15 + 8 = 23. Options 1, 2, and 3 each represent the error of tracking only one route from t to f (or multiplying instead of summing). The key insight is that every path from the independent variable t to f contributes its own term, and all contributions are summed."

- question: "If f: ℝ² → ℝ is differentiable and x: ℝ → ℝ² is a differentiable path, the derivative of the composition f(x(t)) is best described as:"
  type: multiple-choice
  options:
    - "The product of f′(x) and x′(t) treated as two scalars"
    - "The dot product of the gradient ∇f evaluated at x(t) with the velocity vector x′(t)"
    - "The sum of all second-order partial derivatives of f along x(t)"
    - "∂f/∂t, computed by directly differentiating f with respect to t"
  answer: 1
  explanation: "In the Jacobian (matrix) formulation, the derivative of a composition is the product of the Jacobians. For scalar-valued f, the Jacobian is the gradient ∇f (a row vector), and the Jacobian of x is x′(t) (a column vector of component rates). Their product is the dot product ∇f · x′(t). Written out for two components, this is exactly (∂f/∂x)(dx/dt) + (∂f/∂y)(dy/dt). Option 4 is wrong because f has no direct dependence on t — t enters only through x and y."

- question: "If f(x, y) = x + y, x(t) = t, and y(t) = 0 for all t, then df/dt = ∂f/∂x."
  type: true-false
  answer: true
  explanation: "Applying the chain rule: df/dt = (∂f/∂x)(dx/dt) + (∂f/∂y)(dy/dt) = 1·1 + 1·0 = 1. Since ∂f/∂x = 1, the statement is true. When y is constant, dy/dt = 0 and the y-branch contributes nothing, so the multivariable chain rule collapses to the single-variable rule in x. This is a useful sanity check: the multivariable formula should reduce to the familiar single-variable case when all but one intermediate variable is frozen."

- question: "The partial derivatives ∂f/∂x and ∂f/∂y in the chain rule formula df/dt = (∂f/∂x)(dx/dt) + (∂f/∂y)(dy/dt) are evaluated at the value of t, not at the point (x(t), y(t))."
  type: true-false
  answer: false
  explanation: "The partial derivatives are properties of f evaluated at a point in its domain, which is ℝ². They must be evaluated at (x(t), y(t)) — the current location of the path in the plane — not at the scalar t. This is a common notational confusion: t is the parameter of the path, but ∂f/∂x and ∂f/∂y measure how f varies in the (x, y)-plane at the specific point the path occupies at time t."

- question: "In your own words, explain why the multivariable chain rule sums the partial-derivative contributions rather than, say, multiplying them."
  type: short-answer
  answer: "Each intermediate variable (x, y) provides an independent channel through which a change in t can affect f. A small change dt causes dx = (dx/dt)dt change in x, which then produces a (∂f/∂x)dx change in f via the x-channel; simultaneously it causes a (∂f/∂y)dy change via the y-channel. Because both channels act at the same time and their effects on f add together (not multiply), the total change in f is the sum of all individual contributions."
  explanation: "The additive structure comes from f being approximately linear near any point (the definition of differentiability): df ≈ (∂f/∂x)dx + (∂f/∂y)dy. The total differential is a sum because small changes in independent directions add. This is unlike multiplying because the two paths (t→x→f) and (t→y→f) are parallel routes to the same output, not sequential steps — you add parallel contributions, you multiply sequential ones."
```

## Explainer

From single-variable calculus you know the chain rule: if y = f(g(t)), then dy/dt = f'(g(t)) · g'(t). The idea is that a small change in t propagates through g first, producing a change in g(t), which then propagates through f. In multivariable calculus the same logic applies, but now the "middle variable" x = x(t) is not a single number — it may be a point (x(t), y(t)) in the plane, and f depends on *both* components. Each component of the path contributes its own chain of partial derivatives, and all contributions are added.

The formula df/dt = (∂f/∂x)(dx/dt) + (∂f/∂y)(dy/dt) has a natural reading: the rate at which f changes as t changes is the sum of (how sensitive f is to x) × (how fast x is moving) plus (how sensitive f is to y) × (how fast y is moving). Each **partial derivative** plays the role that f'(g(t)) played in the single-variable rule — it measures sensitivity along one direction — and each dx/dt or dy/dt measures how fast the path is moving in that direction. If x and y are independent (x(t) = t, y(t) = 0), the formula reduces to the single-variable derivative in x, as expected.

The general multivariable chain rule is most cleanly written using Jacobians. If **x**: ℝᵏ → ℝⁿ is a differentiable function and f: ℝⁿ → ℝᵐ is differentiable, then the derivative of the composition f(**x**(t)) is the **matrix product** Df · D**x** — the Jacobian of f multiplied by the Jacobian of **x**. For scalar-valued f this becomes a row vector (the gradient ∇f) dotted with the matrix of partial derivatives of **x**. The summation form you saw above is just this matrix product written out explicitly for the case n = 2, m = 1, k = 1.

A powerful consequence is **implicit differentiation** in several variables, which you will meet next. If F(x, y) = 0 defines y implicitly as a function of x, then differentiating both sides with respect to x and applying the chain rule gives (∂F/∂x) + (∂F/∂y)(dy/dx) = 0, so dy/dx = −(∂F/∂x)/(∂F/∂y) wherever ∂F/∂y ≠ 0. The chain rule is also the engine behind the gradient and directional derivatives: the rate of change of f along a path with velocity vector **v** is exactly ∇f · **v**, which is the chain rule applied to the path **x**(t) with **x**'(t) = **v**.
