---
id: systems-nonlinear
title: Nonlinear Systems of Equations
domain: mathematics
course: algebra-2
prerequisites:
- id: systems-substitution
  type: hard
- id: graphing-quadratics
  type: soft
- id: conic-sections-circles
  type: soft
builds-toward: []
tags:
- systems
- nonlinear
- quadratic
- conics
- substitution
stage: formal-systems
status: validated
---
# Nonlinear Systems of Equations

## Core Idea
A nonlinear system contains at least one equation that is not linear — typically a quadratic, circle, or other conic. Solving these systems means finding all points where the curves intersect. A line and a parabola can intersect in 0, 1, or 2 points; two conics can intersect in up to 4 points. The primary algebraic method is substitution: solve the simpler equation for one variable and substitute into the other. Graphing provides a visual check on the number and approximate location of solutions. Nonlinear systems model real-world situations where a constraint interacts with a curved relationship, such as projectile trajectories meeting boundaries.

## How It's Best Learned
Start with a line-parabola system where substitution is straightforward, then progress to circle-line and two-conic systems. Always sketch the graphs first so students can predict how many solutions to expect. After solving algebraically, plot the solutions on the graph to confirm. Include systems with no real solutions to reinforce that intersection is not guaranteed.

## Common Misconceptions
- Assuming a line and parabola always intersect in exactly two points — they may intersect in 0 or 1.
- Forgetting to substitute back to find both coordinates after solving for one variable.

## Explainer

In linear systems, the equations are lines, and lines can intersect in exactly one point, no points (parallel), or infinitely many points (same line). Once at least one equation is nonlinear, the curves have more complex shapes, and intersections become richer: more solutions are possible, and the geometry becomes more interesting. A **nonlinear system** is simply any system where at least one equation is not linear — often a quadratic, parabola, or circle.

The algebraic workhorse is **substitution**, the same technique you used for linear systems. The strategy: pick the simpler equation, isolate one variable, and substitute the resulting expression into the other equation. What changes compared to linear systems is that after substitution you often face a quadratic equation, which you must solve — potentially getting 0, 1, or 2 values. Each value of x gives a y (or vice versa), so you may end up with multiple solution pairs. Always substitute back into the original to find the complete (x, y) pair, not just the x-value.

Geometry guides your expectations. Before solving algebraically, sketch both curves to count expected intersections. A line and a parabola can intersect in 0, 1, or 2 points depending on whether the line misses, is tangent to, or crosses the parabola. A circle and a line have the same three cases. Two parabolas or a circle and a parabola can intersect in up to 4 points. When your algebra produces a quadratic with a negative discriminant, that signals 0 real intersections — the curves don't meet in the real plane. A discriminant of zero means exactly 1 intersection (tangency).

Consider the system y = x² and y = x + 2. Substitute the first into the second: x² = x + 2, giving x² − x − 2 = 0, which factors as (x − 2)(x + 1) = 0. So x = 2 or x = −1. Substituting back: when x = 2, y = 4; when x = −1, y = 1. The solutions are (2, 4) and (−1, 1). This matches what a sketch confirms: the line y = x + 2 crosses the upward parabola y = x² in two places. The combination of geometric reasoning — which tells you how many solutions to expect — and algebraic substitution — which finds them precisely — is the complete toolkit for nonlinear systems.
