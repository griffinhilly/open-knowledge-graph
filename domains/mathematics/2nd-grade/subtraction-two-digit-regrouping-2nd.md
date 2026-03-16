---
id: subtraction-two-digit-regrouping-2nd
title: Two-Digit Subtraction With Regrouping
domain: mathematics
course: 2nd-grade
prerequisites:
- id: two-digit-subtraction-no-regrouping-2nd
  type: hard
- id: regrouping-subtraction-trading-tens-for-ones
  type: hard
builds-toward:
- subtraction-three-digit-numbers-2nd
tags:
- subtraction
- two-digit
- regrouping
- borrowing
stage: concrete-operations
status: draft
---

# Two-Digit Subtraction With Regrouping

## Core Idea
When the ones digit being subtracted exceeds the minuend's ones, regroup 1 ten into 10 ones. In 32 - 15, cannot subtract 5 from 2, so regroup: 32 = 2 tens + 12 ones, then 12 - 5 = 7 ones, 2 - 1 = 1 ten, result is 17.

## Explainer

You have already learned to subtract two-digit numbers when the ones column works out cleanly — like 46 − 23, where 6 − 3 = 3 with no trouble. Regrouping kicks in when the problem tries to take a bigger ones digit away from a smaller one. In 32 − 15, the ones column asks you to subtract 5 from 2. You cannot do that without going negative. The solution is to **regroup**: borrow one group of ten from the tens column and break it into 10 ones.

Think of it with physical objects. You have 3 stacks of 10 blocks and 2 loose blocks — that is 32. You need to take away 15. You cannot grab 5 loose blocks because you only have 2. So you unwrap one stack: now you have 2 stacks of 10 and 12 loose blocks. The total is still 32, but the arrangement changed. Now you can take 5 loose blocks away (12 − 5 = 7), and take 1 stack away from the 2 remaining stacks (2 − 1 = 1). Result: 1 stack and 7 blocks = 17.

In the written algorithm, regrouping is recorded by crossing out the tens digit, writing a number one smaller, and placing a small "1" in front of the ones digit. In 32 − 15, cross out the 3, write 2 above it (because you used one ten), and write 12 in the ones column. Then subtract normally: 12 − 5 = 7, and 2 − 1 = 1. The **key insight** is that regrouping does not change the value of the number — 32 is still 32 whether written as 3 tens + 2 ones or 2 tens + 12 ones. You are just rearranging for convenience.

Watch out for the most common mistake: forgetting to reduce the tens digit after borrowing. If you borrow a ten but don't cross it out, you have secretly added 10 to the number. Always cross out the old tens digit and write the new, smaller one before subtracting in the tens column.
