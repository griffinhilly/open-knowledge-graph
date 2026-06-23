---
id: place-value-hundreds-2nd
title: 'Place Value: Hundreds, Tens, and Ones'
domain: mathematics
course: 2nd-grade
prerequisites:
- id: place-value-tens-and-ones
  type: hard
- id: place-value-tens-and-ones-2nd-grade
  type: hard
builds-toward:
- comparing-ordering-three-digit-numbers-2nd
- three-digit-addition
- three-digit-subtraction
tags:
- place-value
- hundreds
- three-digit
- base-ten
stage: concrete-operations
status: validated
---

# Place Value: Hundreds, Tens, and Ones

## Core Idea
Three-digit numbers contain a hundreds place, a tens place, and a ones place. The hundreds digit represents groups of one hundred. For example, 245 = 2 hundreds + 4 tens + 5 ones = 200 + 40 + 5.

## Questions

```yaml
- question: "The digit 3 appears in two numbers: 345 and 837. What is the value of the digit 3 in each number?"
  type: multiple-choice
  options:
    - "3 in both — the digit always represents its face value"
    - "300 in 345 and 30 in 837"
    - "30 in 345 and 300 in 837"
    - "3 in 345 and 30 in 837"
  answer: 1
  explanation: "In 345, the digit 3 is in the hundreds place, so its value is 3 × 100 = 300. In 837, the digit 3 is in the tens place, so its value is 3 × 10 = 30. The same digit can represent completely different amounts depending on which position it occupies. This is the core insight of place value: position determines value, not the digit alone."

- question: "What does the zero in 307 tell you?"
  type: multiple-choice
  options:
    - "There are no tens — so 307 = 300 + 7, and the zero holds the tens place empty"
    - "The number is approximately round"
    - "You should skip the tens column when reading this number"
    - "The number could also be written as 37 since the zero contributes nothing"
  answer: 0
  explanation: "Zero as a placeholder is essential — without it, the digits 3 and 7 would slide together and form 37, a completely different number. The zero in 307 holds the tens place, ensuring the 3 stays in the hundreds position (worth 300) and the 7 stays in the ones position (worth 7). Removing it would change the number's value entirely."

- question: "The digit 5 in the number 500 is worth exactly 100 times more than the digit 5 in the number 5."
  type: true-false
  answer: true
  explanation: "In 500, the digit 5 is in the hundreds place: value = 500. In 5, the digit 5 is in the ones place: value = 5. Since 500 ÷ 5 = 100, the hundreds-place digit is indeed worth 100 times more. Each place to the left multiplies a digit's value by 10 — moving two places left multiplies by 100."

- question: "In the number 423, the digit 2 is worth 2."
  type: true-false
  answer: false
  explanation: "The digit 2 in 423 is in the tens place, so its value is 2 × 10 = 20. The face value of a digit (the numeral itself) is not the same as its place value. To find a digit's actual value, you must look at which position it occupies and multiply accordingly."

- question: "Why is the zero in 370 important? What would happen to the number if it weren't there?"
  type: short-answer
  answer: "The zero in 370 holds the ones place empty, keeping the 3 in the hundreds position (worth 300) and the 7 in the tens position (worth 70). Without it, the digits 3 and 7 would form the number 37 — a completely different value. Zeros are not 'nothing'; they are placeholders that preserve the correct position of every other digit."
  explanation: "This question reveals whether students understand that zero's role is structural, not numerical. A student who thinks zeros can be removed without consequence has not grasped place value. The zero in 370 is what separates 370 (three hundred seventy) from 37 (thirty-seven)."
```

## Explainer

You already know that a two-digit number like 37 means 3 tens and 7 ones — that is, 30 + 7. The tens place tells you how many groups of ten you have. Now we add one more place to the left: the **hundreds place**. Just as ten ones make one ten, ten tens make one hundred. The hundreds place tells you how many groups of one hundred you have.

Think of it like bundling. Start with single blocks (ones). Bundle 10 ones together and you get a tens rod. Bundle 10 tens rods together and you get a hundreds flat — a big square made of 100 small blocks. A number like 352 means you have 3 of those hundreds flats, 5 tens rods, and 2 single blocks. In expanded form: 300 + 50 + 2.

The position of each digit is what gives it its value — this is the big idea behind our **base-ten** number system. The digit 3 in 352 is worth 300, not 3. The same digit 3 in 38 is worth 30. The digit's value comes entirely from which place it sits in. This is why the system is so powerful: you only need the digits 0 through 9 to write any number, no matter how large, just by using different places.

A useful way to practice is to read three-digit numbers aloud using place value: "245 is two hundreds, four tens, five ones." Then try working backwards: "3 hundreds, 7 tens, 0 ones" must be 370 — the zero is a placeholder that holds the ones position empty so the 3 and 7 land in the correct places. Place value makes addition, subtraction, and comparison of three-digit numbers systematic, which is where these skills lead next.
