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

## Questions

```yaml
- question: "A student computes 42 − 17. In the ones column, she tries to subtract 7 from 2 and gets stuck. What should she do?"
  type: multiple-choice
  options:
    - "Write a negative number in the ones column and continue"
    - "Skip the ones column and subtract only the tens: 4 − 1 = 3, so the answer is 30"
    - "Regroup: borrow 1 ten from the tens column, making the ones column 12, then subtract 12 − 7 = 5"
    - "Round both numbers before subtracting to avoid the problem"
  answer: 2
  explanation: "When the ones digit being subtracted is larger than the ones digit in the number, you must regroup. You borrow 1 ten from the tens column (reducing 4 tens to 3 tens) and add it to the ones column as 10 ones (making 2 + 10 = 12 ones). Then 12 − 7 = 5 ones, and 3 − 1 = 2 tens, giving 25. Skipping columns or getting a negative ones digit would produce wrong answers."

- question: "A student is computing 53 − 28. After regrouping, what does the number 53 become?"
  type: multiple-choice
  options:
    - "4 tens and 13 ones — the total is still 53"
    - "4 tens and 3 ones — the total is now 43"
    - "5 tens and 13 ones — you added ones without changing tens"
    - "3 tens and 13 ones — you borrowed two tens"
  answer: 0
  explanation: "Regrouping converts 53 into 4 tens + 13 ones. You take 1 ten from the tens column (reducing 5 to 4), and give it to the ones column as 10 ones (adding 10 to 3 to make 13). The total value stays at 53: 4 × 10 + 13 = 40 + 13 = 53. This is the key insight: regrouping rearranges the representation without changing the value. Option B incorrectly subtracts from the total; option C doesn't reduce the tens; option D takes two tens."

- question: "When you regroup in 32 − 15, the value of 32 changes to 22 because you took away one of the tens."
  type: true-false
  answer: false
  explanation: "This is the most important conceptual point about regrouping: it does not change the value of the number. After regrouping, 32 is represented as 2 tens + 12 ones instead of 3 tens + 2 ones, but 2 × 10 + 12 = 32 either way. You have not removed anything from the number — you have only changed how it is arranged. If students think the value changed, they will add or subtract incorrectly in the tens column."

- question: "In the problem 41 − 18, you cannot subtract the ones column without regrouping."
  type: true-false
  answer: true
  explanation: "In 41 − 18, the ones column asks you to subtract 8 from 1. Since 8 > 1, you cannot do this without going negative, so regrouping is required. You borrow 1 ten from the tens column (reducing 4 to 3) and add it to the ones (making 11), then compute 11 − 8 = 3 ones and 3 − 1 = 2 tens, giving 23. Whenever the ones digit being subtracted is larger than the ones digit in the top number, regrouping is necessary."

- question: "Why must you cross out the tens digit and write a smaller number after you regroup? What happens if you forget this step?"
  type: short-answer
  answer: "When you borrow a ten, that ten moves to the ones column — it no longer belongs to the tens column. If you don't reduce the tens digit, you're counting that ten twice: once in the ones column (where you added it) and once in the tens column (where you left it). This secretly adds 10 to your number and makes the final answer wrong."
  explanation: "Forgetting to reduce the tens digit is the most common regrouping error. For example, in 32 − 15, if you regroup to get 12 ones but leave the tens as 3 instead of writing 2, you will compute 2 − 1 = 1 ten and record 17 — the correct answer. But if you leave it as 3, you'll compute 3 − 1 = 2 tens, giving 27, which is wrong. The act of crossing out the old tens digit and writing the new one is the record-keeping step that prevents double-counting."
```

## Explainer

You have already learned to subtract two-digit numbers when the ones column works out cleanly — like 46 − 23, where 6 − 3 = 3 with no trouble. Regrouping kicks in when the problem tries to take a bigger ones digit away from a smaller one. In 32 − 15, the ones column asks you to subtract 5 from 2. You cannot do that without going negative. The solution is to **regroup**: borrow one group of ten from the tens column and break it into 10 ones.

Think of it with physical objects. You have 3 stacks of 10 blocks and 2 loose blocks — that is 32. You need to take away 15. You cannot grab 5 loose blocks because you only have 2. So you unwrap one stack: now you have 2 stacks of 10 and 12 loose blocks. The total is still 32, but the arrangement changed. Now you can take 5 loose blocks away (12 − 5 = 7), and take 1 stack away from the 2 remaining stacks (2 − 1 = 1). Result: 1 stack and 7 blocks = 17.

In the written algorithm, regrouping is recorded by crossing out the tens digit, writing a number one smaller, and placing a small "1" in front of the ones digit. In 32 − 15, cross out the 3, write 2 above it (because you used one ten), and write 12 in the ones column. Then subtract normally: 12 − 5 = 7, and 2 − 1 = 1. The **key insight** is that regrouping does not change the value of the number — 32 is still 32 whether written as 3 tens + 2 ones or 2 tens + 12 ones. You are just rearranging for convenience.

Watch out for the most common mistake: forgetting to reduce the tens digit after borrowing. If you borrow a ten but don't cross it out, you have secretly added 10 to the number. Always cross out the old tens digit and write the new, smaller one before subtracting in the tens column.
