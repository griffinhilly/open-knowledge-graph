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

## Explainer

In single-variable calculus, finding extrema meant setting f'(x) = 0 and checking. For a function of two variables, the same instinct applies but the geometry is richer. A **critical point** of f(x, y) is a point where both partial derivatives vanish: f_x = 0 and f_y = 0. The intuition is the same as in one dimension — at a local max or min, the function must be "flat" in every direction, so its rate of change in the x-direction and in the y-direction must both be zero. From your work with partial derivatives, you know how to compute f_x and f_y, so finding critical points reduces to solving this 2×2 system.

The key complication compared to one variable is that vanishing partial derivatives no longer guarantee an extremum. Imagine a mountain pass: at the saddle point, the trail running east-west reaches a local minimum (you're at the bottom of the pass), while the trail running north-south reaches a local maximum (you're at the top of the ridge). Both partial derivatives are zero, but you're neither at a local max nor a local min of the full function — you're at a **saddle point**. The surface curves upward in some directions and downward in others. This is the fundamentally new phenomenon in multivariable calculus.

So finding critical points is the first step; classifying them is the second. The **second partials test** (which this topic builds toward) uses the **Hessian** — the matrix of second partial derivatives — to determine the nature of each critical point. The discriminant D = f_xx f_yy − (f_xy)² tells the story: D > 0 and f_xx > 0 means local minimum, D > 0 and f_xx < 0 means local maximum, D < 0 means saddle point, and D = 0 is inconclusive. Without this classification step, you know where to look for extrema but not which candidates are actually extrema.

One more important subtlety: on a closed, bounded domain, the global extrema might not occur at interior critical points at all — they might occur on the **boundary**. The complete procedure for finding global extrema on a closed domain is: find all interior critical points, evaluate f at each; then analyze the boundary separately (reducing to a one-variable optimization on each boundary piece); then compare all values. Critical points with f_x = f_y = 0 are necessary but not sufficient for a global extremum, and they play no role at boundaries where the domain constrains the point to stay on the edge.
