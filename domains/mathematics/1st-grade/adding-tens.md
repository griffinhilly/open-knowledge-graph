---
id: adding-tens
title: Adding Tens to a Two-Digit Number
domain: mathematics
course: 1st-grade
prerequisites:
- id: place-value-tens-and-ones
  type: hard
- id: addition-within-10
  type: hard
- id: skip-counting-by-10s
  type: soft
builds-toward:
- two-digit-addition-no-regrouping
tags:
- addition
- tens
- place-value
- mental-math
- two-digit
stage: pre-formal
status: validated
---

# Adding Tens to a Two-Digit Number

## Core Idea
Adding a multiple of ten to any two-digit number changes only the tens digit — the ones digit stays the same. For example, 34 + 20 = 54 because 3 tens + 2 tens = 5 tens, and the 4 ones are untouched. This mental math skill flows directly from place value understanding and previews column addition.

## How It's Best Learned
Use base-ten blocks: add ten-rods without disturbing the unit cubes. Show on a hundred chart that adding 10 moves one row down while staying in the same column (same ones digit). Connect to skip counting by 10s from a non-round starting number.

## Common Misconceptions
- Changing both digits instead of only the tens digit.
- Adding the 0 in a multiple of ten to the ones digit.
- Not recognizing that only the tens place changes when adding a round ten.

## Questions

```yaml
- question: "What is 46 + 30?"
  type: multiple-choice
  options:
    - "49 — the tens digit stays the same and you add 3 to the ones"
    - "76 — only the tens digit increases by 3"
    - "79 — both digits increase by 3"
    - "166 — you add all the digits together"
  answer: 1
  explanation: "Adding 30 means adding 3 tens. The 4 in 46 is in the tens place, so 4 + 3 = 7 tens. The 6 ones have nothing added to them — 30 has zero ones — so the ones digit stays 6. Answer: 76. Option A shows the misconception of keeping the tens digit and adding 3 to the ones instead. Option C shows the misconception of adding 3 to both digits."

- question: "A student says: '54 + 20 = 74, so 62 + 20 must equal 82.' Is this student's reasoning correct?"
  type: multiple-choice
  options:
    - "No — the rule only works when the ones digit is 4"
    - "No — adding 20 changes both digits, so 62 + 20 = 84"
    - "Yes — when you add 20, only the tens digit increases by 2, regardless of the ones digit"
    - "Yes — but only because 62 ends in 2"
  answer: 2
  explanation: "The student's reasoning is exactly right. When you add a multiple of ten, only the tens digit changes — the ones digit is always untouched. This works for any two-digit number: 62 + 20 = 82 because 6 + 2 = 8 tens and the ones digit stays 2. The rule does not depend on what the ones digit is."

- question: "When you add 30 to 47, the ones digit of the answer is 7."
  type: true-false
  answer: true
  explanation: "True. 30 is 3 tens and 0 ones. Adding it to 47 affects only the tens place: 4 + 3 = 7 tens. The ones digit (7) is unchanged because you are adding zero ones. 47 + 30 = 77."

- question: "To solve 35 + 20, you need to check what happens to both the tens digit and the ones digit before writing the answer."
  type: true-false
  answer: false
  explanation: "False. When adding a multiple of ten, the ones digit never changes — there is nothing to check. Multiples of ten have 0 ones, so they contribute nothing to the ones place. 35 + 20 = 55: the tens digit goes from 3 to 5, and the ones digit stays 5 automatically."

- question: "Why does the ones digit never change when you add a multiple of ten (like 20, 30, or 40) to a two-digit number?"
  type: short-answer
  answer: "Multiples of ten (20, 30, 40…) contain zero ones — their ones digit is always 0. When you add 0 ones to the ones digit of any number, nothing changes. All the addition happens in the tens place."
  explanation: "The key is to think in place value, not raw digits. The 2 in 20 is 2 tens, not a plain 2. It can only be added to the tens place. Since multiples of ten have 0 ones, the ones digit is always left untouched."
```

## Explainer

You've already learned place value — that a two-digit number is made of tens and ones, and that the digits in each place carry independent values. You've also practiced addition within 10. Adding tens to a two-digit number is the first time you use both of those things at once: it's a test of whether you really understand that the tens and ones places work independently.

Here is the key insight: when you add a multiple of ten (like 20, 30, or 40) to a two-digit number, **only the tens digit changes**. The ones digit stays exactly the same. Try it: 34 + 20. The 34 has 3 tens and 4 ones. The 20 has 2 tens and 0 ones. You're adding 3 tens and 2 tens, which gives 5 tens. The 4 ones haven't been touched. So the answer is 54 — same ones digit, new tens digit. This works every time because adding a round ten contributes zero new ones.

The hundred chart makes this visible. Find 34 on the chart. Adding 10 moves you one row down — to 44. Adding 10 again moves you to 54. Notice that you've stayed in the same column the entire time. The column is determined by the ones digit, which never changed. This visual confirms what place value tells you: tens and ones are separate tracks, and adding tens only moves you along the tens track.

The most common mistake is treating both digits as if they interact — thinking 34 + 20 means "3 + 2 = 5 and 4 + 2 = 6, so 56." This confusion disappears if you return to place value: the 2 in 20 is 2 tens, not a plain 2. It can only be added to the tens digit of 34, not to the ones digit. **Think in place value, not in digits.** Whenever you see a number like 20 or 30 in an addition problem, immediately translate it: "that's 2 tens" or "that's 3 tens" — then you'll naturally add it only to the tens column and leave the ones digit untouched.
