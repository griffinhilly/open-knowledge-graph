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

## Questions

```yaml
- question: "A dataset has the five-number summary: min=10, Q1=20, median=25, Q3=50, max=90. What does this suggest about the distribution's shape?"
  type: multiple-choice
  options:
    - "Symmetric — the quartiles are evenly spaced from the median"
    - "Left-skewed — the lower tail is longer than the upper tail"
    - "Right-skewed — the gap above the median (25 to 90) is larger than the gap below (10 to 25)"
    - "Bimodal — the large range between Q3 and max indicates two clusters"
  answer: 2
  explanation: "The spacing between the five values reveals skewness. Below the median, the spread is 25−10 = 15 (min to median). Above the median, the spread is 90−25 = 65 (median to max). The upper tail is much larger, so the distribution is right-skewed (long upper tail). The large Q3-to-max gap (40 units) versus the Q1-to-min gap (10 units) confirms this. Skewness is read from the relative spacing of the summary values, not from the values themselves. No formula is needed."

- question: "A researcher reports salary data for 500 employees, including a CEO earning $12 million while most employees earn $50,000–$80,000. Which summary is most useful, and why?"
  type: multiple-choice
  options:
    - "Mean and standard deviation — they use all data points and are more precise"
    - "Five-number summary — the median and quartiles are resistant to the CEO's extreme salary"
    - "Mean and five-number summary both — they give identical pictures with large samples"
    - "Five-number summary — but only after removing the outlier from the dataset"
  answer: 1
  explanation: "The mean and standard deviation are pulled strongly by the $12M outlier, giving a misleadingly high 'average' salary. The median and IQR are based on rank, not magnitude, so the CEO's salary only moves the maximum — it cannot shift Q1, the median, or Q3. The five-number summary gives an honest picture of the typical employee's salary. Option D reflects a common mistake: you should not remove outliers just because they distort the mean — the five-number summary handles this without deletion."

- question: "In the five-number summary, each of the four intervals [min, Q1], [Q1, median], [median, Q3], and [Q3, max] contains the same number of data points."
  type: true-false
  answer: true
  explanation: "This is the defining property of quartiles. Q1 is the 25th percentile, meaning 25% of data falls below it. The median is the 50th percentile. Q3 is the 75th percentile. So exactly 25% of observations fall in each of the four intervals. The intervals may differ widely in width (range of values) — a skewed distribution will have unequal widths — but the frequency in each interval is equal. Confusing width with frequency is the central misconception about the five-number summary."

- question: "Adding one very large outlier to a dataset will significantly shift the median and Q1 upward."
  type: true-false
  answer: false
  explanation: "The median and quartiles are resistant (robust) to outliers because they are based on rank position, not magnitude. Adding one extreme value changes the rank ordering only slightly — in a large dataset, it shifts the median's rank by at most one position. For Q1 to move significantly, many values near Q1 would need to change. An outlier primarily affects the maximum (and possibly Q3 in small datasets) but leaves the middle of the distribution intact. This robustness is precisely why the five-number summary is preferred when outliers are possible."

- question: "How does the five-number summary reveal the skewness of a distribution without computing any formula?"
  type: short-answer
  answer: "By comparing the spacing between the five values. If the gap from the median to Q3 (and from Q3 to the max) is larger than the gap from the median to Q1 (and from Q1 to the min), the distribution is right-skewed. If the gap below the median is larger, it is left-skewed. Equal spacing suggests symmetry. Since each interval contains the same number of data points, unequal spacing means some quarter of the data is stretched out over a larger range of values — which is exactly what skewness means."
  explanation: "This is the power of a rank-based summary: skewness shows up directly as asymmetric spacing rather than requiring calculation of a skewness statistic. A right-skewed distribution bunches data on the left and trails far to the right, so the upper intervals are wide while the lower intervals are narrow — visible immediately from the five numbers."
```

## Explainer

From measures of spread you know how to compute the range (max minus min) and the interquartile range (IQR = Q3 - Q1). The **five-number summary** organizes the five values that generate those measures — and more — into a single compact description of a dataset's distribution. The five numbers are: **minimum**, **Q1** (first quartile, 25th percentile), **median** (Q2, 50th percentile), **Q3** (third quartile, 75th percentile), and **maximum**. Together they divide the ordered dataset into four equal-sized groups: 25% of observations fall in each interval [min, Q1], [Q1, median], [median, Q3], [Q3, max].

To compute the summary, sort the data first. The **median** is the middle value for odd n, or the average of the two middle values for even n. Q1 is the median of the lower half of the data (excluding the overall median if n is odd), and Q3 is the median of the upper half. The exact convention for whether to include or exclude the overall median when n is odd varies by textbook, which is why different calculators sometimes return slightly different quartile values — but the interpretation is always the same: Q1 marks the 25th percentile and Q3 marks the 75th.

The key virtue of the five-number summary is **robustness**. The mean and standard deviation are pulled strongly by outliers: a single very large observation inflates both. The median and IQR, by contrast, are based on order (rank), not magnitude. A single outlier can only move Q3 or the maximum — it cannot distort the middle three values. This makes the five-number summary the right tool when data might contain extreme values, measurement errors, or heavy-tailed distributions. You can describe a salary distribution with a $10 million CEO without that outlier distorting your picture of what a typical employee earns.

The five-number summary also reveals **skewness** without any formula. Compare the spacing of the five values: if the median is close to Q1 but far from Q3, the data is right-skewed (a long upper tail). If the gap above the median is smaller than the gap below, the data is left-skewed. If all four intervals are roughly equal in width, the distribution is approximately symmetric. This visual diagnostic is one reason the summary translates directly into a **boxplot** — a graphical representation that displays all five values as a box (from Q1 to Q3) with a line at the median and whiskers extending to the min and max (or to a defined outlier boundary). You will explore that visualization next.
