---
id: tangent-planes-linear-approximation
title: Tangent Planes and Linear Approximation
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: tangent-planes
  type: hard
- id: directional-derivatives
  type: soft
builds-toward:
- optimization-multivariable-basics
tags:
- tangent-plane
- linearization
stage: formal-systems
status: draft
---

# Tangent Planes and Linear Approximation

## Core Idea
The tangent plane to z = f(x, y) at (a, b) is z = f(a,b) + f_x(a,b)(x-a) + f_y(a,b)(y-b). This plane is the best linear approximation to f near (a, b), used for error propagation and differential approximation.

## Explainer

In single-variable calculus, the tangent line to y = f(x) at x = a is y = f(a) + f'(a)(x − a). It touches the curve at one point and best approximates the curve locally — nearby function values are close to the corresponding line values, with error that vanishes faster than the distance from a. For a function of two variables f(x, y), the analogous object is a **tangent plane**: a flat surface that touches the graph z = f(x, y) at the point (a, b, f(a,b)) and provides the best linear approximation near that point.

The formula is:  z = f(a, b) + fₓ(a, b)(x − a) + f_y(a, b)(y − b). Each partial derivative contributes one term. The term fₓ(a,b)(x − a) accounts for how f changes as you move in the x-direction, and f_y(a,b)(y − b) accounts for motion in the y-direction. Together they define a plane: every direction of motion away from (a, b) in the xy-plane corresponds to a slope computed as a linear combination of fₓ and f_y. When f is differentiable at (a, b) — which you've studied as the condition guaranteeing a good linear approximation — this plane is exactly the tangent plane, and the approximation error is small of higher order.

The **linearization** L(x, y) = f(a, b) + fₓ(a, b)(x − a) + f_y(a, b)(y − b) is a function you can evaluate cheaply, while f(x, y) might be complicated. Near (a, b), f(x, y) ≈ L(x, y). This is used for **error propagation** in applied settings: if x has uncertainty Δx and y has uncertainty Δy, then the resulting uncertainty in f is approximately Δz ≈ |fₓ| Δx + |f_y| Δy. Engineers use this constantly — the tangent plane formula converts uncertainties in inputs into estimates of uncertainty in outputs.

The tangent plane also encodes directional information. Every **directional derivative** of f at (a, b) is the slope of the tangent plane in the corresponding direction. The slope in direction u = (cos θ, sin θ) is fₓ cos θ + f_y sin θ = ∇f · u, where ∇f = (fₓ, f_y) is the **gradient**. The tangent plane is thus the geometric object that packages the gradient: its tilt and orientation are determined entirely by the two partial derivatives. This is why the tangent plane is the natural starting point for optimization — finding where the gradient vanishes, which is where the tangent plane is horizontal, identifies the critical points of f.
