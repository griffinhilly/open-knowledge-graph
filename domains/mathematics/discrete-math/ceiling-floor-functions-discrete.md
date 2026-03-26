---
id: ceiling-floor-functions-discrete
title: Ceiling and Floor Functions
domain: mathematics
course: discrete-math
prerequisites:
- id: absolute-value
  type: soft
builds-toward:
- counting-principles
tags:
- discrete-math
- functions
- notation
stage: formal-systems
status: validated
---

# Ceiling and Floor Functions

## Core Idea
The floor function ⌊x⌋ returns the greatest integer ≤ x, while the ceiling function ⌈x⌉ returns the least integer ≥ x. These functions are essential in discrete mathematics for rounding, analyzing algorithms, and counting problems where integer solutions are required.

## Questions

```yaml
- question: "What is ⌊−2.7⌋?"
  type: multiple-choice
  options:
    - "−2"
    - "−3"
    - "2"
    - "3"
  answer: 1
  explanation: "The floor function returns the greatest integer less than or equal to x. For −2.7, we need the greatest integer that is ≤ −2.7. That is −3 (since −3 < −2.7 < −2, and −3 is the greatest integer on the left). The common error is choosing −2, which is greater than −2.7, not less than or equal to it. For negative numbers, 'rounding down' means going further from zero — floor always moves toward negative infinity."

- question: "A computer must divide an array of 15 elements into groups of 4 for parallel processing. If there are leftover elements, they still need a group. How many groups are required?"
  type: multiple-choice
  options:
    - "3, because ⌊15/4⌋ = 3"
    - "4, because ⌈15/4⌉ = 4"
    - "3.75, because 15 ÷ 4 = 3.75"
    - "4, because you always round up in computer science"
  answer: 1
  explanation: "When leftover elements still need a group, you need ⌈n/k⌉ groups — enough groups so no element is left behind. ⌈15/4⌉ = ⌈3.75⌉ = 4. Option A gives ⌊15/4⌋ = 3, which counts only complete groups — three groups of 4 handle 12 elements, leaving 3 unprocessed. Option C gives the real number, not an integer count. Option D happens to give the right answer but for the wrong reason — you use floor when counting complete groups and ceiling when counting groups needed to accommodate everyone."

- question: "For any real number x, ⌊x⌋ generally rounds x toward zero."
  type: true-false
  answer: false
  explanation: "Floor rounds toward negative infinity, not toward zero. For positive numbers, these happen to be the same direction (⌊3.7⌋ = 3 moves toward zero). But for negative numbers they diverge: ⌊−1.2⌋ = −2, which moves away from zero (further negative), not toward it. The correct statement is: floor returns the greatest integer ≤ x, which is always at or to the left of x on the number line — toward negative infinity."

- question: "If x is not an integer, then ⌈x⌉ = ⌊x⌋ + 1."
  type: true-false
  answer: true
  explanation: "For any non-integer x, the floor traps x from below (⌊x⌋ < x) and the ceiling traps x from above (⌈x⌉ > x). Since there are no integers between ⌊x⌋ and x, and no integers between x and ⌈x⌉, the ceiling must be exactly one more than the floor. The only exception is when x is itself an integer, in which case ⌊x⌋ = ⌈x⌉ = x, so the difference is 0."

- question: "You need to find how many complete weeks fit in a 100-day period, and separately, how many weeks are needed to fully contain a 100-day period (i.e., no day is left uncovered). Express both answers using floor and ceiling functions and explain the difference."
  type: short-answer
  answer: "Complete weeks: ⌊100/7⌋ = ⌊14.28...⌋ = 14. Weeks needed to fully contain: ⌈100/7⌉ = ⌈14.28...⌉ = 15. The floor counts how many groups of 7 fit entirely within 100; the ceiling counts how many groups of 7 are needed so that every day falls in some week, even if the last week is incomplete."
  explanation: "This is the canonical application of floor vs. ceiling: floor for 'how many complete groups fit,' ceiling for 'how many groups are needed to cover everything.' The distinction arises everywhere in computing: dividing memory into pages, distributing tasks across processors, scheduling events. The formula ⌈n/k⌉ = ⌊(n + k − 1)/k⌋ is an equivalent way to compute the ceiling using only floor, useful in contexts where ceiling is not a built-in operation."
```

## Explainer

The real number line is continuous — there are infinitely many values between any two integers. But discrete mathematics lives in the world of whole numbers. The **floor function** ⌊x⌋ and **ceiling function** ⌈x⌉ are the bridge between these two worlds: they take any real number and snap it to the nearest integer in a well-defined direction.

Think of floor as "round down, always." ⌊3.7⌋ = 3, ⌊−1.2⌋ = −2 (because −2 is the greatest integer *less than or equal to* −1.2 — note that for negative numbers, rounding down means going further from zero). Ceiling is "round up, always": ⌈3.2⌉ = 4, ⌈−1.7⌉ = −1. When x is exactly an integer, both functions return x itself: ⌊5⌋ = ⌈5⌉ = 5. This is important to internalize before working with them algebraically.

You already know **absolute value** snaps a number onto the non-negative half of the real line. Floor and ceiling are a different kind of snapping: they project onto the integers. Their power shows up in counting arguments. Suppose you have n items and want to divide them into groups of k — the number of complete groups is ⌊n/k⌋, and the number of groups needed if you can't split items is ⌈n/k⌉. This distinction is ubiquitous in algorithm analysis: if you're dividing an array of 100 elements in half repeatedly, after log₂(100) ≈ 6.64 steps you need ⌈log₂(100)⌉ = 7 actual levels.

Two useful identities to internalize: ⌊x⌋ ≤ x < ⌊x⌋ + 1, and ⌈x⌉ − 1 < x ≤ ⌈x⌉. These bounds let you convert floor/ceiling expressions into inequalities, which is how they appear in proofs. Also note that ⌈x⌉ = ⌊x⌋ + 1 when x is not an integer, and ⌈x⌉ = ⌊x⌋ when x is an integer. The relationship between the two is: ⌈x⌉ = −⌊−x⌋. This symmetry can simplify problems that initially seem to require separate cases for floor and ceiling.
