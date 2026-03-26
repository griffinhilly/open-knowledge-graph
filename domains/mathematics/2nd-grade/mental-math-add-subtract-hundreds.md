---
id: mental-math-add-subtract-hundreds
title: 'Mental Math: Adding and Subtracting Hundreds'
domain: mathematics
course: 2nd-grade
prerequisites:
- id: mental-math-add-subtract-tens
  type: hard
- id: place-value-hundreds
  type: hard
- id: skip-counting-by-100s
  type: soft
- id: rounding-to-nearest-hundred
  type: soft
builds-toward:
- three-digit-addition
- three-digit-subtraction
tags:
- mental-math
- hundreds
- strategies
- place-value
stage: concrete-operations
status: validated
---
# Mental Math: Adding and Subtracting Hundreds

## Core Idea
Adding or subtracting a multiple of 100 changes only the hundreds digit. To compute 400 + 300, think: 4 hundreds + 3 hundreds = 7 hundreds = 700. To compute 850 − 200, think: 8 hundreds − 2 hundreds = 6 hundreds, result is 650. This strategy extends the tens mental-math pattern to the hundreds place, reinforcing the structure of the base-ten system.

## How It's Best Learned
Build on the mental-math-tens skill explicitly. Show the parallel: just as 47 + 30 only changes the tens digit, 470 + 300 only changes the hundreds digit. Practice with a mix of tens and hundreds problems so students choose the right strategy.

## Common Misconceptions
- Adding hundreds to the wrong place (e.g., 450 + 300 = 480).
- Not recognizing when this fast strategy applies vs. when full regrouping is needed.
- Confusing hundreds addition with tens addition when numbers are similar.

## Questions

```yaml
- question: "What is 650 + 300?"
  type: multiple-choice
  options:
    - "680 — add 3 to the tens digit"
    - "950 — add 3 to the hundreds digit, tens and ones unchanged"
    - "9500 — multiply by 3"
    - "653 — add 3 to the ones digit"
  answer: 1
  explanation: "300 is 3 hundreds. You already have 6 hundreds in 650. 6 hundreds + 3 hundreds = 9 hundreds. The tens (5) and ones (0) are untouched. Result: 950. Only the hundreds digit changes — this is the whole point of the mental math strategy for hundreds. Option A is a common error: adding to the wrong column."

- question: "A student computes 450 + 300 = 480. What mistake did the student make?"
  type: multiple-choice
  options:
    - "They forgot to carry the 1"
    - "They added 300 to the tens place instead of the hundreds place"
    - "They should have added 300 to each digit separately"
    - "They made an arithmetic error: 4 + 3 = 8 is wrong, it should be 7"
  answer: 1
  explanation: "300 affects only the hundreds column. The student added 3 to the tens digit (5 + 3 = 8) instead of the hundreds digit (4 + 3 = 7). The correct answer is 750: 4 hundreds + 3 hundreds = 7 hundreds, and the '50' rides along unchanged. This error reveals a place-value confusion — not knowing which column a multiple of 100 belongs to."

- question: "To solve 740 − 200 mentally, you only need to change the hundreds digit."
  type: true-false
  answer: true
  explanation: "200 is 2 hundreds. Subtract 2 hundreds from the 7 hundreds in 740: 7 − 2 = 5 hundreds. The tens digit (4) and ones digit (0) are untouched. Result: 540. The strategy works because subtracting a multiple of 100 affects only the hundreds column — the tens and ones are irrelevant."

- question: "Adding 300 to any number typically changes three digits in the result."
  type: true-false
  answer: false
  explanation: "Adding 300 changes only the hundreds digit (unless that causes regrouping into the thousands, which won't happen within the range of these problems). The tens and ones digits stay completely the same. For example, 450 + 300 = 750: only the hundreds digit changed from 4 to 7. The idea that '300 is a three-digit number so it changes three digits' is an intuitive but false conclusion."

- question: "Why can you add or subtract hundreds without ever touching the tens and ones digits?"
  type: short-answer
  answer: "Because multiples of 100 add to the hundreds column only. In our base-ten system, 100 is exactly one unit in the hundreds place and zero units in every other place. So adding 300 means adding 3 to the hundreds digit. The tens and ones digits represent a completely separate part of the number — they are not involved in hundreds arithmetic at all."
  explanation: "This is the column-independence principle of place value: each column operates independently when you're adding a number that belongs entirely to one column. The same logic explains why adding 30 changes only the tens digit (not the ones), and adding 3 changes only the ones. Understanding this unlocks mental math across all place values."
```

## Explainer

You already know how to add and subtract tens in your head — for example, 47 + 30 = 77 because 4 tens + 3 tens = 7 tens, and only the tens digit changes. Adding and subtracting hundreds works in exactly the same way, just one place-value column to the left.

When you see 400 + 300, don't think of it as four hundred plus three hundred. Think of it as **4 hundreds + 3 hundreds = 7 hundreds = 700**. The ones and tens digits stay at zero; only the hundreds digit changes. The same idea works with non-round numbers: in 450 + 300, the 50 is untouched — you're only adding hundreds, so 4 hundreds + 3 hundreds = 7 hundreds, giving 750.

Subtraction works the same way in reverse. For 850 − 200, ask: "how many hundreds do I have, and how many am I taking away?" You have 8 hundreds; take away 2 hundreds; left with 6 hundreds. The tens and ones (50) ride along unchanged: 650. This is the same move you made when subtracting tens, just one column over.

The pattern here is bigger than this one skill — it's a window into how the **base-ten system** works. Every place value behaves by the same rules; only the column name changes. Once you can add and subtract ones, tens, and hundreds mentally, you're building the number sense that makes bigger arithmetic feel manageable. When you encounter a problem like 570 + 400, you can immediately see it as a hundreds problem, answer 970 in seconds, and move on — no paper, no counting. That speed and confidence is the payoff of understanding place value deeply.
