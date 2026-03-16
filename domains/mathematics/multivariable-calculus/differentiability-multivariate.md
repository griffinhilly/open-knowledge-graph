---
id: differentiability-multivariate
title: Differentiability in Multivariable Functions
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: partial-derivatives
  type: hard
- id: limits-continuity-multivariable
  type: hard
builds-toward:
- total-differential
- chain-rule-multivariable
- tangent-planes-linear-approximation
tags:
- differentiability
- continuity
- linear-approximation
stage: formal-systems
status: draft
---

# Differentiability in Multivariable Functions

## Core Idea
A function f(x, y) is differentiable at (a, b) if it can be well-approximated by a linear function; equivalently, if the error in the linear approximation vanishes faster than the distance to (a, b). Existence of continuous partial derivatives guarantees differentiability.

## Explainer

In single-variable calculus, differentiability at a point a meant the function had a tangent line — a linear function L(x) = f(a) + f'(a)(x − a) that approximated f so well that the relative error vanished: [f(x) − L(x)] / (x − a) → 0 as x → a. You learned from partial derivatives that f has well-defined rates of change in the x-direction and y-direction at any point. Differentiability in the multivariable setting asks for something stronger: a **tangent plane** that approximates f well from *every* direction, not just the coordinate directions.

Formally, f(x, y) is **differentiable** at (a, b) if there exist constants L₁ and L₂ such that the error in the linear approximation vanishes faster than the distance:

  lim₍h,k₎→(0,0) [f(a+h, b+k) − f(a,b) − L₁h − L₂k] / √(h² + k²) = 0

When differentiability holds, L₁ = fₓ(a, b) and L₂ = f_y(a, b) must be the partial derivatives. So differentiability does not introduce new numbers — it imposes a *quality condition* on the partial derivatives: the linear function built from them must approximate f well in all directions, not just along the axes.

The subtle point is that partial derivatives *alone* do not guarantee differentiability. You can construct functions where fₓ and f_y both exist at a point, yet the function is not even continuous there — the rates along the axes exist, but the function behaves wildly in diagonal directions. Differentiability is a genuinely stronger condition than the mere existence of partial derivatives because it constrains the function's behavior uniformly across all approaching directions.

The practical theorem you will use most: if fₓ and f_y exist and are **continuous** in a neighborhood of (a, b), then f is differentiable at (a, b). Continuous partial derivatives are the reliable sufficient condition. This guarantees the chain rule applies, the tangent plane formula is valid, and directional derivatives in every direction can be computed as the dot product of the gradient with the direction vector. The hierarchy is: continuous partial derivatives ⟹ differentiable ⟹ continuous, and each implication is strict — the converses fail in general.
