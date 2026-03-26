---
id: critical-points-multivariable-classification
title: Critical Points and Classification of Extrema
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: gradient-vector
  type: hard
- id: critical-points-multivariable
  type: hard
builds-toward:
- second-partials-test-extrema
tags:
- critical-points
- extrema
- saddle-points
stage: formal-systems
status: validated
---

# Critical Points and Classification of Extrema

## Core Idea
A critical point (a, b) of f(x, y) satisfies ∇f(a, b) = 0 (or ∇f is undefined). Critical points are candidates for local maxima, local minima, or saddle points. Every continuous function on a closed bounded set attains its absolute maximum and minimum.

## Questions

```yaml
- question: "At a critical point of f(x, y), the second partial derivatives are f_xx = 3, f_yy = 1, and f_xy = 2. How should this point be classified?"
  type: multiple-choice
  options:
    - "Local minimum, because f_xx > 0 and f_yy > 0"
    - "Local maximum, because the mixed partial f_xy is positive"
    - "Saddle point, because D = f_xx · f_yy − (f_xy)² = 3 − 4 = −1 < 0"
    - "Inconclusive, because f_xx and f_yy have different magnitudes"
  answer: 2
  explanation: "The discriminant D = f_xx · f_yy − (f_xy)² = (3)(1) − (2)² = 3 − 4 = −1 < 0, which classifies this as a saddle point regardless of the signs of f_xx and f_yy. Option A is the most tempting error: students see positive f_xx and f_yy and conclude 'upward curvature everywhere.' But the mixed partial term in D captures the twisting of the surface that produces a saddle. D < 0 means the principal curvatures have opposite signs — the surface curves up in some directions and down in others."

- question: "You are maximizing f(x, y) over a closed bounded region. You find all interior critical points where ∇f = 0 and apply the second derivative test. What must you still do before identifying the absolute maximum?"
  type: multiple-choice
  options:
    - "Nothing — the largest value at any local maximum candidate is the absolute maximum"
    - "Verify that D > 0 at each critical point to confirm they are true extrema"
    - "Evaluate f on the boundary of the region and compare all values"
    - "Check whether the function is concave down globally by verifying f_xx < 0 everywhere"
  answer: 2
  explanation: "By the extreme value theorem, a continuous function on a closed bounded region attains its absolute maximum and minimum — but the maximum might occur on the boundary, not at an interior critical point. You must parameterize the boundary (it's typically a curve), optimize f along it using single-variable methods, and then compare those boundary values against the interior critical point values. Stopping at interior critical points misses any extrema that occur on the edge of the domain."

- question: "A saddle point of f(x, y) is a critical point where the gradient ∇f is zero but the point is neither a local maximum nor a local minimum."
  type: true-false
  answer: true
  explanation: "At a saddle point, ∇f = 0 exactly as at a local extremum — the gradient condition alone cannot distinguish the cases. A saddle point looks like a mountain pass: the function rises in some directions from the point and falls in others. The discriminant D = f_xx · f_yy − (f_xy)² < 0 detects this by signaling that the surface has opposite curvatures in different directions."

- question: "If the discriminant D > 0 at a critical point, then that point is a local minimum."
  type: true-false
  answer: false
  explanation: "D > 0 means the curvature has a consistent sign in all directions (a pure bowl shape), but it does not specify which way the bowl opens. If D > 0 and f_xx > 0, the bowl opens upward — local minimum. If D > 0 and f_xx < 0, the bowl opens downward — local maximum. Both conditions together are needed: D > 0 rules out saddle points, and the sign of f_xx reveals whether the bowl is a minimum or maximum."

- question: "Why is the condition ∇f = 0 necessary but not sufficient to conclude that a point is a local minimum of f(x, y)?"
  type: short-answer
  answer: "A local minimum requires the function to increase in every direction away from the point, which forces both partial derivatives to be zero — hence ∇f = 0 is necessary. But saddle points also have ∇f = 0: the function rises in some directions and falls in others, so there is no local extremum despite the zero gradient. The gradient test cannot distinguish between local minima, local maxima, and saddle points. Additional information about the second-order behavior — specifically the discriminant D and the sign of f_xx — is required to classify which type of critical point it is."
  explanation: "This mirrors the one-variable situation: f′(x) = 0 is necessary for a local extremum, but inflection points also satisfy f′ = 0 (e.g., f(x) = x³ at x = 0). The second derivative test resolves the ambiguity in one variable; the discriminant resolves it in two variables."
```

## Explainer

From your prerequisite on the gradient, you know that ∇f at a point gives the direction and magnitude of steepest ascent. A **critical point** is where this steepest-ascent direction ceases to exist in the usual sense: the gradient is zero, meaning the function is instantaneously flat in every direction. In single-variable calculus you found critical points where f′(x) = 0; the multivariable condition ∇f = 0 is the exact generalization — it requires both ∂f/∂x = 0 and ∂f/∂y = 0 simultaneously.

The three types of critical point correspond to three distinct topographic shapes. A **local minimum** looks like the bottom of a bowl: the function rises in every direction away from the point. A **local maximum** looks like the top of a hill: the function falls in every direction. A **saddle point** looks like a mountain pass: the function rises in some directions and falls in others. The gradient is zero at all three, so the gradient condition alone cannot tell them apart — that requires additional information about the second-order behavior.

The **second derivative test** for two variables uses the **Hessian matrix** H, whose entries are the second partial derivatives: H = [[f_xx, f_xy], [f_yx, f_yy]]. The **discriminant** D = f_xx · f_yy − (f_xy)² captures the Hessian's determinant. If D > 0 and f_xx > 0, the point is a local minimum (bowl opening upward). If D > 0 and f_xx < 0, it's a local maximum (bowl opening downward). If D < 0, it's a saddle point. If D = 0, the test is inconclusive — higher-order methods are needed. The intuition: D > 0 means both principal curvatures have the same sign (pure bowl), while D < 0 means they have opposite signs (saddle).

For optimization on a closed bounded region, the story extends beyond interior critical points. By the extreme value theorem, a continuous function on a compact set attains its absolute extrema somewhere. The candidates are: all interior critical points where ∇f = 0, and all points on the boundary. The boundary is typically a curve, so you parameterize it and apply single-variable optimization there. Checking all candidates and comparing values gives the absolute maximum and minimum — this is the complete algorithm for constrained optimization on closed bounded domains.
