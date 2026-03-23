---
id: three-digit-number-decomposition
title: Decomposing Three-Digit Numbers by Place Value
domain: mathematics
course: 2nd-grade
prerequisites:
- id: place-value-hundreds
  type: hard
- id: place-value-whole-numbers
  type: hard
builds-toward:
- place-value-understanding-4th
tags:
- place-value
- decomposition
stage: concrete-operations
status: validated
---

# Decomposing Three-Digit Numbers by Place Value

## Core Idea
A three-digit number like 247 can be decomposed as 2 hundreds + 4 tens + 7 ones, or 200 + 40 + 7. Understanding this decomposition is essential for addition, subtraction, and developing number sense about magnitude.

## How It's Best Learned
Use base-ten blocks (flats for hundreds, rods for tens, units for ones) to represent numbers. Write the expanded form (200 + 40 + 7) alongside the standard form (247). Trade blocks to show equivalent representations.

## Common Misconceptions
- Confusing the digit's face value with its place value (the 2 in 247 represents 200, not 2).
- Not understanding that different decompositions of the same number have the same value.
- Difficulty recognizing the relationship between base-ten block representations and written numbers.

## Questions

```yaml
- question: "A student looks at the number 352 and says 'the 3 is worth 3.' Is the student correct?"
  type: multiple-choice
  options:
    - "Yes — a digit always has the value shown, regardless of its position"
    - "No — the 3 is in the hundreds place, so it represents 3 × 100 = 300"
    - "Yes — place value only changes the value of 0, which becomes a placeholder"
    - "No — in a three-digit number, every digit is worth ten times its face value"
  answer: 1
  explanation: "A digit's value depends entirely on its position (place), not just its face. The 3 in 352 sits in the hundreds place, making it worth 300. This is the core concept of place value. Option D is partially right in spirit (each place is 10× the one to its right) but too broad — the ones digit is always worth its face value."

- question: "Which of the following correctly shows the expanded form of 405?"
  type: multiple-choice
  options:
    - "4 + 0 + 5"
    - "40 + 5"
    - "400 + 0 + 5"
    - "400 + 50"
  answer: 2
  explanation: "405 decomposes as 4 hundreds + 0 tens + 5 ones = 400 + 0 + 5. Option A shows face values, not place values (4 ≠ 400). Option B omits the hundreds place entirely. Option D incorrectly assigns 50 to the tens place when there are actually 0 tens. The zero is crucial — it holds the 4 in the hundreds place and the 5 in the ones place."

- question: "The number 305 and the number 35 represent the same value because both contain the digits 3 and 5."
  type: true-false
  answer: false
  explanation: "305 = 300 + 0 + 5; 35 = 30 + 5. These are completely different numbers. The zero in 305 is a placeholder that places the digit 3 in the hundreds position. Remove the zero and the 3 drops from the hundreds place to the tens place, changing the number entirely. Same digits, different positions, different values."

- question: "247 and 200 + 40 + 7 are two different ways of writing exactly the same number."
  type: true-false
  answer: true
  explanation: "Standard form (247) and expanded form (200 + 40 + 7) represent identical values — they are just different notations. Expanded form reveals the place-value structure; standard form is compact. Converting between them doesn't change the number, only how it is written."

- question: "Why does the digit 0 in a three-digit number matter, even though it contributes zero value?"
  type: short-answer
  answer: "Zero acts as a placeholder — it signals that there are no units of that denomination, but it also holds all other digits in their correct positions. In 305, the zero keeps the 3 in the hundreds place and the 5 in the ones place. Without the zero, you would have 35 — a completely different number. Zero's job is to preserve the positional meaning of surrounding digits, not to add value."
  explanation: "This is the trickiest case in three-digit decomposition. Students who understand non-zero digits sometimes still write 305 as '35' or '3 + 5 = 8' because zero 'doesn't count.' But the zero is doing critical work: it is the reason 305 is three hundred five and not thirty-five."
```

## Explainer

You already know that our number system is built on place value — that a digit's position tells you what it's worth. You've seen this with two-digit numbers: the 3 in 35 means 30, not 3. **Three-digit number decomposition** extends that same idea one more place to the left, adding hundreds.

Take the number 247. The digit 2 sits in the hundreds place, so it represents 2 × 100 = 200. The 4 sits in the tens place, so it represents 4 × 10 = 40. The 7 sits in the ones place, so it represents 7 × 1 = 7. Put it all together and you get the **expanded form**: 200 + 40 + 7. The standard form (247) and the expanded form are just two ways of writing the same number — like saying "two hundred forty-seven" out loud. The value doesn't change, only the notation.

This matters enormously when you add or subtract large numbers. When you add 247 + 135, you're really adding the hundreds together (200 + 100), the tens together (40 + 30), and the ones together (7 + 5). Decomposition is the hidden engine inside the column-addition algorithm you've learned. Understanding it means you're not just following steps — you know *why* the steps work.

Watch out for zeros, which are the trickiest case. The number 305 decomposes as 300 + 0 + 5, or just 300 + 5. The zero in the tens place is a placeholder — it tells you there are no tens — but it's still worth zero, not nothing. Writing the zero is what keeps the 3 in the hundreds position and the 5 in the ones position. If you forgot it and wrote 35, you'd have a completely different number.
