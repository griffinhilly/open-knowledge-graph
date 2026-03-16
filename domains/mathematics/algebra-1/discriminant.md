---
id: discriminant
title: The Discriminant
domain: mathematics
course: algebra-1
prerequisites:
- id: quadratic-formula
  type: hard
builds-toward:
- complex-numbers-intro
- conic-sections-overview
tags:
- discriminant
- quadratics
- number-of-solutions
- roots
stage: abstract-reasoning
status: validated
---
# The Discriminant

## Core Idea
The discriminant is the expression b² − 4ac from inside the square root of the quadratic formula. Its value determines the number and type of solutions to ax² + bx + c = 0 without actually solving the equation. If b² − 4ac > 0, there are two distinct real solutions. If b² − 4ac = 0, there is exactly one real solution (a repeated root). If b² − 4ac < 0, there are no real solutions (the solutions are complex numbers). The discriminant also has a geometric interpretation: it tells you how many times the parabola y = ax² + bx + c crosses the x-axis.

## How It's Best Learned
Compute the discriminant for several quadratics, predict the number of solutions, then solve to verify. Connect to graphing: show parabolas that cross the x-axis twice (D > 0), touch it once (D = 0), and miss it entirely (D < 0). Practice using the discriminant to answer "how many solutions?" questions without solving. Include word problems where the discriminant determines whether a scenario is possible.

## Common Misconceptions
- Computing b² − 4ac incorrectly (forgetting to square b, or computing b² − 4a × c with wrong grouping).
- Thinking D = 0 means "no solution" instead of "one repeated solution."
- Confusing "no real solutions" with "no solutions at all" — complex solutions exist but are beyond algebra 1.

## Explainer

You already know the quadratic formula: x = (−b ± √(b² − 4ac)) / 2a. The **discriminant** is simply the expression under the square root, D = b² − 4ac. The reason it deserves its own name is that it single-handedly determines the nature of the solutions before you do any division or subtraction. It is a diagnostic tool built into the formula.

The logic is geometric as well as algebraic. The parabola y = ax² + bx + c intersects the x-axis exactly where y = 0, i.e., at the solutions of the quadratic equation. If D > 0, the square root is a positive real number, and the ± gives two distinct values — two x-intercepts. If D = 0, the square root is zero, and the ± produces the same value both times: x = −b/2a. This is the vertex of the parabola sitting exactly on the x-axis — one **repeated root**. If D < 0, you are taking the square root of a negative number, which has no real value — the parabola misses the x-axis entirely, floating above or below it.

The discriminant also tells you about the quality of the solutions. If D is a perfect square (like 9, 25, 100), then the solutions are rational numbers — the quadratic factors nicely over the integers. If D > 0 but not a perfect square (like 7 or 11), the solutions are irrational, involving an irreducible square root. This means factoring over integers is impossible; the quadratic formula is the only clean route to exact solutions.

A practical use of the discriminant is checking feasibility without solving. Suppose a projectile's height is h(t) = −5t² + 20t + 3, and you want to know whether it ever reaches a height of 30 meters. Setting h(t) = 30 gives −5t² + 20t − 27 = 0, or equivalently 5t² − 20t + 27 = 0. Compute D = (−20)² − 4(5)(27) = 400 − 540 = −140. Since D < 0, there is no real time when the projectile reaches 30 meters — the answer is no, without solving. The discriminant lets you answer existence questions about solutions before you ever commit to the full calculation.


