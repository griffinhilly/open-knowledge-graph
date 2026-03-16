---
id: three-digit-addition
title: Three-Digit Addition
domain: mathematics
course: 2nd-grade
prerequisites:
- id: addition-within-100
  type: hard
- id: place-value-hundreds
  type: hard
- id: mental-math-add-subtract-hundreds
  type: soft
- id: number-line-to-1000
  type: soft
- id: three-digit-number-forms
  type: soft
builds-toward:
- three-digit-subtraction
- multi-digit-addition
- two-step-word-problems
tags:
- addition
- three-digit
- regrouping
- algorithm
stage: concrete-operations
status: validated
---
# Three-Digit Addition

## Core Idea
Adding three-digit numbers extends the same column-by-column algorithm used for two-digit numbers: add ones, regroup if needed; add tens (including any carried ten), regroup if needed; add hundreds (including any carried hundred). A problem may require regrouping in one column, both columns, or neither. Understanding why regrouping occurs — not just the steps — is essential.

## How It's Best Learned
Use base-ten blocks for the first examples, trading cubes for rods and rods for flats as needed. Then connect the blocks to the written algorithm step by step. Include examples with no regrouping, one regrouping, and two regroupings so students learn to check each column independently.

## Common Misconceptions
- Forgetting to carry from the tens column to the hundreds.
- Carrying a digit but then not adding it in the next column.
- Adding hundreds + tens + ones as if they are all the same place (treating 3-digit numbers as 3 separate single digits).

## Explainer

You already know how to add two-digit numbers with regrouping — for example, 47 + 38: you add the ones (7 + 8 = 15), write the 5, carry the 1 ten, then add the tens column (4 + 3 + 1 = 8). Three-digit addition is exactly the same process, just extended one column to the left. The algorithm doesn't change — it just has one more column to work through.

Take 364 + 278. Start at the **ones column**: 4 + 8 = 12. Write the 2, carry the 1 (one extra ten). Move to the **tens column**: 6 + 7 = 13, then add the carried 1 to get 14. Write the 4, carry the 1 (one extra hundred). Move to the **hundreds column**: 3 + 2 = 5, then add the carried 1 to get 6. Answer: 642. Notice that regrouping happened twice here — the ones pushed into the tens, and the tens pushed into the hundreds. Each column is independent; you only need to track what spills over into the next column to the left.

The underlying logic is **place value**. When you write a 2 in the ones place and carry a 1, you're saying "I have 12 ones, which equals 1 ten and 2 ones — so I record 2 ones here and send 1 ten up to the tens column." The carried digit is never just a floating number; it represents a real group of ten (or a hundred) that belongs in the next column.

Problems can require regrouping in zero, one, or both columns — and you should check each column independently. Don't assume that because the ones column didn't regroup, the tens won't either. A useful habit: after completing the addition, verify by estimating (300 + 300 = 600, so 642 is reasonable). This extension of the algorithm to three digits is a direct preview of how the same method handles four-digit, five-digit, or any-digit addition — the process just keeps adding columns to the left.
