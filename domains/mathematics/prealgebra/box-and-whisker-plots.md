---
id: box-and-whisker-plots
title: Box-and-Whisker Plots
domain: mathematics
course: prealgebra
prerequisites:
- id: mean-median-mode-with-data-sets
  type: hard
- id: stem-and-leaf-plots
  type: soft
builds-toward:
- measures-of-spread
tags:
- statistics
- box-plot
- quartiles
- data-display
stage: abstract-reasoning
status: validated
---
# Box-and-Whisker Plots

## Core Idea
A box-and-whisker plot (box plot) displays a data set using five key values: the minimum, first quartile (Q1), median (Q2), third quartile (Q3), and maximum. The "box" spans from Q1 to Q3 (the interquartile range, or IQR), with a line at the median. The "whiskers" extend to the minimum and maximum. This display shows the spread, center, and symmetry of data at a glance and is especially useful for comparing multiple data sets side by side. It introduces quartiles and the IQR, which are foundational concepts in statistics.

## How It's Best Learned
Start by ordering a data set and finding the median. Then find the median of each half (Q1 and Q3). Draw the plot step by step on a number line. Compare two data sets using side-by-side box plots. Discuss what a wide box vs. a narrow box means (more vs. less spread in the middle 50%). Connect to real data (sports statistics, test scores) for engagement.

## Common Misconceptions
- Thinking the longer whisker means more data points are in that region (it means the data is more spread out, not more numerous).
- Confusing the median with the mean — the line in the box is the median.
- Including the median value in both halves when finding Q1 and Q3 (conventions vary; be explicit about which method you use).
- Thinking equal-sized box sections mean equal numbers of data points (each section contains about 25% of the data, regardless of width).

## Explainer

You already know how to find the mean, median, and mode of a data set. A box-and-whisker plot turns five specific values — the minimum, three quartiles, and maximum — into a compact picture of the entire distribution. Once you learn to read it, a single glance tells you more about a data set than any list of numbers can.

Start by ordering the data and locating the **median** (Q2): the middle value. This is the center line of the box. Then split the data in half: the lower half is everything below the median, and the upper half is everything above. The **first quartile** Q1 is the median of the lower half, and the **third quartile** Q3 is the median of the upper half. The box spans from Q1 to Q3, capturing the middle 50% of the data. This span is the **interquartile range** (IQR = Q3 − Q1), a measure of spread that is robust to extreme values — outliers affect the mean but not the quartiles. The whiskers extend out to the minimum and maximum, showing the full range of the data.

Reading a box plot means asking three questions. First, where is the center? The median line's position in the box tells you whether the middle of the data is symmetric (line near center of box), or skewed (line toward one side). Second, how spread out is the data? A wide box means the middle 50% of values covers a large range; a narrow box means they're tightly clustered. Long whiskers indicate extreme values at the tails. Third, is there asymmetry? If one whisker is much longer than the other, or if the median line is off-center in the box, the distribution is skewed in that direction.

The most useful application is comparison. Place two or more box plots side by side on the same scale and you can immediately compare medians, spreads, and shapes. For example, comparing test scores from two classes: if Class A's box sits entirely above Class B's median, then at least half of Class A outperformed the typical Class B student. The box plot makes this visible instantly, in a way that comparing means alone would not. This visual power — seeing the shape and spread of the distribution, not just a single summary number — is exactly why box plots build toward more advanced measures of spread and distributional analysis.
