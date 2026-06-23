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

## Questions

```yaml
- question: "What is the vertex of the parabola y = 3(x − 4)² + 7?"
  type: multiple-choice
  options:
    - "(−4, 7) — reading the number inside the parentheses as −4"
    - "(4, 7) — because x must equal 4 to make (x − 4)² equal zero"
    - "(4, −7) — negating k to find the vertex y-coordinate"
    - "(−4, −7) — negating both h and k"
  answer: 1
  explanation: "In y = a(x − h)² + k, the vertex is (h, k). Here h = 4 and k = 7, so the vertex is (4, 7). The most common error is reading h as −4 because of the minus sign in (x − 4)². The minus sign is built into the form's structure: you need x = 4 (not x = −4) to make (x − 4)² equal zero, so the vertex is at x = +4."

- question: "Compared to the parent function y = x², how does the parabola y = (1/3)(x − 2)² + 1 differ in width?"
  type: multiple-choice
  options:
    - "Narrower — because the coefficient 1/3 is smaller, making it more compressed"
    - "Wider — because |a| = 1/3 < 1 causes vertical compression that spreads the parabola outward"
    - "Same width — only shifted right 2 and up 1"
    - "Narrower and opens downward because of the fraction"
  answer: 1
  explanation: "When |a| < 1, the parabola is wider (flatter) than y = x². When |a| > 1, it is narrower. The coefficient 1/3 compresses the vertical scale, which visually spreads the parabola outward. The most common misconception is reversing this relationship: thinking a smaller coefficient makes a narrower graph because 'smaller = less.' Think of it instead as: a larger a value pulls the sides of the parabola inward (steeper), while a smaller a lets them spread out (flatter)."

- question: "In the equation y = (x + 3)² + 1, the vertex is at (3, 1) because the number inside the parentheses is 3."
  type: true-false
  answer: false
  explanation: "The vertex is at (−3, 1). Rewriting in standard vertex form: y = (x + 3)² + 1 = (x − (−3))² + 1, so h = −3 and k = 1. The vertex is where the squared expression equals zero: x + 3 = 0 gives x = −3. The sign trap works in both directions — when you see (x + 3)², the vertex is at x = −3, not x = +3."

- question: "The vertex form y = a(x − h)² + k and the standard form y = ax² + bx + c represent the same quadratic function — they are algebraically equivalent, just written differently."
  type: true-false
  answer: true
  explanation: "They are identical functions. Vertex form can be expanded to standard form by multiplying out (x − h)², distributing a, and collecting constants. Standard form can be converted to vertex form by completing the square. The same parabola, the same a value, the same vertex — just different algebraic presentations that make different information immediately visible."

- question: "In y = a(x − h)² + k, why does the graph shift RIGHT by h units rather than LEFT when h is positive? Many students expect the direction to match the sign shown."
  type: short-answer
  answer: "The vertex is located where the squared expression equals zero — the minimum (or maximum) of the function. For (x − h)², this happens when x = h: substituting x = h gives (h − h)² = 0. So the vertex is at x = h, which means a positive h shifts the parabola to the right. The minus sign in the form (x − h)² is structural: to place the vertex at x = 3, you write (x − 3)², not (x + 3)². The direction of the shift is opposite to what the sign suggests because the vertex must satisfy the equation, not be read directly from the sign."
  explanation: "This sign convention is the most persistent source of error in vertex form. One reliable check: ask 'what value of x makes the expression inside the parentheses equal zero?' That value is always the x-coordinate of the vertex, regardless of what signs appear in the written form."
```

## Explainer

From graphing quadratics, you know that every parabola has a vertex — the turning point where the function changes from decreasing to increasing (or vice versa). **Vertex form**, y = a(x − h)² + k, is designed to make that vertex visible at a glance. The vertex is (h, k), readable directly from the equation. This is the payoff: instead of finding the vertex by computing −b/2a from standard form, you simply read it off.

The form is built from transformations of the parent parabola y = x², which you can think of as the "default" parabola with vertex at the origin. Each parameter shifts or scales it. Adding k shifts the graph up or down by k units — this is a vertical translation. Replacing x with (x − h) shifts the graph right by h units (left if h is negative) — this is a horizontal translation. The sign asymmetry is the main trap: (x − 3)² pushes the vertex to x = 3, not x = −3, because you need x = 3 to make the expression equal zero. Finally, the coefficient a stretches or compresses the parabola. When |a| > 1, the parabola is narrower than y = x²; when 0 < |a| < 1, it is wider. A negative a flips the parabola upside down.

Converting from standard form y = ax² + bx + c to vertex form requires **completing the square** — a technique you'll master in the next topic. But even now, you can convert in reverse: expand y = a(x − h)² + k by multiplying out (x − h)² = x² − 2hx + h², then distribute a, and collect constants. This gives back y = ax² + (−2ah)x + (ah² + k). Matching with standard form: b = −2ah, so h = −b/2a, and c = ah² + k, so k = c − ah². These are the standard formulas for the vertex — but vertex form makes them unnecessary.

The deepest insight is that every quadratic function has a vertex, and that vertex is the geometric center of symmetry of the parabola. The axis of symmetry is the vertical line x = h. Any input h + d gives the same output as h − d (the parabola is mirror-symmetric about this axis), because a(h + d − h)² + k = a(h − d − h)² + k = ad² + k. Vertex form exposes this symmetry that is hidden in standard form. When you later study function transformations, vertex form will generalize: any function can be shifted and scaled in the same pattern, not just quadratics.


