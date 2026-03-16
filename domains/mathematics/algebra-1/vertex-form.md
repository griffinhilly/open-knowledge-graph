---
id: vertex-form
title: Vertex Form of Quadratic Functions
domain: mathematics
course: algebra-1
prerequisites:
- id: graphing-quadratics
  type: hard
- id: solving-multi-step-equations
  type: hard
builds-toward:
- solving-quadratic-equations-completing-the-square
- function-transformations
tags:
- vertex-form
- quadratics
- parabolas
- transformations
stage: abstract-reasoning
status: validated
---
# Vertex Form of Quadratic Functions

## Core Idea
Vertex form is y = a(x − h)² + k, where (h, k) is the vertex of the parabola and a determines the direction and width. This form makes graphing straightforward — plot the vertex and use the value of a to determine the shape. Converting from standard form (y = ax² + bx + c) to vertex form requires completing the square. Vertex form reveals the transformations applied to the parent function y = x²: the graph is shifted h units horizontally, k units vertically, and stretched or compressed by a factor of |a|.

## How It's Best Learned
Start with the parent function y = x² and apply transformations one at a time: vertical shift (y = x² + k), horizontal shift (y = (x − h)²), then both together. Show that a > 1 narrows the parabola and 0 < a < 1 widens it. Practice converting between vertex form and standard form by expanding and by completing the square. Graph directly from vertex form without converting.

## Common Misconceptions
- Getting the sign of h wrong: in y = (x − 3)² + 1, the vertex is (3, 1), not (−3, 1). The minus sign is built into the form.
- Confusing the effect of a on width (larger |a| = narrower, not wider).
- Thinking vertex form and standard form are different functions (they are the same function written differently).

## Explainer

From graphing quadratics, you know that every parabola has a vertex — the turning point where the function changes from decreasing to increasing (or vice versa). **Vertex form**, y = a(x − h)² + k, is designed to make that vertex visible at a glance. The vertex is (h, k), readable directly from the equation. This is the payoff: instead of finding the vertex by computing −b/2a from standard form, you simply read it off.

The form is built from transformations of the parent parabola y = x², which you can think of as the "default" parabola with vertex at the origin. Each parameter shifts or scales it. Adding k shifts the graph up or down by k units — this is a vertical translation. Replacing x with (x − h) shifts the graph right by h units (left if h is negative) — this is a horizontal translation. The sign asymmetry is the main trap: (x − 3)² pushes the vertex to x = 3, not x = −3, because you need x = 3 to make the expression equal zero. Finally, the coefficient a stretches or compresses the parabola. When |a| > 1, the parabola is narrower than y = x²; when 0 < |a| < 1, it is wider. A negative a flips the parabola upside down.

Converting from standard form y = ax² + bx + c to vertex form requires **completing the square** — a technique you'll master in the next topic. But even now, you can convert in reverse: expand y = a(x − h)² + k by multiplying out (x − h)² = x² − 2hx + h², then distribute a, and collect constants. This gives back y = ax² + (−2ah)x + (ah² + k). Matching with standard form: b = −2ah, so h = −b/2a, and c = ah² + k, so k = c − ah². These are the standard formulas for the vertex — but vertex form makes them unnecessary.

The deepest insight is that every quadratic function has a vertex, and that vertex is the geometric center of symmetry of the parabola. The axis of symmetry is the vertical line x = h. Any input h + d gives the same output as h − d (the parabola is mirror-symmetric about this axis), because a(h + d − h)² + k = a(h − d − h)² + k = ad² + k. Vertex form exposes this symmetry that is hidden in standard form. When you later study function transformations, vertex form will generalize: any function can be shifted and scaled in the same pattern, not just quadratics.


