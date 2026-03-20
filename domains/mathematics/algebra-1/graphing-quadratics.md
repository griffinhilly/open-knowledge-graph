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

## Questions

```yaml
- question: "A student begins graphing y = −3x² + 12x − 5 and expects a U-shaped curve opening upward. What will actually appear?"
  type: multiple-choice
  options:
    - "A U-shaped curve opening upward, since the coefficient of x is positive"
    - "A U-shaped curve opening upward, since the equation has three terms"
    - "An inverted U-shape opening downward, because the leading coefficient a = −3 is negative"
    - "A straight line, because the negative sign cancels the squaring effect"
  answer: 2
  explanation: "The sign of the leading coefficient a determines whether the parabola opens upward (a > 0, a 'smile') or downward (a < 0, a 'frown'). Here a = −3, so the parabola opens downward and has a maximum point. The common misconception is to focus on the positive middle term (+12x) and expect upward opening — but only the sign of the coefficient on x² determines direction. A negative a always produces a downward-opening parabola."

- question: "For y = 2x² + 8x + 3, a student calculates the vertex x-coordinate as x = b/(2a) = 8/(4) = 2. What error was made?"
  type: multiple-choice
  options:
    - "The student used the wrong value for b — it should be the coefficient of x², not x"
    - "The student forgot the negative sign: the correct formula is x = −b/(2a) = −8/4 = −2"
    - "The formula for the vertex is x = −b/a, not −b/(2a)"
    - "The student calculated correctly; the vertex x-coordinate is 2"
  answer: 1
  explanation: "The vertex formula is x = −b/(2a), with a critical negative sign. The student computed b/(2a) instead, getting the wrong sign. For this function, the correct vertex x-coordinate is −8/(2·2) = −8/4 = −2, not +2. Forgetting the negative sign in the vertex formula is one of the most common errors in graphing quadratics. The symmetry of a parabola means that using +2 instead of −2 produces a point on the curve, but not the vertex."

- question: "All parabolas open upward because the x² term always represents a positive squared value."
  type: true-false
  answer: false
  explanation: "This confuses the sign of x² (which is always non-negative as a mathematical expression) with the sign of the coefficient a. The coefficient a multiplies x², and if a < 0, the product ax² is negative for any nonzero x. This makes the parabola open downward. For example, y = −x² produces y ≤ 0 for all x, giving a downward-opening parabola with a maximum at the origin. The key is whether a is positive or negative, not whether x² is positive."

- question: "A quadratic function whose discriminant is negative has no graph — since it has no real x-intercepts, the parabola does not exist."
  type: true-false
  answer: false
  explanation: "A parabola with no real x-intercepts still has a complete graph — it simply floats entirely above the x-axis (if a > 0) or below it (if a < 0) without ever touching zero. For example, y = x² + 1 is a perfectly valid upward-opening parabola with vertex at (0, 1) that never crosses the x-axis. The x-intercepts are the solutions to the equation set equal to zero; their absence means no real roots, not no graph. This is an important distinction: every quadratic function has a parabolic graph."

- question: "Explain how the axis of symmetry can be used to plot a parabola efficiently. What is the relationship between points on either side of the axis?"
  type: short-answer
  answer: "The axis of symmetry is the vertical line x = −b/(2a) that passes through the vertex, dividing the parabola into two mirror-image halves. Any point on the parabola has a corresponding point at equal distance on the other side of the axis with the same y-value. This means once you find the vertex and plot a few points on one side, you can immediately place their mirror images on the other side without additional calculation. For example, if the axis is x = 2 and you find the point (0, 5) on the parabola, then (4, 5) is also on the parabola by symmetry."
  explanation: "This symmetry property follows from the fact that squaring is an even function: (−h)² = h². So the y-value depends only on how far x is from the vertex's x-coordinate, not on which direction. Exploiting this symmetry is much more efficient than plugging in every x-value independently. In practice: find the vertex, find the y-intercept, reflect the y-intercept across the axis, add one or two more calculated points and their reflections — you now have enough to sketch an accurate parabola."
```

## Explainer

You already know how to graph a line: pick two points, connect them, and the slope tells you how steeply it rises. A quadratic function y = ax² + bx + c produces a **parabola** — a U-shaped curve — because squaring the input causes the output to grow faster and faster as x moves away from the center. Unlike a line, which changes at a constant rate, a quadratic accelerates. The sign of a immediately tells you the story: if a > 0, the parabola opens upward (a smile) with a minimum point; if a < 0, it opens downward (a frown) with a maximum point.

The most important feature to find first is the **vertex** — the tip of the U. It sits at x = −b/(2a), and you find the y-coordinate by plugging that x back into the equation. Think of the vertex as the "pivot point" of the curve. Everything else is symmetric around it, because squaring (x − h) gives the same value whether you go left or right from h. This symmetry gives you the **axis of symmetry**, the vertical line x = −b/(2a) that cuts the parabola exactly in half. Any point on one side of the axis has a mirror image on the other side at the same height — a fact you can use to plot the curve efficiently.

The y-intercept is always easy: set x = 0 and the formula gives y = c immediately, so the curve crosses the y-axis at the point (0, c). The **x-intercepts** (also called zeros or roots) are the solutions to ax² + bx + c = 0 — the same equations you solved by factoring in your prerequisite work. If the equation has two real solutions, the parabola crosses the x-axis at two points. If it has one repeated solution, the parabola just touches the x-axis at the vertex. If there are no real solutions, the parabola floats entirely above (or below) the x-axis — it still exists as a graph, it just never crosses zero.

The coefficient a controls more than direction: it controls **width**. A large |a| makes the parabola narrow and steep; a small |a| close to zero makes it wide and flat. Comparing y = x², y = 3x², and y = (1/3)x² on the same axes makes this vivid. This shape-stretching is a preview of function transformations you will study next, where multiplying the entire function by a constant stretches or compresses it vertically. Everything you learn about parabolas here — vertex, axis, roots, shape — will carry forward into vertex form, completing the square, conic sections, and eventually calculus, where the vertex is the point where the derivative equals zero.
