---
id: tangent-planes
title: Tangent Planes and Linear Approximation
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: partial-derivatives
  type: hard
- id: linear-approximation
  type: hard
- id: gradient-vector
  type: soft
builds-toward:
- chain-rule-multivariable
tags:
- tangent-plane
- linearization
- differentiability
- approximation
stage: formal-systems
status: validated
---

# Tangent Planes and Linear Approximation

## Core Idea
The tangent plane to z = f(x, y) at the point (a, b, f(a,b)) has equation z = f(a,b) + f_x(a,b)(x−a) + f_y(a,b)(y−b). This is the multivariable analogue of the tangent line: it best approximates the surface near the point. The linear approximation L(x,y) = f(a,b) + f_x(a,b)(x−a) + f_y(a,b)(y−b) is the linearization of f at (a,b). A function is differentiable at (a,b) if this linear approximation is a good approximation (the error vanishes faster than the distance to (a,b)).

## How It's Best Learned
Connect to single-variable linearization: L(x) = f(a) + f′(a)(x−a) becomes L(x,y) = f(a,b) + f_x(a,b)(x−a) + f_y(a,b)(y−b). Have students compute the tangent plane for a simple surface like z = x² + y² and verify visually that it is flat (horizontal) at the minimum.

## Common Misconceptions
- Existence of both partial derivatives at a point does not guarantee differentiability (the tangent plane exists only when f is 'smooth enough').
- The tangent plane equation requires evaluated (numerical) partial derivatives at the specific point, not general formulas.
- For a level surface F(x,y,z) = c, the tangent plane normal is ∇F, which is a different setup than z = f(x,y).

## Questions

```yaml
- question: "A function f(x,y) has partial derivatives f_x(0,0) = 2 and f_y(0,0) = 3 at the origin. A student concludes that the tangent plane z = f(0,0) + 2x + 3y must exist and provide a good local approximation. What assumption is this student making that may be wrong?"
  type: multiple-choice
  options:
    - "The student forgot to evaluate the partial derivatives at the specific point — they need numerical values, not symbolic expressions"
    - "The student is assuming differentiability, but the existence of both partial derivatives at a point does not guarantee differentiability — the tangent plane only gives a reliable approximation when the error vanishes faster than the distance to (0,0)"
    - "The student should use the gradient vector ∇f rather than individual partial derivatives"
    - "The tangent plane formula also requires second-order partial derivatives to be meaningful"
  answer: 1
  explanation: "This is the most important subtlety in multivariable differentiability. Partial derivatives measure slopes along the coordinate axes only. A function can have well-defined partial derivatives at a point while still having a crease or corner in other directions — the plane z = f(0,0) + 2x + 3y exists algebraically but may not be a good approximation to f near (0,0). Differentiability requires that the error |f(x,y) − L(x,y)| → 0 faster than the distance √(x² + y²) → 0, a condition that partial derivatives alone cannot guarantee."

- question: "You know f(1, 3) = 5, f_x(1, 3) = 2, and f_y(1, 3) = −1. Using the linear approximation, what is the best estimate of f(1.01, 2.98)?"
  type: multiple-choice
  options:
    - "5 + 2(1.01) + (−1)(2.98) = 4.04 — substitute the full coordinates into the partial derivatives"
    - "5 + 2(0.01) + (−1)(−0.02) = 5.04 — substitute the changes Δx = 0.01 and Δy = −0.02"
    - "5 + 2(0.01) + (−1)(0.02) = 4.98 — treat both changes as positive displacements"
    - "5 × [1 + 2(0.01) − 1(0.02)] = 5.00 — the correction terms multiply the base value"
  answer: 1
  explanation: "The linear approximation is L(x,y) = f(a,b) + f_x(a,b)(x−a) + f_y(a,b)(y−b). The key is to substitute the *changes* Δx = x − a and Δy = y − b, not the raw coordinates. Here Δx = 1.01 − 1 = 0.01 and Δy = 2.98 − 3 = −0.02. So L = 5 + 2(0.01) + (−1)(−0.02) = 5 + 0.02 + 0.02 = 5.04. Option A is the classic error of plugging raw coordinates into the formula instead of the differences."

- question: "If both partial derivatives f_x and f_y exist at a point (a,b), then f is differentiable at (a,b) and the tangent plane exists as a reliable local approximation."
  type: true-false
  answer: false
  explanation: "This is explicitly listed as a common misconception. Partial derivatives measure the function's slope only along the x-axis and y-axis directions. A function can fail to be differentiable at a point where both partials exist if it has a crease, corner, or other irregularity in a diagonal direction. Differentiability requires the stronger condition that the linear approximation error goes to zero *faster than* the distance to (a,b) — partial existence alone is not enough."

- question: "The tangent plane to z = f(x,y) at the point (a, b, f(a,b)) shares the same z-value and the same slopes in both the x and y directions as the surface f at that point."
  type: true-false
  answer: true
  explanation: "This is precisely what makes the tangent plane the 'best' linear approximation. At x = a, y = b, the plane gives z = f(a,b) — matching the surface value. Its slope in the x-direction (partial derivative with respect to x) equals f_x(a,b), and its slope in the y-direction equals f_y(a,b). No other plane through (a, b, f(a,b)) matches both slopes simultaneously. This is the direct generalization of the tangent line in single-variable calculus, which matches both the function value and the slope at the point of tangency."

- question: "A student says: 'I computed both partial derivatives at a point — that gives me the tangent plane.' Why might the student be wrong, and what additional condition is needed for the tangent plane to be a valid linear approximation?"
  type: short-answer
  answer: "Partial derivatives only tell you the slope of the surface along two specific directions (the x-axis and y-axis). A surface could have well-defined partials but still be 'creased' or non-smooth in a diagonal direction, making the tangent plane formula valid algebraically but not a good local approximation. What's needed is differentiability: the error |f(x,y) − L(x,y)| must go to zero faster than the distance |(x,y) − (a,b)| as (x,y) → (a,b). Continuity of the partial derivatives at the point is a sufficient (though not necessary) condition for this."
  explanation: "The distinction matters in practice: for most smooth functions you encounter (polynomials, trigonometric functions, exponentials), continuity of partials is guaranteed and differentiability follows automatically. The pathological cases — piecewise-defined functions, functions with isolated discontinuities — are where the gap between partial existence and differentiability becomes real."
```

