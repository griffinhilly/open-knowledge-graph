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

## Explainer

You already know how to solve quadratics by factoring — but factoring only works cleanly when the equation has nice integer roots. Completing the square is the universal method: it works on any quadratic, and it reveals the structure of the solution rather than just producing answers.

The key idea is transforming a messy quadratic into the form (x − h)² = k, which you can solve immediately by taking square roots: x = h ± sqrt(k). The process is geometric in origin. The expression x² + bx is a partial square — it is "almost" (x + b/2)², which expands to x² + bx + (b/2)². The missing piece is (b/2)², the **completing term**. Adding it to both sides creates a perfect square on the left without changing the equality. For x² + 6x − 7 = 0: move the constant to get x² + 6x = 7, add (6/2)² = 9 to both sides: x² + 6x + 9 = 16, which is (x + 3)² = 16. So x + 3 = ±4, giving x = 1 or x = −7.

The ± from taking the square root is the structural source of two solutions. If k > 0, there are two distinct real solutions; if k = 0, there is exactly one (a **repeated root** where the parabola touches but does not cross the x-axis); if k < 0, the square root is imaginary and the solutions are complex — the parabola sits entirely above or below the x-axis. The **quadratic formula** is just completing the square applied to the general ax² + bx + c = 0: divide through by a, complete the square, simplify, and you get x = (−b ± sqrt(b² − 4ac)) / 2a. The expression b² − 4ac is the **discriminant**, and its sign determines exactly which case applies.

Completing the square does double duty: it solves equations and converts quadratics to **vertex form** a(x − h)² + k, which directly reveals the vertex (h, k) of the parabola and the direction it opens. This connection between the algebraic manipulation and the geometric shape is why the technique feeds into graphing quadratic functions and into the conic sections work you will do next, where completing the square in both x and y is the standard tool for identifying circles and other conics from general-form equations.
