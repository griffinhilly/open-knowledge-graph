---
id: mean-median-mode-probability-and-statistics
title: Mean, Median, and Mode
domain: mathematics
course: probability-and-statistics
prerequisites: []
builds-toward:
- measures-of-spread
- five-number-summary
tags:
- center
- location
- descriptive-statistics
stage: formal-systems
status: draft
---

# Mean, Median, and Mode

## Core Idea
The mean is the arithmetic average (Σx/n); the median is the middle value when data is ordered; the mode is the most frequent value. These three measures of center often differ, especially in skewed or bimodal data. The mean is sensitive to outliers, the median is robust, and the mode appears in any dataset. Choice of measure depends on the data's shape and the question being answered.

## How It's Best Learned
Compute all three for various datasets. Visualize how each changes when outliers are added. Relate each to different questions about typical values.

## Common Misconceptions
Thinking the mean must be a data value. Assuming mean = median in non-symmetric data. Confusing 'mode' with mathematical modes of functions.

## Explainer

The three measures represent three different answers to the question "what is a typical value?" The **mean** asks: if I divided all the data equally among everyone, what would each person get? Calculate it by summing all values and dividing by the count. For the dataset {2, 4, 6, 8, 10}, the mean is 30/5 = 6. The mean treats every data point as contributing equally to the total — it is a leveling device, and because every value matters to the calculation, extreme values can pull it dramatically in one direction.

The **median** asks instead: what is the value in the middle position when everything is sorted? Order the data, then find the midpoint. For {2, 4, 6, 8, 10}, the median is also 6 — the third of five values. For an even count like {2, 4, 6, 8}, the median is the average of the two middle values: (4+6)/2 = 5. Unlike the mean, the median only cares about position, not magnitude — replacing the 10 in our dataset with 10,000 leaves the median unchanged. This insensitivity to extremes makes the median **robust**.

The **mode** asks a different question entirely: what value shows up most often? In {1, 2, 2, 3, 4}, the mode is 2. A dataset can have no mode (all values unique), one mode (**unimodal**), or multiple modes (**bimodal** or **multimodal**). The mode is the only measure that makes sense for categorical data — you can find the most common shoe size or favorite color, but you cannot average them.

The real power of knowing all three is in comparison. When mean, median, and mode all agree (or nearly agree), the data is roughly symmetric. When the mean is pulled higher than the median, the data is likely **right-skewed** — a few very large values drag the mean up (think household incomes, where billionaires skew the average without moving the median). When the mean falls below the median, the data is likely **left-skewed**. This gap between mean and median is a built-in diagnostic for the shape of your distribution, available before you draw a single graph.
