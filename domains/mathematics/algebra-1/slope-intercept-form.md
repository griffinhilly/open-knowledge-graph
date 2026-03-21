---
id: slope-intercept-form
title: Slope-Intercept Form
domain: mathematics
course: algebra-1
prerequisites:
  - id: slope-concept
    type: hard
  - id: literal-equations
    type: soft
builds-toward:
  - writing-linear-equations
  - graphing-linear-equations
  - parallel-and-perpendicular-slopes
  - systems-graphing
tags: [slope-intercept, linear-equations, graphing, y-intercept]
stage: abstract-reasoning
status: validated
---

# Slope-Intercept Form

## Core Idea
Slope-intercept form is y = mx + b, where m is the slope and b is the y-intercept (the point where the line crosses the y-axis). This form is the most intuitive for graphing: start at (0, b) on the y-axis, then use the slope to find additional points. It is also the most natural for interpreting linear models: b is the starting value and m is the rate of change. For example, a phone plan costing $30/month plus a $50 activation fee is modeled by y = 30x + 50, where x is months and y is total cost. Slope-intercept form is the workhorse of linear algebra.

## How It's Best Learned
Graph lines by plotting the y-intercept first, then using rise/run from the slope to plot a second point. Convert equations from other forms to slope-intercept form by solving for y. Practice identifying m and b from equations, graphs, and word problems. Emphasize that every non-vertical linear equation can be written in this form.

## Common Misconceptions
- Confusing the slope and y-intercept (swapping m and b).
- Forgetting that b is the y-coordinate of the y-intercept, not a point — the full y-intercept point is (0, b).
- When the equation is not solved for y (e.g., 2y = 4x + 6), reading m = 4 instead of dividing first (m = 2).

## Questions

```yaml
- question: "The equation 3x + 2y = 12 is given. What is the slope of this line?"
  type: multiple-choice
  options:
    - "3"
    - "-3/2"
    - "2"
    - "6"
  answer: 1
  explanation: "To read slope and y-intercept, the equation must be solved for y first. Subtract 3x from both sides: 2y = -3x + 12. Divide by 2: y = -(3/2)x + 6. Now the slope is the coefficient of x, which is -3/2. The common mistake is reading the coefficient of x from the unsolved equation (3) or forgetting to divide the coefficient by 2 along with the constant."

- question: "A streaming service costs $8 per month plus a one-time $15 setup fee. The equation y = 8x + 15 models total cost y after x months. What does the value 15 represent?"
  type: multiple-choice
  options:
    - "The cost increases by $15 each month"
    - "The total cost after 15 months"
    - "The cost before any months have passed — what you owe at month zero"
    - "The number of months until the service breaks even"
  answer: 2
  explanation: "In y = mx + b, b is the y-intercept — the value of y when x = 0. Here, x = 0 means zero months have passed, so y = 8(0) + 15 = 15. This is the setup fee paid before any monthly charges accrue. The value 8 (the coefficient m) is the rate — cost increases by $8 per month. Confusing m and b is the most common error with slope-intercept interpretation."

- question: "In y = mx + b, b alone is the y-coordinate of the point where the line crosses the y-axis, and the full y-intercept point is (0, b)."
  type: true-false
  answer: true
  explanation: "When x = 0, the equation becomes y = m(0) + b = b. So the line crosses the y-axis at the point (0, b); b is the y-coordinate of that point. This distinction matters when graphing: the starting point to plot is (0, b), not just a height of b floating without location."

- question: "For the equation 4x + 2y = 10, the slope is 4 and the y-intercept is 10."
  type: true-false
  answer: false
  explanation: "You cannot read slope and y-intercept from an equation not solved for y. First isolate y: subtract 4x to get 2y = -4x + 10, then divide by 2 to get y = -2x + 5. The slope is -2 (not 4) and the y-intercept is 5 (not 10). Skipping the division step produces the coefficient of x in the original equation — a systematic error that multiplies both m and b by the missing factor."

- question: "Why must you solve an equation for y before reading off the slope and y-intercept? What specific error occurs if you skip this step with an equation like 6x + 3y = 18?"
  type: short-answer
  answer: "Slope-intercept form requires y to be isolated: y = mx + b. Only then does the coefficient of x equal m and the constant equal b. For 6x + 3y = 18, solving gives y = -2x + 6 (slope -2, y-intercept 6). Without solving, a student might read slope as 6 and y-intercept as 18 — both wrong by a factor of 3, because the division by the coefficient of y was never applied."
  explanation: "The key is that slope-intercept form demands a coefficient of exactly 1 in front of y. When y has a different coefficient, every other term must be divided by it too. Missing this produces a slope and y-intercept that are both scaled incorrectly, a systematic error that can go unnoticed without checking by substituting a point."
```

## Explainer

From your work on slope, you know that slope measures steepness: it's the ratio of vertical change to horizontal change, rise over run. Slope tells you *how fast* y changes when x changes. But knowing the rate of change alone doesn't tell you where the line is — two parallel lines have the same slope but are completely different lines. You also need a starting point. The **y-intercept** provides exactly that: it's where the line crosses the y-axis, the value of y when x = 0.

**Slope-intercept form** y = mx + b packages both pieces of information into one compact equation. The coefficient m is the slope, and the constant b is the y-intercept (the y-coordinate when x = 0). Reading a line's equation in this form is immediate: y = 3x + 7 has slope 3 and y-intercept 7. Graphing it is equally direct — plot the point (0, 7), then use the slope 3 (meaning "up 3, right 1") to find another point at (1, 10), and draw the line through them.

The real-world power of slope-intercept form comes from interpreting m and b as meaningful quantities. Consider a parking garage that charges a $5 entry fee plus $2 per hour. The total cost is y = 2x + 5, where x is hours and y is dollars. Here b = 5 is the flat entry cost (what you owe before parking at all), and m = 2 is the rate — each additional hour adds $2. This pattern appears everywhere: monthly subscriptions (flat fee + per-unit cost), taxi rides (base fare + per-mile rate), temperature conversion. Whenever a quantity changes at a constant rate from some starting value, slope-intercept form is the natural model.

When a linear equation is *not* already solved for y — say 3x + 2y = 12 — convert it by isolating y: subtract 3x from both sides to get 2y = −3x + 12, then divide by 2 to get y = −(3/2)x + 6. Now you can immediately read off slope m = −3/2 (the line falls as x increases) and y-intercept b = 6. This conversion step — solving for y — is the bridge that makes slope-intercept form universally usable, no matter how a linear equation is originally written.
