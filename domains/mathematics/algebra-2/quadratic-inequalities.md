---
id: quadratic-inequalities
title: Quadratic Inequalities
domain: mathematics
course: algebra-2
prerequisites:
- id: graphing-quadratic-functions
  type: hard
- id: quadratic-formula-review
  type: hard
- id: solving-inequalities
  type: hard
- id: solving-absolute-value-equations-review
  type: soft
builds-toward:
- polynomial-functions-degree-and-leading-coefficient
tags:
- quadratics
- inequalities
- sign-analysis
- intervals
stage: abstract-reasoning
status: validated
---
# Quadratic Inequalities

## Core Idea
A quadratic inequality like ax^2 + bx + c > 0 asks for the x-values where the parabola is above (or below) the x-axis. Solve by: (1) find the zeros of the corresponding equation, (2) determine the sign of the quadratic in each interval defined by the zeros, (3) select the intervals satisfying the inequality. Solutions are typically unions of intervals. This introduces the sign analysis technique used for all polynomial and rational inequalities.

## How It's Best Learned
Graph the parabola and identify where it is positive/negative. Connect the algebraic sign analysis to the visual graph. Practice with both < and > (open intervals) and <= and >= (closed intervals). Use a number line with test points. Introduce interval notation.

## Common Misconceptions
- Dividing both sides by a negative number and forgetting to flip the inequality sign.
- Writing the solution as a single interval instead of a union (e.g., x < -2 or x > 3, not -2 < x < 3).
- Forgetting to check whether endpoints are included (strict vs. non-strict inequality).
- Trying to solve quadratic inequalities the same way as linear ones.

## Questions

```yaml
- question: "You solve x² - x - 6 > 0, find roots x = -2 and x = 3, and the parabola opens upward. What is the solution set?"
  type: multiple-choice
  options:
    - "(-2, 3)"
    - "(-∞, -2) ∪ (3, ∞)"
    - "(-∞, -2)"
    - "(3, ∞)"
  answer: 1
  explanation: "When a parabola opens upward, it is BELOW the x-axis between the roots and ABOVE it outside them. So x² - x - 6 > 0 (positive) gives the two outer regions: x < -2 or x > 3. The tempting wrong answer (-2, 3) is actually the solution to x² - x - 6 < 0. Recognizing which region satisfies the inequality requires understanding the parabola's shape, not just finding the roots."

- question: "A student solves (x - 2)(x - 3) < 0, finds roots 2 and 3, and writes the solution as 'x < 2 or x > 3.' What error did they make?"
  type: multiple-choice
  options:
    - "They factored incorrectly — the roots should be -2 and -3"
    - "For < 0 with an upward parabola, the solution is the interval BETWEEN the roots: (2, 3), not outside them"
    - "They should have included the endpoints: x ≤ 2 or x ≥ 3"
    - "Quadratic inequalities cannot be solved by factoring"
  answer: 1
  explanation: "The sign pattern of an upward parabola is: positive | negative | positive across the three intervals defined by its roots. The expression (x - 2)(x - 3) is negative only between the roots, giving the bounded interval (2, 3). Writing 'x < 2 or x > 3' confuses the solution to > 0 with the solution to < 0 — the two solutions are exact complements."

- question: "The solution to x² - 4 > 0 can be written as the single interval x > 2."
  type: true-false
  answer: false
  explanation: "x² - 4 = (x + 2)(x - 2) has roots at x = -2 and x = 2. Since the parabola opens upward, it is positive in TWO regions: x < -2 and x > 2. Writing only 'x > 2' misses the entire left branch. The correct solution is (-∞, -2) ∪ (2, ∞)."

- question: "You cannot solve a quadratic inequality by treating it like a linear inequality — algebraically isolating x on one side — because the parabola's sign changes in a way that linear manipulation cannot track."
  type: true-false
  answer: true
  explanation: "Linear inequalities have a consistent direction of solution (x > k or x < k). Quadratic inequalities produce sign patterns that depend on the parabola's shape, and solutions are often unions of intervals. Additionally, dividing by a term containing x is illegal since you don't know its sign. The correct method is always: find zeros first, then test signs in each resulting interval."

- question: "Why do solutions to quadratic inequalities often consist of two separate intervals rather than one connected interval, and how does the parabola's graph make this clear?"
  type: short-answer
  answer: "An upward-opening parabola dips below the x-axis only between its roots and rises above it on both outer sides. So a > 0 inequality picks up both outer regions (a union of two unbounded intervals), while a < 0 inequality picks up the single bounded region between the roots. The graph makes this visual: you can see exactly where the curve lies above or below the axis, and the solution is simply the x-projection of those regions."
  explanation: "This is why quadratic solutions don't look like linear ones. Linear inequalities produce a half-line; quadratic inequalities produce a bounded segment or a union of two rays, depending on direction. Connecting the algebraic sign analysis to the geometric parabola is the key insight that makes the general method intuitive."
```

## Explainer

From graphing quadratic functions, you know that y = ax² + bx + c traces a parabola — a U-shaped (or inverted-U-shaped) curve that crosses the x-axis at the zeros of the quadratic, if they exist. A quadratic inequality like ax² + bx + c > 0 is simply asking: for which x-values does the parabola sit *above* the x-axis? For < 0: where is it *below*? The graph answers this question visually; sign analysis answers it algebraically.

The procedure has three steps that flow directly from your prerequisites. First, find the zeros using the **quadratic formula** (or factoring) — these are the x-values where the parabola touches or crosses the x-axis. The zeros divide the number line into intervals: if the zeros are r₁ < r₂, you have three regions: x < r₁, r₁ < x < r₂, and x > r₂. Second, determine the **sign** of the quadratic in each interval by plugging in a convenient test point. Because a continuous function cannot change sign without passing through zero, the sign within each interval is constant — you only need one test point per interval. Third, select the intervals where the sign matches the inequality (positive for > 0, negative for < 0), and include the endpoints if the inequality is non-strict (≥ or ≤).

The structure of the solution depends on the leading coefficient and the inequality direction. If the parabola opens upward (a > 0), the quadratic is negative between the two roots and positive outside them. So ax² + bx + c < 0 gives a bounded interval (r₁, r₂), while ax² + bx + c > 0 gives the union (−∞, r₁) ∪ (r₂, ∞) — two separate pieces. This is why solutions to quadratic inequalities are often **unions of intervals**, not a single interval like the linear case. The most common mistake is writing a single interval like r₁ < x < r₂ when the correct answer is x < r₁ or x > r₂.

You cannot solve quadratic inequalities the way you solve linear ones — dividing both sides by a variable-containing expression is illegal because you do not know its sign, and "taking the square root" of an inequality introduces errors. The zero-finding-then-sign-analysis approach works for any polynomial or rational inequality and is the technique you will use throughout precalculus and calculus. Mastering it here, where the zeros are easy to find, makes the general method feel natural.
