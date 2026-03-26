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

## Questions

```yaml
- question: "For x² + 4x + 13 = 0, you calculate the discriminant as 16 − 52 = −36. Before finishing the calculation, what can you immediately conclude?"
  type: multiple-choice
  options:
    - "There is one repeated real solution because the discriminant is a perfect square"
    - "There are no solutions at all — the equation is unsolvable"
    - "There are two complex conjugate solutions — the parabola does not cross the x-axis"
    - "There are two real solutions because 36 is positive"
  answer: 2
  explanation: "A negative discriminant (D < 0) means the square root in the formula is the square root of a negative number, which is imaginary. The result is two complex conjugate solutions of the form p ± qi. Graphically, the parabola lies entirely above (or below) the x-axis and never crosses it. The discriminant delivers this verdict before you finish computing — that is its power. Option D confuses the absolute value of D with its sign."

- question: "For 3x² − 6x + 3 = 0, the discriminant equals b² − 4ac = 36 − 36 = 0. What does this tell you geometrically?"
  type: multiple-choice
  options:
    - "The parabola crosses the x-axis at two distinct points"
    - "The vertex of the parabola touches the x-axis exactly once — one repeated real root"
    - "The parabola is entirely below the x-axis with no real roots"
    - "The discriminant being zero means the equation has no solution"
  answer: 1
  explanation: "When D = 0, the ± in the formula adds and subtracts zero, collapsing to a single value: x = −b/(2a) = 6/6 = 1. Geometrically, the vertex of the parabola sits exactly on the x-axis — it touches but does not cross. This is called a repeated (or double) root. Students sometimes confuse D = 0 with no solution, but one solution is not the same as no solution."

- question: "The quadratic formula is expected to be memorized as an independent rule because it can seldom be derived from techniques already learned in algebra."
  type: true-false
  answer: false
  explanation: "The quadratic formula is the direct result of completing the square on the general form ax² + bx + c = 0. Every step is the same completing-the-square procedure applied symbolically. Knowing the derivation means you understand where the formula comes from, can re-derive it if needed, and are less likely to misremember it. It is not a separate fact — it is a packaged version of something you already know how to do."

- question: "When the discriminant equals zero, the quadratic has exactly one real solution, corresponding to the vertex of the parabola touching the x-axis."
  type: true-false
  answer: true
  explanation: "D = 0 means √D = 0, so the ± term vanishes and both 'solutions' from the ± collapse to the single value x = −b/(2a). This is the x-coordinate of the vertex, confirming the geometric picture: the parabola is tangent to the x-axis at exactly one point. This solution is called a repeated root because it counts algebraically as a root of multiplicity 2."

- question: "Why does −b in the quadratic formula require special care when b is already negative, and what type of error commonly results from mishandling this sign?"
  type: short-answer
  answer: "The formula uses −b, which means you negate whatever b is. If b = −5, then −b = −(−5) = +5. If you forget the negation and write b instead of −b, you get the wrong value for the numerator. The most common error is substituting b = −5 and writing −5 in the formula instead of +5, effectively computing the formula with the wrong sign on the linear term. Careful substitution — writing out −(−5) explicitly before simplifying — prevents this mistake."
  explanation: "Sign errors in the quadratic formula account for a large fraction of wrong answers on assessments. The issue is compounded because the error affects both terms in the ± simultaneously, and the resulting 'solutions' may still look plausible. Checking solutions by substituting back into the original equation is the reliable safeguard."
```

## Explainer

The quadratic formula is not magic — it is the result of completing the square on the general equation ax² + bx + c = 0, which you already know how to do. Every step of completing the square can be followed symbolically: divide by a, move c/a to the right, add (b/2a)² to both sides to form a perfect square trinomial, take the square root of both sides, and isolate x. The formula that falls out, x = (−b ± √(b² − 4ac)) / (2a), is just that process packaged for any quadratic at once. Knowing the derivation means you never need to memorize it as a separate fact — you could re-derive it from scratch if needed.

The **discriminant**, D = b² − 4ac, is the quantity under the square root and it determines everything about the nature of the solutions before you finish computing them. If D > 0, the ± gives two distinct real numbers. If D = 0, the ± adds and subtracts zero, giving one repeated solution (the vertex of the parabola touches the x-axis exactly once). If D < 0, the square root of a negative number enters the picture — and this is where your prerequisite work on complex numbers pays off. The square root of a negative number is imaginary, so the two solutions are **complex conjugates**: one is of the form p + qi and the other is p − qi, where p = −b/(2a) and q = √|D|/(2a). No real solutions exist when D < 0, but two complex solutions always exist.

A common source of errors is the sign of −b. If b = −5, then −b = +5. If b = 0, the formula simplifies to x = ±√(−c/a)/1, which gives ±√(−c/a). If a = 1, the formula is x = (−b ± √(b² − 4c)) / 2. Working slowly through substitution before simplifying prevents most arithmetic mistakes. Similarly, the entire expression −b ± √(b² − 4ac) forms the numerator, and the entire expression must be divided by 2a — not just the radical term.

The formula has a geometric interpretation: −b/(2a) is the x-coordinate of the **vertex** of the parabola y = ax² + bx + c, and ±√(b² − 4ac)/(2a) is the horizontal distance from the vertex to each root. The two roots are symmetric about the axis of symmetry x = −b/(2a). This geometric reading connects the algebraic formula to the graphical behavior of parabolas you will study next and reinforces why the discriminant governs whether the parabola crosses, touches, or misses the x-axis entirely.
