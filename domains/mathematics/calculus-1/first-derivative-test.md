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

## Explainer

The derivative gives the instantaneous rate of change of f at each point. When f'(x) > 0, the function is climbing left to right; when f'(x) < 0, it is falling. A **critical point** is any x-value where this climbing-or-falling behavior could reverse — either because f'(c) = 0 (the slope is momentarily flat) or because f'(c) is undefined (a corner or vertical tangent). The first derivative test turns this qualitative picture into a classification procedure.

Here is the core procedure. Find all critical points by computing f'(x), setting it to zero, and identifying where it is undefined. Mark these points on a number line. Pick one **test point** in each resulting interval and evaluate the sign of f' there. A positive sign means f is increasing in that interval; negative means decreasing. Then read off the extrema from the sign transitions: if f' goes from **positive to negative** at c, the function rose then fell — c is a **local maximum**. If f' goes from **negative to positive**, c is a **local minimum**. If the sign is the same on both sides, no extremum: c is an **inflection point** of the slope (the standard example is f(x) = x³ at x = 0, where f' = 3x² ≥ 0 on both sides).

The **sign chart** is the organizational tool that makes this systematic. Draw a number line, mark all critical points, choose a test value in each interval, compute f' at each test value, and record + or −. The chart tells you everything: increasing/decreasing behavior and the classification of each critical point, all from a single organized table. You are not computing f everywhere — you are asking a binary question (is f' positive or negative?) in each region, which is far easier.

Because you know the chain rule, you can find critical points for composite functions like f(x) = (x² − 1)^(2/3). Here f' involves a factor that is undefined at x = ±1, even though f itself is defined there — those are critical points that a naive "set f' = 0" step would miss. Always hunt for *both* sources of critical points: f'(c) = 0 and f'(c) undefined. The sign chart catches all of them once you have identified them.
