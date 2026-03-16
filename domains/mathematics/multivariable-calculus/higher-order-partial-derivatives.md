---
id: higher-order-partial-derivatives
title: Higher-Order Partial Derivatives
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: partial-derivatives
  type: hard
- id: higher-order-derivatives
  type: soft
builds-toward:
- second-partials-test
tags:
- second-order
- mixed-partials
- Clairaut
stage: formal-systems
status: validated
---

# Higher-Order Partial Derivatives

## Core Idea
Higher-order partial derivatives are obtained by differentiating partial derivatives with respect to any variable. The second-order mixed partial ∂²f/∂x∂y means 'differentiate first with respect to y, then with respect to x.' Clairaut's theorem states that if the mixed partials are continuous, the order of differentiation does not matter: ∂²f/∂x∂y = ∂²f/∂y∂x. For functions with continuous second-order partials, there are three distinct second-order derivatives: f_xx, f_yy, and f_xy.

## Common Misconceptions
- ∂²f/∂x∂y means differentiate with respect to y first, then x — the notation is read right to left.
- Clairaut's theorem requires continuity of the mixed partials, not just their existence.
- The Hessian matrix collects all second-order partial derivatives and is symmetric when Clairaut's theorem applies.

## Explainer

From your work with partial derivatives, you know that ∂f/∂x measures the rate of change of f in the x-direction with y held fixed, and ∂f/∂y does the same in y with x held fixed. Higher-order partial derivatives simply repeat this process: take a partial derivative, and then take a partial derivative of the result. For a function f(x, y), the **second-order partial derivatives** are f_xx (differentiate twice with respect to x), f_yy (twice with respect to y), and the **mixed partial derivatives** f_xy and f_yx (differentiate with respect to one variable, then the other). All four exist whenever f is sufficiently smooth.

The most important warning is about notation. The Leibniz notation ∂²f/∂x∂y is read right to left: differentiate with respect to y first, then differentiate the result with respect to x. In subscript notation, f_xy means differentiate with respect to x first, then y — the opposite convention. Different textbooks use different conventions, so always verify which order is intended. The practical rule: in ∂²f/∂x∂y, the variable closest to f (on the right) is differentiated first. For f(x,y) = x²y³, the computation of ∂²f/∂x∂y goes: ∂f/∂y = 3x²y², then ∂/∂x(3x²y²) = 6xy².

**Clairaut's theorem** is the key result: if the mixed partial derivatives f_xy and f_yx are both continuous at a point, then f_xy = f_yx at that point — the order of differentiation does not matter. For virtually every function encountered in practice, this condition holds everywhere, and you can differentiate in whichever order is computationally easier. The continuity requirement is not merely a technicality: pathological functions exist where f_xy(0,0) ≠ f_yx(0,0), but those functions necessarily have discontinuous mixed partials at the origin. In smooth settings, Clairaut's theorem is essentially always available.

All of the second-order information about f is collected into the **Hessian matrix**: H = [[f_xx, f_xy], [f_xy, f_yy]] (when Clairaut's theorem applies and the off-diagonal entries are equal). The Hessian is the multivariable analogue of the second derivative. Just as f''(a) > 0 tells you a critical point is a local minimum in single-variable calculus, the Hessian's determinant and the sign of f_xx determine whether a critical point of f(x,y) is a local minimum, local maximum, or saddle point — this is the second partials test, your next topic. Mastering the computation of f_xx, f_yy, and f_xy is the prerequisite for that test, making the Hessian the natural destination toward which higher-order partials build.
