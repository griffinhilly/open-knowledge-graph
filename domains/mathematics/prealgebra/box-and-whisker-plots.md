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

## Questions

```yaml
- question: "Two classes took the same test. Class A's box plot has a median of 75, Q1 = 65, Q3 = 85, with a long whisker extending to 40 on the left. Class B's box plot has a median of 78, Q1 = 72, Q3 = 84. What can you conclude?"
  type: multiple-choice
  options:
    - "Class A has more students who scored below 65 than Class B does"
    - "Class A's distribution is more spread out in the lower half than Class B's, but about 25% of Class A scored between 40 and 65"
    - "The long left whisker in Class A means more students scored low than in Class B"
    - "Class B performed better because its median is higher"
  answer: 1
  explanation: "The long left whisker of Class A indicates spread, not count. Approximately 25% of Class A's students scored between the minimum (40) and Q1 (65) — that's the same proportion as any other quartile section. The whisker is long because those scores are spread across a wide range (40 to 65), not because more students scored there. Class B's narrow IQR (72 to 84) means the middle 50% are tightly clustered. The medians are close (75 vs 78), so option D oversimplifies."

- question: "A data set has Q1 = 50 and Q3 = 80. What does the IQR of 30 tell you?"
  type: multiple-choice
  options:
    - "The range of the entire data set is 30"
    - "The middle 50% of the data values fall within a 30-unit span"
    - "The average value in the data set is around 65"
    - "There are 30 data values between Q1 and Q3"
  answer: 1
  explanation: "The IQR (Q3 − Q1 = 80 − 50 = 30) measures the spread of the middle 50% of the data — it is the width of the box. It tells you nothing about the number of data points in that range (each quartile always contains about 25% of the data regardless of IQR width) and nothing about the mean (option C) or total range (option A). A wide IQR means the middle half is spread out; a narrow IQR means it is tightly clustered."

- question: "In a box-and-whisker plot, a longer whisker on one side means there are more data points in that region than in a shorter whisker region."
  type: true-false
  answer: false
  explanation: "This is the most common misconception about box plots. Each section of a box plot — including each whisker — contains approximately 25% of the data values, regardless of its length. A long whisker means the data in that quartile is spread across a wider range of values; a short whisker means those same 25% of values are clustered close together. Length signals spread, not frequency."

- question: "Each of the four sections of a box plot (min to Q1, Q1 to median, median to Q3, Q3 to max) contains approximately 25% of the data values, regardless of how wide each section appears."
  type: true-false
  answer: true
  explanation: "This is the foundational principle that makes box plots useful: quartiles divide the data into four equal-frequency groups. By definition, Q1 is the value below which 25% of data falls, Q2 (median) is the midpoint, and Q3 is the value below which 75% falls. So each of the four sections contains about 25% of values. The visual widths of those sections reflect how spread out the values are, not how many values are in each section."

- question: "A box plot shows the median line very close to Q3 (the right side of the box), with Q1 much farther to the left. What does this reveal about the shape of the distribution?"
  type: short-answer
  answer: "When the median sits close to Q3, the middle half of the data is clustered near the upper end of the box. This means the data is left-skewed (negatively skewed): there is a long tail on the lower end, with most values concentrated toward the higher end of the range. The asymmetric position of the median within the box is the key visual signal — a centered median suggests a symmetric distribution, while a median shifted toward one quartile suggests skewness in the opposite direction."
  explanation: "Reading skewness from a box plot is one of its most practical applications. A histogram shows shape more clearly for a single data set, but a box plot enables fast comparison of skewness across multiple groups on the same scale. If Class A has a median near Q3 and Class B has a centered median, you immediately know Class A's scores are more concentrated at the high end while Class B's are more symmetric — insights that a simple comparison of means would miss."
```

## Explainer

You already know how to find the mean, median, and mode of a data set. A box-and-whisker plot turns five specific values — the minimum, three quartiles, and maximum — into a compact picture of the entire distribution. Once you learn to read it, a single glance tells you more about a data set than any list of numbers can.

Start by ordering the data and locating the **median** (Q2): the middle value. This is the center line of the box. Then split the data in half: the lower half is everything below the median, and the upper half is everything above. The **first quartile** Q1 is the median of the lower half, and the **third quartile** Q3 is the median of the upper half. The box spans from Q1 to Q3, capturing the middle 50% of the data. This span is the **interquartile range** (IQR = Q3 − Q1), a measure of spread that is robust to extreme values — outliers affect the mean but not the quartiles. The whiskers extend out to the minimum and maximum, showing the full range of the data.

Reading a box plot means asking three questions. First, where is the center? The median line's position in the box tells you whether the middle of the data is symmetric (line near center of box), or skewed (line toward one side). Second, how spread out is the data? A wide box means the middle 50% of values covers a large range; a narrow box means they're tightly clustered. Long whiskers indicate extreme values at the tails. Third, is there asymmetry? If one whisker is much longer than the other, or if the median line is off-center in the box, the distribution is skewed in that direction.

The most useful application is comparison. Place two or more box plots side by side on the same scale and you can immediately compare medians, spreads, and shapes. For example, comparing test scores from two classes: if Class A's box sits entirely above Class B's median, then at least half of Class A outperformed the typical Class B student. The box plot makes this visible instantly, in a way that comparing means alone would not. This visual power — seeing the shape and spread of the distribution, not just a single summary number — is exactly why box plots build toward more advanced measures of spread and distributional analysis.
