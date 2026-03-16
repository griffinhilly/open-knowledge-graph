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

## Explainer

You already know two things from your prerequisites. From the first derivative test: a critical point where f'(c) = 0 is a local minimum if f' changes from negative to positive there, and a local maximum if f' changes from positive to negative. From concavity: f''(x) > 0 means the graph is **concave up** (curves upward like a bowl), and f''(x) < 0 means **concave down** (curves downward like a dome). The second derivative test combines these into a single check at the critical point itself, without examining the sign of f' on both sides.

Here is the geometric intuition. If f'(c) = 0 and f''(c) > 0, the function has zero slope at c and is concave up there — like the bottom of a valley. A valley bottom is a local minimum. If f'(c) = 0 and f''(c) < 0, the function has zero slope and is concave down — like the top of a hill. A hilltop is a local maximum. The second derivative is essentially asking: "At this zero-slope point, is the graph curving upward or downward?" Upward → minimum; downward → maximum.

The test is often faster than the first derivative test because it requires evaluating one number (f''(c)) rather than checking the sign of f' on both sides of c. The procedure: (1) find critical points by solving f'(x) = 0; (2) compute f''(c) at each critical point; (3) classify. For example, f(x) = x³ − 3x has f'(x) = 3x² − 3 = 0 at x = ±1. Then f''(x) = 6x gives f''(1) = 6 > 0 (local minimum) and f''(−1) = −6 < 0 (local maximum). No sign-checking of f' on intervals is needed.

The **inconclusive case** — when f''(c) = 0 — is essential to handle correctly. It does not mean there is no extremum; it means the second derivative test gives no information. The functions f(x) = x⁴ (local minimum at 0), f(x) = −x⁴ (local maximum at 0), and f(x) = x³ (neither — an inflection point) all satisfy f''(0) = 0, yet they behave completely differently. When f''(c) = 0, fall back to the first derivative test: examine the sign of f' just to the left and right of c. The two tests are complementary — use the second derivative test for speed when f'' is easy to compute and nonzero at the critical point, and rely on the first derivative test as a dependable fallback.
