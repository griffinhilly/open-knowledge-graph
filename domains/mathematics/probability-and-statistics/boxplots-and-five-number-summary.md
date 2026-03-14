---
id: boxplots-and-five-number-summary
title: Boxplots and the Five-Number Summary
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: box-and-whisker-plots
  type: hard
- id: measures-of-spread
  type: hard
- id: histograms-and-frequency-distributions
  type: soft
tags:
- boxplot
- five-number-summary
- IQR
- quartiles
- outliers
stage: formal-systems
status: validated
---

# Boxplots and the Five-Number Summary

## Core Idea
The five-number summary — minimum, Q1, median, Q3, maximum — divides a dataset into four equal-frequency parts and forms the basis of a boxplot. The interquartile range (IQR = Q3 − Q1) measures the spread of the middle 50% of data and is resistant to outliers. Formal outlier detection uses the 1.5 × IQR rule: values below Q1 − 1.5·IQR or above Q3 + 1.5·IQR are flagged as potential outliers and plotted as separate points.

## How It's Best Learned
Compare side-by-side boxplots of two or more groups — this is the primary use case. Students should practice reading IQR, identifying outliers, and comparing distributions from the box shape alone. Emphasize that equal-area boxes do not mean equal-height bars.

## Common Misconceptions
- Thinking the box width represents the number of observations rather than the IQR.
- Assuming symmetric boxes mean normally distributed data.
- Forgetting that the 1.5 × IQR rule identifies suspected outliers, not definitive ones.
