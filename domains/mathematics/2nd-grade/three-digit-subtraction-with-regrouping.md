---
id: three-digit-subtraction-with-regrouping
title: Three-Digit Subtraction With Regrouping
domain: mathematics
course: 2nd-grade
prerequisites:
- id: three-digit-subtraction-no-regrouping
  type: hard
- id: regrouping-subtraction-trading-tens-for-ones
  type: hard
builds-toward:
- multi-digit-subtraction
tags:
- subtraction
- regrouping
stage: concrete-operations
status: validated
---

# Three-Digit Subtraction With Regrouping

## Core Idea
When subtracting three-digit numbers and a digit in the minuend is smaller than the digit below it, regroup by trading one ten for ten ones (or one hundred for ten tens). This allows you to solve problems like 325 - 148.

## How It's Best Learned
Model with base-ten blocks the trading process: breaking a ten into ones when needed. Use guided practice with problems that require regrouping in different places.

## Common Misconceptions
- Subtracting before regrouping occurs to the student.
- Regrouping but forgetting to subtract the amount borrowed.
- Regrouping from a zero.

## Questions

```yaml
- question: "You are solving 425 - 167. In the ones column, 5 - 7 is not possible. What is the correct first step?"
  type: multiple-choice
  options:
    - "Write 0 in the ones column and move on to the tens"
    - "Subtract 5 from 7 instead, giving 2, and write 2 in the ones column"
    - "Regroup: borrow 1 ten from the tens column, making the ones column 15 - 7"
    - "Start with the hundreds column first since the ones column has a problem"
  answer: 2
  explanation: "When the top digit in a column is smaller than the bottom digit, you regroup (borrow) from the next column. Take 1 ten from the tens place, reducing the tens digit from 2 to 1 and increasing the ones column from 5 to 15. Now 15 - 7 = 8. Option A (writing 0 and skipping) is wrong. Option B reverses the subtraction — subtracting 5 from 7 instead of 7 from 15 — a very common error that produces an incorrect result."

- question: "What must you do when you need to regroup in the ones column but the tens digit of the top number is 0?"
  type: multiple-choice
  options:
    - "Write 0 in the tens place and borrow from the ones column instead"
    - "Skip that step and only regroup in the hundreds column"
    - "First borrow from the hundreds to give the tens column something to lend, then borrow from the tens"
    - "The problem cannot be solved when a 0 appears in the tens place"
  answer: 2
  explanation: "A 0 in the tens column means you can't borrow from it directly — it's empty. The solution is a two-step trade: borrow 1 hundred from the hundreds column, which turns 0 tens into 10 tens. Now take 1 of those 10 tens for the ones column (giving 10 additional ones), leaving 9 tens. This is the trickiest regrouping case, but the logic is the same: you're trading across two columns instead of one."

- question: "Regrouping in subtraction changes the total value of the number you are subtracting from."
  type: true-false
  answer: false
  explanation: "Regrouping never changes the value of the number — it only changes how that value is written in place-value columns. For example, 325 can be written as 3 hundreds + 2 tens + 5 ones, or equivalently as 3 hundreds + 1 ten + 15 ones. Both represent exactly 325. You are renaming the number in a different form to make column subtraction possible, not adding or removing any quantity."

- question: "When you 'borrow' a ten during subtraction, you must remember to pay it back at the end of the problem."
  type: true-false
  answer: false
  explanation: "Nothing is actually borrowed or paid back — this is why the word 'borrow' is misleading. Regrouping renames the number: trading 1 ten for 10 ones changes how the digits appear in each column, but the total value is identical before and after. Once you've regrouped, the subtraction proceeds normally. There is no separate 'payback' step. The word 'regroup' or 'trade' describes the operation more accurately than 'borrow.'"

- question: "Explain why regrouping is sometimes called 'renaming' rather than 'borrowing,' and what stays the same during a regroup."
  type: short-answer
  answer: "Regrouping is 'renaming' because you rewrite the number in an equivalent form — changing 3 hundreds + 2 tens into 3 hundreds + 1 ten + 10 ones, for example. The total quantity (325) doesn't change, only how it's expressed in columns. Unlike 'borrowing,' nothing needs to be repaid — the new form is just as valid as the original."
  explanation: "Students who understand regrouping as renaming are much less likely to make procedural errors (like forgetting to reduce the tens digit after borrowing) because they understand WHY each step happens. The concept of equivalent representations — that 325 = 300 + 20 + 5 = 300 + 10 + 15 — is foundational to place-value understanding."
```

## Explainer

You already know two important skills from your prerequisites: how to subtract three-digit numbers when no regrouping is needed, and how to regroup when subtracting two-digit numbers — trading a ten for ten ones. Three-digit subtraction with regrouping combines these skills and extends them: now you may need to trade across two columns instead of one.

**Regrouping** (sometimes called borrowing) is the key operation. When the digit you're subtracting is larger than the digit above it, you can't subtract directly — you need to trade from the next column to get enough to work with. In 325 − 148: the ones column shows 5 − 8, which is impossible as-is. So you trade — take one ten from the tens column (turning 2 tens into 1 ten) and add those ten ones to the ones column (turning 5 ones into 15 ones). Now 15 − 8 = 7. Moving left: the tens column now shows 1 − 4, also impossible. Trade from the hundreds: turn 3 hundreds into 2 hundreds, and give 10 tens to the tens column (1 + 10 = 11 tens). Now 11 − 4 = 7. Finally, 2 − 1 = 1. The answer is 177.

The trickiest case is regrouping through a zero. If the tens digit is 0, you can't borrow a ten from there — it's empty. Instead, borrow from the hundreds column first: trade 1 hundred for 10 tens, then immediately trade 1 of those tens for 10 ones. This is a two-step trade across two columns. Base-ten blocks make this concrete: you physically exchange one hundreds flat for ten tens rods, then one rod for ten ones cubes, and see that the total quantity hasn't changed — only the form.

The important thing to understand is that regrouping doesn't change the value of the numbers — it only changes how they're written. 3 hundreds + 2 tens + 5 ones is the same quantity as 2 hundreds + 12 tens + 5 ones, or 2 hundreds + 11 tens + 15 ones. You're re-packaging the quantity into forms that make column subtraction possible. Once you see regrouping as renaming rather than "borrowing" (nothing is actually paid back), the whole procedure makes logical sense.