## Explainer

In single-variable calculus, the **tangent line** to y = f(x) at the point (a, f(a)) was your best linear approximation: L(x) = f(a) + f′(a)(x − a). It matched the function's value and slope at x = a, and it was a good local approximation nearby. The **tangent plane** to z = f(x, y) is the exact multivariable analogue — now the surface has slopes in two independent directions, and the tangent plane must match both.

The formula z = f(a, b) + f_x(a, b)(x − a) + f_y(a, b)(y − b) encodes this: the partial derivative f_x is the slope of the surface in the x-direction, and f_y is the slope in the y-direction. Together, these two numbers uniquely determine a plane through the point (a, b, f(a, b)). Just as the tangent line was the unique line through (a, f(a)) with slope f′(a), the tangent plane is the unique plane through (a, b, f(a, b)) with the correct x-slope and y-slope. No other plane is as "flat" against the surface at that point.

The **linear approximation** L(x, y) uses this plane to estimate f(x, y) for points (x, y) near (a, b). Instead of computing f(1.01, 1.99) exactly, if you know f(1, 2), f_x(1, 2), and f_y(1, 2), you can evaluate L(1.01, 1.99) = f(1, 2) + f_x(1, 2)(0.01) + f_y(1, 2)(−0.01). The accuracy of this approximation is governed by **differentiability**: f is differentiable at (a, b) if and only if the error |f(x, y) − L(x, y)| goes to zero faster than the distance ‖(x, y) − (a, b)‖ as (x, y) → (a, b). This is a stronger condition than just having both partial derivatives — it rules out surfaces with creases or corners.

For **implicit surfaces** defined by F(x, y, z) = c (rather than z = f(x, y)), the tangent plane takes a cleaner form. The gradient ∇F(a, b, c) is perpendicular to the level surface at P = (a, b, c), so the tangent plane is {(x, y, z) : ∇F(a, b, c) · ⟨x − a, y − b, z − c⟩ = 0}. For example, on the unit sphere F(x, y, z) = x² + y² + z² = 1 at the point (1, 0, 0), we get ∇F = ⟨2, 0, 0⟩, so the tangent plane is 2(x − 1) = 0, i.e., x = 1 — the vertical plane touching the sphere at its rightmost point. This implicit approach handles surfaces that cannot be globally written as z = f(x, y).
