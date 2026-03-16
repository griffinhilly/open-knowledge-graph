---
id: percent-of-a-number
title: Percent of a Number
domain: mathematics
course: prealgebra
prerequisites:
- id: percent-concept
  type: hard
- id: multiplying-integers
  type: hard
- id: converting-fractions-decimals-percents
  type: soft
- id: solving-proportions
  type: soft
builds-toward:
- percent-increase-decrease
- simple-interest
tags:
- percent
- multiplication
- applications
stage: abstract-reasoning
status: validated
---
# Percent of a Number

## Core Idea
Finding a percent of a number means computing a fractional part of that number. The key operation is multiplication: "percent of" translates to "decimal times." To find 35% of 80, convert 35% to 0.35 and multiply: 0.35 × 80 = 28. Equivalently, you can use the fraction form: 35/100 × 80 = 28. This skill is used for calculating tips, taxes, discounts, commissions, and interest — it is arguably the single most frequently used math skill in adult life.

## How It's Best Learned
Teach the three-step process: (1) convert percent to decimal, (2) multiply by the number, (3) interpret the result in context. Practice benchmark percents mentally (10%, 25%, 50%) before moving to arbitrary percents. Use the proportion method (part/whole = percent/100) as an alternative approach. Real-world word problems (sale prices, tip amounts) build motivation and fluency.

## Common Misconceptions
- Students sometimes divide instead of multiply when finding "percent of."
- Forgetting to convert the percent to a decimal before multiplying (computing 35 × 80 = 2800 instead of 0.35 × 80 = 28).
- Confusing "what is 20% of 50?" with "20 is what percent of 50?" — these are different problem types.

## Questions

```yaml
- question: "A jacket costs $120 and is on sale for 25% off. How much is the discount?"
  type: multiple-choice
  options: ["$3", "$25", "$30", "$95"]
  answer: 2
  explanation: "25% of $120 = 0.25 × $120 = $30. The discount is $30, making the sale price $90. A common error is multiplying without the decimal conversion (25 × 120 = 3,000 ÷ 100 is one corrective path) or subtracting 25 directly from 120."

- question: "To find 40% of 70, you should divide 70 by 40."
  type: true-false
  answer: false
  explanation: "The phrase 'percent of' means multiply, not divide. 40% of 70 = 0.40 × 70 = 28. Dividing gives 70 ÷ 40 = 1.75, which is unrelated. This is the most common error with this skill: 'of' is the mathematical signal for multiplication."

- question: "What are the three steps to find any percent of a number, and why is the decimal conversion step necessary?"
  type: short-answer
  answer: "Step 1: Convert the percent to a decimal by dividing by 100 (e.g., 35% → 0.35). Step 2: Multiply the decimal by the number. Step 3: Interpret the result in context. The conversion is necessary because percent means 'per hundred' — without it, multiplying 35 × 80 gives 2,800, which is 100 times too large."
  explanation: "The decimal conversion makes the meaning of 'per hundred' explicit in the arithmetic. Writing 35% as 35/100 = 0.35 and then multiplying by 80 correctly scales the result: you are taking 35 out of every 100 parts of 80."
```

## Explainer

You already know from the percent concept that "percent" means "per hundred" — 35% is the fraction 35/100. Finding a percent of a number means applying that fraction to a real-world quantity, and the core operation is multiplication. The phrase "percent of a number" translates directly into math: "of" means multiply, and "percent" means divide by 100. So "35% of 80" becomes (35/100) × 80 = 0.35 × 80 = 28.

The three-step process makes this mechanical and reliable: (1) convert the percent to a decimal, (2) multiply by the given number, (3) interpret the result in context. Step 1 is where most errors originate. Students who skip it and compute 35 × 80 get 2,800 — a result 100 times too large. The conversion is not just a notational formality; it is what makes "per hundred" appear in the arithmetic. You can also use the fraction form directly: (35/100) × 80, which gives the same answer and makes the "per hundred" visible.

Benchmark percents are worth knowing by heart because they appear constantly and can be computed mentally without a calculator. Ten percent of any number is just the number shifted one decimal place left: 10% of 80 = 8. Fifty percent is half. Twenty-five percent is a quarter. Twenty percent is twice the 10% value. These benchmarks let you estimate before computing and check whether a calculated answer is reasonable. If you are finding 40% of 70 and get 1.75, the benchmark check immediately flags the error: 40% of 70 should be less than 70 but more than 10% (which is 7), so the answer must be somewhere in that range.

Notice the direction of the operation: a percent of a number is always smaller than the original when the percent is below 100%, and larger when it exceeds 100%. This sanity check — ask yourself "should the answer be bigger or smaller than the original?" — catches the divide-instead-of-multiply error immediately. Dividing 70 by 40 gives 1.75, which is far smaller than the 10% benchmark of 7, so something is clearly wrong.

This skill is the engine behind a wide range of everyday calculations: a 15% restaurant tip, an 8.5% sales tax, a 30% clearance discount, a 6% real-estate commission, or monthly interest on a loan balance. In every case the structure is identical — find a percent of a base number. The base is always the "whole" you are taking a part of. Mastering the three-step method and internalizing the two misconceptions (divide vs. multiply; forgetting the decimal conversion) prepares you for percent increase and decrease, which extend this single skill to comparisons and change.
