---
id: second-partials-test
title: The Second Partials Test
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: critical-points-multivariable
  type: hard
- id: higher-order-partial-derivatives
  type: hard
- id: second-derivative-test
  type: soft
builds-toward:
- lagrange-multipliers
tags:
- second-derivative-test
- Hessian
- discriminant
- local-extrema
stage: formal-systems
status: validated
---

# The Second Partials Test

## Core Idea
At a critical point (a, b) of f(x, y), the discriminant D = f_xx f_yy − (f_xy)² classifies the critical point. If D > 0 and f_xx > 0, it is a local minimum; if D > 0 and f_xx < 0, it is a local maximum; if D < 0, it is a saddle point; if D = 0, the test is inconclusive. Geometrically, D is the determinant of the Hessian matrix H = [[f_xx, f_xy], [f_xy, f_yy]], which encodes all second-order curvature information at the critical point.

## How It's Best Learned
Connect D to the Hessian determinant explicitly. Have students practice with examples where each case occurs, including D = 0 (to show the test's limits). Emphasize that D > 0 means the surface curves the same way in all directions (definite curvature), while D < 0 means it curves differently in different directions (indefinite curvature — a saddle).

## Common Misconceptions
- D > 0 alone is not sufficient; you must also check the sign of f_xx to distinguish max from min.
- D = 0 is genuinely inconclusive — all three outcomes (max, min, saddle) are possible, and higher-order terms must be examined.
- The second partials test applies to interior critical points only; boundary behavior requires separate analysis.

## Questions

```yaml
- question: "At a critical point of f(x,y), you compute f_xx = -3, f_yy = -2, f_xy = 1. What is the correct classification?"
  type: multiple-choice
  options:
    - "Saddle point, because f_xx and f_yy have the same sign"
    - "Local maximum, because D = f_xx·f_yy − (f_xy)² = 5 > 0 and f_xx < 0"
    - "Local minimum, because both f_xx and f_yy are negative"
    - "Inconclusive, because D > 0 alone is insufficient without knowing f_xy's sign"
  answer: 1
  explanation: "D = (-3)(-2) − (1)² = 6 − 1 = 5 > 0, so curvature is consistent in all directions (the Hessian is definite). Since f_xx = -3 < 0, the surface curves downward in the x-direction, so it is a local maximum — not a minimum. Option C is the most tempting wrong answer: students see that both diagonal entries are negative and conclude minimum, forgetting that the correct procedure is to check the sign of f_xx after confirming D > 0."

- question: "At a critical point of g(x,y), the discriminant D = f_xx·f_yy − (f_xy)² = 0. A student concludes: 'D = 0 means the Hessian is singular, so this must be a saddle point.' Is this correct?"
  type: multiple-choice
  options:
    - "Yes — a singular Hessian always corresponds to a saddle point in two variables"
    - "No — D = 0 is genuinely inconclusive; the critical point could be a local max, local min, or saddle"
    - "No — D = 0 means the test is inconclusive, but in practice it always indicates a flat region, not an extremum"
    - "Yes — D = 0 means one principal curvature is zero, ruling out strict extrema"
  answer: 1
  explanation: "D = 0 is genuinely inconclusive — all three outcomes (local max, local min, saddle point) are possible, and examples can be constructed for each. The function f(x,y) = x⁴ + y⁴ has a local minimum at (0,0) with D = 0; g(x,y) = x³ has a saddle at (0,0) with D = 0; h(x,y) = −x⁴ − y⁴ has a local max with D = 0. When D = 0, higher-order behavior must be examined. The student's reasoning — that a singular Hessian implies a saddle — is a common but incorrect inference."

- question: "At a critical point where D > 0, the sign of f_yy can be used instead of f_xx to determine whether the point is a local max or min, and it will give the same classification."
  type: true-false
  answer: true
  explanation: "When D > 0, the Hessian is positive definite (f_xx > 0 and f_yy > 0 → local min) or negative definite (f_xx < 0 and f_yy < 0 → local max). Because D > 0 forces f_xx and f_yy to have the same sign (if they differed in sign, D = f_xx·f_yy − (f_xy)² ≤ f_xx·f_yy < 0), checking f_yy gives the same answer as checking f_xx. The convention to use f_xx is just that — a convention, not a mathematical requirement."

- question: "At a critical point where D < 0, the second partials test is inconclusive — more information is needed to determine whether the point is a max, min, or saddle."
  type: true-false
  answer: false
  explanation: "D < 0 is conclusive: it guarantees a saddle point. A negative discriminant means the Hessian is indefinite — the surface curves upward in some directions and downward in others. You can always find two directions through the critical point where one cross-section is concave up and the other is concave down. This incompatibility between directions is precisely what defines a saddle point. The genuinely inconclusive case is D = 0, not D < 0."

- question: "Explain geometrically why D < 0 at a critical point guarantees a saddle point rather than a local extremum."
  type: short-answer
  answer: "D < 0 means the Hessian matrix is indefinite — its eigenvalues have opposite signs. Geometrically, this means the surface has positive curvature (concave up) in some directions through the critical point and negative curvature (concave down) in others. A local minimum requires the surface to curve upward in every direction; a local maximum requires it to curve downward in every direction. When curvature changes sign depending on direction, neither condition is met, and the critical point must be a saddle — a point that is a local minimum along some cross-sections and a local maximum along others."
  explanation: "The discriminant D = f_xx·f_yy − (f_xy)² is the determinant of the Hessian, which is the product of its eigenvalues. A negative determinant means the eigenvalues have opposite signs — precisely the mathematical statement that curvature is not consistent in all directions. The geometric picture — slicing the surface at various angles through the critical point and observing that some slices curve up while others curve down — makes this intuitively clear."
```

## Explainer

From the single-variable second derivative test (your soft prerequisite), you know that at a critical point where f'(x) = 0, the sign of f''(x) tells you the curvature: f'' > 0 means concave up (local min), f'' < 0 means concave down (local max). The multivariable version faces a harder question: a surface at a critical point can curve differently in different directions. It might curve upward along one cross-section and downward along another — that is a saddle point, and no single second derivative can detect it alone.

The **Hessian matrix** H at a critical point (a, b) collects all second-order information: H = [[f_xx, f_xy], [f_xy, f_yy]], where the diagonal entries measure curvature along the x- and y-axes, and the off-diagonal entry f_xy captures how the x-slope changes as y varies (the "twist"). The **discriminant** D = f_xx · f_yy − (f_xy)² is the determinant of H. Geometrically, D encodes whether H is positive definite (curves the same way in every direction), negative definite (curves the opposite way in every direction), or indefinite (curves differently in different directions).

The classification rule flows from this: if D > 0, all directions of curvature have the same sign, so the surface is either a bowl (all curving up → local min) or an inverted bowl (all curving down → local max). Checking f_xx resolves which: f_xx > 0 means the x-cross-section curves up, so it is a **local minimum**; f_xx < 0 means a **local maximum**. If D < 0, the Hessian is indefinite — the surface curves up in some directions and down in others, producing a **saddle point**. If D = 0, the Hessian is singular and the test gives no information; you must analyze higher-order behavior.

A helpful geometric intuition: imagine slicing the surface with vertical planes through the critical point at various angles. If D > 0, every such cross-section is either concave up or concave down (all agreeing), like a bowl. If D < 0, some cross-sections are concave up and others concave down — you can find a direction where the surface looks like a local minimum and another direction where it looks like a local maximum, creating the characteristic saddle shape. The discriminant being negative detects this geometric incompatibility between different directions, exactly capturing why the critical point can be neither a max nor a min.
