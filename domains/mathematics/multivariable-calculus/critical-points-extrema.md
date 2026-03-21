---
id: critical-points-extrema
title: Critical Points and Local Extrema
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: critical-points-multivariable
  type: hard
- id: partial-derivatives-basics
  type: hard
builds-toward:
- second-partials-test
- optimization-multivariable-basics
tags:
- critical-points
- extrema
stage: advanced
status: draft
---

# Critical Points and Local Extrema

## Core Idea
A critical point satisfies f_x = 0 and f_y = 0 (where partials exist). Extrema occur at critical points, boundary points, or points where partials don't exist. Not all critical points are extrema; some are saddle points.

## Questions

```yaml
- question: "You find a point (a, b) where f_x(a,b) = 0 and f_y(a,b) = 0, and computing the Hessian gives D = f_xx·f_yy − (f_xy)² = −5. What can you conclude about this point?"
  type: multiple-choice
  options:
    - "It is a local minimum because D is negative"
    - "It is a local maximum because the discriminant is negative"
    - "It is a saddle point — the function has a local min in some directions and a local max in others through this point"
    - "The test is inconclusive; more information is needed to classify the point"
  answer: 2
  explanation: "D < 0 is the definitive sign of a saddle point. The function increases in some directions through (a, b) and decreases in others — like the geometry of a mountain pass. D > 0 is required for the point to be an extremum (with the sign of f_xx then distinguishing max from min). D = 0 is the inconclusive case. Options A and B confuse the sign rule: a negative D does not indicate a minimum or maximum of any kind."

- question: "You want to find the global minimum of f(x, y) = x² − y² on the closed disk x² + y² ≤ 4. After setting f_x = f_y = 0, you find one interior critical point at the origin. What must you do next to guarantee you have found the global minimum?"
  type: multiple-choice
  options:
    - "Evaluate f at the origin — since it is the only critical point, it must be the global minimum"
    - "Use the second partials test to classify the origin, and if it is a minimum, it must be the global minimum"
    - "Also evaluate f along the boundary circle x² + y² = 4, compare all values, and take the smallest"
    - "Check for additional interior critical points using the Hessian's eigenvalues"
  answer: 2
  explanation: "For global extrema on a closed, bounded domain, you must compare the values at ALL candidates: interior critical points AND boundary points. The origin is actually a saddle point here (D = (2)(−2) − 0² = −4 < 0), so the global minimum lies on the boundary. On the boundary circle, f = x² − y² = x² − (4 − x²) = 2x² − 4, minimized at x = 0, giving f = −4. The boundary analysis is not optional — on a closed domain, global extrema can and often do occur on the boundary."

- question: "Every critical point of a differentiable function f(x, y) — every point where f_x = 0 and f_y = 0 — is either a local maximum or a local minimum."
  type: true-false
  answer: false
  explanation: "Saddle points are critical points that are neither local maxima nor local minima. At a saddle point, the function increases in some directions and decreases in others. A classic example is f(x, y) = x² − y², where the origin satisfies f_x = f_y = 0 but is a saddle: the x-axis slice shows a minimum, and the y-axis slice shows a maximum. The second partials test (using the discriminant D) is needed to classify critical points, and D < 0 identifies saddle points."

- question: "The global maximum of a continuous function on a closed, bounded region might occur on the boundary rather than at a point where both partial derivatives are zero."
  type: true-false
  answer: true
  explanation: "On a closed domain, boundary points are candidates for global extrema that are completely missed by setting partial derivatives to zero. Interior critical points are candidates only in the interior. A simple example: f(x, y) = x on the unit square [0,1]² has no interior critical points (f_x = 1 ≠ 0 everywhere), so the maximum of 1 is achieved on the boundary edge x = 1. The complete procedure always requires checking interior critical points AND performing a separate optimization on each boundary piece."

- question: "What is the key new phenomenon that distinguishes critical point analysis for functions of two variables from the single-variable case, and how does the second partials test address it?"
  type: short-answer
  answer: "In single-variable calculus, a critical point (f'(x) = 0) is classified simply as a max, min, or inflection point. In two variables, a third type of critical point appears: the saddle point, where the function has a local minimum in some cross-sectional directions and a local maximum in others. The second partials test addresses this by computing the discriminant D = f_xx·f_yy − (f_xy)², which measures the curvature behavior simultaneously in all directions. D > 0 means the surface curves the same way in every direction (bowl-shaped up or down = extremum); D < 0 means it curves in opposite directions in different cross-sections (saddle). This classification has no single-variable analogue."
  explanation: "The geometric intuition is crucial: in one variable, you're on a curve and a flat-slope point must be a turnaround. In two variables, you're on a surface, and a flat-slope point could be a peak, a valley, or a mountain pass where you're at the bottom of the pass in one direction and the top of the ridge in another. The Hessian matrix and its determinant D capture whether the surface behaves like a bowl (consistent curvature) or a saddle (opposing curvatures)."
```

## Explainer

In single-variable calculus, finding extrema meant setting f'(x) = 0 and checking. For a function of two variables, the same instinct applies but the geometry is richer. A **critical point** of f(x, y) is a point where both partial derivatives vanish: f_x = 0 and f_y = 0. The intuition is the same as in one dimension — at a local max or min, the function must be "flat" in every direction, so its rate of change in the x-direction and in the y-direction must both be zero. From your work with partial derivatives, you know how to compute f_x and f_y, so finding critical points reduces to solving this 2×2 system.

The key complication compared to one variable is that vanishing partial derivatives no longer guarantee an extremum. Imagine a mountain pass: at the saddle point, the trail running east-west reaches a local minimum (you're at the bottom of the pass), while the trail running north-south reaches a local maximum (you're at the top of the ridge). Both partial derivatives are zero, but you're neither at a local max nor a local min of the full function — you're at a **saddle point**. The surface curves upward in some directions and downward in others. This is the fundamentally new phenomenon in multivariable calculus.

So finding critical points is the first step; classifying them is the second. The **second partials test** (which this topic builds toward) uses the **Hessian** — the matrix of second partial derivatives — to determine the nature of each critical point. The discriminant D = f_xx f_yy − (f_xy)² tells the story: D > 0 and f_xx > 0 means local minimum, D > 0 and f_xx < 0 means local maximum, D < 0 means saddle point, and D = 0 is inconclusive. Without this classification step, you know where to look for extrema but not which candidates are actually extrema.

One more important subtlety: on a closed, bounded domain, the global extrema might not occur at interior critical points at all — they might occur on the **boundary**. The complete procedure for finding global extrema on a closed domain is: find all interior critical points, evaluate f at each; then analyze the boundary separately (reducing to a one-variable optimization on each boundary piece); then compare all values. Critical points with f_x = f_y = 0 are necessary but not sufficient for a global extremum, and they play no role at boundaries where the domain constrains the point to stay on the edge.
