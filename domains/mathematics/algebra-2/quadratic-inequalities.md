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

## Explainer

From graphing quadratic functions, you know that y = ax² + bx + c traces a parabola — a U-shaped (or inverted-U-shaped) curve that crosses the x-axis at the zeros of the quadratic, if they exist. A quadratic inequality like ax² + bx + c > 0 is simply asking: for which x-values does the parabola sit *above* the x-axis? For < 0: where is it *below*? The graph answers this question visually; sign analysis answers it algebraically.

The procedure has three steps that flow directly from your prerequisites. First, find the zeros using the **quadratic formula** (or factoring) — these are the x-values where the parabola touches or crosses the x-axis. The zeros divide the number line into intervals: if the zeros are r₁ < r₂, you have three regions: x < r₁, r₁ < x < r₂, and x > r₂. Second, determine the **sign** of the quadratic in each interval by plugging in a convenient test point. Because a continuous function cannot change sign without passing through zero, the sign within each interval is constant — you only need one test point per interval. Third, select the intervals where the sign matches the inequality (positive for > 0, negative for < 0), and include the endpoints if the inequality is non-strict (≥ or ≤).

The structure of the solution depends on the leading coefficient and the inequality direction. If the parabola opens upward (a > 0), the quadratic is negative between the two roots and positive outside them. So ax² + bx + c < 0 gives a bounded interval (r₁, r₂), while ax² + bx + c > 0 gives the union (−∞, r₁) ∪ (r₂, ∞) — two separate pieces. This is why solutions to quadratic inequalities are often **unions of intervals**, not a single interval like the linear case. The most common mistake is writing a single interval like r₁ < x < r₂ when the correct answer is x < r₁ or x > r₂.

You cannot solve quadratic inequalities the way you solve linear ones — dividing both sides by a variable-containing expression is illegal because you do not know its sign, and "taking the square root" of an inequality introduces errors. The zero-finding-then-sign-analysis approach works for any polynomial or rational inequality and is the technique you will use throughout precalculus and calculus. Mastering it here, where the zeros are easy to find, makes the general method feel natural.
