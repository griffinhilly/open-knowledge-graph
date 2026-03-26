---
id: graphing-quadratic-functions
title: 'Graphing Quadratic Functions: Vertex and Intercepts'
domain: mathematics
course: algebra-2
prerequisites:
- id: solving-quadratic-equations-completing-the-square
  type: hard
- id: quadratic-formula-review
  type: hard
- id: vertex-form
  type: soft
builds-toward:
- quadratic-inequalities
- conic-sections-parabolas
tags:
- quadratics
- graphing
- vertex-form
- parabolas
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

## Questions

```yaml
- question: "What is the vertex of the parabola f(x) = (x + 5)² − 3?"
  type: multiple-choice
  options:
    - "(5, −3)"
    - "(−5, −3)"
    - "(5, 3)"
    - "(−5, 3)"
  answer: 1
  explanation: "In vertex form f(x) = a(x − h)² + k, the vertex is at (h, k). To read h correctly, rewrite (x + 5)² as (x − (−5))², so h = −5 and k = −3, giving vertex (−5, −3). The most common error is reading the vertex as (5, −3), taking the sign that appears in the expression rather than the actual value of h. The vertex is where the squared term equals zero, which happens when x = h = −5."

- question: "Before solving, you calculate the discriminant of a quadratic and get −4. What does this tell you about the graph?"
  type: multiple-choice
  options:
    - "The parabola opens downward"
    - "The vertex is below the x-axis"
    - "The parabola has no x-intercepts and lies entirely above or below the x-axis"
    - "The parabola touches the x-axis at exactly one point"
  answer: 2
  explanation: "A negative discriminant (b² − 4ac < 0) means the quadratic equation has no real solutions — the roots are complex. Graphically, this means the parabola never crosses the x-axis. Whether it lies entirely above or below depends on the sign of a: if a > 0 (opens upward) and the vertex is above the x-axis, it stays above; if a < 0 (opens downward) and the vertex is below, it stays below. A discriminant of zero means exactly one x-intercept (tangent touch); positive means two x-intercepts."

- question: "The axis of symmetry of a parabola always passes through the vertex."
  type: true-false
  answer: true
  explanation: "By definition, the axis of symmetry is the vertical line x = h, where h is the x-coordinate of the vertex. Every parabola is symmetric about this line — if you fold the parabola along it, both halves match perfectly. This relationship also explains why the axis of symmetry is the midpoint of the two x-intercepts when they exist: the x-intercepts are equidistant from the vertex on either side."

- question: "A parabola with a positive leading coefficient (a > 0) generally has two x-intercepts."
  type: true-false
  answer: false
  explanation: "The number of x-intercepts depends on the discriminant, not the sign of a. A parabola with a > 0 opens upward, but if its vertex is above the x-axis (k > 0), it never crosses the x-axis and has no real x-intercepts. For example, f(x) = x² + 1 has vertex (0, 1), opens upward, and has no x-intercepts. The sign of a determines direction of opening, not the number of intercepts."

- question: "Without solving the quadratic, explain how the discriminant lets you predict the shape and position of the graph relative to the x-axis."
  type: short-answer
  answer: "The discriminant b² − 4ac counts the real solutions to f(x) = 0, which are the x-intercepts. If positive: two real roots → parabola crosses the x-axis at two points. If zero: one repeated root → parabola touches the x-axis at exactly one point (the vertex is on the x-axis). If negative: no real roots → parabola doesn't cross the x-axis at all, lying entirely above (a > 0) or below (a < 0) it. Combined with the sign of a (direction) and the vertex coordinates, this gives a complete picture of the graph before any solving."
  explanation: "The discriminant is powerful because it answers the qualitative question ('how does this parabola relate to the x-axis?') instantly, without the work of the quadratic formula. In applied contexts — like determining whether a projectile reaches a certain height — this qualitative answer is often all you need."
```

## Explainer

You've already solved quadratic equations by completing the square and by the quadratic formula — both of which find the x-intercepts. Graphing quadratics draws on both skills but shifts the goal: instead of just finding specific x-values, you want to see the shape of the entire function and understand what determines it.

The **vertex** is the most important feature of a parabola. It's the turning point — the minimum if the parabola opens upward (a > 0) or the maximum if it opens downward (a < 0). From standard form f(x) = ax² + bx + c, the vertex x-coordinate is x = −b/(2a). This formula isn't arbitrary: it's the midpoint of the two x-intercepts, which are symmetric about the axis of symmetry. You can derive it by completing the square on ax² + bx + c — the same process you practiced before — which transforms the expression directly into **vertex form** f(x) = a(x − h)² + k, where (h, k) is the vertex.

The sign trap in vertex form trips almost everyone initially. In f(x) = a(x − h)² + k, the vertex is at x = h, not x = −h. Why? Because the expression (x − h)² equals zero when x = h, making the squared term vanish and leaving f(h) = k. If you see f(x) = (x + 3)² − 1, rewrite it as (x − (−3))² − 1 to read off h = −3, k = −1. The vertex is (−3, −1), not (3, −1).

To graph a parabola systematically: (1) find the vertex, (2) note whether it opens up or down from the sign of a, (3) find the y-intercept by setting x = 0 (it's just c), and (4) find x-intercepts by solving ax² + bx + c = 0, using the quadratic formula if needed. The discriminant b² − 4ac tells you how many x-intercepts to expect before you solve: two if positive, one (a tangent touch) if zero, none (complex roots) if negative. Parabolas with no real x-intercepts live entirely above or entirely below the x-axis, and the vertex reveals which case you're in.
