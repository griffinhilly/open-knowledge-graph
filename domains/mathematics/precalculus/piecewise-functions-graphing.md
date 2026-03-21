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
