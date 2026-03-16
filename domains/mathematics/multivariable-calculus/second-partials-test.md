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

## Explainer

From the single-variable second derivative test (your soft prerequisite), you know that at a critical point where f'(x) = 0, the sign of f''(x) tells you the curvature: f'' > 0 means concave up (local min), f'' < 0 means concave down (local max). The multivariable version faces a harder question: a surface at a critical point can curve differently in different directions. It might curve upward along one cross-section and downward along another — that is a saddle point, and no single second derivative can detect it alone.

The **Hessian matrix** H at a critical point (a, b) collects all second-order information: H = [[f_xx, f_xy], [f_xy, f_yy]], where the diagonal entries measure curvature along the x- and y-axes, and the off-diagonal entry f_xy captures how the x-slope changes as y varies (the "twist"). The **discriminant** D = f_xx · f_yy − (f_xy)² is the determinant of H. Geometrically, D encodes whether H is positive definite (curves the same way in every direction), negative definite (curves the opposite way in every direction), or indefinite (curves differently in different directions).

The classification rule flows from this: if D > 0, all directions of curvature have the same sign, so the surface is either a bowl (all curving up → local min) or an inverted bowl (all curving down → local max). Checking f_xx resolves which: f_xx > 0 means the x-cross-section curves up, so it is a **local minimum**; f_xx < 0 means a **local maximum**. If D < 0, the Hessian is indefinite — the surface curves up in some directions and down in others, producing a **saddle point**. If D = 0, the Hessian is singular and the test gives no information; you must analyze higher-order behavior.

A helpful geometric intuition: imagine slicing the surface with vertical planes through the critical point at various angles. If D > 0, every such cross-section is either concave up or concave down (all agreeing), like a bowl. If D < 0, some cross-sections are concave up and others concave down — you can find a direction where the surface looks like a local minimum and another direction where it looks like a local maximum, creating the characteristic saddle shape. The discriminant being negative detects this geometric incompatibility between different directions, exactly capturing why the critical point can be neither a max nor a min.
