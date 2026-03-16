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

## Explainer

From your work on slope, you know that slope measures steepness: it's the ratio of vertical change to horizontal change, rise over run. Slope tells you *how fast* y changes when x changes. But knowing the rate of change alone doesn't tell you where the line is — two parallel lines have the same slope but are completely different lines. You also need a starting point. The **y-intercept** provides exactly that: it's where the line crosses the y-axis, the value of y when x = 0.

**Slope-intercept form** y = mx + b packages both pieces of information into one compact equation. The coefficient m is the slope, and the constant b is the y-intercept (the y-coordinate when x = 0). Reading a line's equation in this form is immediate: y = 3x + 7 has slope 3 and y-intercept 7. Graphing it is equally direct — plot the point (0, 7), then use the slope 3 (meaning "up 3, right 1") to find another point at (1, 10), and draw the line through them.

The real-world power of slope-intercept form comes from interpreting m and b as meaningful quantities. Consider a parking garage that charges a $5 entry fee plus $2 per hour. The total cost is y = 2x + 5, where x is hours and y is dollars. Here b = 5 is the flat entry cost (what you owe before parking at all), and m = 2 is the rate — each additional hour adds $2. This pattern appears everywhere: monthly subscriptions (flat fee + per-unit cost), taxi rides (base fare + per-mile rate), temperature conversion. Whenever a quantity changes at a constant rate from some starting value, slope-intercept form is the natural model.

When a linear equation is *not* already solved for y — say 3x + 2y = 12 — convert it by isolating y: subtract 3x from both sides to get 2y = −3x + 12, then divide by 2 to get y = −(3/2)x + 6. Now you can immediately read off slope m = −3/2 (the line falls as x increases) and y-intercept b = 6. This conversion step — solving for y — is the bridge that makes slope-intercept form universally usable, no matter how a linear equation is originally written.
