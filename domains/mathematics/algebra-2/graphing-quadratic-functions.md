---
id: graphing-quadratic-functions
title: "Graphing Quadratic Functions: Vertex and Intercepts"
domain: mathematics
course: algebra-2
prerequisites:
  - id: solving-quadratic-equations-completing-the-square
    type: hard
  - id: quadratic-formula-review
    type: hard
builds-toward:
  - quadratic-inequalities
  - conic-sections-parabolas
tags: [quadratics, graphing, vertex-form, parabolas]
stage: abstract-reasoning
status: validated
---

# Graphing Quadratic Functions: Vertex and Intercepts

## Core Idea
The graph of f(x) = ax^2 + bx + c is a parabola. Key features: the vertex is at (-b/(2a), f(-b/(2a))), which is the minimum (a > 0) or maximum (a < 0); the axis of symmetry is x = -b/(2a); x-intercepts come from solving f(x) = 0; the y-intercept is c. Vertex form f(x) = a(x - h)^2 + k directly reveals the vertex (h, k). Converting between standard and vertex form via completing the square is essential.

## How It's Best Learned
Graph parabolas by finding the vertex, axis of symmetry, intercepts, and a few additional points. Practice converting between standard form and vertex form. Discuss how the sign and magnitude of a affect the parabola's direction and width. Use graphing technology to verify hand-drawn graphs.

## Common Misconceptions
- Getting the sign of h wrong when reading vertex form (y = a(x - h)^2 + k has vertex at (h, k), not (-h, k)).
- Thinking the vertex is always at the y-intercept.
- Not recognizing that a parabola with no real x-intercepts (D < 0) does not cross the x-axis.

## Explainer

You've already solved quadratic equations by completing the square and by the quadratic formula — both of which find the x-intercepts. Graphing quadratics draws on both skills but shifts the goal: instead of just finding specific x-values, you want to see the shape of the entire function and understand what determines it.

The **vertex** is the most important feature of a parabola. It's the turning point — the minimum if the parabola opens upward (a > 0) or the maximum if it opens downward (a < 0). From standard form f(x) = ax² + bx + c, the vertex x-coordinate is x = −b/(2a). This formula isn't arbitrary: it's the midpoint of the two x-intercepts, which are symmetric about the axis of symmetry. You can derive it by completing the square on ax² + bx + c — the same process you practiced before — which transforms the expression directly into **vertex form** f(x) = a(x − h)² + k, where (h, k) is the vertex.

The sign trap in vertex form trips almost everyone initially. In f(x) = a(x − h)² + k, the vertex is at x = h, not x = −h. Why? Because the expression (x − h)² equals zero when x = h, making the squared term vanish and leaving f(h) = k. If you see f(x) = (x + 3)² − 1, rewrite it as (x − (−3))² − 1 to read off h = −3, k = −1. The vertex is (−3, −1), not (3, −1).

To graph a parabola systematically: (1) find the vertex, (2) note whether it opens up or down from the sign of a, (3) find the y-intercept by setting x = 0 (it's just c), and (4) find x-intercepts by solving ax² + bx + c = 0, using the quadratic formula if needed. The discriminant b² − 4ac tells you how many x-intercepts to expect before you solve: two if positive, one (a tangent touch) if zero, none (complex roots) if negative. Parabolas with no real x-intercepts live entirely above or entirely below the x-axis, and the vertex reveals which case you're in.
