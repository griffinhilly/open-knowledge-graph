---
id: step-functions
title: Step Functions
domain: mathematics
course: algebra-2
prerequisites:
- id: piecewise-functions
  type: hard
builds-toward: []
tags:
- functions
- step-function
- floor
- ceiling
- piecewise
stage: abstract-reasoning
status: validated
---
# Step Functions

## Core Idea
A step function is a piecewise-constant function whose graph resembles a staircase — it holds a constant value over each interval and then jumps to a new value. The most important example is the greatest integer function (floor function), written f(x) = floor(x), which returns the largest integer less than or equal to x: floor(3.7) = 3, floor(-1.2) = -2. The ceiling function rounds up instead: ceil(3.2) = 4. Step functions model real-world situations where output changes in discrete jumps rather than continuously, such as postage rates (cost stays the same within a weight bracket), parking fees, and tax brackets.

## How It's Best Learned
Start by evaluating the floor function at several values, including negatives, to build intuition. Graph by hand using open and closed circles at the jump points to show which endpoint is included. Connect to the piecewise function definition students already know — a step function is just a piecewise function where each piece is a horizontal segment. Use real-world examples like "shipping costs $5 for 0-1 lbs, $8 for 1-2 lbs" to motivate why step functions exist.

## Common Misconceptions
- Thinking floor(-1.2) = -1 instead of -2 — the floor function rounds toward negative infinity, not toward zero.
- Drawing the graph as a continuous staircase without distinguishing open and closed endpoints at each jump.

## Explainer

You already know piecewise functions — functions defined by different rules on different intervals. A **step function** is just a piecewise function where every piece is a constant, so the graph looks like a staircase rather than a curve. Instead of a smoothly changing rule, the output sits still for a while, then abruptly jumps to a new constant value. The jump points are where the action is, and the open and closed circles you draw there communicate which endpoint each horizontal piece claims.

The most important step function is the **floor function**, written ⌊x⌋ (also called the greatest-integer function). Its rule: ⌊x⌋ = the largest integer that does not exceed x. For positive inputs this is ordinary truncation: ⌊3.7⌋ = 3, ⌊5.0⌋ = 5. For negative inputs, students often misapply the rule by rounding toward zero. But ⌊−1.2⌋ is not −1 — the largest integer not exceeding −1.2 is −2, because −1 > −1.2. The floor function always rounds toward negative infinity. The companion **ceiling function** ⌈x⌉ rounds toward positive infinity: ⌈3.2⌉ = 4, ⌈−1.2⌉ = −1.

Graphing the floor function makes the open-and-closed-endpoint rule concrete. On the interval [2, 3), the output is 2 — so at x = 2 there is a closed circle (2 is included) and at x = 3 there is an open circle (3 is not included in this piece; it belongs to the next). The graph is a series of horizontal segments, each closed on the left and open on the right. This is a direct consequence of the piecewise definition you already know — each piece is [n, n+1) for integer n, so the closed endpoint is always on the left.

Real-world step functions are everywhere once you recognize them. Postage rates: it costs the same to mail a 0.5 oz letter as a 0.9 oz letter, but more to mail a 1.1 oz letter. Parking garages: the fee is the same for 1 hour and 1 hour 59 minutes, then jumps at 2 hours. Tax brackets: income tax rates apply to ranges of income, not to individual dollars. In each case the output is piecewise-constant — it holds steady over an interval and jumps at the boundary. Identifying where the jumps occur and whether each boundary is included or excluded is the key analytical skill for working with step functions.
