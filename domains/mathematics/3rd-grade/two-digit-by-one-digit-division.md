---
id: two-digit-by-one-digit-division
title: Two-Digit by One-Digit Division
domain: mathematics
course: 3rd-grade
prerequisites:
- id: division-facts-within-100
  type: hard
- id: two-digit-by-one-digit-multiplication
  type: soft
builds-toward:
- long-division-intro
tags:
- division
- two-digit
- algorithms
stage: concrete-operations
status: draft
---

# Two-Digit by One-Digit Division

## Core Idea
Dividing two-digit numbers (e.g., 48 ÷ 3) builds on division facts and understanding of tens and ones. Students might think '4 tens ÷ 3 = 1 ten remainder 1 ten (10 ones), then 10 + 8 = 18 ones ÷ 3 = 6 ones, so 48 ÷ 3 = 16.'

## Explainer

You already know division facts within 100 — if someone says 24 ÷ 6, you can answer 4 immediately. Those single-digit facts are the engine of everything in this topic. Dividing a two-digit number by a one-digit number is not a new operation; it is a structured way of applying the division facts you already know by working one place value at a time.

The key strategy is **place-value decomposition**: break the two-digit number into its tens and ones, divide each part, and handle any leftover. Take 48 ÷ 3. The number 48 is 4 tens and 8 ones. Ask: can I divide 4 tens evenly by 3? 3 goes into 4 once with 1 ten left over. That leftover ten gets converted to 10 ones, added to the existing 8 ones, giving 18 ones total. Now ask: can I divide 18 ones by 3? Yes — 3 goes into 18 exactly 6 times. Combine: 1 ten and 6 ones = 16. So 48 ÷ 3 = 16.

The relationship between division and multiplication is your primary checking tool. Since 3 × 16 = 48, you know the answer is correct. Multiplication is the "reverse gear" of division — every division problem has a corresponding multiplication equation. When you are not sure if your answer is right, multiply back and see if you recover the original number. This inverse relationship also helps you set up the problem: if 48 ÷ 3 = ?, you are asking "3 times what equals 48?" Your multiplication facts guide you toward the answer.

This two-digit division strategy is the conceptual foundation for **long division**, which you will encounter next. Long division is essentially this same place-value process written out in a formal column format, extended to handle three-digit and larger numbers. The algorithm may look complicated, but every step in it — how many times does the divisor go into the leading digits? what's the remainder? bring down the next digit — is just one iteration of the thinking you are doing now. Building this mental model with two-digit numbers makes the long division algorithm legible rather than mysterious.
