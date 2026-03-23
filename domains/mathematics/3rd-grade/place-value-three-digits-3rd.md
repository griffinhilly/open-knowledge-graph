---
id: place-value-three-digits-3rd
title: Three-Digit Place Value
domain: mathematics
course: 3rd-grade
prerequisites:
- id: place-value-tens-and-ones
  type: hard
builds-toward:
- multi-digit-addition-subtraction-3rd
- rounding-whole-numbers
tags:
- place-value
- hundreds
- expanded-form
stage: concrete-operations
status: validated
---

# Three-Digit Place Value

## Core Idea
Three-digit numbers have hundreds, tens, and ones places. 347 = 3 hundreds + 4 tens + 7 ones = 300 + 40 + 7. Understanding place value is essential for operations and rounding.

## How It's Best Learned
Use base-ten blocks (flats, rods, units). Write numbers in expanded form.

## Common Misconceptions
Confusing digit with place value; not understanding regrouping; misplacing values.

## Questions

```yaml
- question: "In the number 347, what is the value of the digit 3?"
  type: multiple-choice
  options:
    - "3 — that is the digit itself"
    - "30 — it is the second-largest digit in the number"
    - "300 — it is in the hundreds place"
    - "3,000 — there are three digits following it"
  answer: 2
  explanation: "The digit 3 is in the hundreds place, so its value is 3 × 100 = 300. This is the core idea of a positional number system: the same digit has a different value depending on its position. The digit 3 in 347 contributes 300 to the total, not 3."

- question: "Which correctly represents 305 in expanded form?"
  type: multiple-choice
  options:
    - "30 + 5"
    - "300 + 50 + 5"
    - "300 + 5"
    - "3 + 0 + 5"
  answer: 2
  explanation: "305 = 3 hundreds + 0 tens + 5 ones = 300 + 0 + 5 = 300 + 5. Option A (30 + 5 = 35) places the 3 in the tens position instead of hundreds. Option B (300 + 50 + 5 = 355) incorrectly assigns 50 to the tens place when there is a 0 there. Option D treats each digit as its face value instead of its positional value."

- question: "The 0 in 507 is a placeholder that prevents the number from being misread as 57."
  type: true-false
  answer: true
  explanation: "True. The 0 in 507 holds the tens place open, keeping the 5 in the hundreds place and the 7 in the ones place. Without it, the number would collapse to 57 — five tens and seven ones — which is entirely different. Zero as a placeholder is essential to a positional number system."

- question: "In the number 263, the digit 2 has a smaller value than the digit 6."
  type: true-false
  answer: false
  explanation: "False. The digit 2 is in the hundreds place, giving it a value of 200. The digit 6 is in the tens place, giving it a value of 60. 200 > 60, so the digit 2 represents a larger portion of the number than the digit 6, even though 6 > 2 as raw face values. Position determines value."

- question: "What does it mean to say our number system is 'positional'? Use the number 444 to illustrate your answer."
  type: short-answer
  answer: "In a positional system, a digit's value depends on where it appears, not just what digit it is. In 444, every digit is 4, but the leftmost 4 is worth 400 (hundreds place), the middle 4 is worth 40 (tens place), and the rightmost 4 is worth 4 (ones place). The same digit has three different values because of its position."
  explanation: "444 = 400 + 40 + 4, all from the same digit in three different positions. This is why we call it a 'place value' system — the digit is just a symbol, and its position multiplies it by 1, 10, 100, and so on."
```

## Explainer

You already understand that two-digit numbers are made of tens and ones. The number 47 means 4 tens and 7 ones — not 47 separate objects, but a bundled structure. Three-digit numbers extend that same idea by adding one more level: **hundreds**. Just as 10 ones bundle into 1 ten, 10 tens bundle into 1 hundred. The system keeps going by the same rule at every level.

So the number 347 isn't just "three-four-seven." It means: 3 groups of one hundred, 4 groups of ten, and 7 ones. **Expanded form** makes this visible: 347 = 300 + 40 + 7. That's a powerful notation because it shows the value each digit actually contributes. The digit 3 in 347 is worth 300 — not 3. Its position (the hundreds place) is what gives it that value. This is the essential idea of a **positional number system**: the same digit has different values depending on where it sits.

With base-ten blocks, a hundreds flat is a square of 100 small cubes. To show 347, you'd lay out 3 flats, 4 rods, and 7 unit cubes. Notice that 3 flats + 4 rods + 7 units is the same total as 347 loose unit cubes — just organized. This bundling is what makes arithmetic manageable; operating on 3 organized groups of 100 is much easier than counting 300 individual cubes.

Understanding three-digit place value also means recognizing zeros as placeholders. The number 305 has a 0 in the tens place — meaning there are 0 tens, just 3 hundreds and 5 ones. Without that zero, 305 would collapse to 35, an entirely different number. The zero's job is to hold the position so the 3 stays in the hundreds place and the 5 stays in the ones place. This will become critical when you start adding and subtracting multi-digit numbers, where regrouping moves value between these exact positions.
