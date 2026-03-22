---
id: piecewise-functions-graphing
title: Piecewise Functions — Graphing and Analysis
domain: mathematics
course: precalculus
prerequisites:
  - id: function-notation-review
    type: hard
  - id: domain-and-range
    type: hard
builds-toward:
  - continuity-definition
  - one-sided-limits
tags: [functions, piecewise, graphing]
stage: formal-systems
status: validated
---

# Piecewise Functions

## Core Idea
A piecewise function uses different formulas on different intervals of its domain. The absolute value function f(x) = |x| is the simplest example: it equals x when x >= 0 and -x when x < 0. Piecewise functions model real situations where rules change at thresholds (tax brackets, shipping rates, speed limits). They also motivate the concepts of continuity and one-sided limits.

## How It's Best Learned
Practice evaluating piecewise functions at specific points, especially at the boundary values. Graph by drawing each piece on its interval, paying attention to open vs. closed endpoints. Discuss continuity informally: does the graph have a break at the boundary?

## Common Misconceptions
- Applying the wrong formula at boundary points.
- Forgetting to check open vs. closed endpoints (filled vs. open circles on the graph).
- Assuming piecewise functions are always discontinuous at the boundaries.

## Explainer

From your study of function notation and domain/range, you know that a function assigns exactly one output to each input. A **piecewise function** does this using different formulas on different parts of its domain. The simplest example is the absolute value function: f(x) = x when x ≥ 0 and f(x) = −x when x < 0. There is no contradiction — at any particular input, exactly one formula applies. The function is perfectly well-defined; it just uses different rules in different regions.

Piecewise functions model real situations where rules change at thresholds. Tax brackets are piecewise: your tax rate on the first $10,000 of income differs from the rate on income above $10,000. Shipping costs often jump at weight thresholds. Speed limits change at city boundaries. In each case, the underlying relationship is a single function of one variable, but the formula governing it switches at specific boundary values. Recognizing these as piecewise functions connects abstract function notation to the stepped, threshold-based rules you encounter constantly in everyday life.

**Graphing** a piecewise function requires attention to three things: drawing each piece on its correct interval, marking boundary points carefully with open or closed circles, and checking whether the pieces connect. An open circle at a boundary means the function does not include that point (strict inequality); a closed circle means it does (inclusive inequality). For f(x) = { x² if x < 2; 3x − 1 if x ≥ 2 }, you draw the parabola y = x² only for x-values strictly less than 2 (open circle at (2, 4)), then the line y = 3x − 1 for x ≥ 2 (closed circle at (2, 5)). The gap between the open and closed circles reveals a **jump discontinuity** at x = 2.

Not all piecewise functions are discontinuous at their boundaries. If the pieces happen to agree at the boundary — if the left-hand limit, the right-hand limit, and the function value all match — the function is continuous there and the graph passes through the boundary without a break. For example, f(x) = { x if x < 1; 1 if x ≥ 1 } is continuous at x = 1 because both pieces approach 1. This observation previews the formal concept of **continuity** and **one-sided limits** that you will study rigorously in calculus. The intuition you build here — checking whether pieces "connect" at boundaries — is exactly what the ε-δ definition of continuity will formalize.

## Questions

```yaml
- question: "For f(x) = { x², if x < 2; 3x − 1, if x ≥ 2 }, what is f(2)?"
  type: multiple-choice
  options:
    - "4, by substituting into x²"
    - "5, by substituting into 3x − 1"
    - "4.5, by averaging the two formulas"
    - "Undefined, because 2 is a boundary point"
  answer: 1
  explanation: "Since x = 2 satisfies x ≥ 2, the second formula applies: 3(2) − 1 = 5. The first formula only applies when x < 2 — the strict inequality means x = 2 is excluded from that piece. Boundary points are not special exceptions; you simply determine which piece's domain they belong to."

- question: "Consider f(x) = { x + 1, if x < 2; x + 3, if x ≥ 2 }. Is f continuous at x = 2?"
  type: multiple-choice
  options:
    - "Yes — f(2) is defined and equals 5, so the function is continuous there"
    - "Yes — piecewise functions are always continuous at their boundaries"
    - "No — the left-hand limit as x → 2⁻ equals 3, but f(2) = 5, so there is a jump"
    - "No — piecewise functions are never continuous at their boundaries"
  answer: 2
  explanation: "The left-hand limit is lim(x→2⁻) (x+1) = 3. The right-hand limit is lim(x→2⁺) (x+3) = 5 = f(2). Because the left-hand limit (3) does not equal f(2) (5), there is a jump discontinuity. Option A is the classic error: f(2) being defined is necessary but not sufficient for continuity — the limits must also agree with f(2)."

- question: "A piecewise function is always discontinuous at its boundary points."
  type: true-false
  answer: false
  explanation: "Piecewise functions can be perfectly continuous at their boundaries if the pieces connect without a gap or jump. For example, f(x) = { x, if x < 1; 1, if x ≥ 1 } is continuous at x = 1 because both pieces approach 1 from their respective sides. The pieces meeting at a boundary just needs left limit = right limit = f(boundary)."

- question: "For f(x) = { x² if x < 0; −x if x ≥ 0 }, f(0) = 0."
  type: true-false
  answer: true
  explanation: "Since x = 0 satisfies x ≥ 0, we apply the second formula: f(0) = −(0) = 0. The first formula (x²) applies only for strictly negative x, so it is not used here. Note that both pieces happen to approach 0 as x → 0, making this function continuous at the boundary."

- question: "Why must you pay careful attention to open versus closed endpoints when graphing a piecewise function?"
  type: short-answer
  answer: "Whether an endpoint is open or closed determines which formula gives the function's value at that exact boundary point, and it controls whether the graph shows a filled circle (value included) or an open circle (value excluded). If x = a appears as x < a in one piece and x ≥ a in another, then a belongs to the second piece. Getting this wrong produces both an incorrect function value and a misleading graph."
  explanation: "Open and closed endpoints also preview the concept of continuity: if the two pieces yield the same value at a boundary, the dot and open circle coincide and the function is continuous there. If they yield different values, a jump appears. This distinction is precisely what one-sided limits formalize."
```
