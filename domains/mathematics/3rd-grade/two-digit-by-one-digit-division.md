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

## Questions

```yaml
- question: "To solve 52 ÷ 4 using place-value thinking, what are the correct steps?"
  type: multiple-choice
  options:
    - "Subtract 4 from 52 repeatedly and count how many subtractions it takes"
    - "Divide 5 tens by 4: get 1 ten with 1 ten (10 ones) leftover; add to 2 ones = 12 ones; divide 12 ones by 4 = 3; answer is 13"
    - "Multiply 52 × 4, then divide the product by 2 to get the answer"
    - "Split 52 into 50 and 2, divide each by 4 independently and add the results"
  answer: 1
  explanation: "Place-value decomposition: 52 = 5 tens and 2 ones. Ask: how many times does 4 go into 5 tens? Once (4 tens), with 1 ten leftover. Convert the leftover ten to 10 ones and combine with the existing 2 ones: 12 ones. Now ask: how many times does 4 go into 12 ones? Three times exactly. Result: 1 ten + 3 ones = 13. Option D fails because 50 ÷ 4 = 12.5 (not a whole number), so you cannot divide the tens independently without handling the remainder — the leftover must be passed down to the ones place."

- question: "After dividing the tens digit in 48 ÷ 3, there is 1 ten left over. What do you do with that leftover ten?"
  type: multiple-choice
  options:
    - "Ignore it — remainders in the tens place are too small to affect the answer"
    - "Write it as a decimal remainder in the final answer"
    - "Convert it to 10 ones and add it to the existing ones before dividing again"
    - "Subtract it from the original number and start the division over"
  answer: 2
  explanation: "The leftover ten cannot stay as a ten — you are now working in the ones place. So you convert it: 1 ten = 10 ones. Add those 10 ones to the existing ones digit (8) to get 18 ones total, then divide: 18 ÷ 3 = 6. This 'bring down' move is the core of the place-value decomposition strategy, and it is exactly what the long division algorithm formalizes. Ignoring the remainder would produce a wrong answer (1 ten = 10 is a significant part of 48)."

- question: "After dividing 48 ÷ 3 = 16, you can verify your answer by computing 3 × 16 = 48."
  type: true-false
  answer: true
  explanation: "Multiplication is the inverse of division, so multiplying the quotient by the divisor should return the dividend. 3 × 16 = 48 confirms that 48 ÷ 3 = 16 is correct. This check is always available and takes only a few seconds. It also reinforces the conceptual relationship: division and multiplication are reverse operations — every division problem has a corresponding multiplication equation."

- question: "If the tens digit of a two-digit number cannot be divided evenly by the divisor, there is no valid answer and the problem cannot be completed."
  type: true-false
  answer: false
  explanation: "An uneven division of the tens digit is normal and expected — it simply produces a remainder that gets converted to ones and added to the existing ones digit before dividing again. For example, in 52 ÷ 4, the tens (5) don't divide evenly by 4: 4 goes into 5 once with 1 leftover. That leftover ten becomes 10 ones, combined with 2 to make 12 ones, which divides evenly by 4 to give 3. The answer is 13. The 'no valid answer' misconception comes from applying whole-number thinking at each step independently, rather than carrying the remainder forward."

- question: "Explain in your own words how place-value decomposition helps you divide 63 ÷ 3. Show the steps."
  type: short-answer
  answer: "63 = 6 tens and 3 ones. Divide the tens: 6 tens ÷ 3 = 2 tens exactly, no remainder. Divide the ones: 3 ones ÷ 3 = 1 one exactly. Combine: 2 tens + 1 one = 21. Check: 3 × 21 = 63. Answer: 21."
  explanation: "When the tens divide evenly (as in this example), place-value decomposition is especially clean. The key insight is that dividing each place value separately and combining the results is equivalent to dividing the whole number — because of how our base-10 number system works. When there is a remainder in the tens, you carry it forward; when there is not, you simply move on. This strategy is the conceptual foundation of the long division algorithm."
```

## Explainer

You already know division facts within 100 — if someone says 24 ÷ 6, you can answer 4 immediately. Those single-digit facts are the engine of everything in this topic. Dividing a two-digit number by a one-digit number is not a new operation; it is a structured way of applying the division facts you already know by working one place value at a time.

The key strategy is **place-value decomposition**: break the two-digit number into its tens and ones, divide each part, and handle any leftover. Take 48 ÷ 3. The number 48 is 4 tens and 8 ones. Ask: can I divide 4 tens evenly by 3? 3 goes into 4 once with 1 ten left over. That leftover ten gets converted to 10 ones, added to the existing 8 ones, giving 18 ones total. Now ask: can I divide 18 ones by 3? Yes — 3 goes into 18 exactly 6 times. Combine: 1 ten and 6 ones = 16. So 48 ÷ 3 = 16.

The relationship between division and multiplication is your primary checking tool. Since 3 × 16 = 48, you know the answer is correct. Multiplication is the "reverse gear" of division — every division problem has a corresponding multiplication equation. When you are not sure if your answer is right, multiply back and see if you recover the original number. This inverse relationship also helps you set up the problem: if 48 ÷ 3 = ?, you are asking "3 times what equals 48?" Your multiplication facts guide you toward the answer.

This two-digit division strategy is the conceptual foundation for **long division**, which you will encounter next. Long division is essentially this same place-value process written out in a formal column format, extended to handle three-digit and larger numbers. The algorithm may look complicated, but every step in it — how many times does the divisor go into the leading digits? what's the remainder? bring down the next digit — is just one iteration of the thinking you are doing now. Building this mental model with two-digit numbers makes the long division algorithm legible rather than mysterious.
