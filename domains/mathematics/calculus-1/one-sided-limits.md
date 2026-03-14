---
id: one-sided-limits
title: One-Sided Limits
domain: mathematics
course: calculus-1
prerequisites:
- id: limit-definition-intuitive
  type: hard
- id: piecewise-functions
  type: soft
- id: piecewise-functions-graphing
  type: soft
builds-toward:
- continuity-definition
- infinite-limits
tags:
- limits
- one-sided
- left-right
stage: formal-systems
status: validated
---
# One-Sided Limits

## Core Idea
A one-sided limit describes the behavior of f(x) as x approaches a from only one direction: from the left (x -> a-) or from the right (x -> a+). The two-sided limit exists if and only if both one-sided limits exist and are equal. One-sided limits are essential for analyzing piecewise functions, absolute value functions, and functions with jump discontinuities.

## How It's Best Learned
Evaluate one-sided limits from graphs and from piecewise function definitions. Compare left and right limits to determine whether the two-sided limit exists. Connect to continuity: a function is continuous at a only if both one-sided limits equal f(a).

## Common Misconceptions
- Assuming the limit exists whenever one side exists (both sides must agree).
- Confusing the notation: the minus sign in x -> a- means "from the left," not "negative a."
- Forgetting that at endpoints of a domain, only one-sided limits make sense.
