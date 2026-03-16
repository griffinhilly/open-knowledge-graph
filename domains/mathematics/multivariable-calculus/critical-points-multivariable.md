---
id: critical-points-multivariable
title: Critical Points of Multivariable Functions
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: partial-derivatives
  type: hard
- id: gradient-vector
  type: hard
- id: optimization-problems
  type: soft
builds-toward:
- second-partials-test
- lagrange-multipliers
tags:
- critical-points
- optimization
- saddle-points
- local-extrema
stage: formal-systems
status: validated
---

# Critical Points of Multivariable Functions

## Core Idea
A critical point of f(x, y) is a point where ∇f = 0 (both partial derivatives are zero) or where ∇f is undefined. Critical points are candidates for local maxima, local minima, and saddle points. Unlike single-variable calculus, critical points in ℝ² can be saddle points — points that are local minima in one direction and local maxima in another, with no extreme value. Finding critical points requires solving a system of equations f_x = 0 and f_y = 0 simultaneously.

## How It's Best Learned
The saddle point concept has no single-variable analogue and requires geometric visualization. Show the surface z = x² − y² (a classic saddle) and identify that its critical point at the origin is neither a max nor a min. Then contrast with z = x² + y² (paraboloid) whose critical point at the origin is a minimum.

## Common Misconceptions
- Not every critical point is a local extremum — saddle points are critical points that are neither maxima nor minima.
- Setting f_x = 0 alone is insufficient; both partial derivatives must be zero (or undefined) simultaneously.
- A function defined on a closed bounded domain can also attain its extrema on the boundary, not just at interior critical points.

## Explainer

In single-variable calculus, you found candidates for local extrema by solving f′(x) = 0. The gradient ∇f you have studied is the multivariable generalization of f′: a vector whose components are the partial derivatives in each coordinate direction. A **critical point** of f(x, y) is a point where ∇f = **0** — that is, where both f_x = 0 and f_y = 0 simultaneously. Just as f′(x) = 0 was necessary (but not sufficient) for a local extremum in one variable, ∇f = **0** is necessary (but not sufficient) in two or more variables.

The geometric reason is the same as in one dimension. The gradient points in the direction of steepest ascent; if ∇f ≠ **0** at a point, you can move in the direction of ∇f to increase f, or opposite to it to decrease f. So any point with a nonzero gradient cannot be a local max or min — you can always improve the function value from there. Only when ∇f = **0** — all directional derivatives vanish — is the point a true standstill and a candidate for an extremum.

But multivariable calculus introduces a qualitatively new phenomenon with no single-variable analogue: the **saddle point**. Consider f(x, y) = x² − y². At the origin, f_x = 2x = 0 and f_y = −2y = 0, so the origin is a critical point. Moving along the x-axis (setting y = 0), the function equals x², which increases away from the origin — the origin looks like a minimum in this direction. Moving along the y-axis (setting x = 0), the function equals −y², which decreases — the origin looks like a maximum in this direction. No neighborhood of the origin contains it as either a local max or a local min; it is a saddle. In single-variable calculus, a critical point that is not a max or min is an inflection point — a single, degenerate case. In two dimensions, saddle points are a robust, generic phenomenon.

Finding critical points in practice requires solving the system f_x = 0 and f_y = 0 simultaneously, often yielding multiple solutions. Once you have the candidates, the second derivatives test (which builds on this topic) tells you which are maxima, which are minima, and which are saddles. For functions on a **closed bounded domain**, remember that global extrema may occur on the boundary rather than at interior critical points — boundary analysis must be combined with interior critical point analysis to find the true global max and min.

## Questions

```yaml
- question: "Find all critical points of f(x, y) = x³ − 3x + y² − 4y."
  type: short-answer
  answer: "Set f_x = 3x² − 3 = 0, giving x = ±1. Set f_y = 2y − 4 = 0, giving y = 2. Critical points are (1, 2) and (−1, 2)."
  explanation: "Each partial derivative is set to zero independently. f_x = 0 gives x² = 1, so x = 1 or x = −1. f_y = 0 gives y = 2. These combine to yield two critical points. Both are candidates for extrema; the second derivatives test distinguishes their nature."

- question: "A critical point is always a local maximum or local minimum."
  type: true-false
  answer: false
  explanation: "Saddle points are critical points that are neither local maxima nor local minima. At a saddle point, the function increases in some directions and decreases in others. The classic example is f(x, y) = x² − y², whose critical point at the origin is a saddle."

- question: "Why must you also check boundary points when optimizing a function on a closed bounded domain, not just interior critical points?"
  type: short-answer
  answer: "On a closed bounded domain, a continuous function is guaranteed (by the extreme value theorem) to attain its global maximum and minimum somewhere on the domain. These extrema may occur either at interior critical points (where ∇f = 0) or on the boundary. Interior critical points are only candidates for extrema inside the open domain; the boundary is a separate region that must be analyzed independently."
  explanation: "Consider f(x, y) = x + y on the unit disk x² + y² ≤ 1. The only critical point of the unrestricted function is nowhere (∇f = (1,1) ≠ 0 everywhere), so all extrema are on the boundary. The maximum is at (1/√2, 1/√2) and the minimum at (−1/√2, −1/√2), both on the boundary circle."
```
