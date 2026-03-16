---
id: dividing-decimals
title: Dividing Decimals
domain: mathematics
course: 5th-grade
prerequisites:
- id: intro-to-long-division
  type: hard
- id: multiplying-decimals
  type: soft
- id: decimal-place-value
  type: hard
- id: multiplying-dividing-by-powers-of-ten
  type: soft
builds-toward: []
tags:
- decimals
- division
- arithmetic
stage: concrete-operations
status: validated
---
# Dividing Decimals

## Core Idea
Dividing decimals involves two main cases: dividing a decimal by a whole number (straightforward -- just divide and bring the decimal point straight up into the quotient) and dividing by a decimal (multiply both dividend and divisor by a power of 10 to make the divisor a whole number, then divide). For example, 7.2 / 0.3 becomes 72 / 3 = 24. This "clearing the decimal" works because multiplying numerator and denominator by the same number does not change the value of a division (it is equivalent to multiplying by 1). Estimating before dividing is critical for verifying decimal point placement.

## How It's Best Learned
Start with division by whole numbers: 8.4 / 4 = 2.1. Use money contexts: $8.40 shared among 4 people. Then introduce division by decimals by showing the equivalence: 7.2 / 0.3 has the same answer as 72 / 3. Use estimation as a check: 7.2 / 0.3 should be around 7 / 0.3, which is roughly 20-something. Practice both cases extensively.

## Common Misconceptions
- Ignoring the decimal point entirely and dividing as whole numbers without adjusting.
- Moving the decimal point in the dividend but not the divisor (or vice versa).
- Getting confused about which direction the decimal point moves when multiplying by powers of 10.

## Explainer

Dividing decimals has two distinct cases, and the key to success is recognizing which one you are looking at. **Case 1**: the divisor (the number you are dividing by) is a whole number. **Case 2**: the divisor is itself a decimal. You already know long division with whole numbers, you understand decimal place value, and you know how multiplying by powers of ten shifts digits — this topic connects all three of those skills.

In Case 1, dividing a decimal by a whole number, the procedure mirrors long division exactly: you simply bring the decimal point straight up into your quotient at the same position. For example, 8.4 ÷ 4: divide as you would for 84 ÷ 4 = 21, then place the decimal point directly above where it sits in the dividend — giving 2.1. A quick mental check: 8.4 ÷ 4 should be close to 2, since 8 ÷ 4 = 2. Money makes this intuitive — $8.40 shared equally among 4 people gives each person $2.10.

Case 2 requires a preliminary transformation. Dividing by a decimal feels awkward because your long division algorithm expects a whole-number divisor. The fix comes from your work on multiplying and dividing by powers of ten: you can multiply both the dividend and divisor by the same power of ten without changing the result, because division is a fraction and multiplying numerator and denominator by the same number leaves the fraction's value unchanged. For 7.2 ÷ 0.3, multiply both by 10: you get 72 ÷ 3 = 24. The divisor's decimal places tell you exactly which power of ten to use — one decimal place means multiply by 10, two decimal places means multiply by 100, and so on.

**Estimation** is your most powerful error-checking tool. Before calculating, make a rough estimate. For 7.2 ÷ 0.3, think: 7 ÷ 0.3 ≈ 7 ÷ (1/3) = 21 — so the answer should be in the low twenties. If your calculation produced 2.4 or 240, the estimate immediately signals a decimal placement error. The most dangerous mistake in decimal division is placing the decimal point in the wrong position in the answer, and a quick estimate catches this before you commit to a wrong answer. Always estimate first, calculate second, then compare.
