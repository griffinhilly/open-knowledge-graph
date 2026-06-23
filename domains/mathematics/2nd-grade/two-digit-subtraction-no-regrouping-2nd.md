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
- id: place-value-tens-and-ones-2nd-grade
  type: hard
builds-toward:
- subtraction-two-digit-regrouping-2nd
tags:
- subtraction
- two-digit
- algorithm
stage: concrete-operations
status: validated
---

# Two-Digit Subtraction Without Regrouping

## Core Idea
Subtracting two-digit numbers without regrouping means subtracting ones from ones and tens from tens separately, maintaining place value. Example: 35 - 12 = (30 - 10) + (5 - 2) = 20 + 3 = 23.

## Questions

```yaml
- question: "What is 57 - 23?"
  type: multiple-choice
  options:
    - "34 — subtract ones from ones (7 - 3 = 4) and tens from tens (5 - 2 = 3)"
    - "30 — subtract only the tens and ignore the ones"
    - "36 — add the difference of each digit column"
    - "24 — subtract all the digits and combine them"
  answer: 0
  explanation: "Two-digit subtraction without regrouping works by treating each place value column independently: 7 ones - 3 ones = 4 ones, and 5 tens - 2 tens = 3 tens. Result: 3 tens and 4 ones = 34. The key is that the columns do not interact — ones subtraction stays in the ones place, tens subtraction stays in the tens place."

- question: "A student is about to subtract 48 - 25. Before calculating, how can she check whether the problem requires regrouping?"
  type: multiple-choice
  options:
    - "Check whether the answer will be larger than 20"
    - "Check whether the tens digit of 48 is larger than the tens digit of 25"
    - "Check whether the ones digit of 48 (8) is greater than or equal to the ones digit of 25 (5)"
    - "Regrouping is only needed when the numbers are more than 50 apart"
  answer: 2
  explanation: "Regrouping is required when the ones digit on top is smaller than the ones digit on the bottom — because you cannot subtract a larger number from a smaller one without borrowing. In 48 - 25, the ones digit 8 ≥ 5, so no regrouping is needed. In 32 - 15, the ones digit 2 < 5, so regrouping would be required. Checking the ones column first is the reliable way to classify a problem before starting."

- question: "In 79 - 34, the tens column and the ones column are solved completely independently — the ones subtraction has no effect on the tens subtraction."
  type: true-false
  answer: true
  explanation: "True — and this is the defining feature of no-regrouping subtraction. When the top digit in every column is greater than or equal to the bottom digit, each column subtracts cleanly without borrowing from the column to its left. The ones subtraction (9 - 4 = 5) is entirely separate from the tens subtraction (7 - 3 = 4). Columns only interact in regrouping problems."

- question: "For 65 - 32, you could subtract the tens first (65 - 30 = 35) and then subtract the ones (35 - 2 = 33) and get the correct answer, because the columns act independently."
  type: true-false
  answer: true
  explanation: "True. Because 32 = 30 + 2, you can subtract the tens and ones in any order and get the same result. This works because place value columns are independent in a no-regrouping problem — tens subtraction and ones subtraction do not interfere with each other. This flexibility is a useful mental math strategy that builds on the same column-independence principle as the standard algorithm."

- question: "What does it mean for place value columns to act independently in two-digit subtraction, and why does this only hold when there is no regrouping?"
  type: short-answer
  answer: "Acting independently means the ones column and tens column each perform their subtraction separately, with no borrowing between them. The ones digit of the answer comes purely from the ones column; the tens digit comes purely from the tens column. This holds only when every column's top digit is greater than or equal to its bottom digit — because then each column has enough to subtract from without needing to borrow from the column to its left. If the ones digit is too small to subtract from, it must borrow from the tens column (regrouping), breaking the independence."
  explanation: "Understanding this independence is what makes the no-regrouping algorithm clean: it is literally two single-digit subtractions placed side by side. Recognizing when independence breaks down — when the ones digit is smaller than the number being subtracted — is the conceptual bridge to the next skill: regrouping."
```

## Explainer

You already know how to subtract small numbers (within 20) and you understand that two-digit numbers are built from tens and ones. Two-digit subtraction without regrouping puts those two ideas together: handle the ones column and the tens column separately, exactly the same way you would for smaller numbers.

Think of 35 as 3 tens and 5 ones, and 12 as 1 ten and 2 ones. When you subtract, take the ones away from ones: 5 ones − 2 ones = 3 ones. Then take the tens away from tens: 3 tens − 1 ten = 2 tens. Put the results together: 2 tens and 3 ones = 23. The key insight is that each **place value column acts independently** — the ones never borrow from the tens, and the tens never borrow from the ones, as long as the top digit in each column is bigger than or equal to the bottom digit.

The phrase "without regrouping" means every column subtracts cleanly. You can check this before you start: look at the ones digits — if the top is greater than or equal to the bottom, no regrouping is needed. In 47 − 23, the ones digit 7 ≥ 3 and the tens digit 4 ≥ 2, so subtract column by column: 7 − 3 = 4, 4 tens − 2 tens = 2 tens, answer = 24. If you ever see a column where the top digit is smaller (like 32 − 15, where 2 < 5), that problem requires regrouping — a different skill you will learn next.

Writing the problem in stacked form (vertical format) helps you keep the columns lined up: ones under ones, tens under tens. This alignment is what lets you treat each column independently without mixing up the digits. Practice stacking numbers carefully, and subtraction becomes a simple process of two small subtractions side by side.
