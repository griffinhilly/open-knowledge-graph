---
id: second-partials-test-extrema
title: Second Partial Test for Local Extrema (Hessian)
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: higher-order-partials-mixed
  type: hard
- id: critical-points-multivariable-classification
  type: hard
builds-toward:
- constrained-optimization-lagrange
tags:
- second-derivative-test
- hessian
- eigenvalues
stage: formal-systems
status: draft
---

# Second Partial Test for Local Extrema (Hessian)

## Core Idea
At critical point (a, b), compute the Hessian matrix H = [[f_xx, f_xy], [f_xy, f_yy]]. If det(H) > 0 and f_xx > 0, it's a local min; if f_xx < 0, local max. If det(H) < 0, it's a saddle point. If det(H) = 0, test is inconclusive.

## Questions

```yaml
- question: "At a critical point of f(x,y), you find f_xx = 3, f_yy = 4, and f_xy = 5. What type of point is this?"
  type: multiple-choice
  options:
    - "A local minimum, because f_xx > 0 and f_yy > 0"
    - "A local maximum, because both second partials are positive"
    - "A saddle point, because D = f_xx·f_yy − (f_xy)² = 12 − 25 = −13 < 0"
    - "The test is inconclusive because D = 0"
  answer: 2
  explanation: "D = f_xx·f_yy − (f_xy)² = (3)(4) − (5)² = 12 − 25 = −13 < 0. When D < 0, the critical point is a saddle point regardless of the signs of the individual second partials. The large cross-term f_xy = 5 introduces enough twisting to create a saddle even though f_xx and f_yy are both positive. Option A is the classic error: seeing f_xx > 0 and f_yy > 0 and concluding local minimum without computing D."

- question: "What does D = f_xx·f_yy − (f_xy)² geometrically measure at a critical point?"
  type: multiple-choice
  options:
    - "The rate of change of the gradient vector"
    - "The average curvature of the surface at the critical point"
    - "Whether the Hessian's eigenvalues have the same sign (D > 0) or opposite signs (D < 0), determining if the surface curves the same way in all directions or curves up in some and down in others"
    - "The distance between the critical point and the nearest saddle point"
  answer: 2
  explanation: "D is the determinant of the Hessian. Its sign reflects whether the Hessian's eigenvalues agree in sign. When D > 0, both eigenvalues are positive (local min) or both negative (local max) — the surface curves the same way in every direction. When D < 0, eigenvalues have opposite signs — the surface curves up in some directions and down in others, producing a saddle. The cross-term f_xy encodes twisting; when large relative to f_xx and f_yy, it forces eigenvalues to have opposite signs."

- question: "If D = f_xx·f_yy − (f_xy)² = 0 at a critical point, the second partials test is inconclusive — the point could be a local min, local max, or saddle."
  type: true-false
  answer: true
  explanation: "When D = 0, the Hessian is singular and the test provides no information. The critical point could be any type. Other methods — evaluating f near the point, higher-order analysis, or geometric inspection — are required to classify it."

- question: "If f_xx > 0 and f_yy > 0 at a critical point of f(x,y), then the point must be a local minimum."
  type: true-false
  answer: false
  explanation: "Not necessarily — you must also confirm that D = f_xx·f_yy − (f_xy)² > 0. Even when both axial second partials are positive, a sufficiently large cross-derivative f_xy can make D negative, producing a saddle point. The function curves upward along the coordinate axes but curves downward in a diagonal direction, creating a saddle."

- question: "Why can a large f_xy value turn what appears to be a local minimum (f_xx > 0, f_yy > 0) into a saddle point?"
  type: short-answer
  answer: "f_xx and f_yy measure curvature only along the x and y axes. f_xy measures the 'twisting' of the surface — how the slope in the x-direction changes as you move in the y-direction. When f_xy is large relative to f_xx and f_yy, the surface curves sharply in a diagonal direction not captured by the axial second partials. D = f_xx·f_yy − (f_xy)² going negative means the twisting overwhelms the axial curvature, creating a direction along which the function decreases despite the positive axial second partials."
  explanation: "This is the multivariable lesson that you can't just check curvature along each axis independently — the mixed partial captures cross-direction interactions that can reverse the sign of curvature in off-axis directions."
```

## Explainer

In single-variable calculus, the second derivative test says: if f'(c) = 0 and f''(c) > 0, then c is a local minimum. The sign of the second derivative tells you the concavity — whether the function curves upward (bowl) or downward (hill) near the critical point. The second partials test generalizes this to functions of two variables, but the geometry is richer: near a critical point of f(x, y), the surface could curve upward in every direction (a local minimum), downward in every direction (a local maximum), or upward in some directions and downward in others (a saddle point, shaped like a mountain pass).

From your work on higher-order mixed partials, you know that f_xy = f_yx for smooth functions. The **Hessian matrix** H packages all this second-order information:

H = [[f_xx, f_xy], [f_xy, f_yy]]

The determinant D = det(H) = f_xx · f_yy − (f_xy)² is the key quantity. Think about what D measures geometrically. If D > 0, both eigenvalues of H have the same sign — meaning the surface curves the same way (both up or both down) in every cross-sectional direction through the critical point. Then f_xx (or equivalently f_yy) tells you which way: f_xx > 0 means concave up in all directions (local min), f_xx < 0 means concave down in all directions (local max). If D < 0, the eigenvalues have opposite signs — the surface curves up in some directions and down in others, producing a **saddle point**. The function increases if you walk one way, decreases if you walk another way; there is no local extremum.

A useful analogy: D is like the discriminant of the second-order behavior. Just as the discriminant of a quadratic b² − 4ac tells you whether roots are real or complex, D = f_xx f_yy − f_xy² tells you whether the critical point is a "definite" extremum or an indefinite saddle. The cross-term f_xy encodes the "twisting" of the surface; a large f_xy relative to f_xx and f_yy can turn a point that looks like an extremum along the axes into a saddle.

The test is applied in two steps: first locate critical points by solving ∇f = 0 (both partial derivatives vanish), then evaluate D and f_xx at each critical point. The inconclusive case D = 0 requires other methods — higher-order analysis, comparison with nearby values, or geometric inspection. This test extends conceptually to higher dimensions via the eigenvalues of the Hessian: a local min requires all eigenvalues positive (positive definite), a local max requires all negative (negative definite), and a saddle requires mixed signs (indefinite).
