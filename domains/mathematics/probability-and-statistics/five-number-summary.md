---
id: five-number-summary
title: Five-Number Summary
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: measures-of-spread
  type: hard
builds-toward:
- boxplots-and-five-number-summary
tags:
- five-number-summary
- quartiles
- quantiles
stage: formal-systems
status: draft
---

# Five-Number Summary

## Core Idea
The five-number summary consists of minimum, first quartile (Q1, 25th percentile), median (Q2, 50th percentile), third quartile (Q3, 75th percentile), and maximum. These values divide the data into four equal-sized groups and provide a complete picture of the distribution's center, spread, and asymmetry. The five-number summary is particularly useful because it is robust to outliers and easy to visualize as a boxplot.

## Explainer

From measures of spread you know how to compute the range (max minus min) and the interquartile range (IQR = Q3 - Q1). The **five-number summary** organizes the five values that generate those measures — and more — into a single compact description of a dataset's distribution. The five numbers are: **minimum**, **Q1** (first quartile, 25th percentile), **median** (Q2, 50th percentile), **Q3** (third quartile, 75th percentile), and **maximum**. Together they divide the ordered dataset into four equal-sized groups: 25% of observations fall in each interval [min, Q1], [Q1, median], [median, Q3], [Q3, max].

To compute the summary, sort the data first. The **median** is the middle value for odd n, or the average of the two middle values for even n. Q1 is the median of the lower half of the data (excluding the overall median if n is odd), and Q3 is the median of the upper half. The exact convention for whether to include or exclude the overall median when n is odd varies by textbook, which is why different calculators sometimes return slightly different quartile values — but the interpretation is always the same: Q1 marks the 25th percentile and Q3 marks the 75th.

The key virtue of the five-number summary is **robustness**. The mean and standard deviation are pulled strongly by outliers: a single very large observation inflates both. The median and IQR, by contrast, are based on order (rank), not magnitude. A single outlier can only move Q3 or the maximum — it cannot distort the middle three values. This makes the five-number summary the right tool when data might contain extreme values, measurement errors, or heavy-tailed distributions. You can describe a salary distribution with a $10 million CEO without that outlier distorting your picture of what a typical employee earns.

The five-number summary also reveals **skewness** without any formula. Compare the spacing of the five values: if the median is close to Q1 but far from Q3, the data is right-skewed (a long upper tail). If the gap above the median is smaller than the gap below, the data is left-skewed. If all four intervals are roughly equal in width, the distribution is approximately symmetric. This visual diagnostic is one reason the summary translates directly into a **boxplot** — a graphical representation that displays all five values as a box (from Q1 to Q3) with a line at the median and whiskers extending to the min and max (or to a defined outlier boundary). You will explore that visualization next.
