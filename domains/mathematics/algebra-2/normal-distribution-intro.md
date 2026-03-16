---
id: normal-distribution-intro
title: Normal Distribution Introduction
domain: mathematics
course: algebra-2
prerequisites:
- id: probability-with-combinatorics
  type: soft
- id: exponential-functions-and-graphs
  type: soft
builds-toward: []
tags:
- statistics
- normal-distribution
- bell-curve
- standard-deviation
stage: abstract-reasoning
status: validated
---
# Normal Distribution Introduction

## Core Idea
The normal distribution (bell curve) is a continuous probability distribution defined by its mean (center) and standard deviation (spread). It is symmetric about the mean. The empirical rule: approximately 68% of data falls within 1 standard deviation, 95% within 2, and 99.7% within 3. Z-scores standardize values: z = (x - mean)/sd, measuring how many standard deviations a value is from the mean. Many real-world datasets approximate the normal distribution.

## How It's Best Learned
Start with real data that is approximately normal (heights, test scores). Plot histograms and overlay the bell curve. Introduce mean and standard deviation as parameters. Apply the empirical rule to estimate probabilities. Compute z-scores and use z-tables or technology to find probabilities. Compare to skewed distributions.

## Common Misconceptions
- Thinking all data is normally distributed (many distributions are skewed or multimodal).
- Confusing the empirical rule percentages (68-95-99.7 applies to normal distributions, not all distributions).
- Not understanding that the normal distribution is continuous (probabilities are areas, not heights).
- Thinking a z-score of 0 means the value is 0 (it means the value equals the mean).

## Questions

```yaml
- question: "In a normal distribution with mean 70 and standard deviation 10, approximately what percentage of values fall between 60 and 80?"
  type: multiple-choice
  options: ["50%", "68%", "95%", "99.7%"]
  answer: 1
  explanation: "60 and 80 are each exactly 1 standard deviation from the mean (70 ± 10). The empirical rule states that approximately 68% of data in a normal distribution falls within 1 standard deviation of the mean."

- question: "A z-score of 0 means the data value is 0."
  type: true-false
  answer: false
  explanation: "A z-score of 0 means the data value equals the mean, not that the value itself is 0. The formula is z = (x − mean) / sd, so z = 0 precisely when x = mean, regardless of what the mean actually is."

- question: "A dataset of human heights is approximately normal with mean 170 cm and standard deviation 8 cm. A height of 186 cm has a z-score of 2. What does that z-score tell you?"
  type: short-answer
  answer: "It means 186 cm is 2 standard deviations above the mean. By the empirical rule, about 95% of heights fall within 2 standard deviations (154–186 cm), so 186 cm sits at the high end of the typical range."
  explanation: "z = (186 − 170) / 8 = 16 / 8 = 2. A z-score converts any value from any normal distribution into a universal scale: how many standard deviations above or below the mean. This allows meaningful comparisons across distributions with different means and spreads."
```

## Explainer

Many real-world measurements cluster around a typical value and spread out symmetrically in both directions — most people are near average height, fewer are very short or very tall, and the extremes are rare. When you plot a histogram of such data it takes on a symmetric bell shape. The normal distribution is the mathematical model for this pattern.

A normal distribution is completely described by two numbers: the **mean** (μ), which locates the center of the bell, and the **standard deviation** (σ), which controls how wide or narrow it is. A small standard deviation means data is tightly clustered around the mean; a large one means it is spread out. The curve is perfectly symmetric, so exactly half the data falls above the mean and half below.

The **empirical rule** gives quick probability estimates for any normal distribution. About 68% of values land within 1 standard deviation of the mean, 95% within 2, and 99.7% within 3. If exam scores are normally distributed with mean 75 and standard deviation 8, roughly 68% of students scored between 67 and 83, and about 95% scored between 59 and 91. This rule is specific to normal distributions — it does not apply to skewed or bimodal data, which is a common mistake.

The **z-score** standardizes any value: z = (x − mean) / sd. It measures how many standard deviations a value is above (positive) or below (negative) the mean. A z-score converts every normal distribution to the **standard normal distribution** (mean = 0, sd = 1), which is what z-tables are built on. A z-score of 0 does not mean the value is zero — it means the value equals the mean. This is one of the most frequent points of confusion.

One important conceptual point: the normal distribution is continuous. Probability is measured as the **area under the curve**, not the height at a point. The probability that a continuous variable takes any single exact value is technically 0 — only intervals have nonzero probability. When you use a z-table or calculator, you are finding the area to the left or right of a z-score, which represents the fraction of the distribution in that region.
