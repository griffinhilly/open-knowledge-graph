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

## Questions

```yaml
- question: "Which compound inequality correctly represents the solutions to |x − 7| > 3?"
  type: multiple-choice
  options:
    - "4 < x < 10"
    - "x < 4 OR x > 10"
    - "x < −10 OR x > −4"
    - "−10 < x < 4"
  answer: 1
  explanation: "|x − 7| > 3 uses the 'greater-than = or' pattern: values more than 3 units from 7. 7 − 3 = 4 and 7 + 3 = 10, so the solution is x < 4 OR x > 10. Option A (4 < x < 10) is the most tempting wrong answer — it's exactly what you'd get by applying the 'less-than = and' pattern, the precise reversal of the correct rule."

- question: "What is the solution set of |2x + 1| < −5?"
  type: multiple-choice
  options:
    - "x < −3 OR x > 2"
    - "−3 < x < 2"
    - "All real numbers"
    - "No solution"
  answer: 3
  explanation: "Absolute value is always greater than or equal to zero, so it can never be less than a negative number. The inequality |expression| < (negative number) has no solution — the solution set is empty. Before applying the 'less-than = and' pattern, always check whether the right side is negative. If it is, stop: the answer is immediately 'no solution.'"

- question: "The inequality |x − 4| < 6 is asking for all values of x that are more than 6 units from 4."
  type: true-false
  answer: false
  explanation: "This reverses the direction. |x − 4| < 6 asks for values that are *less than* 6 units from 4 — values close to 4, forming a bounded interval: −2 < x < 8. Values more than 6 units from 4 would be the solution to |x − 4| > 6, which gives x < −2 OR x > 10 — the 'greater-than = or' case. Confusing the two is the most common error in absolute value inequalities."

- question: "For the inequality |x| > −3, the solution is no real numbers, since no number can be a negative distance from zero."
  type: true-false
  answer: false
  explanation: "This is the opposite edge case. Absolute value is always ≥ 0, and 0 > −3, so |x| > −3 is satisfied by every real number — the solution is all real numbers. This flips the usual intuition: when the right side is negative, a 'less than' absolute value inequality has no solution, but a 'greater than' absolute value inequality is always true. Both cases follow directly from the fact that absolute values are never negative."

- question: "Why does |x − a| < k produce an AND compound inequality while |x − a| > k produces an OR compound inequality?"
  type: short-answer
  answer: "Because they ask opposite geometric questions on the number line. |x − a| < k asks which values of x are within k units of a — a connected region centered at a. Every such value satisfies BOTH x > a − k AND x < a + k simultaneously, giving a bounded interval. |x − a| > k asks which values lie more than k units from a — outside the interval on either side. No number can be far to the left AND far to the right at the same time, so the solution splits into two disconnected rays joined by OR."
  explanation: "The distance interpretation makes the logic airtight. 'Less than k units away' means 'between a − k and a + k' — a single region requiring both boundaries (AND). 'More than k units away' means 'left of a − k or right of a + k' — two disconnected regions where either boundary suffices (OR). Memorizing 'less than = and, greater than = or' is useful shorthand, but understanding why prevents reversal errors and handles edge cases correctly."
```

## Explainer

You already know from absolute value equations that |x| is the distance from x to zero on the number line. When you solved |x − 3| = 5, you found the two points exactly 5 units from 3: namely x = 8 and x = −2. Absolute value inequalities extend this distance idea from exact locations to regions — instead of asking "which points are exactly 5 units away?", you ask "which points are *less than* 5 units away?" or "which points are *more than* 5 units away?"

The distance picture makes the two cases clear. If you want all numbers within 5 units of 3, you want a connected interval centered at 3: the values between −2 and 8. This is the **"less than = and" pattern**: |x − 3| < 5 becomes −2 < x < 8, which is a compound inequality joined by AND (both conditions must hold simultaneously). The solution is a bounded interval — a segment of the number line. Conversely, if you want all numbers more than 5 units from 3, you want the two separate regions outside that interval: numbers to the left of −2 or to the right of 8. This is the **"greater than = or" pattern**: |x − 3| > 5 becomes x < −2 OR x > 8. The solution is a union of two rays pointing away from the center.

In practice, always isolate the absolute value expression before applying the pattern. If you have 2|x + 1| − 3 < 7, first add 3 and divide by 2 to get |x + 1| < 5, then apply the pattern to get −5 < x + 1 < 5, then solve the resulting compound inequality. From your compound inequality prerequisites, you know how to handle each branch algebraically. The final step — graphing on a number line and checking a test point — confirms your answer and helps catch sign errors.

Two edge cases are worth memorizing. If the right side is negative, say |expression| < −4, no real number has an absolute value less than a negative number, so the solution is the empty set. If the right side is negative with a greater-than inequality, say |expression| > −4, every real number satisfies this (since absolute value is always ≥ 0 > −4), so the solution is all real numbers. These cases seem strange but follow directly from the definition: absolute value is always nonneg, so comparing it to a negative number gives a trivial result.
