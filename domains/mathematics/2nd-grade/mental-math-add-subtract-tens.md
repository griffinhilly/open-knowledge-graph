---
id: mental-math-add-subtract-tens
title: 'Mental Math: Adding and Subtracting Tens'
domain: mathematics
course: 2nd-grade
prerequisites:
- id: adding-tens
  type: hard
- id: place-value-tens-and-ones
  type: hard
builds-toward:
- addition-within-100
- subtraction-within-100
- mental-math-add-subtract-hundreds
tags:
- mental-math
- tens
- strategies
- place-value
stage: concrete-operations
status: validated
---

# Mental Math: Adding and Subtracting Tens

## Core Idea
Adding or subtracting a multiple of 10 from any two-digit number changes only the tens digit, leaving the ones digit unchanged. To compute 47 + 30, think: 4 tens + 3 tens = 7 tens, so the result is 77. Similarly, 82 − 50 = 32 because 8 tens − 5 tens = 3 tens. This mental strategy is faster than the written algorithm and builds number sense.

## How It's Best Learned
Use a hundred chart and have students move up or down rows (each row = 10) to visualize adding or subtracting tens. Then practice mentally, gradually removing the chart. Emphasize the pattern: 'only the tens digit changes.'

## Common Misconceptions
- Changing the ones digit when adding tens (e.g., computing 47 + 30 = 80 instead of 77).
- Not applying this strategy spontaneously — students may revert to column addition even when mental math is faster.
- Confusion when the tens addition causes regrouping (e.g., 75 + 40 = 115, crossing into the hundreds).

## Questions

```yaml
- question: "What is 63 + 20?"
  type: multiple-choice
  options:
    - "83 — add 2 to the tens digit, leave the ones digit unchanged"
    - "85 — add 20 to both the tens and ones digits"
    - "65 — add 2 to the ones digit"
    - "280 — add the digits and multiply by 10"
  answer: 0
  explanation: "Adding 20 means adding 2 tens. Only the tens digit changes: 6 tens + 2 tens = 8 tens. The ones digit (3) stays exactly as it is. The answer is 83. Option C shows the most common error — mistakenly adding to the ones digit instead of the tens digit."

- question: "A student computes 47 + 30 and gets 80. What mistake did she most likely make?"
  type: multiple-choice
  options:
    - "She added 30 to the ones digit (7 + 3 = 10, carried, and lost the original ones digit)"
    - "She added the individual digits of 47 and 30 together and multiplied"
    - "She used subtraction instead of addition"
    - "She forgot to carry a digit into the hundreds place"
  answer: 0
  explanation: "The most common error when adding tens is accidentally modifying the ones digit. If she computed 7 + 3 = 10 and wrote 8 tens with 0 ones, she got 80 instead of 77. The correct reasoning: adding 30 only affects the tens digit. 4 tens + 3 tens = 7 tens, ones digit stays 7, answer = 77. The ones digit is completely untouched by adding a multiple of 10."

- question: "When you add 40 to a two-digit number, the ones digit of the result is always the same as the ones digit of the original number."
  type: true-false
  answer: true
  explanation: "True. Adding 40 means adding 4 tens. Tens additions only affect the tens column. The ones digit is completely independent and unchanged. This holds for any two-digit number plus any multiple of 10, as long as the tens sum does not exceed 9 and carry into the hundreds."

- question: "The mental strategy of 'mainly change the tens digit' typically produces a two-digit answer, even when large multiples of 10 are added."
  type: true-false
  answer: false
  explanation: "False. When the tens digits sum to 10 or more, the result crosses into the hundreds. For example, 75 + 40: 7 tens + 4 tens = 11 tens = 1 hundred and 1 ten, plus the 5 ones = 115. The ones digit (5) is still unchanged, but there is now a hundreds digit. The strategy still works conceptually — you only add the tens — but regrouping into the hundreds must be handled."

- question: "Why does adding 30 to 47 change only the tens digit and not the ones digit? Explain using place value."
  type: short-answer
  answer: "Because 30 is made entirely of tens — it has 0 ones. When you add 30 to 47, you are adding 3 tens to the 4 tens in 47. The ones column (which has 7 ones) receives nothing from 30, so it stays at 7. Place value columns are independent: a tens addition only interacts with the tens column. The result is 7 tens and 7 ones = 77."
  explanation: "Place value separates numbers into independent columns. A multiple of 10 like 30 has no ones component, so it can only interact with the tens column. This independence is what makes the mental math strategy work — and also reveals why the common mistake of changing the ones digit is wrong: nothing in 30 touches the ones place."
```

## Explainer

You already know how place value works: a two-digit number like 47 is made of 4 tens and 7 ones. That structure is the key to mental addition and subtraction with tens. When you add a multiple of 10 — a number like 20, 30, or 50 — you are only adding to the tens part of the number. The ones part stays exactly the same.

Imagine a hundred chart laid out in front of you. Every row is a group of 10. When you add 30, you jump down three rows. Your column — your ones digit — never changes. If you start at 47 (column 7, row 4), jumping down three rows lands you at 77. The ones digit is still 7. This is why the rule works: **adding tens only changes the tens digit**.

The same idea runs backwards for subtraction. To compute 82 − 50, ask: "8 tens minus 5 tens is how many tens?" The answer is 3 tens — and the 2 in the ones place never moved. So 82 − 50 = 32. No writing required. You are doing tens arithmetic just like you learned to do ones arithmetic, using the same counting skills but applied one column to the left.

The one situation that requires extra care is when the tens digits add up to 10 or more, causing a carry into the hundreds. For example, 75 + 40: 7 tens + 4 tens = 11 tens = 110, plus the 5 ones = 115. The ones digit is still 5, but you now have a hundreds digit too. The strategy still works — you just need to handle the regrouping in your head, which gets easier with practice.
