---
id: absolute-value-inequalities
title: Absolute Value Inequalities
domain: mathematics
course: algebra-1
prerequisites:
- id: absolute-value-equations
  type: hard
- id: compound-inequalities
  type: hard
builds-toward:
- piecewise-functions
tags:
- absolute-value
- inequalities
- compound
- graphing
stage: abstract-reasoning
status: validated
---
# Absolute Value Inequalities

## Core Idea
Absolute value inequalities combine distance reasoning with inequality solving. |x − 3| < 5 asks: which values of x are less than 5 units from 3? The answer is the "and" compound inequality −2 < x < 8. Conversely, |x − 3| > 5 asks: which values are more than 5 units from 3? The answer is the "or" compound inequality x < −2 OR x > 8. The pattern: "less than" produces an "and" (intersection), "greater than" produces an "or" (union). This topic connects absolute value, inequalities, and distance on the number line into a unified framework.

## How It's Best Learned
Teach the "less than = and, greater than = or" pattern with the distance interpretation. Isolate the absolute value first, then apply the pattern. For |expression| < k, write −k < expression < k. For |expression| > k, write expression < −k OR expression > k. Graph all solutions on a number line and verify with test points. Include cases where k is negative or zero.

## Common Misconceptions
- Reversing the pattern: using "or" for less-than and "and" for greater-than.
- Not isolating the absolute value before applying the pattern.
- Forgetting that |x| < −3 has no solution and |x| > −3 is true for all real numbers.

## Explainer

You already know from absolute value equations that |x| is the distance from x to zero on the number line. When you solved |x − 3| = 5, you found the two points exactly 5 units from 3: namely x = 8 and x = −2. Absolute value inequalities extend this distance idea from exact locations to regions — instead of asking "which points are exactly 5 units away?", you ask "which points are *less than* 5 units away?" or "which points are *more than* 5 units away?"

The distance picture makes the two cases clear. If you want all numbers within 5 units of 3, you want a connected interval centered at 3: the values between −2 and 8. This is the **"less than = and" pattern**: |x − 3| < 5 becomes −2 < x < 8, which is a compound inequality joined by AND (both conditions must hold simultaneously). The solution is a bounded interval — a segment of the number line. Conversely, if you want all numbers more than 5 units from 3, you want the two separate regions outside that interval: numbers to the left of −2 or to the right of 8. This is the **"greater than = or" pattern**: |x − 3| > 5 becomes x < −2 OR x > 8. The solution is a union of two rays pointing away from the center.

In practice, always isolate the absolute value expression before applying the pattern. If you have 2|x + 1| − 3 < 7, first add 3 and divide by 2 to get |x + 1| < 5, then apply the pattern to get −5 < x + 1 < 5, then solve the resulting compound inequality. From your compound inequality prerequisites, you know how to handle each branch algebraically. The final step — graphing on a number line and checking a test point — confirms your answer and helps catch sign errors.

Two edge cases are worth memorizing. If the right side is negative, say |expression| < −4, no real number has an absolute value less than a negative number, so the solution is the empty set. If the right side is negative with a greater-than inequality, say |expression| > −4, every real number satisfies this (since absolute value is always ≥ 0 > −4), so the solution is all real numbers. These cases seem strange but follow directly from the definition: absolute value is always nonneg, so comparing it to a negative number gives a trivial result.
