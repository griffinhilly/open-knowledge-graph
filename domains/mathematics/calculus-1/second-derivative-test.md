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
status: draft
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
