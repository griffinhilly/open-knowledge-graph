---
id: boxplots-and-five-number-summary
title: Boxplots and Five-Number Summary
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: five-number-summary
  type: hard
tags:
- boxplot
- outlier-detection
- distribution-shape
stage: formal-systems
status: draft
---

# Boxplots and Five-Number Summary

## Core Idea
A boxplot is a graphical representation of the five-number summary with a box spanning Q1 to Q3 (containing 50% of data), a line at the median, and whiskers extending to the minimum and maximum (or to boundaries determined by the 1.5×IQR outlier rule). Boxplots excel at comparing multiple distributions and identifying outliers. They reveal symmetry and skewness without assuming any particular distribution family.

## How It's Best Learned
Draw boxplots directly from five-number summaries. Compare boxplots of different datasets. Identify and discuss outliers defined by the 1.5×IQR rule.

## Common Misconceptions
Thinking the box always contains 50% of the data (true only for symmetric distributions when whiskers are equal). Confusing box width with IQR magnitude. Misidentifying which points are labeled as outliers.

## Explainer

From the five-number summary, you have the minimum, Q1, median (Q2), Q3, and maximum of a dataset. A **boxplot** is a standardized way to draw those five numbers as a picture. Draw a number line. Draw a box from Q1 to Q3 — its width on the number line represents the **interquartile range (IQR)** = Q3 − Q1, which spans the middle 50% of the data. Draw a vertical line inside the box at the median. Then extend **whiskers** outward from each side of the box. The precise rule: calculate the **lower fence** as Q1 − 1.5 × IQR and the **upper fence** as Q3 + 1.5 × IQR. The whiskers extend to the most extreme data points that still fall within these fences. Any point beyond a fence is plotted individually as an **outlier dot**.

The most important thing a boxplot shows is **distributional shape** without assuming any particular model. If the median line sits close to Q1, the data is right-skewed — most values are packed toward the lower end with a long tail of high values stretching the upper whisker. If the median sits close to Q3, the data is left-skewed. If the median is centered in the box and both whiskers are similar length, the distribution is roughly symmetric. You can read all of this instantly from the picture in a way that a table of numbers makes harder.

The real power of boxplots emerges when comparing multiple groups side by side. Suppose you want to compare exam scores across five different sections of a course. Five histograms would clutter the page and make comparison difficult. Five boxplots on the same scale let you immediately see which section had the highest median, which had the most spread, and which had outliers. The box widths and median positions are directly comparable across groups. This is why boxplots appear constantly in scientific papers and statistical reports: they pack a great deal of distributional information into a compact, comparable format.

One subtlety worth noting: the box always spans Q1 to Q3, so by definition it contains the middle 50% of data values — not 50% in the sense of equal area, but 50% in the sense of 50% of observations fall between Q1 and Q3. The whiskers do not have fixed coverage; they extend to wherever the data actually reaches up to the fence. In a very skewed dataset one whisker can be much longer than the other. Outliers flagged by the 1.5 × IQR rule are not automatically "wrong" values — they are simply unusually extreme, and whether they are errors or genuine observations requires domain knowledge to decide.
