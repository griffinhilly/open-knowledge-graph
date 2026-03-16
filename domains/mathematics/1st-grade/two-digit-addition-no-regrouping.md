---
id: two-digit-addition-no-regrouping
title: Two-Digit Addition Without Regrouping
domain: mathematics
course: 1st-grade
prerequisites:
- id: place-value-tens-and-ones
  type: hard
- id: addition-within-20
  type: hard
builds-toward:
- addition-subtraction-word-problems
tags:
- addition
- two-digit
- algorithms
stage: pre-formal
status: draft
---

# Two-Digit Addition Without Regrouping

## Core Idea
Adding two-digit numbers without regrouping means adding tens to tens and ones to ones separately. For example, 23 + 15 becomes (20+10) + (3+5) = 38. No carrying is needed.

## Explainer

You already know from place value that a two-digit number like 34 means 3 tens and 4 ones — not 34 separate objects but a structured bundle. Two-digit addition without regrouping builds directly on that idea: because tens are separate from ones, you can add the parts in each "column" independently, then combine the results.

Take 23 + 15. Rather than counting all the way up from 23 to 38, you can think: the tens column has 2 tens + 1 ten = 3 tens, and the ones column has 3 ones + 5 ones = 8 ones. Put them together: 3 tens and 8 ones = 38. You didn't need to count by ones at all — place value did the organizing for you.

The phrase "no regrouping" is the important constraint here. It means each column's sum stays below 10, so you never have to trade 10 ones for 1 ten. The ones sum is just ones, and the tens sum is just tens. This clean separation is why the method works: each column behaves like a simpler addition-within-20 problem you've already mastered.

When you use the stacking method — writing one number above the other and aligning them vertically — you're using the column structure to make this independence visible. The ones digit of 23 sits directly above the ones digit of 15, and the tens digit sits above the tens digit. As long as each column adds to 9 or less, you can work column by column and simply read off the answer.
