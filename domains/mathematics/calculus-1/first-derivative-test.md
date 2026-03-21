---
id: first-derivative-test
title: First Derivative Test
domain: mathematics
course: calculus-1
prerequisites:
  - id: mean-value-theorem
    type: soft
  - id: chain-rule
    type: hard
builds-toward:
  - curve-sketching
  - optimization-problems
tags: [derivatives, applications, extrema, increasing-decreasing]
stage: formal-systems
status: validated
---

# First Derivative Test

## Core Idea
The first derivative test classifies critical points (where f'(c) = 0 or f'(c) is undefined) as local maxima, local minima, or neither. If f' changes from positive to negative at c, then f has a local maximum at c. If f' changes from negative to positive, it is a local minimum. If f' does not change sign, c is neither (like x^3 at x = 0). The test works by analyzing the sign of f' on intervals determined by critical points.

## How It's Best Learned
Find critical points by setting f'(x) = 0 and identifying where f' is undefined. Build a sign chart for f' across the intervals. Determine increasing/decreasing behavior. Classify each critical point by the sign change pattern.

## Common Misconceptions
- Assuming f'(c) = 0 always means there is a local extremum (x^3 at 0 is a counterexample).
- Forgetting to check where f' is undefined (these are also critical points).
- Only checking the sign at one point per interval instead of determining the sign throughout.

## Questions

```yaml
- question: "For f(x) = x³ − 3x, we find f'(x) = 3x² − 3, which equals zero at x = ±1. The sign of f' changes from positive (for x < −1) to negative (for −1 < x < 1) at x = −1. What does the first derivative test conclude about x = −1?"
  type: multiple-choice
  options:
    - "x = −1 is an inflection point because the derivative equals zero there"
    - "x = −1 is a local minimum because f'(−1) = 0 and the function is decreasing afterward"
    - "x = −1 is a local maximum because f' changes from positive to negative"
    - "We cannot classify x = −1 without also computing f''(−1)"
  answer: 2
  explanation: "The first derivative test classifies critical points by sign change, not by the value of f'' or anything else. When f' changes from positive (function rising) to negative (function falling), the function peaked — it is a local maximum. f'(−1) = 0 only tells us x = −1 is a critical point; the sign change is what determines it is a local maximum. The second derivative test is an alternative, not a requirement — the first derivative test is self-contained."

- question: "For the function g(x) where g'(x) = (x − 2)² for all x, the point x = 2 is a critical point since g'(2) = 0. What does the first derivative test say about x = 2?"
  type: multiple-choice
  options:
    - "It is a local minimum, since (x − 2)² ≥ 0 means g' is never negative near x = 2"
    - "It is a local maximum, since g' = 0 at x = 2 and positive everywhere else"
    - "It is neither a local maximum nor a local minimum, since g' does not change sign at x = 2"
    - "The first derivative test is inconclusive here; we must use the second derivative test"
  answer: 2
  explanation: "Since (x − 2)² ≥ 0 for all x, g'(x) ≥ 0 on both sides of x = 2 — positive before, zero at, positive after. There is no sign change. The function is non-decreasing on both sides; it simply pauses its ascent momentarily without ever falling. This is the classic pattern of a 'saddle-like' critical point (like x³ at 0 in one dimension): f'(c) = 0 but no extremum. The first derivative test is decisive here — 'no sign change' is a valid conclusion, not an inconclusive one."

- question: "Every point where f'(c) = 0 is either a local maximum or a local minimum of f."
  type: true-false
  answer: false
  explanation: "f'(c) = 0 is a necessary condition for a local extremum at an interior point, but not sufficient. The classic counterexample is f(x) = x³ at c = 0: f'(0) = 0, yet x = 0 is neither a maximum nor a minimum — the function is increasing on both sides. The first derivative test shows this: f'(x) = 3x² ≥ 0 on both sides of 0, so there is no sign change and no extremum. f'(c) = 0 means the function is momentarily flat; whether it turns around depends on what happens to the sign of f' nearby."

- question: "The first derivative test requires examining the sign of f' on both sides of a critical point, not just confirming that f'(c) = 0."
  type: true-false
  answer: true
  explanation: "This is the entire content of the first derivative test. f'(c) = 0 (or undefined) merely identifies c as a critical point — a candidate for classification. The classification itself comes from the sign pattern: positive-to-negative means local max, negative-to-positive means local min, same sign on both sides means neither. A student who only verifies f'(c) = 0 has done half the work and drawn no valid conclusion about extrema."

- question: "Explain why f'(c) = 0 is a necessary but not sufficient condition for a local extremum. Give a concrete example where the condition fails and explain what additional information the first derivative test provides."
  type: short-answer
  answer: "f'(c) = 0 is necessary because at a smooth local extremum the tangent must be horizontal — the function cannot be rising or falling at a peak or valley. But it is not sufficient because the function could be momentarily flat without reversing direction. Example: f(x) = x³ at c = 0. f'(x) = 3x², so f'(0) = 0, yet x = 0 is not an extremum — the function increases on both sides. The first derivative test provides the missing information: examine the sign of f' just left and just right of c. Only if the sign changes (positive-to-negative or negative-to-positive) is there an extremum. If the sign is the same on both sides, f' = 0 is a pause, not a reversal."
  explanation: "The intuition is that a local extremum requires the function to change from rising to falling (max) or falling to rising (min). f'(c) = 0 says the instantaneous slope is zero, but says nothing about whether the slope was positive before and is negative after. The sign chart captures exactly this reversal."
```

## Explainer

The derivative gives the instantaneous rate of change of f at each point. When f'(x) > 0, the function is climbing left to right; when f'(x) < 0, it is falling. A **critical point** is any x-value where this climbing-or-falling behavior could reverse — either because f'(c) = 0 (the slope is momentarily flat) or because f'(c) is undefined (a corner or vertical tangent). The first derivative test turns this qualitative picture into a classification procedure.

Here is the core procedure. Find all critical points by computing f'(x), setting it to zero, and identifying where it is undefined. Mark these points on a number line. Pick one **test point** in each resulting interval and evaluate the sign of f' there. A positive sign means f is increasing in that interval; negative means decreasing. Then read off the extrema from the sign transitions: if f' goes from **positive to negative** at c, the function rose then fell — c is a **local maximum**. If f' goes from **negative to positive**, c is a **local minimum**. If the sign is the same on both sides, no extremum: c is an **inflection point** of the slope (the standard example is f(x) = x³ at x = 0, where f' = 3x² ≥ 0 on both sides).

The **sign chart** is the organizational tool that makes this systematic. Draw a number line, mark all critical points, choose a test value in each interval, compute f' at each test value, and record + or −. The chart tells you everything: increasing/decreasing behavior and the classification of each critical point, all from a single organized table. You are not computing f everywhere — you are asking a binary question (is f' positive or negative?) in each region, which is far easier.

Because you know the chain rule, you can find critical points for composite functions like f(x) = (x² − 1)^(2/3). Here f' involves a factor that is undefined at x = ±1, even though f itself is defined there — those are critical points that a naive "set f' = 0" step would miss. Always hunt for *both* sources of critical points: f'(c) = 0 and f'(c) undefined. The sign chart catches all of them once you have identified them.
