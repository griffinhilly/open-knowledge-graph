---
id: graphing-quadratics
title: Graphing Quadratic Functions
domain: mathematics
course: algebra-1
prerequisites:
- id: solving-quadratics-by-factoring
  type: hard
- id: graphing-linear-equations
  type: hard
builds-toward:
- vertex-form
- function-transformations
- conic-sections-overview
tags:
- quadratics
- graphing
- parabolas
- vertex
- axis-of-symmetry
stage: abstract-reasoning
status: validated
---
# Graphing Quadratic Functions

## Core Idea
The graph of y = ax² + bx + c is a parabola — a U-shaped curve that opens upward when a > 0 and downward when a < 0. Key features include the vertex (the highest or lowest point), the axis of symmetry (the vertical line through the vertex, x = −b/(2a)), the y-intercept (at c), and the x-intercepts (the zeros or roots, found by solving ax² + bx + c = 0). Understanding parabolas is essential because quadratic functions model projectile motion, area optimization, revenue curves, and many other real-world phenomena.

## How It's Best Learned
Find the vertex using x = −b/(2a), then evaluate to find the y-coordinate. Plot the vertex, axis of symmetry, y-intercept, and x-intercepts (if they exist). Use additional points for accuracy, exploiting symmetry (points equidistant from the axis have equal y-values). Compare graphs with different values of a (wider, narrower, upward, downward). Connect roots on the graph to solutions of the equation.

## Common Misconceptions
- Forgetting the negative sign in x = −b/(2a) for the vertex.
- Thinking all parabolas open upward (the sign of a determines direction).
- Confusing the vertex with the y-intercept.
- Thinking a parabola that does not cross the x-axis has "no graph" (it exists, just no real x-intercepts).

## Explainer

You already know how to graph a line: pick two points, connect them, and the slope tells you how steeply it rises. A quadratic function y = ax² + bx + c produces a **parabola** — a U-shaped curve — because squaring the input causes the output to grow faster and faster as x moves away from the center. Unlike a line, which changes at a constant rate, a quadratic accelerates. The sign of a immediately tells you the story: if a > 0, the parabola opens upward (a smile) with a minimum point; if a < 0, it opens downward (a frown) with a maximum point.

The most important feature to find first is the **vertex** — the tip of the U. It sits at x = −b/(2a), and you find the y-coordinate by plugging that x back into the equation. Think of the vertex as the "pivot point" of the curve. Everything else is symmetric around it, because squaring (x − h) gives the same value whether you go left or right from h. This symmetry gives you the **axis of symmetry**, the vertical line x = −b/(2a) that cuts the parabola exactly in half. Any point on one side of the axis has a mirror image on the other side at the same height — a fact you can use to plot the curve efficiently.

The y-intercept is always easy: set x = 0 and the formula gives y = c immediately, so the curve crosses the y-axis at the point (0, c). The **x-intercepts** (also called zeros or roots) are the solutions to ax² + bx + c = 0 — the same equations you solved by factoring in your prerequisite work. If the equation has two real solutions, the parabola crosses the x-axis at two points. If it has one repeated solution, the parabola just touches the x-axis at the vertex. If there are no real solutions, the parabola floats entirely above (or below) the x-axis — it still exists as a graph, it just never crosses zero.

The coefficient a controls more than direction: it controls **width**. A large |a| makes the parabola narrow and steep; a small |a| close to zero makes it wide and flat. Comparing y = x², y = 3x², and y = (1/3)x² on the same axes makes this vivid. This shape-stretching is a preview of function transformations you will study next, where multiplying the entire function by a constant stretches or compresses it vertically. Everything you learn about parabolas here — vertex, axis, roots, shape — will carry forward into vertex form, completing the square, conic sections, and eventually calculus, where the vertex is the point where the derivative equals zero.
