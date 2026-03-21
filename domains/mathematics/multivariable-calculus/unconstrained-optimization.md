---
id: unconstrained-optimization
title: 'Unconstrained Optimization: Finding Extrema'
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: hessian-matrix-second-derivative-test
  type: hard
builds-toward:
- lagrange-multipliers
tags:
- optimization
- extrema
- applications
stage: formal-systems
status: draft
---

# Unconstrained Optimization: Finding Extrema

## Core Idea
To optimize f(x, y) without constraints: (1) find critical points by setting ∇f = 0, (2) classify each using the Hessian test, (3) check boundary behavior. This process identifies global maxima and minima.

## Questions

```yaml
- question: "You find a critical point of f(x,y) where D = f_xx · f_yy − (f_xy)² = 25 and f_xx = −5. What type of critical point is this?"
  type: multiple-choice
  options:
    - "A saddle point, because f_xx is negative"
    - "A local minimum, because D > 0"
    - "A local maximum, because D > 0 and f_xx < 0"
    - "An inflection point, because D is positive but one second derivative is negative"
  answer: 2
  explanation: "When D > 0 and f_xx < 0, the Hessian is negative definite: the function curves downward in all directions at this point, making it a local maximum. When D > 0 and f_xx > 0, it is a local minimum. When D < 0, it is a saddle point. The sign of f_xx alone does not determine the type — both D and f_xx must be considered together."

- question: "A student finds all critical points of f(x,y) on the closed bounded domain {(x,y) : x² + y² ≤ 4}, classifies them using the Hessian test, and identifies a local minimum in the interior. She concludes this is the global minimum. What has she most likely forgotten?"
  type: multiple-choice
  options:
    - "She forgot to verify that D > 0 at the critical point"
    - "She forgot to check the boundary of the domain, where the global minimum might be located"
    - "She forgot to compute f_xy and verify it equals f_yx"
    - "She forgot that the Hessian test only applies to unbounded domains"
  answer: 1
  explanation: "On a closed bounded domain, global extrema can occur either at interior critical points or on the boundary. A local interior minimum is only guaranteed to be global if you have also checked boundary behavior and found no smaller values there. For a disc, this means parameterizing the boundary circle and optimizing f along it. Forgetting this step is described as 'the most common source of wrong answers in applied optimization problems.'"

- question: "A critical point where D = f_xx · f_yy − (f_xy)² < 0 is a saddle point — a local minimum in one direction and a local maximum in a perpendicular direction."
  type: true-false
  answer: true
  explanation: "When D < 0, the Hessian is indefinite — it has both positive and negative eigenvalues. The function curves upward in some directions and downward in others from that point. Like a mountain pass, the point is a minimum if you walk along the ridge but a maximum if you walk across it. This is neither a local max nor a local min overall."

- question: "Setting ∇f = 0 at a point is sufficient to conclude that the point is a local maximum or minimum of f."
  type: true-false
  answer: false
  explanation: "∇f = 0 is necessary but not sufficient for an extremum. It identifies all candidates — called critical points — but some are saddle points (D < 0), not extrema. If the second-derivative test is inconclusive (D = 0), further analysis is needed. Setting ∇f = 0 is the first step; classification requires the Hessian test; global optimality also requires checking boundary behavior."

- question: "Explain the role of D = f_xx · f_yy − (f_xy)² in the second-derivative test. What does its sign tell you, and why can't you conclude anything from f_xx alone?"
  type: short-answer
  answer: "D is the determinant of the Hessian matrix, which encodes curvature in all directions. D > 0 means the Hessian is definite (consistent curvature — either all upward or all downward), so the critical point is an extremum. D < 0 means the Hessian is indefinite (mixed curvature) — a saddle point. f_xx alone tells you curvature only in the x-direction; the cross terms f_xy capture how curvature in one direction depends on the other, and D combines the full picture."
  explanation: "The intuition: f_xx could be positive (bowl-shaped in x) while f_yy is negative (inverted in y) — that's a saddle. The determinant D = f_xx·f_yy − f_xy² is the product of the Hessian's eigenvalues, so its sign tells you whether both eigenvalues share a sign (definite — extremum) or have opposite signs (indefinite — saddle)."
```

## Explainer

Optimization in single-variable calculus works by finding points where f'(x) = 0 (critical points) and then applying the second derivative test to classify them as local max, min, or neither. Multivariable unconstrained optimization follows exactly the same logical structure, with the gradient replacing the derivative and the Hessian replacing the second derivative.

The first step is finding **critical points**: solve ∇f = 0, meaning both ∂f/∂x = 0 and ∂f/∂y = 0 simultaneously. Geometrically, the gradient points in the direction of steepest ascent; setting it to zero means the surface is locally "flat" at that point — neither ascending nor descending in any direction. Solving the system ∂f/∂x = 0 and ∂f/∂y = 0 gives you the candidate locations for extrema. This is typically a system of nonlinear equations, and solving it may require algebraic manipulation, substitution, or numerical methods.

The second step is **classifying each critical point** using the Hessian matrix H, whose entries are the second partial derivatives: H = [[f_xx, f_xy], [f_yx, f_yy]]. You already know that the Hessian encodes the local curvature of f in all directions. The second derivative test says: compute D = f_xx · f_yy − (f_xy)². If D > 0 and f_xx > 0, the point is a **local minimum**. If D > 0 and f_xx < 0, it is a **local maximum**. If D < 0, it is a **saddle point** — like the center of a mountain pass, which is a minimum along one direction but a maximum along another. If D = 0, the test is inconclusive. The quantity D is the determinant of H, and its sign tells you whether H is positive definite (bowl-shaped upward), negative definite (bowl-shaped downward), or indefinite (saddle).

The third step — checking boundary behavior — depends on the domain. If f is defined on all of ℝ² and f → ∞ in all directions, then a local minimum is a global minimum. But if the domain is bounded, you must also examine what happens as you approach the boundary (or, on a closed bounded domain, optimize f on the boundary using single-variable techniques). A critical point in the interior is only guaranteed to be a **global** optimum if the function behaves appropriately at infinity or at the boundary. Forgetting this step is the most common source of wrong answers in applied optimization problems.
