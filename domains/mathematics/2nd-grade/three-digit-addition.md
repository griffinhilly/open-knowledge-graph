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

## Questions

```yaml
- question: "A student solves 456 + 278 step by step. They correctly carry a 1 from the tens column but forget to add it when computing the hundreds column. What is wrong with their final answer?"
  type: multiple-choice
  options:
    - "The ones digit is wrong."
    - "The tens digit is wrong."
    - "The hundreds digit is 1 too small — one carried hundred was never added in."
    - "Nothing — the carried digit from the tens column has no effect on the hundreds column."
  answer: 2
  explanation: "When the tens-column sum (including any carry from the ones) reaches 10 or more, you carry a 1 to the hundreds column. If you forget to add that carry in the hundreds column, your hundreds digit is 1 less than it should be, making the entire answer 100 short. This is the most common error in three-digit addition: the carry is generated but then dropped."

- question: "In the problem 364 + 278, after adding the ones column (4 + 8 = 12), what does the carried '1' above the tens column actually represent?"
  type: multiple-choice
  options:
    - "A reminder note with no specific value."
    - "One extra ten — because 12 ones equals 1 ten and 2 ones, and that ten must move to the tens column."
    - "One extra hundred that needs to be added at the end."
    - "An instruction to add 1 to every remaining column."
  answer: 1
  explanation: "When you add 4 + 8 = 12, you have 12 ones. That equals 1 ten and 2 ones. You record the 2 ones in the ones column and send the 1 ten to the tens column, where it belongs. The carried digit is a real place-value object — not an abstract bookkeeping mark. Understanding this is what lets you extend the algorithm to any number of columns."

- question: "A three-digit addition problem can require regrouping in both the ones column and the tens column."
  type: true-false
  answer: true
  explanation: "When the ones-column sum is 10 or more, you carry a ten. When the tens-column sum (including any carry from ones) is also 10 or more, you carry a hundred into the hundreds column. Problems like 364 + 278 require two regroupings. Each column is evaluated independently — one carry does not prevent another."

- question: "If the ones column in a three-digit addition problem does not require regrouping, then the tens column will not require regrouping either."
  type: true-false
  answer: false
  explanation: "The columns are independent. Whether the tens column requires regrouping depends on its own digit sums plus any carry from ones — not on what happened in the ones column. Even if the ones column sums cleanly (e.g., 2 + 3 = 5), the tens column could still sum to 10 or more (e.g., 7 + 8 = 15). You must evaluate each column on its own."

- question: "What does the carried digit actually represent in three-digit addition, and why must it be included in the next column?"
  type: short-answer
  answer: "The carried digit represents a real place-value group — a ten (or a hundred) — that was too large to stay in the current column. For example, if the ones column gives 14, that is 1 ten and 4 ones. The 4 stays in the ones place and the 1 ten must move left to the tens column because that is where tens belong. If you skip the carry, your answer is missing an entire group of ten (or hundred), making it 10 or 100 less than it should be."
  explanation: "Students who treat the carry as a memorized rule often forget it or misplace it. Students who understand it as a real place-value group naturally carry it to the correct column and notice when they've forgotten — because the answer feels too small."
```

## Explainer

You already know how to add two-digit numbers with regrouping — for example, 47 + 38: you add the ones (7 + 8 = 15), write the 5, carry the 1 ten, then add the tens column (4 + 3 + 1 = 8). Three-digit addition is exactly the same process, just extended one column to the left. The algorithm doesn't change — it just has one more column to work through.

Take 364 + 278. Start at the **ones column**: 4 + 8 = 12. Write the 2, carry the 1 (one extra ten). Move to the **tens column**: 6 + 7 = 13, then add the carried 1 to get 14. Write the 4, carry the 1 (one extra hundred). Move to the **hundreds column**: 3 + 2 = 5, then add the carried 1 to get 6. Answer: 642. Notice that regrouping happened twice here — the ones pushed into the tens, and the tens pushed into the hundreds. Each column is independent; you only need to track what spills over into the next column to the left.

The underlying logic is **place value**. When you write a 2 in the ones place and carry a 1, you're saying "I have 12 ones, which equals 1 ten and 2 ones — so I record 2 ones here and send 1 ten up to the tens column." The carried digit is never just a floating number; it represents a real group of ten (or a hundred) that belongs in the next column.

Problems can require regrouping in zero, one, or both columns — and you should check each column independently. Don't assume that because the ones column didn't regroup, the tens won't either. A useful habit: after completing the addition, verify by estimating (300 + 300 = 600, so 642 is reasonable). This extension of the algorithm to three digits is a direct preview of how the same method handles four-digit, five-digit, or any-digit addition — the process just keeps adding columns to the left.
