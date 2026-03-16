---
id: two-digit-subtraction-no-regrouping-2nd
title: Two-Digit Subtraction Without Regrouping
domain: mathematics
course: 2nd-grade
prerequisites:
- id: subtraction-within-20
  type: hard
- id: place-value-tens-and-ones
  type: hard
- id: decomposing-two-digit-numbers
  type: soft
builds-toward:
- subtraction-two-digit-regrouping-2nd
tags:
- subtraction
- two-digit
- algorithm
stage: concrete-operations
status: draft
---

# Two-Digit Subtraction Without Regrouping

## Core Idea
Subtracting two-digit numbers without regrouping means subtracting ones from ones and tens from tens separately, maintaining place value. Example: 35 - 12 = (30 - 10) + (5 - 2) = 20 + 3 = 23.

## Explainer

You already know how to subtract small numbers (within 20) and you understand that two-digit numbers are built from tens and ones. Two-digit subtraction without regrouping puts those two ideas together: handle the ones column and the tens column separately, exactly the same way you would for smaller numbers.

Think of 35 as 3 tens and 5 ones, and 12 as 1 ten and 2 ones. When you subtract, take the ones away from ones: 5 ones − 2 ones = 3 ones. Then take the tens away from tens: 3 tens − 1 ten = 2 tens. Put the results together: 2 tens and 3 ones = 23. The key insight is that each **place value column acts independently** — the ones never borrow from the tens, and the tens never borrow from the ones, as long as the top digit in each column is bigger than or equal to the bottom digit.

The phrase "without regrouping" means every column subtracts cleanly. You can check this before you start: look at the ones digits — if the top is greater than or equal to the bottom, no regrouping is needed. In 47 − 23, the ones digit 7 ≥ 3 and the tens digit 4 ≥ 2, so subtract column by column: 7 − 3 = 4, 4 tens − 2 tens = 2 tens, answer = 24. If you ever see a column where the top digit is smaller (like 32 − 15, where 2 < 5), that problem requires regrouping — a different skill you will learn next.

Writing the problem in stacked form (vertical format) helps you keep the columns lined up: ones under ones, tens under tens. This alignment is what lets you treat each column independently without mixing up the digits. Practice stacking numbers carefully, and subtraction becomes a simple process of two small subtractions side by side.
