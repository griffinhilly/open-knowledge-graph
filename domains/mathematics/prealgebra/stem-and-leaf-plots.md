---
id: stem-and-leaf-plots
title: Stem-and-Leaf Plots
domain: mathematics
course: prealgebra
prerequisites:
- id: mean-median-mode-with-data-sets
  type: soft
- id: decimal-place-value
  type: hard
builds-toward:
- box-and-whisker-plots
- histograms-and-frequency-distributions
tags:
- statistics
- data-display
- stem-and-leaf
- visualization
stage: abstract-reasoning
status: validated
---
# Stem-and-Leaf Plots

## Core Idea
A stem-and-leaf plot organizes numerical data by splitting each value into a "stem" (all digits except the last) and a "leaf" (the last digit). For the data set {23, 25, 31, 34, 34, 38, 42}, the stems are 2, 3, 4 and the leaves are grouped accordingly: 2 | 3 5, 3 | 1 4 4 8, 4 | 2. This display preserves every individual data point while also showing the shape of the distribution — you can see clusters, gaps, and outliers at a glance. Unlike a histogram, no information is lost. Stem-and-leaf plots bridge raw data and more abstract statistical displays.

## How It's Best Learned
Start with a small data set and build the plot step by step. Emphasize ordering the leaves from least to greatest. Show how to read the plot back into the original data. Compare to a histogram to show that the stem-and-leaf plot gives the same shape but retains exact values. Practice finding the median and mode directly from the plot.

## Common Misconceptions
- Not ordering the leaves within each stem.
- Forgetting to include a key (e.g., "3 | 4 means 34").
- Confusing which digit is the stem and which is the leaf for three-digit numbers.

## Explainer

You already know how to find the mean, median, and mode of a data set by working with a list of numbers. But a list gives you no visual sense of the shape of the data — where values cluster, where gaps appear, and whether any values are unusually far from the rest. A **stem-and-leaf plot** solves this problem while keeping every original value intact. It organizes numbers into a compact display that functions like a histogram you can read exact values from.

The construction is straightforward. Take each number in your data set and split it into two parts: the **stem** (all digits except the last) and the **leaf** (the last digit). For two-digit numbers like 23, the stem is 2 and the leaf is 3. Write all the distinct stems in a column from smallest to largest. Then, next to each stem, write the corresponding leaves in order from smallest to largest. Always include a **key** — for example, "3 | 4 means 34" — because without it the reader cannot decode the plot. The vertical line separating stems from leaves is a visual reminder of where one part ends and the other begins.

Reading a stem-and-leaf plot is just as valuable as constructing one. The **median** is the middle value when all data points are listed in order — and since the leaves are already sorted, you can simply count from either end to find it. The **mode** is the leaf that appears most often within a stem (or the stem-leaf pair that repeats). You can also see the overall **shape** of the distribution: a long row of leaves on one stem means many values cluster there. A gap between stems means no values fall in that range. A single isolated leaf far from the rest is a potential **outlier**.

The stem-and-leaf plot's main advantage over a histogram is that it preserves exact data values. A histogram shows you that "6 values fall between 30 and 40," but a stem-and-leaf plot shows you those values are exactly 31, 34, 34, 38, 39, and 39. Its main disadvantage is that it works best for small-to-medium data sets — with hundreds of values, the rows of leaves become unwieldy and a histogram or box plot is more readable. As you continue to more advanced statistical displays, you'll find that each plot type makes a different tradeoff between detail and clarity.
