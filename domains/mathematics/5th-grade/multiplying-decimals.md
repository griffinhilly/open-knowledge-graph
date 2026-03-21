---
id: multiplying-decimals
title: Multiplying Decimals
domain: mathematics
course: 5th-grade
prerequisites:
- id: multi-digit-multiplication
  type: hard
- id: decimal-place-value
  type: hard
- id: powers-of-ten
  type: soft
- id: adding-subtracting-decimals
  type: soft
- id: multiplying-dividing-by-powers-of-ten
  type: soft
builds-toward:
- dividing-decimals
tags:
- decimals
- multiplication
- arithmetic
stage: concrete-operations
status: validated
---
# Multiplying Decimals

## Core Idea
Multiplying decimals follows the whole-number multiplication algorithm, with a rule for placing the decimal point in the product: the number of decimal places in the product equals the total number of decimal places in both factors. 2.4 x 1.3 = 3.12 (one decimal place + one decimal place = two decimal places in the product). This rule works because 2.4 x 1.3 is equivalent to (24 x 13) / 100 -- each factor was multiplied by 10 to remove the decimal, so the product must be divided by 10 x 10 = 100. Understanding this connection to place value and powers of ten prevents the rule from being arbitrary.

## How It's Best Learned
Start with estimation: 2.4 x 1.3 should be close to 2 x 1 = 2 (and indeed 3.12 is close). Use area models with decimal side lengths. Show the connection explicitly: multiply as whole numbers, then adjust by counting decimal places. Practice with factors that have different numbers of decimal places. Always estimate first to check that the decimal point placement makes sense.

## Common Misconceptions
- Aligning decimal points as in addition (this is wrong for multiplication).
- Miscounting decimal places in the product.
- Not estimating, so failing to catch gross errors (e.g., placing the decimal point to get 31.2 instead of 3.12).

## Questions

```yaml
- question: "A student calculates 0.6 × 0.04 by multiplying 6 × 4 = 24 and then writing 0.24 as the answer. Is this correct?"
  type: multiple-choice
  options:
    - "Yes — multiply the digits and keep the decimal between the two digits"
    - "No — the decimal point should be aligned with the factors, just like in addition"
    - "No — there are three total decimal places in the factors (1 + 2), so the answer should be 0.024"
    - "Yes — when both factors are less than 1, the product is always between them"
  answer: 2
  explanation: "0.6 has 1 decimal place and 0.04 has 2 decimal places — a total of 3. So the product of the digits (24) must have 3 decimal places: 0.024. The answer 0.24 only has 2 decimal places, which means the student miscounted. A quick estimate confirms: 0.6 × 0.04 ≈ 0.6 × 0 = near-zero, and 0.024 is much closer to zero than 0.24."

- question: "Why does the total number of decimal places in the factors equal the number of decimal places in the product?"
  type: multiple-choice
  options:
    - "It is a rule that must be memorized — there is no underlying reason"
    - "Because each decimal factor is a whole number divided by a power of 10, so the product must be divided by the product of those same powers of 10"
    - "Because decimal points always shift right during multiplication"
    - "Because the denominators of fractions are always added together when multiplying"
  answer: 1
  explanation: "2.4 = 24 ÷ 10 and 1.3 = 13 ÷ 10, so 2.4 × 1.3 = (24 × 13) ÷ (10 × 10) = 312 ÷ 100 = 3.12. Dividing by 100 means moving the decimal point two places left — which is exactly the same as counting two total decimal places. The rule isn't arbitrary; it's a shorthand for this powers-of-ten reasoning. Understanding the 'why' lets you handle unusual cases like 0.003 × 0.002 confidently."

- question: "When multiplying decimals, you should align the decimal points, just as you do when adding or subtracting decimals."
  type: true-false
  answer: false
  explanation: "Aligning decimal points is the rule for addition and subtraction, not multiplication. When multiplying, you ignore the decimal points entirely, multiply the digits as whole numbers, then count the total decimal places in the factors and place the decimal point that many positions from the right in the product. Applying the addition rule to multiplication is one of the most common errors students make."

- question: "For 2.4 × 1.3, the correct product has two decimal places because each factor has one decimal place."
  type: true-false
  answer: true
  explanation: "One decimal place (in 2.4) plus one decimal place (in 1.3) equals two decimal places in the product. So 24 × 13 = 312 becomes 3.12. You can verify with estimation: 2.4 × 1.3 ≈ 2 × 1 = 2, and 3.12 is close to 2, confirming the decimal placement. If you'd placed it as 31.2 or 0.312, estimation would immediately flag the error."

- question: "Explain why 0.6 × 0.04 = 0.024 using the logic of powers of ten, rather than just applying the decimal-place counting rule."
  type: short-answer
  answer: "0.6 is the same as 6 ÷ 10, and 0.04 is the same as 4 ÷ 100. So 0.6 × 0.04 = (6 ÷ 10) × (4 ÷ 100) = (6 × 4) ÷ (10 × 100) = 24 ÷ 1000 = 0.024. Dividing by 1000 moves the decimal point three places to the left, which is equivalent to counting three total decimal places in the original factors (1 from 0.6, plus 2 from 0.04). The counting rule is just a shortcut for this reasoning."
  explanation: "Students who only memorize 'count the decimal places' are helpless when they miscount. Students who understand the powers-of-ten reasoning can reconstruct the rule from scratch — and can estimate to verify: 0.6 × 0.04 is roughly 0.6 × 0 = near zero, so an answer in the thousandths range (0.024) makes sense, while 0.24 or 24 clearly do not."
```

## Explainer

You already know two things that unlock decimal multiplication: multi-digit whole-number multiplication and decimal place value. The strategy is to use the whole-number algorithm you know — and then figure out where the decimal point belongs in the answer using place value reasoning.

Here's the key idea: every decimal can be converted into a whole number by multiplying by a power of ten. The decimal 2.4 is just 24 ÷ 10. The decimal 1.3 is just 13 ÷ 10. So 2.4 × 1.3 is the same as (24 ÷ 10) × (13 ÷ 10) = (24 × 13) ÷ 100. You can compute 24 × 13 = 312 using your standard algorithm, then divide by 100 to get 3.12. Dividing by 100 moves the decimal point two places to the left — which is exactly the same as counting two total decimal places in the original factors (one in 2.4, one in 1.3).

This is the **decimal place rule**: count the total number of digits to the right of the decimal point in all the factors, and place the decimal point that many places from the right in the product. 2.4 × 1.3: one decimal place + one decimal place = two decimal places in the answer, so 312 becomes 3.12. For 0.6 × 0.04: one place + two places = three decimal places, so 6 × 4 = 24 becomes 0.024. The rule isn't magic — it's a shortcut for the "multiply by powers of ten, then divide back" reasoning above.

Always **estimate first**. Before you even start the multiplication, round each factor to the nearest whole number and multiply: 2.4 × 1.3 ≈ 2 × 1 = 2, so the answer should be close to 2. When you get 3.12, it passes the check. If you accidentally placed the decimal point to get 31.2, estimation immediately reveals the error — 31.2 is nowhere near 2. This habit catches the most common mistake (off-by-a-factor-of-10 decimal placement) before it costs you points. Estimation is not a backup plan; it is the first step.
