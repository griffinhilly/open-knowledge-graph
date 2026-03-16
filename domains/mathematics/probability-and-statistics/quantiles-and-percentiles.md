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

## Explainer

You already know from descriptive statistics that the **mean** and **standard deviation** summarize a dataset's center and spread. But these two numbers are sensitive to extreme values — a single outlier can pull the mean far from where most of the data actually lives. Quantiles offer an alternative: they summarize the distribution by recording *where specific fractions of the data fall*, entirely without reference to arithmetic averages. The result is a description of shape that stays meaningful even when data is heavily skewed.

A **percentile** answers the question: "what value separates the bottom p% of the data from the top (100−p)%?" If your exam score is at the 85th percentile, it means roughly 85% of test-takers scored below you. More precisely, the **pth percentile** is the value x_p such that p% of observations fall at or below it. When you have exactly 100 data points sorted in order, this is almost literal: the 37th percentile is approximately the 37th value. For other dataset sizes, a linear interpolation formula extends the idea. Different textbooks and software packages use slightly different interpolation conventions — there are nine recognized methods — which is why computed quantiles from different tools can differ slightly on the same data.

**Quartiles** are the three percentiles that divide the sorted data into four equal-sized groups: **Q1** (25th percentile), **Q2** (50th percentile, the median), and **Q3** (75th percentile). The gap between Q1 and Q3 is called the **interquartile range (IQR)**, and it captures the spread of the middle 50% of the data. The IQR is robust to outliers in a way that the standard deviation is not — extreme values lie outside this middle band and simply don't affect it. More generally, any division of sorted data into equal-sized groups gives **quantiles**: **deciles** divide into tenths, **quintiles** into fifths, and so on.

The **five-number summary** — minimum, Q1, median, Q3, maximum — packages these ideas into a compact, distribution-free profile of any dataset. "Distribution-free" means it makes no assumptions about whether the data follows a normal distribution or any other shape. The five numbers tell you where the data starts, where the lower quarter ends, where the middle lies, where the upper quarter begins, and where the data ends. The gap between min and Q1 tells you how spread out the bottom quarter is; the gap between Q3 and max tells you how spread out the top quarter is. When those gaps are unequal, the data is skewed — an asymmetry you will formalize when you study distribution shape and kurtosis. The five-number summary is also what the **boxplot** makes visual: the box spans Q1 to Q3, the line inside is the median, and the whiskers extend to the min and max (or to a multiple of the IQR, with points beyond that plotted as individual outliers).
