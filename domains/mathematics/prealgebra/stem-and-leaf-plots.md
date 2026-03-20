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

## Questions

```yaml
- question: "A data set contains the values {12, 15, 21, 22, 28, 34}. What does the row for stem '2' look like in a correctly constructed stem-and-leaf plot?"
  type: multiple-choice
  options:
    - "2 | 1 2 8"
    - "2 | 8 2 1"
    - "2 | 21 22 28"
    - "2 | 1 1 2 8"
  answer: 0
  explanation: "For two-digit numbers, the stem is the tens digit and the leaf is the units digit. The values 21, 22, and 28 all have stem 2 and leaves 1, 2, and 8 respectively. Leaves must be written in ascending order — so '2 | 1 2 8' is correct. Option B has unordered leaves (a common error). Option C writes full values rather than just the leaf digits. Option D duplicates the leaf '1' incorrectly."

- question: "What is the key advantage of a stem-and-leaf plot over a histogram displaying the same data?"
  type: multiple-choice
  options:
    - "It is easier to construct for data sets with hundreds of values"
    - "It reveals the exact value of every individual data point, not just a count by interval"
    - "It displays the mean more clearly than a histogram"
    - "It eliminates the need to sort data before analysis"
  answer: 1
  explanation: "A histogram shows how many values fall within each interval (e.g., '6 values between 30 and 40') but discards the exact values. A stem-and-leaf plot shows that those 6 values are, say, 31, 34, 34, 38, 39, and 39 — you can reconstruct the original data set from the plot. This is the defining feature. The tradeoff is that stem-and-leaf plots become unwieldy with very large data sets, where histograms are more readable."

- question: "In a stem-and-leaf plot of two-digit numbers, reading a stem and any one of its leaves together always recovers an original data value."
  type: true-false
  answer: true
  explanation: "This is precisely what makes stem-and-leaf plots unique. The stem holds all digits except the last, and the leaf is the last digit — so stem 3 and leaf 7 means 37. Unlike a histogram, which groups values into intervals and loses the original numbers, a stem-and-leaf plot is reversible: every entry can be decoded back to the exact data point."

- question: "A data set contains both 43 and 34. Because these values use the same two digits, they would appear in the same row of a stem-and-leaf plot."
  type: true-false
  answer: false
  explanation: "The stem is determined by all digits except the last, which for two-digit numbers is the tens digit. The value 43 has stem 4 and leaf 3; the value 34 has stem 3 and leaf 4. They appear in different rows. This is a common confusion — it is the position of digits, not the set of digits, that determines placement. The key (e.g., '3 | 4 means 34') makes this explicit."

- question: "A classmate constructs a stem-and-leaf plot but forgets to include a key. Explain why the key is essential, and give an example of the ambiguity that results without it."
  type: short-answer
  answer: "Without a key, a reader cannot determine what the stem and leaf values represent. For example, a stem of '1' and a leaf of '5' could mean 15, 150, 1.5, or 105 depending on the scale of the data. The key (e.g., '1 | 5 means 15') tells the reader exactly how to combine stem and leaf to recover the original value. Without it, the plot looks the same for data measured in ones, tens, or decimals."
  explanation: "The key is not optional decoration — it is the decoder ring for the entire display. This matters most when the data involves decimals (stem '3' leaf '2' means 3.2, not 32) or three-digit numbers (stem '12' leaf '4' means 124). Even for simple two-digit integers, without a key a reader is guessing the scale."
```

## Explainer

You already know how to find the mean, median, and mode of a data set by working with a list of numbers. But a list gives you no visual sense of the shape of the data — where values cluster, where gaps appear, and whether any values are unusually far from the rest. A **stem-and-leaf plot** solves this problem while keeping every original value intact. It organizes numbers into a compact display that functions like a histogram you can read exact values from.

The construction is straightforward. Take each number in your data set and split it into two parts: the **stem** (all digits except the last) and the **leaf** (the last digit). For two-digit numbers like 23, the stem is 2 and the leaf is 3. Write all the distinct stems in a column from smallest to largest. Then, next to each stem, write the corresponding leaves in order from smallest to largest. Always include a **key** — for example, "3 | 4 means 34" — because without it the reader cannot decode the plot. The vertical line separating stems from leaves is a visual reminder of where one part ends and the other begins.

Reading a stem-and-leaf plot is just as valuable as constructing one. The **median** is the middle value when all data points are listed in order — and since the leaves are already sorted, you can simply count from either end to find it. The **mode** is the leaf that appears most often within a stem (or the stem-leaf pair that repeats). You can also see the overall **shape** of the distribution: a long row of leaves on one stem means many values cluster there. A gap between stems means no values fall in that range. A single isolated leaf far from the rest is a potential **outlier**.

The stem-and-leaf plot's main advantage over a histogram is that it preserves exact data values. A histogram shows you that "6 values fall between 30 and 40," but a stem-and-leaf plot shows you those values are exactly 31, 34, 34, 38, 39, and 39. Its main disadvantage is that it works best for small-to-medium data sets — with hundreds of values, the rows of leaves become unwieldy and a histogram or box plot is more readable. As you continue to more advanced statistical displays, you'll find that each plot type makes a different tradeoff between detail and clarity.
