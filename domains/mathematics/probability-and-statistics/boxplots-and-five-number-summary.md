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
status: validated
---

# Boxplots and Five-Number Summary

## Core Idea
A boxplot is a graphical representation of the five-number summary with a box spanning Q1 to Q3 (containing 50% of data), a line at the median, and whiskers extending to the minimum and maximum (or to boundaries determined by the 1.5×IQR outlier rule). Boxplots excel at comparing multiple distributions and identifying outliers. They reveal symmetry and skewness without assuming any particular distribution family.

## How It's Best Learned
Draw boxplots directly from five-number summaries. Compare boxplots of different datasets. Identify and discuss outliers defined by the 1.5×IQR rule.

## Common Misconceptions
Thinking the box always contains 50% of the data (true only for symmetric distributions when whiskers are equal). Confusing box width with IQR magnitude. Misidentifying which points are labeled as outliers.

## Questions

```yaml
- question: "A boxplot shows Q1 = 40, median = 42, Q3 = 70, lower whisker reaching 30, upper whisker reaching 95. What does this tell you about the distribution?"
  type: multiple-choice
  options:
    - "The distribution is symmetric — both whiskers extend from the box"
    - "The distribution is left-skewed — the median is near Q1"
    - "The distribution is right-skewed — the median is near Q1 and the upper whisker is much longer"
    - "The distribution is bimodal — the median is not centered in the box"
  answer: 2
  explanation: "Right skew (positive skew) is signaled by two features acting together: the median sitting close to Q1 (lower edge of the box), indicating most values are packed in the lower half of the IQR, and the upper whisker being much longer than the lower whisker, revealing a tail extending toward high values. Left skew is the mirror: median near Q3 and longer lower whisker. Symmetric distributions have a roughly centered median and roughly equal whisker lengths."

- question: "A dataset has Q1 = 10, Q3 = 20, and a data point at value 40. Should this point be plotted as an outlier?"
  type: multiple-choice
  options:
    - "No — 40 is only 20 units above Q3, which is not unusually large"
    - "No — only the single largest value in the dataset can be an outlier"
    - "Yes — the upper fence is Q3 + 1.5 × IQR = 20 + 15 = 35, so 40 exceeds it"
    - "It depends on whether 40 is the maximum value in the dataset"
  answer: 2
  explanation: "IQR = Q3 − Q1 = 20 − 10 = 10. Upper fence = Q3 + 1.5 × IQR = 20 + 15 = 35. Since 40 > 35, it is beyond the upper fence and is plotted as an individual outlier dot; the whisker extends only to the most extreme non-outlier (the largest value ≤ 35). The 1.5 × IQR rule determines outlier classification — proximity to Q3 alone is insufficient."

- question: "The box in a boxplot always contains exactly 50% of the data values."
  type: true-false
  answer: true
  explanation: "By definition, Q1 is the 25th percentile and Q3 is the 75th percentile, so the middle 50% of observations fall between them — exactly the region spanned by the box. This is a definitional property of quartiles and holds regardless of the distribution's shape. Note that 50% of values (observations) is different from 50% of visual area; in a skewed distribution the box may look asymmetric while still containing exactly half the data."

- question: "An outlier flagged by the 1.5 × IQR rule must be an error and should be removed before any analysis."
  type: true-false
  answer: false
  explanation: "The 1.5 × IQR rule identifies unusually extreme values for investigation, not automatic deletion. Outliers can be genuine observations — a legitimately exceptional measurement, a real extreme case, or even the most important finding in the dataset. Whether to remove an outlier requires domain knowledge: Was it recorded correctly? Does the phenomenon naturally produce extremes? Blindly removing outliers inflates apparent precision and can introduce serious bias. The rule's purpose is to flag, not to condemn."

- question: "How does a boxplot reveal the shape (skewness) of a distribution? What specific features indicate right-skew, left-skew, and symmetry?"
  type: short-answer
  answer: "A boxplot reveals skewness through two features: the position of the median line within the box, and the relative lengths of the whiskers. Right skew: median near Q1 (lower box edge) and upper whisker longer than lower. Left skew: median near Q3 (upper box edge) and lower whisker longer than upper. Symmetric: median approximately centered in the box with roughly equal whisker lengths."
  explanation: "These features work together because skewness means values are pulled toward one tail. In a right-skewed distribution, the mass is concentrated at low values (packed near Q1), with the upper whisker stretched toward outlying high values. Boxplots make this pattern immediately visible in a compact, comparable format — especially useful when showing multiple groups side by side."
```

## Explainer

From the five-number summary, you have the minimum, Q1, median (Q2), Q3, and maximum of a dataset. A **boxplot** is a standardized way to draw those five numbers as a picture. Draw a number line. Draw a box from Q1 to Q3 — its width on the number line represents the **interquartile range (IQR)** = Q3 − Q1, which spans the middle 50% of the data. Draw a vertical line inside the box at the median. Then extend **whiskers** outward from each side of the box. The precise rule: calculate the **lower fence** as Q1 − 1.5 × IQR and the **upper fence** as Q3 + 1.5 × IQR. The whiskers extend to the most extreme data points that still fall within these fences. Any point beyond a fence is plotted individually as an **outlier dot**.

The most important thing a boxplot shows is **distributional shape** without assuming any particular model. If the median line sits close to Q1, the data is right-skewed — most values are packed toward the lower end with a long tail of high values stretching the upper whisker. If the median sits close to Q3, the data is left-skewed. If the median is centered in the box and both whiskers are similar length, the distribution is roughly symmetric. You can read all of this instantly from the picture in a way that a table of numbers makes harder.

The real power of boxplots emerges when comparing multiple groups side by side. Suppose you want to compare exam scores across five different sections of a course. Five histograms would clutter the page and make comparison difficult. Five boxplots on the same scale let you immediately see which section had the highest median, which had the most spread, and which had outliers. The box widths and median positions are directly comparable across groups. This is why boxplots appear constantly in scientific papers and statistical reports: they pack a great deal of distributional information into a compact, comparable format.

One subtlety worth noting: the box always spans Q1 to Q3, so by definition it contains the middle 50% of data values — not 50% in the sense of equal area, but 50% in the sense of 50% of observations fall between Q1 and Q3. The whiskers do not have fixed coverage; they extend to wherever the data actually reaches up to the fence. In a very skewed dataset one whisker can be much longer than the other. Outliers flagged by the 1.5 × IQR rule are not automatically "wrong" values — they are simply unusually extreme, and whether they are errors or genuine observations requires domain knowledge to decide.
