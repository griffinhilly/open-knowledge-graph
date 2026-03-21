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
stage: formal-systems
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

## Questions

```yaml
- question: "Evaluate ⌊−2.7⌋."
  type: multiple-choice
  options:
    - "−2"
    - "−3"
    - "2"
    - "3"
  answer: 1
  explanation: "The floor function returns the largest integer that does not exceed the input. The integers less than −2.7 are …, −5, −4, −3, and the largest among them is −3. Many students incorrectly choose −2, applying the intuition of 'rounding toward zero.' But the floor function always rounds toward negative infinity, so for negative numbers it goes further negative, not closer to zero."

- question: "A parking garage charges $6 for each full or partial hour. A driver parks for 1 hour and 25 minutes. What is the correct charge?"
  type: multiple-choice
  options:
    - "$6.00 — they've been there less than 1.5 hours, so the first-hour rate applies"
    - "$8.50 — multiply the hourly rate by 1.42 hours"
    - "$12.00 — 1 hour and any partial additional hour means they are charged for 2 hours"
    - "$9.00 — round to the nearest hour"
  answer: 2
  explanation: "This is a ceiling-function scenario: ⌈1.42⌉ = 2, so the driver is charged for 2 full hours at $6 = $12. Step functions model discrete jumps, not continuous scaling. The charge stays at $6 for all of [0,1) hours, then jumps to $12 for all of [1,2) hours. A driver parked 1 hour 1 minute pays exactly the same as one parked 1 hour 59 minutes."

- question: "The floor function ⌊x⌋ rounds any non-integer input toward the nearest integer."
  type: true-false
  answer: false
  explanation: "The floor function always rounds toward negative infinity, not toward the nearest integer. For positive numbers, 'toward negative infinity' and 'toward zero' look the same (⌊3.7⌋ = 3, and 3 is both the nearest integer below and nearer to 0). But for negative numbers they diverge: ⌊−1.2⌋ = −2 (toward negative infinity), not −1 (the nearest integer). The ceiling function ⌈x⌉ rounds toward positive infinity."

- question: "On the graph of f(x) = ⌊x⌋, the horizontal segment covering the interval [3, 4) has a closed circle at x = 3 and an open circle at x = 4."
  type: true-false
  answer: true
  explanation: "Each piece of the floor function is defined on an interval of the form [n, n+1) — closed on the left, open on the right. At x = 3, the output is 3 and x = 3 IS included (closed circle). At x = 4, the output would jump to 4, so x = 4 is NOT part of this piece (open circle). This open-left/closed-right pattern is directly inherited from the piecewise definition."

- question: "Why does ⌊−1.2⌋ equal −2 rather than −1, and how would you explain the difference to someone applying 'round toward zero'?"
  type: short-answer
  answer: "The floor function returns the largest integer that does not exceed x. −1 does not satisfy this criterion for −1.2 because −1 > −1.2, meaning −1 exceeds the input. The largest integer that is ≤ −1.2 is −2. The 'round toward zero' rule is a mistake imported from ordinary rounding: it produces −1 because −1 is between 0 and −1.2, but the floor function doesn't care about closeness to zero — it cares about not exceeding the input."
  explanation: "The key conceptual test is: does the candidate integer exceed x? −1 exceeds −1.2 (since −1 > −1.2 on the number line), so it fails. −2 does not exceed −1.2 (since −2 < −1.2), so it qualifies. The floor function is essentially asking: 'what integer am I standing on if I walk down the number line from x and stop at the first integer I reach?'"
```

## Explainer

You already know piecewise functions — functions defined by different rules on different intervals. A **step function** is just a piecewise function where every piece is a constant, so the graph looks like a staircase rather than a curve. Instead of a smoothly changing rule, the output sits still for a while, then abruptly jumps to a new constant value. The jump points are where the action is, and the open and closed circles you draw there communicate which endpoint each horizontal piece claims.

The most important step function is the **floor function**, written ⌊x⌋ (also called the greatest-integer function). Its rule: ⌊x⌋ = the largest integer that does not exceed x. For positive inputs this is ordinary truncation: ⌊3.7⌋ = 3, ⌊5.0⌋ = 5. For negative inputs, students often misapply the rule by rounding toward zero. But ⌊−1.2⌋ is not −1 — the largest integer not exceeding −1.2 is −2, because −1 > −1.2. The floor function always rounds toward negative infinity. The companion **ceiling function** ⌈x⌉ rounds toward positive infinity: ⌈3.2⌉ = 4, ⌈−1.2⌉ = −1.

Graphing the floor function makes the open-and-closed-endpoint rule concrete. On the interval [2, 3), the output is 2 — so at x = 2 there is a closed circle (2 is included) and at x = 3 there is an open circle (3 is not included in this piece; it belongs to the next). The graph is a series of horizontal segments, each closed on the left and open on the right. This is a direct consequence of the piecewise definition you already know — each piece is [n, n+1) for integer n, so the closed endpoint is always on the left.

Real-world step functions are everywhere once you recognize them. Postage rates: it costs the same to mail a 0.5 oz letter as a 0.9 oz letter, but more to mail a 1.1 oz letter. Parking garages: the fee is the same for 1 hour and 1 hour 59 minutes, then jumps at 2 hours. Tax brackets: income tax rates apply to ranges of income, not to individual dollars. In each case the output is piecewise-constant — it holds steady over an interval and jumps at the boundary. Identifying where the jumps occur and whether each boundary is included or excluded is the key analytical skill for working with step functions.
