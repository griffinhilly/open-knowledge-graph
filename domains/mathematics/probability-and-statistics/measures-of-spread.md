---
id: measures-of-spread
title: Measures of Spread
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: mean-median-mode
  type: hard
builds-toward:
- five-number-summary
- boxplots-and-five-number-summary
tags:
- spread
- variability
- range
- iqr
- variance
- std-dev
stage: formal-systems
status: draft
---

# Measures of Spread

## Core Idea
Measures of spread quantify variability in data. Range = max - min (sensitive to outliers). Interquartile range (IQR) = Q3 - Q1 (robust to outliers). Variance = average squared deviation from mean. Standard deviation = √variance (in original units). These measures answer 'how spread out is the data?' and are essential for understanding data distributions, comparing datasets, and assessing consistency.

## How It's Best Learned
Compute all measures for the same dataset. Add outliers and observe which measures change. Plot data showing how visual spread matches numerical measures.

## Common Misconceptions
Confusing variance and standard deviation. Thinking IQR includes all data. Believing range alone describes spread adequately.

## Questions

```yaml
- question: "A dataset of exam scores has a mean of 75 but includes one outlier score of 15. Which measure of spread best represents the variability experienced by most students?"
  type: multiple-choice
  options: ["Range", "Variance", "Interquartile range (IQR)", "None — all measures are equally affected"]
  answer: 2
  explanation: "IQR measures the spread of the middle 50% of data (Q3 - Q1), making it resistant to outliers. Range = max - min, so the single score of 15 would dominate it entirely. Variance and standard deviation are also pulled by extreme values because they use squared deviations from the mean."

- question: "The standard deviation of a dataset is always smaller than its variance."
  type: true-false
  answer: false
  explanation: "Standard deviation = √variance. When variance is less than 1, its square root is larger — for example, a variance of 0.25 gives a standard deviation of 0.5. Whether std dev is larger or smaller than variance depends entirely on the scale of the data, not a fixed rule."

- question: "Why is standard deviation usually reported instead of variance when describing how spread out data is?"
  type: short-answer
  answer: "Standard deviation is in the same units as the original data, making it directly interpretable, while variance is in squared units that have no intuitive meaning."
  explanation: "If scores are measured in points, variance is in points-squared, which cannot be compared to the data directly. Standard deviation returns to the original unit, so you can say 'scores varied by about 8 points on average' — a statement that is immediately meaningful to anyone who knows the scale."
```

## Explainer

You already know how to find the center of a dataset — the mean, median, and mode each describe a typical value. But two datasets can have the same mean and look completely different. Imagine one class where every student scores between 70 and 80, and another where scores range from 10 to 100. Both might have a mean of 75. Measures of spread exist to capture this difference.

The simplest measure is the **range**: maximum minus minimum. It is easy to compute but fragile — one extreme outlier can make a dataset look far more variable than it really is. A single student who scores 0 on an exam inflates the range for the whole class, even if everyone else clustered tightly.

The **interquartile range (IQR)** solves this by ignoring the extremes. It measures the span of the middle 50% of data: Q3 (the 75th percentile) minus Q1 (the 25th percentile). IQR is robust to outliers because those extreme values lie outside the range it measures. This is why box plots use IQR as their primary spread statistic — it describes where most of the data lives.

**Variance** takes a different approach: compute each value's distance from the mean, square those distances, and average them. Squaring serves two purposes — it makes all deviations positive, and it penalizes large deviations more heavily than small ones. The downside is that variance is in squared units, which are hard to interpret directly. **Standard deviation** fixes this by taking the square root of variance, returning the result to the original units. This is why standard deviation is the spread measure you will see most often in practice.

The key judgment call is which measure to use. If your data has outliers or is skewed, IQR is more informative than standard deviation. If your data is roughly symmetric and outlier-free, standard deviation is preferred because it uses all the data and connects cleanly to probability theory. Range is useful as a quick sanity check, but rarely sufficient on its own.
