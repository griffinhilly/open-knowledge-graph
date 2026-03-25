---
id: second-partials-test-hessian
title: Second Partial Test and the Hessian
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: second-partials-test
  type: hard
- id: mixed-partials-clairaut
  type: hard
- id: second-partials-test-extrema
  type: soft
builds-toward:
- optimization-multivariable-basics
tags:
- hessian
- classification
stage: formal-systems
status: validated
---
# Second Partial Test and the Hessian

## Core Idea
The Hessian H = [[f_xx, f_xy], [f_xy, f_yy]] classifies critical points. If det(H) > 0 and f_xx > 0, it's a local minimum. If det(H) > 0 and f_xx < 0, it's a maximum. If det(H) < 0, it's a saddle point.

## Questions

```yaml
- question: "At a critical point of f(x, y), you compute f_xx = −4, f_yy = −3, f_xy = 2. What type of critical point is this?"
  type: multiple-choice
  options:
    - "Local minimum, because both f_xx and f_yy are negative"
    - "Saddle point, because one second partial is larger in magnitude than the other"
    - "Local maximum, because D = f_xx·f_yy − (f_xy)² = 8 > 0 and f_xx < 0"
    - "The test is inconclusive because the mixed partial f_xy is nonzero"
  answer: 2
  explanation: "D = (−4)(−3) − (2)² = 12 − 4 = 8 > 0. Since D > 0, the surface curves the same way in all directions — it's either a bowl up or bowl down. The sign of f_xx determines which: f_xx = −4 < 0 means the surface is concave downward, so this is a local maximum. Option A is a common error: having both f_xx < 0 and f_yy < 0 is necessary but not sufficient for a maximum — you must also check that D > 0 to rule out a saddle."

- question: "At a critical point, the Hessian determinant D = 0. What does the second partial derivative test tell you?"
  type: multiple-choice
  options:
    - "The critical point is a saddle point, because zero determinant indicates indefiniteness"
    - "The critical point is a local minimum, because zero is the boundary between positive and negative curvature"
    - "The test is inconclusive — higher-order information is needed to classify the critical point"
    - "The critical point is an inflection point, analogous to the single-variable case when f''(a) = 0"
  answer: 2
  explanation: "D = 0 is exactly the degenerate case where the second-order approximation is neither positive definite, negative definite, nor indefinite — it is semidefinite. The second partial test cannot distinguish between a local minimum, local maximum, and saddle in this case. Higher-order terms in the Taylor expansion are needed. For example, f(x,y) = x⁴ + y⁴ has D = 0 at the origin but a local minimum, while f(x,y) = x³ − y³ also has D = 0 there but a saddle."

- question: "At a critical point where f_xx > 0 and f_yy > 0, the point must be a local minimum."
  type: true-false
  answer: false
  explanation: "This is the most tempting misconception. f_xx > 0 and f_yy > 0 means the surface curves upward in the x- and y-directions individually, but the mixed partial f_xy can introduce a 'twist' that tilts the surface into a saddle shape in an oblique direction. For example, f(x,y) = x² + y² − 4xy has f_xx = 2 > 0, f_yy = 2 > 0, but f_xy = −4, giving D = 4 − 16 = −12 < 0 — a saddle point. The determinant D captures whether the curvature is consistent in ALL directions, not just along the axes."

- question: "If the Hessian determinant D = f_xx·f_yy − (f_xy)² is negative at a critical point, the surface has a saddle shape there — curving upward in one direction and downward in another."
  type: true-false
  answer: true
  explanation: "D < 0 means the quadratic form ax² + 2bxy + cy² (the local approximation) is indefinite — it takes both positive and negative values for different directions (x, y). Geometrically, the surface curves upward along one direction through the critical point and downward along another, creating the characteristic saddle shape. The negative determinant measures the 'imbalance' between the curvatures: f_xx·f_yy < (f_xy)², meaning the cross-curvature overwhelms the product of the axial curvatures."

- question: "Explain geometrically why D < 0 indicates a saddle point rather than an extremum. What role does the cross-term f_xy play in the test?"
  type: short-answer
  answer: "D = f_xx·f_yy − (f_xy)² tests whether the local quadratic approximation curves in the same direction in every direction through the critical point. If D > 0, both 'principal curvatures' have the same sign, so the surface is bowl-shaped. If D < 0, the cross-curvature term (f_xy)² is large enough to flip the curvature in some oblique direction, creating a saddle. The f_xy term measures how the slope in the x-direction changes as you move in the y-direction — a 'twist' — and if this twist is strong enough relative to the axial curvatures, the surface tilts into a saddle even when both f_xx and f_yy are positive."
  explanation: "Formally, the quadratic form f_xx·u² + 2f_xy·uv + f_yy·v² (the second-order Taylor approximation in direction (u,v)) is positive definite iff f_xx > 0 and D > 0 — meaning it's positive in every direction. When D < 0, the form is indefinite: there exist directions where it's positive (the surface rises) and directions where it's negative (the surface falls). This is exactly the definition of a saddle point."
```

## Explainer

In single-variable calculus, the second derivative test classifies critical points: if f′(a) = 0 and f′′(a) > 0, the graph is concave up at a, so a is a local minimum; if f′′(a) < 0, it's concave down, so a is a local maximum. For functions of two variables, you already know that critical points satisfy ∇f = 0 (both partial derivatives are zero). The **Hessian matrix** is the multivariable analogue of the second derivative — it captures the curvature of the surface in all directions simultaneously.

The **Hessian** at a critical point (a, b) is the 2×2 matrix H = [[f_xx, f_xy], [f_xy, f_yy]], where all second partials are evaluated at (a, b). By Clairaut's theorem (which you have studied), f_xy = f_yx under smoothness conditions, so H is symmetric. The entries measure curvature in specific directions: f_xx is the concavity along the x-axis, f_yy is the concavity along the y-axis, and f_xy measures how the x-slope changes as y varies — a cross-curvature or "twist."

The classification hinges on the **determinant** D = det(H) = f_xx · f_yy − (f_xy)². Think of D as the product of curvatures in the two "principal" directions of the surface (the directions where the mixed terms vanish). If D > 0, the surface curves the same way in all directions at that point — it's bowl-shaped (either upward or downward), giving a local extremum. The sign of f_xx (or equivalently f_yy when D > 0) tells you which: positive means bowl-opening-upward (local minimum), negative means bowl-opening-downward (local maximum). If D < 0, the surface curves upward in one direction and downward in another — a **saddle point**, like the surface of a mountain pass that goes up toward ridges but down toward valleys.

Here is the geometric intuition for why D = f_xx · f_yy − (f_xy)² is the right quantity. A quadratic function ax² + 2bxy + cy² (which approximates f near a critical point) curves upward in every direction if and only if a > 0 and ac − b² > 0. The determinant condition is exactly testing whether this quadratic form is positive definite (curves up everywhere), negative definite (curves down everywhere), or indefinite (saddle). When D = 0, the test is inconclusive — you need higher-order information.

The Hessian matrix generalizes naturally beyond two variables: for a function of n variables, H is an n×n symmetric matrix of second partials, and the classification criterion generalizes to checking whether H is positive definite (local min), negative definite (local max), or indefinite (saddle). This is the heart of multivariable optimization, and understanding the Hessian as a curvature object — not just as a formula to memorize — is what makes it usable in more complex settings like constrained optimization and machine learning loss landscapes.
