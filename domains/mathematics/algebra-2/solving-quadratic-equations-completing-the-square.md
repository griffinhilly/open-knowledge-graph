---
id: solving-quadratic-equations-completing-the-square
title: Solving Quadratic Equations by Completing the Square
domain: mathematics
course: algebra-2
prerequisites:
- id: solving-quadratics-by-factoring
  type: hard
- id: square-roots-intro
  type: hard
- id: operations-with-complex-numbers
  type: soft
builds-toward:
- quadratic-formula-review
- graphing-quadratic-functions
- conic-sections-circles
- conic-sections-parabolas
tags:
- quadratics
- completing-the-square
- solving-equations
stage: abstract-reasoning
status: validated
---
# Solving Quadratic Equations by Completing the Square

## Core Idea
Completing the square transforms ax^2 + bx + c = 0 into the form a(x - h)^2 = k, which can be solved by taking square roots. The process: (1) move the constant to the other side, (2) if a != 1, divide through by a, (3) add (b/2a)^2 to both sides, (4) factor the left side as a perfect square, (5) take the square root of both sides. This method always works (unlike factoring) and is the basis for deriving the quadratic formula. It also converts quadratics to vertex form for graphing.

## How It's Best Learned
Start with simple cases where a = 1 and b is even. Build to a = 1 with odd b (fractions appear). Then handle a != 1. Emphasize the geometric meaning: you are literally "completing" a partial square. Show the connection to vertex form. Derive the quadratic formula as the general case.

## Common Misconceptions
- Forgetting to add (b/2)^2 to BOTH sides of the equation.
- Not dividing by a first when a != 1.
- Taking only the positive square root and missing the second solution.
- Arithmetic errors with fractions when b is odd.

## Questions

```yaml
- question: "To complete the square for x² + 10x = 3, what value must be added to both sides?"
  type: multiple-choice
  options:
    - "5, giving (x + 5)² = 8"
    - "25, giving (x + 5)² = 28"
    - "10, giving (x + 10)² = 13"
    - "100, giving (x + 10)² = 103"
  answer: 1
  explanation: "The completing term is (b/2)², where b is the coefficient of x. Here b = 10, so (10/2)² = 5² = 25. Adding 25 to both sides gives x² + 10x + 25 = 28, which factors as (x + 5)² = 28. Option A uses b/2 = 5 instead of (b/2)² = 25 — the most common error. Option C uses b itself. Option D squares b rather than b/2. The critical step is halving the coefficient *before* squaring."

- question: "After completing the square on a quadratic equation, a student obtains (x − 4)² = −9. How many real solutions does the original equation have?"
  type: multiple-choice
  options:
    - "Two real solutions: x = 4 + 9 = 13 and x = 4 − 9 = −5"
    - "One real solution: x = 4, since the negative sign cancels the square"
    - "Zero real solutions: the square root of a negative number is not real"
    - "Two real solutions obtained by taking ±√9 = ±3, giving x = 7 and x = 1"
  answer: 2
  explanation: "The equation (x − 4)² = −9 requires taking the square root of −9, which is not a real number. No real value of x can satisfy this — the square of any real number is non-negative. The solutions are complex: x = 4 ± 3i. Geometrically, this means the parabola sits entirely above or below the x-axis with no real x-intercepts. The sign of k in (x − h)² = k tells you everything: k > 0 gives two real solutions, k = 0 gives one repeated root, k < 0 gives two complex solutions."

- question: "When completing the square for a quadratic where the leading coefficient is not 1, you can skip dividing by that coefficient first and still arrive at the correct answer."
  type: true-false
  answer: false
  explanation: "If the leading coefficient a ≠ 1, dividing through by a first is essential. Without this step, the left side after adding the completing term does not factor as a perfect square trinomial. For 2x² + 8x = 6: dividing by 2 gives x² + 4x = 3, then adding (4/2)² = 4 yields (x + 2)² = 7. Attempting to complete the square directly on 2x² + 8x without dividing first produces a different and incorrect factorization. The technique only works cleanly when the coefficient of x² is 1."

- question: "When solving (x + 3)² = 16 by taking the square root of both sides, there are two solutions: x = 1 and x = −7."
  type: true-false
  answer: true
  explanation: "Taking the square root of both sides gives x + 3 = ±4. The positive case: x + 3 = 4, so x = 1. The negative case: x + 3 = −4, so x = −7. Both check out: (1 + 3)² = 16 ✓ and (−7 + 3)² = (−4)² = 16 ✓. The ± is the structural source of two solutions — a very common error is taking only the positive root and missing the second solution, especially when the completed square has a large or positive h value."

- question: "Why must the completing term (b/2)² be added to both sides of the equation, rather than only to the left side?"
  type: short-answer
  answer: "Adding a value to only one side of an equation changes the equality — it creates a different equation with different solutions. To maintain equivalence (to produce a new equation with the same solutions as the original), whatever is added to the left side must also be added to the right. The completing term is added to create a perfect square trinomial on the left; adding it to the right preserves the original equation's solution set."
  explanation: "This is the fundamental property of equality: if A = B, then A + c = B + c for any constant c. Forgetting to add the completing term to the right side is one of the most common errors in completing the square. The resulting 'solved' equation is inequivalent to the original and its solutions are wrong. Checking by substituting back into the original equation immediately exposes this error, which is why checking solutions is important in algebraic manipulation."
```

## Explainer

You already know how to solve quadratics by factoring — but factoring only works cleanly when the equation has nice integer roots. Completing the square is the universal method: it works on any quadratic, and it reveals the structure of the solution rather than just producing answers.

The key idea is transforming a messy quadratic into the form (x − h)² = k, which you can solve immediately by taking square roots: x = h ± sqrt(k). The process is geometric in origin. The expression x² + bx is a partial square — it is "almost" (x + b/2)², which expands to x² + bx + (b/2)². The missing piece is (b/2)², the **completing term**. Adding it to both sides creates a perfect square on the left without changing the equality. For x² + 6x − 7 = 0: move the constant to get x² + 6x = 7, add (6/2)² = 9 to both sides: x² + 6x + 9 = 16, which is (x + 3)² = 16. So x + 3 = ±4, giving x = 1 or x = −7.

The ± from taking the square root is the structural source of two solutions. If k > 0, there are two distinct real solutions; if k = 0, there is exactly one (a **repeated root** where the parabola touches but does not cross the x-axis); if k < 0, the square root is imaginary and the solutions are complex — the parabola sits entirely above or below the x-axis. The **quadratic formula** is just completing the square applied to the general ax² + bx + c = 0: divide through by a, complete the square, simplify, and you get x = (−b ± sqrt(b² − 4ac)) / 2a. The expression b² − 4ac is the **discriminant**, and its sign determines exactly which case applies.

Completing the square does double duty: it solves equations and converts quadratics to **vertex form** a(x − h)² + k, which directly reveals the vertex (h, k) of the parabola and the direction it opens. This connection between the algebraic manipulation and the geometric shape is why the technique feeds into graphing quadratic functions and into the conic sections work you will do next, where completing the square in both x and y is the standard tool for identifying circles and other conics from general-form equations.
