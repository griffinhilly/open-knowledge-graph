---
id: powers-of-ten
title: Powers of Ten
domain: mathematics
course: 5th-grade
prerequisites:
  - id: decimal-place-value
    type: hard
  - id: multiples-of-ten
    type: hard
builds-toward:
  - multiplying-dividing-by-powers-of-ten
  - multiplying-decimals
tags: [exponents, place-value, number-sense]
stage: concrete-operations
status: validated
---

# Powers of Ten

## Core Idea
Powers of ten express repeated multiplication by 10 in compact form: 10^1 = 10, 10^2 = 100, 10^3 = 1,000, and so on. The exponent tells how many times 10 is multiplied by itself, which also equals the number of zeros in the result. This notation connects to place value: each place in our number system is a power of ten. Understanding powers of ten is the gateway to scientific notation, exponent rules, and a deeper understanding of why our number system works the way it does.

## How It's Best Learned
Build a powers-of-ten table and have students discover the pattern (each row is 10 times the previous). Connect to place value: the thousands place is 10^3, the hundreds place is 10^2, etc. Extend to negative exponents conceptually (10^0 = 1, and the pattern suggests 10^-1 = 0.1, though formal treatment comes later). Practice expressing large numbers using powers of ten.

## Common Misconceptions
- Confusing 10^3 with 10 x 3 = 30 (multiplying by the exponent instead of using it as a repeat count).
- Not recognizing that 10^1 = 10 and 10^0 = 1.
- Thinking the exponent counts the zeros when the base is not 10.

## Questions

```yaml
- question: "A student says '10 to the power of 4 equals 40, because 10 times 4 is 40.' What is the correct value of 10^4?"
  type: multiple-choice
  options:
    - "40 — multiply 10 by the exponent"
    - "14 — add 10 and 4"
    - "10,000 — multiply 10 by itself 4 times: 10 × 10 × 10 × 10"
    - "1,000 — the exponent 4 means shift 3 places"
  answer: 2
  explanation: "The exponent tells how many times 10 appears as a factor. 10^4 = 10 × 10 × 10 × 10 = 10,000. The most common misconception (option A) multiplies 10 by the exponent instead of using it as a repeat count. 10^4 has four zeros, giving 10,000 — not 40."

- question: "What power of 10 corresponds to the thousands place in our place value system?"
  type: multiple-choice
  options:
    - "10^1, because 1,000 has one comma"
    - "10^4, because 1,000 has four digits"
    - "10^3, because 1,000 = 10 × 10 × 10"
    - "10^10, because it's the tens place times one hundred"
  answer: 2
  explanation: "1,000 = 10 × 10 × 10 = 10^3. The exponent 3 equals the number of zeros in 1,000. In place value: ones = 10^0 = 1, tens = 10^1 = 10, hundreds = 10^2 = 100, thousands = 10^3 = 1,000. Each step left adds one to the exponent."

- question: "10^2 = 20, because 10 times 2 equals 20."
  type: true-false
  answer: false
  explanation: "This is the most common error with powers of ten. 10^2 means 10 × 10 = 100, not 10 × 2 = 20. The exponent tells how many times 10 is used as a factor, not how many times 10 is multiplied by the exponent. 10^2 = 100, which has exactly 2 zeros."

- question: "The number of zeros in a power of ten equals the exponent."
  type: true-false
  answer: true
  explanation: "10^1 = 10 (one zero), 10^2 = 100 (two zeros), 10^3 = 1,000 (three zeros), 10^4 = 10,000 (four zeros). This pattern holds because each multiplication by 10 appends one zero. It is a useful shortcut — but only because the base is 10. Don't apply this rule to powers of other bases."

- question: "Why does the exponent in a power of ten equal the number of zeros in the result? Explain using 10^3 as an example."
  type: short-answer
  answer: "Each time you multiply by 10, you append one zero to the result. 10^3 = 10 × 10 × 10: start with 10 (one zero), multiply by 10 to get 100 (two zeros), multiply by 10 again to get 1,000 (three zeros). The exponent counts how many times you multiplied by 10, which is exactly how many zeros accumulated."
  explanation: "Students who only memorize 'count the zeros' can apply it mechanically but break down when asked why, or when the base changes. Understanding why the zeros accumulate builds the foundation for place-value shifts when multiplying or dividing by powers of ten — the next skill in the sequence."
```

## Explainer

You already understand decimal place value — that each place is worth ten times more than the place to its right — and you know your multiples of ten (10, 20, 30..., 100, 200...). **Powers of ten** give you a compact way to write numbers like 1,000 or 1,000,000 and to express why our number system works the way it does.

The notation 10^3 means "10 multiplied by itself 3 times": 10 × 10 × 10 = 1,000. The small raised number is called the **exponent**, and it tells you how many times 10 appears as a factor. So 10^1 = 10, 10^2 = 100, 10^3 = 1,000, 10^4 = 10,000. Notice the pattern: the exponent also equals the number of zeros in the result. 10^3 has three zeros. 10^6 has six zeros. This shortcut works specifically because the base is 10 — don't try it with other bases.

Now connect this to place value, which you already know. The ones place is 10^0 = 1. The tens place is 10^1 = 10. The hundreds place is 10^2 = 100. The thousands place is 10^3 = 1,000. Every time you move one place to the left, you multiply by 10 — which is exactly what adding 1 to the exponent does. Our entire number system is built on powers of ten stacked side by side. The digit 5 in 5,000 means 5 × 10^3; in 500 it means 5 × 10^2; in 50 it means 5 × 10^1.

This matters practically because multiplying or dividing by a power of ten is just a matter of shifting digits left or right across the place-value positions. Multiplying 47 by 10^2 (= 100) gives 4,700 — the digits didn't change, but each one moved two places to the left. Understanding this prepares you for scientific notation (expressing very large or very small numbers compactly) and for multiplying and dividing decimals, where the same shifting logic applies in both directions.
