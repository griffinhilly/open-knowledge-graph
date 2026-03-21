---
id: addition-three-digit-numbers-2nd
title: Three-Digit Addition
domain: mathematics
course: 2nd-grade
prerequisites:
- id: addition-two-digit-regrouping-2nd
  type: hard
- id: place-value-hundreds-2nd
  type: hard
builds-toward:
- addition-word-problems-2nd
tags:
- addition
- three-digit
- regrouping
stage: concrete-operations
status: draft
---

# Three-Digit Addition

## Core Idea
Three-digit addition follows the same principles as two-digit addition, extended to include hundreds. Add ones, regroup if needed; add tens, regroup if needed; add hundreds. Example: 236 + 157 requires attention to carrying across place values.

## Questions

```yaml
- question: "When adding 356 + 278, you add the ones: 6 + 8 = 14. What do you write in the ones place and what do you carry?"
  type: multiple-choice
  options:
    - "Write 14 in the ones place, carry nothing"
    - "Write 4 in the ones place, carry 1 to the tens column"
    - "Write 1 in the ones place, carry 4 to the tens column"
    - "Write 0 in the ones place, carry 14 to the tens column"
  answer: 1
  explanation: "When a column's sum is 10 or more, you write the ones digit of that sum and carry the tens digit to the next column left. 14 has a ones digit of 4 and a tens digit of 1. So you write 4 in the ones place and carry 1 to the tens column. The carried '1' represents 1 group of ten — the same regrouping you practiced with two-digit numbers."

- question: "When adding 475 + 263, a student adds the hundreds and writes '6' in the hundreds place. What error might they have made?"
  type: multiple-choice
  options:
    - "No error — 4 + 2 = 6, so the hundreds digit is always correct"
    - "The student may have forgotten to include a carry from the tens column into the hundreds"
    - "The student added the hundreds first instead of the ones"
    - "Hundreds can never be regrouped, so 6 must be correct"
  answer: 1
  explanation: "A carry from the tens column can change the hundreds sum. In 475 + 263: ones give 5 + 3 = 8 (no carry), tens give 7 + 6 = 13 (write 3, carry 1), hundreds give 4 + 2 + 1 (the carry) = 7, not 6. The student forgot to add the carried 1 from the tens column. Forgetting carries is the most common error in three-digit addition."

- question: "In three-digit addition, you always begin by adding the ones column and work left toward the hundreds."
  type: true-false
  answer: true
  explanation: "Right-to-left order is necessary because a sum in the ones column can produce a carry that must be added to the tens column, and a sum in the tens column can produce a carry for the hundreds column. If you added hundreds first, you wouldn't yet know whether a carry would arrive from the tens. Starting at the ones ensures every carry is included in the column that needs it."

- question: "Three-digit addition requires completely new skills compared to two-digit addition."
  type: true-false
  answer: false
  explanation: "Three-digit addition uses exactly the same regrouping principles as two-digit addition — it simply extends the process to a third column (hundreds). The rule is identical at every step: add the column, check if the sum is 10 or more, write the ones digit, carry the ten to the next column left. Two-digit addition taught you this pattern; three-digit addition applies it one column further."

- question: "Explain why you must start adding in the ones column rather than the hundreds column."
  type: short-answer
  answer: "You start with the ones column because a carry from the ones affects the tens, and a carry from the tens affects the hundreds. If you started at the hundreds, you wouldn't yet know whether an extra ten would arrive from the tens column below. Starting on the right and working left ensures that every carry gets included in the correct column, producing the right answer."
  explanation: "Right-to-left order preserves the chain of dependencies: ones → tens → hundreds. Each column must be resolved before the column to its left can be finalized. This isn't an arbitrary convention — it reflects how place value and carrying work together. The same principle applies whether you're adding two-digit or three-digit numbers."
```

## Explainer

You already know how to add two-digit numbers with regrouping — borrowing and carrying between the ones and tens places. Three-digit addition uses that exact same skill, just with one more column added on the left. Think of it as playing the same game, but now there's a third player: the hundreds place.

Start with the column you already know best: the ones. Add the ones digits first. If the sum is 10 or more, you **regroup** — write down the ones part and carry the ten to the tens column. This is identical to what you did with two-digit numbers. For example, in 236 + 157, add 6 + 7 = 13. Write 3 in the ones place, carry 1 to the tens.

Next, move to the tens column — but don't forget the 1 you carried. Add 3 + 5 + 1 (the carried ten) = 9. No regrouping needed here, so write 9. Finally, add the hundreds: 2 + 1 = 3. The answer is 393. Every step was something you already knew; you just applied it to a new column.

The key insight from your place value work is that each column has its own value — ones, tens, hundreds — and they stay separate except when you carry. **Carrying** moves a group of ten from one column to the next column to the left. It's the same idea whether you're moving 10 ones into the tens place or 10 tens into the hundreds place. The process is always: add the column, check if it's 10 or more, carry if needed, move left.
