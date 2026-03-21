---
id: converting-fractions-decimals-percents
title: Converting Between Fractions, Decimals, and Percents
domain: mathematics
course: prealgebra
prerequisites:
  - id: percent-concept
    type: hard
  - id: multiplying-fractions
    type: hard
  - id: decimal-place-value
    type: hard
builds-toward:
  - percent-of-a-number
  - rational-numbers-operations
tags: [fractions, decimals, percents, conversion]
stage: abstract-reasoning
status: validated
---

# Converting Between Fractions, Decimals, and Percents

## Core Idea
Fractions, decimals, and percents are three different representations of the same quantity. Being fluent in converting between them is critical for problem-solving because different contexts favor different representations. To convert a fraction to a decimal, divide numerator by denominator. To convert a decimal to a percent, multiply by 100. To convert a percent to a fraction, put it over 100 and simplify. Fluency with these conversions is a prerequisite for almost all quantitative reasoning in algebra, statistics, and real-world applications.

## How It's Best Learned
Build a reference chart with common equivalences (1/4 = 0.25 = 25%, 1/3 = 0.333... = 33.3%, etc.) and have students memorize benchmarks. Practice all six conversion directions systematically. Use visual models (number lines, grids) to show that the same point or region can be named three ways. Emphasize repeating decimals and how they relate to fractions (1/3, 1/6, 1/7).

## Common Misconceptions
- Moving the decimal point the wrong direction when converting between decimals and percents (e.g., 0.5 = 5% instead of 50%).
- Writing 1/3 as 0.33 and then as 33% without acknowledging the repeating decimal and rounding.
- Thinking that 0.25% = 1/4 instead of recognizing that 0.25% = 0.0025 = 1/400.

## Questions

```yaml
- question: "A student converts 3/4 to a percent for a report on interest rates and writes '0.75%.' Why is this a significant error?"
  type: multiple-choice
  options:
    - "It is not an error — 3/4 and 0.75% represent the same quantity"
    - "The student moved the decimal in the wrong direction; 3/4 = 75%, not 0.75%"
    - "Fractions cannot be directly converted to percents without using the midpoint formula"
    - "The error is only stylistic — the value is correct but the notation is unusual"
  answer: 1
  explanation: "3/4 = 0.75 as a decimal, and converting to percent means multiplying by 100 (shifting the decimal two places right), giving 75%. Writing 0.75% would mean 0.75 per hundred, which equals 0.0075 — an entirely different quantity. In a real context like interest rates, this error is enormous: a 75% rate versus a 0.75% rate are very different financial realities."

- question: "A savings account advertisement says it pays '0.5% annual interest.' A student calculates the annual interest on a $400 deposit as $200. What went wrong?"
  type: multiple-choice
  options:
    - "Nothing — 0.5% of $400 is indeed $200"
    - "The student treated 0.5% as 0.5 (one-half) instead of 0.005 (one-half of one percent)"
    - "The student should have divided by 100 before multiplying, not after"
    - "Percents cannot be applied to dollar amounts without a unit conversion"
  answer: 1
  explanation: "0.5% means 0.5 per hundred, which as a decimal is 0.005. Multiplying $400 × 0.005 = $2.00. The student treated '0.5%' as though it were '0.5' (the decimal for 50%), computing $400 × 0.5 = $200. This is the classic magnitude error: confusing a number (0.5) with that same number expressed as a percent (0.5%). These differ by a factor of 100."

- question: "The decimal 0.333... (with 3 repeating infinitely) is not exactly equal to 1/3 — it is only an approximation."
  type: true-false
  answer: false
  explanation: "0.333... with the 3 repeating infinitely is exactly equal to 1/3. Repeating decimals are not approximations — they are the complete, exact decimal representation of fractions whose denominators have prime factors other than 2 and 5. The confusion arises because we often round 1/3 to 0.33 for practical purposes, but that rounded value is the approximation. The infinite repeating decimal is the exact equivalent."

- question: "To convert 0.25% to a fraction, you write it as 1/4."
  type: true-false
  answer: false
  explanation: "0.25% means 0.25 per hundred, which equals 0.0025 as a decimal, which equals 25/10000 = 1/400 — not 1/4. The fraction 1/4 equals 25%, not 0.25%. This is the core magnitude trap: the number 0.25 and the percent 0.25% look similar but differ by a factor of 100. Always complete the full conversion: percent → decimal (divide by 100) → fraction."

- question: "A classmate tells you that converting fractions to percents is just 'moving the decimal point.' What is missing from this explanation, and what is the complete correct process?"
  type: short-answer
  answer: "Moving the decimal handles converting between decimals and percents, but it is only one step. To convert a fraction to a percent: first divide the numerator by the denominator to get a decimal (3/4 = 0.75), then multiply by 100 by shifting the decimal two places right (0.75 → 75%). The missing piece is the first step — dividing numerator by denominator — and the direction matters: shift right (multiply by 100) to go decimal→percent, shift left (divide by 100) to go percent→decimal. Getting the direction wrong is the most common error."
  explanation: "Percent literally means 'per hundred,' so multiplying by 100 converts a decimal into its equivalent 'per hundred' expression. Understanding why the rule works prevents reversing it."
```

## Explainer

The central idea is that fractions, decimals, and percents are not different kinds of numbers — they are different notations for the same quantity. The fraction 3/4, the decimal 0.75, and the percent 75% all name the same point on the number line. Your prerequisites — understanding **decimal place value** and how to **multiply fractions** — give you everything you need to move fluently among these three representations.

The most reliable strategy is to understand what each notation literally means. A fraction a/b means "a divided by b," so dividing the numerator by the denominator always produces the decimal. A **percent** means "per hundred" (from the Latin *per centum*), so 75% literally means 75/100 = 0.75. These two anchors unlock all six conversion directions. Fraction to decimal: divide numerator by denominator. Decimal to percent: multiply by 100 (shift the decimal point two places right). Percent to decimal: divide by 100 (shift left two places). Decimal to fraction: read the place value and simplify (0.75 = 75/100 = 3/4). Fraction to percent: convert to decimal first, then multiply by 100. Percent to fraction: write it over 100 and simplify. Practicing all six directions in both directions is what builds true fluency.

One case deserves special attention: **repeating decimals**. When you divide 1 by 3, the result is 0.333..., which never terminates. This is not a computational error — it is the exact decimal expansion of 1/3. Any fraction in lowest terms whose denominator has prime factors other than 2 and 5 will produce a repeating decimal. Common examples to memorize: 1/3 = 0.333... ≈ 33.3%, 1/6 = 0.1666... ≈ 16.7%, 1/7 = 0.142857... ≈ 14.3%. Rounding is acceptable for approximate work, but always acknowledge that you are rounding — 1/3 is not exactly 0.33, and 33% is not exactly 1/3.

Watch magnitudes carefully, especially when percents are small. The familiar chain 3/4 → 0.75 → 75% works because 75% is close to 1 (a large chunk). But 0.25% is a very different thing: it equals 0.0025, which is 1/400 — not 1/4. Confusing "0.25" (a quarter) with "0.25 percent" (a tiny fraction) is a high-stakes error in real-world contexts like interest rates, tax rates, and probability. A simple sanity check: after any conversion, ask whether the result is "about the right size." Converting 3/4 and getting 0.75% should immediately feel wrong — three-quarters of something is a substantial portion, not a fraction of a percent.
