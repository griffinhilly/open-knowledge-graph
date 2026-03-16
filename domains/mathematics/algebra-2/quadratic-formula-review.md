---
id: quadratic-formula-review
title: Quadratic Formula Review and Applications
domain: mathematics
course: algebra-2
prerequisites:
  - id: solving-quadratic-equations-completing-the-square
    type: hard
  - id: complex-numbers-intro
    type: soft
builds-toward:
  - graphing-quadratic-functions
  - quadratic-inequalities
  - fundamental-theorem-of-algebra
tags: [quadratics, quadratic-formula, discriminant, applications]
stage: abstract-reasoning
status: validated
---

# Quadratic Formula Review and Applications

## Core Idea
The quadratic formula x = (-b +/- sqrt(b^2 - 4ac)) / (2a) solves any equation ax^2 + bx + c = 0. The discriminant D = b^2 - 4ac determines the nature of solutions: D > 0 gives two real solutions, D = 0 gives one repeated real solution, D < 0 gives two complex conjugate solutions. In Algebra 2, the formula is extended to complex solutions and applied to modeling problems.

## How It's Best Learned
Review the derivation from completing the square so students understand where it comes from. Practice using the formula with various discriminant values, including negative discriminants (introducing complex solutions). Apply to word problems: projectile motion, area optimization, break-even analysis. Emphasize checking solutions.

## Common Misconceptions
- Sign errors, especially with -b when b is already negative.
- Forgetting to divide the entire numerator by 2a (dividing only the square root term).
- Not simplifying the radical fully.
- Confusing the discriminant with the full formula.

## Explainer

The quadratic formula is not magic — it is the result of completing the square on the general equation ax² + bx + c = 0, which you already know how to do. Every step of completing the square can be followed symbolically: divide by a, move c/a to the right, add (b/2a)² to both sides to form a perfect square trinomial, take the square root of both sides, and isolate x. The formula that falls out, x = (−b ± √(b² − 4ac)) / (2a), is just that process packaged for any quadratic at once. Knowing the derivation means you never need to memorize it as a separate fact — you could re-derive it from scratch if needed.

The **discriminant**, D = b² − 4ac, is the quantity under the square root and it determines everything about the nature of the solutions before you finish computing them. If D > 0, the ± gives two distinct real numbers. If D = 0, the ± adds and subtracts zero, giving one repeated solution (the vertex of the parabola touches the x-axis exactly once). If D < 0, the square root of a negative number enters the picture — and this is where your prerequisite work on complex numbers pays off. The square root of a negative number is imaginary, so the two solutions are **complex conjugates**: one is of the form p + qi and the other is p − qi, where p = −b/(2a) and q = √|D|/(2a). No real solutions exist when D < 0, but two complex solutions always exist.

A common source of errors is the sign of −b. If b = −5, then −b = +5. If b = 0, the formula simplifies to x = ±√(−c/a)/1, which gives ±√(−c/a). If a = 1, the formula is x = (−b ± √(b² − 4c)) / 2. Working slowly through substitution before simplifying prevents most arithmetic mistakes. Similarly, the entire expression −b ± √(b² − 4ac) forms the numerator, and the entire expression must be divided by 2a — not just the radical term.

The formula has a geometric interpretation: −b/(2a) is the x-coordinate of the **vertex** of the parabola y = ax² + bx + c, and ±√(b² − 4ac)/(2a) is the horizontal distance from the vertex to each root. The two roots are symmetric about the axis of symmetry x = −b/(2a). This geometric reading connects the algebraic formula to the graphical behavior of parabolas you will study next and reinforces why the discriminant governs whether the parabola crosses, touches, or misses the x-axis entirely.
