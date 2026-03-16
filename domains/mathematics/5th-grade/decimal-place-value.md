---
id: decimal-place-value
title: Decimal Place Value
domain: mathematics
course: 5th-grade
prerequisites:
- id: intro-to-decimals
  type: hard
- id: place-value-whole-numbers
  type: hard
- id: relating-fractions-and-decimals
  type: soft
builds-toward:
- reading-writing-decimals
- comparing-decimals
- rounding-decimals
tags:
- decimals
- place-value
- number-sense
stage: concrete-operations
status: validated
---
# Decimal Place Value

## Core Idea
Decimal place value extends the base-ten system rightward past the ones place: tenths (1/10), hundredths (1/100), thousandths (1/1,000). Each place is one-tenth the value of the place to its left, maintaining the same times-ten/divided-by-ten pattern that governs whole numbers. In 4.739, the 7 represents 7 tenths (0.7), the 3 represents 3 hundredths (0.03), and the 9 represents 9 thousandths (0.009). Mastering decimal place value is essential for all decimal operations, as every algorithm (adding, multiplying, etc.) depends on aligning or tracking place values correctly.

## How It's Best Learned
Use place-value charts that extend both left and right of the decimal point to show symmetry around the ones place. Base-ten blocks can be repurposed: let the large cube be 1, the flat be 0.1, the rod be 0.01, the small cube be 0.001. Practice decomposing decimals in expanded form (4.739 = 4 + 0.7 + 0.03 + 0.009). Read decimals using place-value language ("four and seven hundred thirty-nine thousandths").

## Common Misconceptions
- Thinking there is a "oneths" place (by analogy with tens/tenths, hundreds/hundredths).
- Treating digits after the decimal point as a separate whole number (reading 3.27 as "three point twenty-seven" and thinking 3.27 > 3.5 because 27 > 5).
- Not understanding that 0.30 and 0.3 are equal.

## Questions

```yaml
- question: "Which of the following numbers is the greatest?"
  type: multiple-choice
  options: ["0.09", "0.100", "0.75", "0.8"]
  answer: 3
  explanation: "Compare tenths digits first: 0.8 has 8 tenths, 0.75 has 7 tenths, 0.100 has 1 tenth, 0.09 has 0 tenths. So 0.8 > 0.75 > 0.100 > 0.09. A common misconception is that 0.100 is largest because it has the most digits — but digits after the decimal must be compared position by position, not as whole numbers."

- question: "0.30 is greater than 0.3 because 30 is greater than 3."
  type: true-false
  answer: false
  explanation: "0.30 and 0.3 are exactly equal — both represent 3 tenths. The trailing zero after the 3 adds no value; it just shows the hundredths place is empty. As fractions: 0.30 = 30/100 = 3/10 = 0.3. Treating the digits after the decimal as a whole number (comparing 30 and 3) is a classic misconception that ignores place value."

- question: "In the number 4.739, what is the value (not just the digit) of the 3?"
  type: short-answer
  answer: "3 hundredths, or 0.03"
  explanation: "The 3 is in the hundredths position — the second digit to the right of the decimal point. Its value is 3 × (1/100) = 3/100 = 0.03. Knowing the digit (3) is not enough; you must know the position to know the value."
```

## Explainer

You already know that in whole numbers, each position to the left is worth ten times more. Decimal place value simply continues that pattern in the other direction: each position to the right of the decimal point is worth ten times less than the one before it. The ones place is worth 1. One step right gives you tenths (1/10). One more step gives hundredths (1/100). Then thousandths (1/1,000). The pattern is perfectly symmetric — multiply by 10 going left, divide by 10 going right.

A useful way to see this: a place-value chart with the decimal point in the middle shows thousands | hundreds | tens | ones | **·** | tenths | hundredths | thousandths. Every column is linked to its neighbors by the same ×10 / ÷10 relationship. The decimal point itself is just a marker showing where whole-number positions end and fractional positions begin — there is no "oneths" place because the ones place is already on the left side of the dot.

When reading a decimal like 4.739, decompose it position by position: 4 ones + 7 tenths + 3 hundredths + 9 thousandths, or 4 + 0.7 + 0.03 + 0.009 = 4.739. This expanded form is your most powerful tool for comparing and operating on decimals. When two decimals have the same whole-number part, compare their tenths digits. If those tie, compare hundredths. You never treat the part after the decimal point as a separate whole number — 0.27 is not "twenty-seven," it is 2 tenths and 7 hundredths.

Trailing zeros after the last significant decimal digit are equal in value to not writing them: 0.3 = 0.30 = 0.300. All three represent 3 tenths. This is different from trailing zeros in whole numbers (30 ≠ 3), which is a common source of confusion. In decimals, the decimal point anchors the positions, so adding zeros to the right doesn't shift anything. However, leading zeros like in 0.030 do matter — the zero in the tenths place means the 3 is in the hundredths position, making 0.030 = 3/100, not 3/10.
