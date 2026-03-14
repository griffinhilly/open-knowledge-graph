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
