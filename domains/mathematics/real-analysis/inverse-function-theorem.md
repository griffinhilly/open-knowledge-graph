---
id: inverse-function-theorem
title: The Inverse Function Theorem
domain: mathematics
course: real-analysis
prerequisites:
  - id: total-differential
    type: hard
  - id: contraction-mapping-theorem
    type: hard
  - id: matrix-inverses
    type: hard
  - id: jacobian-change-of-variables
    type: soft
  - id: mean-value-theorem-rigorous
    type: soft
builds-toward:
  - implicit-function-theorem-on-manifolds
  - exponential-map
tags: [real-analysis, multivariable-analysis, inverse-function-theorem, jacobian, local-invertibility]
stage: advanced
status: validated
---

# The Inverse Function Theorem

## Core Idea
Let f map an open set in ℝⁿ to ℝⁿ, be continuously differentiable, and have an invertible derivative matrix Df(a) at a point a. The inverse function theorem says that f is then invertible near a: there are open sets V containing a and W containing f(a) such that f maps V one-to-one onto W, and the inverse is also continuously differentiable. Its derivative is the inverse matrix, D(f⁻¹)(f(x)) = [Df(x)]⁻¹. The theorem turns a linear-algebra condition at one point (det Df(a) ≠ 0) into a nonlinear conclusion on a neighborhood.

## How It's Best Learned
Start in one variable: a C¹ function with f'(a) ≠ 0 is strictly monotone near a, so it has a local inverse with derivative 1/f'. Then look at maps of the plane, such as polar coordinates, and compute where the Jacobian determinant vanishes. Use the complex exponential map (x, y) ↦ (eˣ cos y, eˣ sin y) to show the result is local. Present the proof as solving f(x) = y by a contraction mapping.

## Common Misconceptions
- If det Df(x) ≠ 0 everywhere, f is one-to-one on its whole domain. (The map (x, y) ↦ (eˣ cos y, eˣ sin y) has Jacobian determinant e²ˣ > 0 everywhere but repeats its values when y increases by 2π.)
- If Df(a) is singular, f cannot be one-to-one near a. (f(x) = x³ is one-to-one on ℝ although f'(0) = 0; what fails is differentiability of the inverse at 0.)
- Differentiability of f at a is enough. (The theorem needs Df to be continuous near a; there are differentiable functions with f'(0) ≠ 0 that are not one-to-one on any interval around 0.)

## Questions

```yaml
- question: "Let F(r, θ) = (r cos θ, r sin θ). At which points does the inverse function theorem guarantee a local C¹ inverse?"
  type: multiple-choice
  options:
    - "At every point"
    - "At points with r ≠ 0"
    - "At points with θ ≠ 0"
    - "Only at the point (1, 0)"
  answer: 1
  explanation: "The Jacobian determinant of polar coordinates is r. It is nonzero exactly when r ≠ 0, so F has a local C¹ inverse near every point with r ≠ 0. At r = 0 every θ maps to the origin, so no local inverse exists there."

- question: "If f: ℝ² → ℝ² is C¹ and det Df(x) ≠ 0 for every x, then f is one-to-one on ℝ²."
  type: true-false
  answer: false
  explanation: "The theorem is local. The map f(x, y) = (eˣ cos y, eˣ sin y) has det Df = e²ˣ, which is never zero, yet f(x, y) = f(x, y + 2π). Each point has a neighborhood on which f is one-to-one, but f is not one-to-one globally."

- question: "Suppose f is C¹ near a, Df(a) is invertible, and b = f(a). Express D(f⁻¹)(b) in terms of Df."
  type: short-answer
  answer: "D(f⁻¹)(b) = [Df(a)]⁻¹"
  explanation: "Differentiate f⁻¹(f(x)) = x with the chain rule at x = a: D(f⁻¹)(b) · Df(a) = I. So the derivative of the inverse is the inverse matrix of the derivative, the n-dimensional version of (f⁻¹)'(b) = 1/f'(a)."

- question: "The function f(x) = x³ shows that the hypothesis det Df(a) ≠ 0 is not necessary for f to be one-to-one near a. What conclusion of the theorem fails for x³ at a = 0?"
  type: short-answer
  answer: "The inverse x^(1/3) is not differentiable at 0."
  explanation: "x³ is a bijection of ℝ, but its inverse has infinite slope at 0. The condition Df(a) invertible is exactly what the inverse needs in order to be differentiable at f(a)."
```

## Explainer

In one variable, if f is continuously differentiable and f'(a) ≠ 0, then f' keeps the same sign near a. So f is strictly increasing or strictly decreasing there and has an inverse function nearby, with (f⁻¹)'(f(a)) = 1/f'(a). The inverse function theorem extends this to maps from ℝⁿ to ℝⁿ, where "f'(a) ≠ 0" becomes "the matrix Df(a) is invertible."

Theorem. Let U ⊆ ℝⁿ be open, f: U → ℝⁿ continuously differentiable, and a ∈ U with det Df(a) ≠ 0. Then there are open sets V ∋ a and W ∋ f(a) such that f: V → W is a bijection, its inverse g: W → V is continuously differentiable, and Dg(f(x)) = [Df(x)]⁻¹ for x in V.

The idea is linear approximation. Near a, f(x) ≈ f(a) + Df(a)(x - a). If Df(a) is invertible, the linear part is a bijection, and the theorem says the small error in the approximation cannot destroy that near a. To make this precise, fix y near f(a) and try to solve f(x) = y. Rewrite the equation as a fixed-point problem: x = x + Df(a)⁻¹(y - f(x)). The map on the right has derivative I - Df(a)⁻¹Df(x), which is small for x near a because Df is continuous. So the map is a contraction on a small closed ball, and the contraction mapping theorem gives exactly one solution x in that ball. This produces the local inverse. A further estimate shows it is differentiable, and the chain rule applied to g(f(x)) = x gives the formula for Dg.

The conclusion is local, and that cannot be improved. The map f(x, y) = (eˣ cos y, eˣ sin y) has Jacobian determinant e²ˣ, which is never zero, so it is locally invertible everywhere. Yet it is not one-to-one, because adding 2π to y gives the same output. This is the complex exponential function in real coordinates.

The hypothesis is sufficient but not necessary for a one-to-one map. The function x³ is a bijection of ℝ with derivative 0 at the origin, but its inverse fails to be differentiable there. Invertibility of Df(a) is what makes the inverse differentiable.

The implicit function theorem, which says when F(x, y) = 0 defines y as a function of x, follows by applying this theorem to the map (x, y) ↦ (x, F(x, y)). Together they are the basic tools for working with smooth manifolds.
