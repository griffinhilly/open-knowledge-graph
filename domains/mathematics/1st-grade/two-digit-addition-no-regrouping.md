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
- id: adding-tens
  type: soft
- id: two-digit-number-composition-1st
  type: hard
- id: core-number
  type: hard
- id: discernment-same-different
  type: soft
builds-toward:
- addition-subtraction-word-problems
tags:
- addition
- two-digit
- algorithms
stage: pre-formal
status: validated
---

# Two-Digit Addition Without Regrouping

## Core Idea
Adding two-digit numbers without regrouping means adding tens to tens and ones to ones separately. For example, 23 + 15 becomes (20+10) + (3+5) = 38. No carrying is needed.

## Questions

```yaml
- question: "Why can you solve 34 + 52 by adding the ones digits and the tens digits separately?"
  type: multiple-choice
  options:
    - "Because the tens digits are always larger, so you save them for last"
    - "Because place value keeps tens and ones in separate groups that don't affect each other"
    - "Because that is just the rule for addition — always start with the ones"
    - "Because the ones column must finish before the tens column can have a value"
  answer: 1
  explanation: "Place value is the reason column-by-column addition works. A two-digit number is structured as tens plus ones — 34 is 30 + 4, and 52 is 50 + 2. Because tens and ones are separate place-value groups, you can add each group independently: 30 + 50 = 80, 4 + 2 = 6, giving 86. The columns are independent because they represent different-sized units. Starting with the ones is a helpful convention, but it isn't the fundamental reason the method works."

- question: "A student writes 23 + 45 vertically. She adds the ones (3 + 5 = 8) and then the tens (2 + 4 = 6) and writes 68. Is she correct, and why?"
  type: multiple-choice
  options:
    - "No — she forgot to add the tens together before writing the answer"
    - "Yes — she correctly used place value to add each column independently"
    - "No — she should have added the tens column before the ones column"
    - "Yes — but only because the ones digits happen to be small numbers"
  answer: 1
  explanation: "Her method is exactly correct. 23 + 45 = (20 + 40) + (3 + 5) = 60 + 8 = 68. Because neither column sums to 10 or more, the result in each column is a single digit that fits directly in its place. What matters is that each column is treated independently, which is what place value makes possible. The order — ones first or tens first — doesn't affect the answer when there is no regrouping."

- question: "In two-digit addition without regrouping, the ones digits must sum to 9 or less for the column method to work cleanly."
  type: true-false
  answer: true
  explanation: "This is the defining condition of 'no regrouping.' When ones digits sum to 9 or less, the result is a single digit that fits in the ones place with nothing left over. If the sum were 10 or more, you'd need to trade 10 ones for 1 ten (regrouping), which would affect the tens column. As long as ones digits sum to 9 or less, the two columns stay independent and the method works without carrying."

- question: "To add 47 + 31, you can add 4 + 3 = 7 (tens) and 7 + 1 = 8 (ones) to get 78, with no regrouping needed."
  type: true-false
  answer: true
  explanation: "Yes — 47 + 31 requires no regrouping because the ones digits 7 + 1 = 8, which is less than 10. So the tens column gives 4 + 3 = 7 tens, and the ones column gives 7 + 1 = 8 ones, for an answer of 78. Each column adds independently and neither overflows. This is the key feature of no-regrouping problems: complete column independence."

- question: "Why does place value make it possible to add two-digit numbers column by column?"
  type: short-answer
  answer: "Place value separates a number into tens and ones — two independent groups with different-sized units. Because tens only affect tens and ones only affect ones, you can add each group separately and combine the results. 23 + 15 = (20 + 10) + (3 + 5) = 30 + 8 = 38. The columns don't interfere with each other as long as no column overflows past 9."
  explanation: "The entire logic of column addition rests on place value. A two-digit number isn't just a pair of digits — it's a structured quantity where the left digit counts tens and the right digit counts ones. Since tens and ones are separate units, adding them in groups is valid and exact. This is why aligning numbers vertically by place value is so important: it makes the column structure visible so you can add corresponding groups together correctly."
```

## Explainer

You already know from place value that a two-digit number like 34 means 3 tens and 4 ones — not 34 separate objects but a structured bundle. Two-digit addition without regrouping builds directly on that idea: because tens are separate from ones, you can add the parts in each "column" independently, then combine the results.

Take 23 + 15. Rather than counting all the way up from 23 to 38, you can think: the tens column has 2 tens + 1 ten = 3 tens, and the ones column has 3 ones + 5 ones = 8 ones. Put them together: 3 tens and 8 ones = 38. You didn't need to count by ones at all — place value did the organizing for you.

The phrase "no regrouping" is the important constraint here. It means each column's sum stays below 10, so you never have to trade 10 ones for 1 ten. The ones sum is just ones, and the tens sum is just tens. This clean separation is why the method works: each column behaves like a simpler addition-within-20 problem you've already mastered.

When you use the stacking method — writing one number above the other and aligning them vertically — you're using the column structure to make this independence visible. The ones digit of 23 sits directly above the ones digit of 15, and the tens digit sits above the tens digit. As long as each column adds to 9 or less, you can work column by column and simply read off the answer.
