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
status: validated
---

# Tangent Planes and Linear Approximation

## Core Idea
The tangent plane to z = f(x, y) at (a, b) is z = f(a,b) + f_x(a,b)(x-a) + f_y(a,b)(y-b). This plane is the best linear approximation to f near (a, b), used for error propagation and differential approximation.

## Questions

```yaml
- question: "For z = f(x,y) with f(1, 2) = 5, fₓ(1, 2) = 3, and f_y(1, 2) = −1, what does the linear approximation give for f(1.1, 1.9)?"
  type: multiple-choice
  options:
    - "z ≈ 5 + 3(0.1) + (−1)(−0.1) = 5.4"
    - "z ≈ 5 + 3(1.1) + (−1)(1.9) = 6.4"
    - "z ≈ 3(0.1) + (−1)(−0.1) = 0.4"
    - "z ≈ 5 + 3(0.1)(−0.1) = 4.97"
  answer: 0
  explanation: "The tangent plane formula is L(x,y) = f(a,b) + fₓ(a,b)(x − a) + f_y(a,b)(y − b). Here (a,b) = (1,2), so x − a = 1.1 − 1 = 0.1 and y − b = 1.9 − 2 = −0.1. L = 5 + 3(0.1) + (−1)(−0.1) = 5 + 0.3 + 0.1 = 5.4. Option B plugs in the raw values of x and y instead of the displacements from (a,b) — a very common error. Option C forgets to add the base value f(a,b). Option D multiplies the displacements together rather than weighting them by their partial derivatives."

- question: "A student claims: 'The tangent plane to f(x,y) at (a,b) is horizontal if and only if both fₓ(a,b) = 0 and f_y(a,b) = 0. So the tangent plane only exists at critical points where the plane happens to be horizontal.' What is the error?"
  type: multiple-choice
  options:
    - "The tangent plane exists everywhere f is continuous, not just where it is differentiable"
    - "The tangent plane exists wherever f is differentiable — critical points are where the plane happens to be horizontal, but the plane exists at all differentiable points"
    - "The tangent plane exists only at saddle points, not at local extrema"
    - "The tangent plane requires fₓ = f_y = 0 to be well-defined, so the student is correct"
  answer: 1
  explanation: "The first sentence is correct: the tangent plane is horizontal when both partial derivatives vanish, which defines a critical point. But the student's conclusion is wrong. The tangent plane exists at every point where f is differentiable — it just has a nonzero tilt whenever the gradient is nonzero. Critical points are the special cases where the tangent plane is horizontal; they are not the only places where a tangent plane exists. This is exactly analogous to the tangent line in single-variable calculus: it exists wherever f is differentiable, and it's horizontal wherever f'(a) = 0."

- question: "If both partial derivatives fₓ(a,b) and f_y(a,b) exist at a point, then the tangent plane formula gives a valid linear approximation to f near (a,b)."
  type: true-false
  answer: false
  explanation: "Existence of partial derivatives is necessary but not sufficient for differentiability. Partial derivatives measure slopes along the coordinate axes only; a function can have both partial derivatives at a point yet behave wildly in diagonal directions. Differentiability requires the linear approximation error to vanish faster than distance from (a,b) in all directions — a stronger condition. A sufficient condition is that the partial derivatives are continuous at (a,b). Without continuity of partials (or some equivalent condition), the tangent plane formula may not actually approximate f well near the point."

- question: "The gradient vector ∇f(a,b) = (fₓ(a,b), f_y(a,b)) contains all the information needed to specify the tangent plane's orientation, given also the base value f(a,b)."
  type: true-false
  answer: true
  explanation: "The tangent plane z = f(a,b) + fₓ(a,b)(x − a) + f_y(a,b)(y − b) is determined by exactly three pieces of information: the base value f(a,b) and the two components of the gradient. The gradient encodes the plane's tilt: the directional derivative in direction u equals ∇f · u, so the slope of the plane in any direction is read directly from the gradient. Once you know the gradient and the base point, the plane is fully specified — its orientation, its slope in every direction, and its height at (a,b)."

- question: "Why is the tangent plane useful for error propagation — estimating how uncertainty in inputs x and y translates to uncertainty in the output f(x,y)?"
  type: short-answer
  answer: "The tangent plane is the best linear approximation to f near (a,b), so for small deviations Δx and Δy the change in f is approximately Δz ≈ fₓ·Δx + f_y·Δy. Each partial derivative acts as a sensitivity coefficient: fₓ scales how much uncertainty in x contributes to output uncertainty, and f_y scales the y contribution. Because the approximation is linear, uncertainties add independently — you can compute worst-case or statistical combinations of input uncertainties to bound the output uncertainty. This converts a complicated nonlinear function into a linear formula valid near the operating point."
  explanation: "The key is that the partial derivatives fₓ and f_y are the rates at which the output responds to each input. Near the operating point, the response is linear in the input deviations. This is why engineers use tangent planes (differentials) for tolerance analysis — not because the function is exactly linear, but because linear is a good enough approximation for small uncertainties, and linear calculations are tractable."
```

## Explainer

In single-variable calculus, the tangent line to y = f(x) at x = a is y = f(a) + f'(a)(x − a). It touches the curve at one point and best approximates the curve locally — nearby function values are close to the corresponding line values, with error that vanishes faster than the distance from a. For a function of two variables f(x, y), the analogous object is a **tangent plane**: a flat surface that touches the graph z = f(x, y) at the point (a, b, f(a,b)) and provides the best linear approximation near that point.

The formula is:  z = f(a, b) + fₓ(a, b)(x − a) + f_y(a, b)(y − b). Each partial derivative contributes one term. The term fₓ(a,b)(x − a) accounts for how f changes as you move in the x-direction, and f_y(a,b)(y − b) accounts for motion in the y-direction. Together they define a plane: every direction of motion away from (a, b) in the xy-plane corresponds to a slope computed as a linear combination of fₓ and f_y. When f is differentiable at (a, b) — which you've studied as the condition guaranteeing a good linear approximation — this plane is exactly the tangent plane, and the approximation error is small of higher order.

The **linearization** L(x, y) = f(a, b) + fₓ(a, b)(x − a) + f_y(a, b)(y − b) is a function you can evaluate cheaply, while f(x, y) might be complicated. Near (a, b), f(x, y) ≈ L(x, y). This is used for **error propagation** in applied settings: if x has uncertainty Δx and y has uncertainty Δy, then the resulting uncertainty in f is approximately Δz ≈ |fₓ| Δx + |f_y| Δy. Engineers use this constantly — the tangent plane formula converts uncertainties in inputs into estimates of uncertainty in outputs.

The tangent plane also encodes directional information. Every **directional derivative** of f at (a, b) is the slope of the tangent plane in the corresponding direction. The slope in direction u = (cos θ, sin θ) is fₓ cos θ + f_y sin θ = ∇f · u, where ∇f = (fₓ, f_y) is the **gradient**. The tangent plane is thus the geometric object that packages the gradient: its tilt and orientation are determined entirely by the two partial derivatives. This is why the tangent plane is the natural starting point for optimization — finding where the gradient vanishes, which is where the tangent plane is horizontal, identifies the critical points of f.
