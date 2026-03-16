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

## Explainer

From single-variable calculus you know the chain rule: if y = f(g(t)), then dy/dt = f'(g(t)) · g'(t). The idea is that a small change in t propagates through g first, producing a change in g(t), which then propagates through f. In multivariable calculus the same logic applies, but now the "middle variable" x = x(t) is not a single number — it may be a point (x(t), y(t)) in the plane, and f depends on *both* components. Each component of the path contributes its own chain of partial derivatives, and all contributions are added.

The formula df/dt = (∂f/∂x)(dx/dt) + (∂f/∂y)(dy/dt) has a natural reading: the rate at which f changes as t changes is the sum of (how sensitive f is to x) × (how fast x is moving) plus (how sensitive f is to y) × (how fast y is moving). Each **partial derivative** plays the role that f'(g(t)) played in the single-variable rule — it measures sensitivity along one direction — and each dx/dt or dy/dt measures how fast the path is moving in that direction. If x and y are independent (x(t) = t, y(t) = 0), the formula reduces to the single-variable derivative in x, as expected.

The general multivariable chain rule is most cleanly written using Jacobians. If **x**: ℝᵏ → ℝⁿ is a differentiable function and f: ℝⁿ → ℝᵐ is differentiable, then the derivative of the composition f(**x**(t)) is the **matrix product** Df · D**x** — the Jacobian of f multiplied by the Jacobian of **x**. For scalar-valued f this becomes a row vector (the gradient ∇f) dotted with the matrix of partial derivatives of **x**. The summation form you saw above is just this matrix product written out explicitly for the case n = 2, m = 1, k = 1.

A powerful consequence is **implicit differentiation** in several variables, which you will meet next. If F(x, y) = 0 defines y implicitly as a function of x, then differentiating both sides with respect to x and applying the chain rule gives (∂F/∂x) + (∂F/∂y)(dy/dx) = 0, so dy/dx = −(∂F/∂x)/(∂F/∂y) wherever ∂F/∂y ≠ 0. The chain rule is also the engine behind the gradient and directional derivatives: the rate of change of f along a path with velocity vector **v** is exactly ∇f · **v**, which is the chain rule applied to the path **x**(t) with **x**'(t) = **v**.
