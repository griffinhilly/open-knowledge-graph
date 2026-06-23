---
id: partial-derivatives
title: 'Partial Derivatives: Definition and Computation'
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: limits-continuity-multivariable
  type: hard
- id: derivative-as-slope-of-tangent
  type: hard
- id: continuity-multivariable
  type: soft
- id: multivariable-functions-intro
  type: hard
- id: multivariable-limits
  type: soft
builds-toward:
- rates-of-change-partial-derivatives
- higher-order-partials
- chain-rule-multivariable
tags:
- partial-derivatives
- partial-notation
- computation
stage: formal-systems
status: validated
---

# Partial Derivatives: Definition and Computation

## Core Idea
The partial derivative ∂f/∂x is the ordinary derivative with respect to x while holding all other variables constant. Partial derivatives measure instantaneous rates of change along coordinate axes and are computed using single-variable differentiation rules.

## Questions

```yaml
- question: "Given f(x, y) = x²y + 3y², what is ∂f/∂x?"
  type: multiple-choice
  options: ["2xy + 6y", "2xy", "x² + 6y", "2x + 3y²"]
  answer: 1
  explanation: "When computing ∂f/∂x, y is treated as a constant. Differentiating x²y with respect to x gives 2xy (y acts as a constant coefficient). The term 3y² has no x in it, so its partial derivative with respect to x is 0. Result: 2xy."

- question: "The partial derivative ∂f/∂x of f(x, y) = x² + y² gives the same result as the total derivative df/dx when y is a function of x."
  type: true-false
  answer: false
  explanation: "When y depends on x, the total derivative df/dx includes an additional term: df/dx = 2x + 2y·(dy/dx) by the chain rule. The partial derivative ∂f/∂x = 2x treats y as constant regardless of whether y actually depends on x. They are equal only when dy/dx = 0."

- question: "Given f(x, y, z) = x²yz + sin(y), what is ∂f/∂y?"
  type: short-answer
  answer: "x²z + cos(y)"
  explanation: "Hold x and z constant. Differentiating x²yz with respect to y gives x²z (since x² and z are constants). Differentiating sin(y) with respect to y gives cos(y). Result: x²z + cos(y)."
```

## Explainer

When you first learned derivatives in single-variable calculus, you always had a function of just one variable — something like f(x) = x³ or g(x) = sin(x). The derivative told you the instantaneous rate of change as x varied. But in multivariable settings, a function like f(x, y) = x²y + 3y² takes two inputs and produces one output. There is no single "slope" anymore — the function can change differently depending on which direction you move. Partial derivatives solve this by asking: what is the rate of change if I move *only* in the x-direction, holding y completely fixed?

The computation rule is elegant: to find ∂f/∂x, treat every variable except x as if it were a constant, then differentiate using all the ordinary single-variable rules you already know. For f(x, y) = x²y + 3y², treating y as a constant coefficient gives ∂f/∂x = 2xy. Treating x as a constant when differentiating with respect to y gives ∂f/∂y = x² + 6y. Each partial derivative is just an ordinary derivative in disguise.

Geometrically, you can think of f(x, y) as defining a surface in three dimensions. If you stand on that surface at the point (x₀, y₀) and walk in the direction parallel to the x-axis, the slope of the surface under your feet is exactly ∂f/∂x at that point. Walk in the y-direction instead, and the slope is ∂f/∂y. Partial derivatives are the tool that lets you measure surface steepness along any coordinate axis.

The most common confusion is mixing up partial derivatives with total derivatives. If y happens to depend on x (say, y = x²), then the total derivative df/dx must account for how y changes too, via the chain rule. The partial derivative ∂f/∂x deliberately ignores that dependence — it freezes y and asks only about direct x-dependence. This distinction matters whenever you are working on a curve or surface defined by a constraint, which you will encounter in Lagrange multipliers and related techniques.

Partial derivatives are the building blocks for almost everything in multivariable calculus. The gradient vector stacks partial derivatives together to point in the direction of steepest ascent. Directional derivatives use them to measure rates of change in any direction. The chain rule in multiple variables chains partial derivatives together. Master the mechanical computation first — it is just single-variable differentiation with extra variables treated as constants — and the geometric intuition will follow naturally from working examples.
