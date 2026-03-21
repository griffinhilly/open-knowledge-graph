---
id: second-derivative-test
title: Second Derivative Test
domain: mathematics
course: calculus-1
prerequisites:
  - id: first-derivative-test
    type: hard
  - id: concavity-and-inflection-points
    type: hard
builds-toward:
  - curve-sketching
  - optimization-problems
tags: [derivatives, applications, extrema, second-derivative]
stage: formal-systems
status: validated
---

# Second Derivative Test

## Core Idea
The second derivative test provides an alternative way to classify critical points: if f'(c) = 0 and f''(c) > 0, then c is a local minimum (concave up). If f'(c) = 0 and f''(c) < 0, then c is a local maximum (concave down). If f''(c) = 0, the test is inconclusive. This test is often quicker than the first derivative test when f'' is easy to compute.

## How It's Best Learned
Apply to functions where f'' is easily computed. Compare results with the first derivative test to build confidence. Emphasize the inconclusive case and what to do when it arises (fall back to the first derivative test).

## Common Misconceptions
- Using the test when f''(c) = 0 and drawing a conclusion (the test is inconclusive in this case).
- Confusing the second derivative test with the test for concavity (the second derivative test is specifically about critical points).
- Forgetting that this test only applies at points where f'(c) = 0, not where f' is undefined.

## Questions

```yaml
- question: "At a critical point c where f'(c) = 0, you compute f''(c) = 0. What is the correct conclusion?"
  type: multiple-choice
  options:
    - "c is an inflection point, not a local extremum"
    - "c is neither a maximum nor a minimum"
    - "The second derivative test is inconclusive; you must use the first derivative test"
    - "c is a local minimum because the concavity is neutral"
  answer: 2
  explanation: "When f''(c) = 0, the second derivative test gives no information — it is inconclusive. All three behaviors are possible: f(x) = x⁴ has a local minimum at 0, f(x) = −x⁴ has a local maximum at 0, and f(x) = x³ has neither (an inflection point). In every case f''(0) = 0. The correct fallback is the first derivative test: check the sign of f' on each side of c."

- question: "A function has f'(2) = 0 and f''(2) = −7. Which statement best explains why x = 2 is a local maximum?"
  type: multiple-choice
  options:
    - "f' is negative at x = 2, so the function is falling there"
    - "f'' is negative, meaning the function is concave down at x = 2 — like the top of a hill with zero slope"
    - "f'' < 0 means f' is decreasing, so the function must be at a minimum"
    - "The negative second derivative shows the function crosses zero at that point"
  answer: 1
  explanation: "The second derivative test classifies via concavity: f''(2) < 0 means the graph is concave down at x = 2 — curving like a dome. Combined with f'(2) = 0 (a flat tangent), this gives a hilltop — a local maximum. Option C contains a true fact (f'' < 0 does mean f' is decreasing) but draws the wrong conclusion; a decreasing f' at a zero-slope point means the function went from rising to falling, confirming a maximum."

- question: "The second derivative test can classify a critical point without examining the sign of f' on both sides of the critical point."
  type: true-false
  answer: true
  explanation: "True. The second derivative test only requires evaluating f''(c) at the critical point itself. If f''(c) > 0, it's a local min; if f''(c) < 0, it's a local max — no need to check f' values nearby. This is the test's main advantage over the first derivative test. The exception is when f''(c) = 0, in which case you must fall back to examining f' on both sides."

- question: "If f''(c) = 0, then c is an inflection point of f."
  type: true-false
  answer: false
  explanation: "False. f''(c) = 0 is a necessary but not sufficient condition for an inflection point. It also means the second derivative test is inconclusive about whether c is an extremum. For example, f(x) = x⁴ has f''(0) = 0, but x = 0 is a local minimum, not an inflection point. An inflection point requires f'' to change sign at c — not merely to equal zero."

- question: "Explain why the second derivative test works geometrically: what do f'(c) = 0 and f''(c) > 0 together tell you about the shape of the graph near c?"
  type: short-answer
  answer: "f'(c) = 0 means the tangent line at c is horizontal — the slope is zero. f''(c) > 0 means the function is concave up at c — the graph curves like the bottom of a bowl. A horizontal tangent at the bottom of a bowl is a local minimum: the function falls approaching from either side and the point c is the lowest nearby value."
  explanation: "The geometric picture is the key insight. Concavity tells you the direction the curve is bending: concave up (f'' > 0) means the curve bends upward, like a valley floor. Zero slope at a valley floor means you're at the bottom — a local minimum. Concave down (f'' < 0) means the curve bends downward, like a hill peak. Zero slope at a hilltop means you're at the top — a local maximum. This is why the second derivative test works without checking both sides of the critical point."
```

## Explainer

You already know two things from your prerequisites. From the first derivative test: a critical point where f'(c) = 0 is a local minimum if f' changes from negative to positive there, and a local maximum if f' changes from positive to negative. From concavity: f''(x) > 0 means the graph is **concave up** (curves upward like a bowl), and f''(x) < 0 means **concave down** (curves downward like a dome). The second derivative test combines these into a single check at the critical point itself, without examining the sign of f' on both sides.

Here is the geometric intuition. If f'(c) = 0 and f''(c) > 0, the function has zero slope at c and is concave up there — like the bottom of a valley. A valley bottom is a local minimum. If f'(c) = 0 and f''(c) < 0, the function has zero slope and is concave down — like the top of a hill. A hilltop is a local maximum. The second derivative is essentially asking: "At this zero-slope point, is the graph curving upward or downward?" Upward → minimum; downward → maximum.

The test is often faster than the first derivative test because it requires evaluating one number (f''(c)) rather than checking the sign of f' on both sides of c. The procedure: (1) find critical points by solving f'(x) = 0; (2) compute f''(c) at each critical point; (3) classify. For example, f(x) = x³ − 3x has f'(x) = 3x² − 3 = 0 at x = ±1. Then f''(x) = 6x gives f''(1) = 6 > 0 (local minimum) and f''(−1) = −6 < 0 (local maximum). No sign-checking of f' on intervals is needed.

The **inconclusive case** — when f''(c) = 0 — is essential to handle correctly. It does not mean there is no extremum; it means the second derivative test gives no information. The functions f(x) = x⁴ (local minimum at 0), f(x) = −x⁴ (local maximum at 0), and f(x) = x³ (neither — an inflection point) all satisfy f''(0) = 0, yet they behave completely differently. When f''(c) = 0, fall back to the first derivative test: examine the sign of f' just to the left and right of c. The two tests are complementary — use the second derivative test for speed when f'' is easy to compute and nonzero at the critical point, and rely on the first derivative test as a dependable fallback.
