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

## Explainer

You already know two things that unlock decimal multiplication: multi-digit whole-number multiplication and decimal place value. The strategy is to use the whole-number algorithm you know — and then figure out where the decimal point belongs in the answer using place value reasoning.

Here's the key idea: every decimal can be converted into a whole number by multiplying by a power of ten. The decimal 2.4 is just 24 ÷ 10. The decimal 1.3 is just 13 ÷ 10. So 2.4 × 1.3 is the same as (24 ÷ 10) × (13 ÷ 10) = (24 × 13) ÷ 100. You can compute 24 × 13 = 312 using your standard algorithm, then divide by 100 to get 3.12. Dividing by 100 moves the decimal point two places to the left — which is exactly the same as counting two total decimal places in the original factors (one in 2.4, one in 1.3).

This is the **decimal place rule**: count the total number of digits to the right of the decimal point in all the factors, and place the decimal point that many places from the right in the product. 2.4 × 1.3: one decimal place + one decimal place = two decimal places in the answer, so 312 becomes 3.12. For 0.6 × 0.04: one place + two places = three decimal places, so 6 × 4 = 24 becomes 0.024. The rule isn't magic — it's a shortcut for the "multiply by powers of ten, then divide back" reasoning above.

Always **estimate first**. Before you even start the multiplication, round each factor to the nearest whole number and multiply: 2.4 × 1.3 ≈ 2 × 1 = 2, so the answer should be close to 2. When you get 3.12, it passes the check. If you accidentally placed the decimal point to get 31.2, estimation immediately reveals the error — 31.2 is nowhere near 2. This habit catches the most common mistake (off-by-a-factor-of-10 decimal placement) before it costs you points. Estimation is not a backup plan; it is the first step.
