---
id: quantiles-and-percentiles
title: Quantiles, Percentiles, and the Five-Number Summary
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: descriptive-statistics-overview
  type: hard
builds-toward:
- distribution-shape-skewness-kurtosis
- boxplots-and-five-number-summary
tags:
- descriptive-statistics
- quantiles
- percentiles
stage: formal-systems
status: draft
---

# Quantiles, Percentiles, and the Five-Number Summary

## Core Idea
The pth percentile is the value below which p% of the data falls. Quartiles divide data into four equal parts. The five-number summary (min, Q1, median, Q3, max) summarizes data location and spread in a distribution-free way.

## How It's Best Learned
Sort data and manually calculate percentiles for small datasets. Use software to find quantiles for large datasets. Relate percentiles to standard scores and cumulative distributions.

## Common Misconceptions
Assuming the median is always at 50% (it is, by definition). Confusing percentile rank with actual values. Not recognizing multiple acceptable definitions of sample quantiles. Thinking all quantiles split data equally.

## Questions

```yaml
- question: "A student scores 720 on a standardized test and is told they are at the 85th percentile. Which interpretation is correct?"
  type: multiple-choice
  options:
    - "The student scored 85% of the total possible points on the test"
    - "Approximately 85% of test-takers scored at or below 720"
    - "The student answered 85 out of 100 questions correctly"
    - "The student scored 85 points above the median"
  answer: 1
  explanation: "The pth percentile identifies a position in the sorted distribution, not an absolute score. Being at the 85th percentile means roughly 85% of test-takers scored at or below 720 — this is the student's percentile rank. The actual score (720) is the percentile value; the 85% describes relative position. These can be entirely disconnected: 720 might represent only 60% of possible points yet still place a student in the 85th percentile if most others scored lower."

- question: "Why is the IQR considered more robust than the standard deviation as a measure of spread?"
  type: multiple-choice
  options:
    - "The IQR is always a smaller number than the standard deviation, so it is more precise"
    - "The IQR spans only the middle 50% of sorted data, so extreme values at the tails cannot affect it"
    - "The IQR can be computed without sorting the data, making it less sensitive to ordering errors"
    - "The standard deviation is only defined for normally distributed data, while the IQR works for any distribution"
  answer: 1
  explanation: "Robustness means resistance to outliers. The IQR = Q3 − Q1 uses only the boundaries of the middle 50% of the data. No matter how extreme the minimum or maximum are, they cannot change Q1 or Q3 — the IQR is unaffected. The standard deviation squares deviations from the mean, which amplifies the influence of extreme values. Option D is a partial truth: the standard deviation is defined for all distributions, but it is less meaningful (not undefined) for skewed data — the real issue is sensitivity to outliers."

- question: "The mean and the median are both measures of center, so they both fall at the 50th percentile of any dataset."
  type: true-false
  answer: false
  explanation: "The median is always the 50th percentile by definition — it is the value that splits the sorted data in half. The mean is an arithmetic average and can be anywhere in the distribution. In right-skewed data (like incomes), a small number of very high values pull the mean far above the median. For example, a dataset where most values are around 30 but a few are in the thousands could have a median of 32 and a mean of 150. Only in perfectly symmetric distributions do the mean and median coincide."

- question: "The five-number summary makes no assumptions about the shape of the underlying distribution."
  type: true-false
  answer: true
  explanation: "This is what 'distribution-free' means. The five-number summary — minimum, Q1, median, Q3, maximum — is computed directly from sorted data positions, requiring no assumption about normality, symmetry, or any parametric form. This contrasts with inference based on the mean and standard deviation, which typically assumes approximate normality for interval estimates. The five-number summary is valid and meaningful for any data distribution, including heavily skewed or multimodal ones."

- question: "Why might a five-number summary give a better description of income data than the mean and standard deviation alone?"
  type: short-answer
  answer: "Income distributions are right-skewed: a small number of very high earners pull the mean far above what most people earn. The mean and standard deviation are sensitive to these outliers, making the mean unrepresentative of the typical income. The five-number summary — based on percentiles — shows where most incomes actually fall (Q1 to Q3) and reveals the skewness through asymmetric gaps (e.g., Q3−median much larger than median−Q1), without being distorted by extreme values."
  explanation: "When the median income is $52,000 and the mean is $80,000, the gap signals right-skew: a few high earners inflate the average. The five-number summary makes the structure visible without being misled. This is why policy discussions about 'typical' household income should reference median, not mean — and why the IQR better captures the spread most families experience."
```

## Explainer

You already know from descriptive statistics that the **mean** and **standard deviation** summarize a dataset's center and spread. But these two numbers are sensitive to extreme values — a single outlier can pull the mean far from where most of the data actually lives. Quantiles offer an alternative: they summarize the distribution by recording *where specific fractions of the data fall*, entirely without reference to arithmetic averages. The result is a description of shape that stays meaningful even when data is heavily skewed.

A **percentile** answers the question: "what value separates the bottom p% of the data from the top (100−p)%?" If your exam score is at the 85th percentile, it means roughly 85% of test-takers scored below you. More precisely, the **pth percentile** is the value x_p such that p% of observations fall at or below it. When you have exactly 100 data points sorted in order, this is almost literal: the 37th percentile is approximately the 37th value. For other dataset sizes, a linear interpolation formula extends the idea. Different textbooks and software packages use slightly different interpolation conventions — there are nine recognized methods — which is why computed quantiles from different tools can differ slightly on the same data.

**Quartiles** are the three percentiles that divide the sorted data into four equal-sized groups: **Q1** (25th percentile), **Q2** (50th percentile, the median), and **Q3** (75th percentile). The gap between Q1 and Q3 is called the **interquartile range (IQR)**, and it captures the spread of the middle 50% of the data. The IQR is robust to outliers in a way that the standard deviation is not — extreme values lie outside this middle band and simply don't affect it. More generally, any division of sorted data into equal-sized groups gives **quantiles**: **deciles** divide into tenths, **quintiles** into fifths, and so on.

The **five-number summary** — minimum, Q1, median, Q3, maximum — packages these ideas into a compact, distribution-free profile of any dataset. "Distribution-free" means it makes no assumptions about whether the data follows a normal distribution or any other shape. The five numbers tell you where the data starts, where the lower quarter ends, where the middle lies, where the upper quarter begins, and where the data ends. The gap between min and Q1 tells you how spread out the bottom quarter is; the gap between Q3 and max tells you how spread out the top quarter is. When those gaps are unequal, the data is skewed — an asymmetry you will formalize when you study distribution shape and kurtosis. The five-number summary is also what the **boxplot** makes visual: the box spans Q1 to Q3, the line inside is the median, and the whiskers extend to the min and max (or to a multiple of the IQR, with points beyond that plotted as individual outliers).
