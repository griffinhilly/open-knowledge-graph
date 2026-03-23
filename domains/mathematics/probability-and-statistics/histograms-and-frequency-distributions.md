---
id: histograms-and-frequency-distributions
title: Histograms and Frequency Distributions
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: mean-median-mode
  type: soft
builds-toward:
- normal-distribution
- sampling-distributions
tags:
- histogram
- frequency
- distribution-shape
- visualization
stage: formal-systems
status: validated
---

# Histograms and Frequency Distributions

## Core Idea
A histogram displays the distribution of numerical data by dividing the range into bins and showing frequency (or density) on the y-axis. Histograms reveal the shape of a distribution: whether it is symmetric, skewed, unimodal, or multimodal. Frequency distributions can be represented as raw counts, relative frequencies (proportions), or densities (for equal-width bins). Histograms are fundamental exploratory data analysis tools that precede and inform statistical inference.

## How It's Best Learned
Create histograms from data using different bin widths. Observe how bin choice affects apparent shape. Connect histogram shapes to distributions discussed (normal, uniform, bimodal, skewed).

## Common Misconceptions
Confusing area with height in density histograms. Thinking bin width choice doesn't matter. Misinterpreting gaps in histograms as zero frequency.

## Questions

```yaml
- question: "A density histogram has two adjacent bins. Bin A has width 5 and height 0.04. Bin B has width 10 and height 0.04. Which bin contains more data?"
  type: multiple-choice
  options:
    - "Bin A, because it has the same height but is narrower, indicating more concentrated data"
    - "Both bins contain the same proportion of data because they have the same height"
    - "Bin B, because its area (10 × 0.04 = 0.40) is twice Bin A's area (5 × 0.04 = 0.20)"
    - "Cannot be determined without knowing the total sample size"
  answer: 2
  explanation: "In a density histogram, the AREA of each bar (width × height) represents the proportion of data in that bin — not the height alone. Bin A: area = 5 × 0.04 = 0.20 (20% of data). Bin B: area = 10 × 0.04 = 0.40 (40% of data). Bin B contains twice as much data despite having the same height. This is the critical insight: equal heights do NOT mean equal frequencies when bin widths differ. Density = frequency / bin width, so height is a rate, not a count."

- question: "A histogram of household incomes in a city is strongly right-skewed. Which statement best describes the relationship between the mean and median?"
  type: multiple-choice
  options:
    - "The mean equals the median, because both measure the center of the distribution"
    - "The median exceeds the mean, because more families are below average than above"
    - "The mean exceeds the median, because a few very high incomes pull the mean upward"
    - "They cannot be compared without knowing the exact distribution"
  answer: 2
  explanation: "In a right-skewed distribution, a small number of very large values drag the mean to the right of the bulk of the data. The median, which depends only on rank order, is resistant to these extreme values and better represents a 'typical' income. This is why median household income is typically reported rather than mean income — the mean is distorted by billionaires. The long right tail of income data is a classic example of right skew."

- question: "Changing the bin width of a histogram built from the same data can make the distribution appear symmetric or skewed."
  type: true-false
  answer: true
  explanation: "Bin width is a major determinant of apparent distribution shape. Too few wide bins compress variation and can mask skewness. Too many narrow bins create jagged noise that obscures the underlying shape. With intermediate bins, the same dataset can appear roughly symmetric or noticeably skewed depending on where bin boundaries fall. This is why analysts try multiple bin widths before drawing conclusions about shape. The choice of bin width is a modeling decision, not an objective fact about the data."

- question: "In a density histogram, the height of each bar represents the proportion of data values in that bin."
  type: true-false
  answer: false
  explanation: "In a density histogram, the AREA of each bar (height × width) represents the proportion, not the height alone. Height represents density (proportion per unit of measurement). This distinction only matters when bins have unequal widths — if all bins are the same width, height is proportional to area and the distinction disappears. The density scaling ensures that all bar areas sum to 1.0, making density histograms directly comparable to probability density functions."

- question: "Why does a gap in a histogram have a specific and meaningful interpretation, unlike gaps in a bar chart for categorical data?"
  type: short-answer
  answer: "A histogram represents a continuous numerical variable divided into adjacent bins covering a contiguous range. Because the bins are adjacent and cover every value in the range without overlap, a gap — a bin with zero height — means no observations fell in that interval. It is not a display artifact or a missing category; it is a real absence of data in that range. In a bar chart for categorical data, categories are unordered and bars are separated by convention, so gaps carry no information about the data. In a histogram, the spatial position of each bar on the number line is meaningful."
  explanation: "This is why histograms have touching bars (no spaces between them) while categorical bar charts typically have spaces. The touching-bar convention signals that the x-axis is continuous and that any visible gap genuinely represents a data-free interval."
```

## Explainer

You already know how to compute the mean, median, and mode of a dataset — single-number summaries of a distribution. A histogram reveals something those summaries cannot: the **shape** of the distribution. Where are values concentrated? Are they spread evenly or clumped? Does the data have one peak or two? A histogram makes these patterns visible at a glance.

To build a histogram, you divide the range of data into equal-width intervals called **bins** and count how many observations fall in each bin. You then draw a bar for each bin, with height proportional to the count (or frequency). The result is a bar chart that shows where data is dense and where it's sparse. Notice that, unlike a bar chart for categorical data, the bars in a histogram are adjacent — no gaps — because the bins cover a continuous range. A gap in a histogram genuinely means no observations in that range.

**Bin width** is a critical design choice. Too few bins and the histogram is a featureless blob that hides structure; too many bins and it becomes jagged noise where every bin has 0 or 1 observation. The right bin width shows meaningful patterns without overfitting noise. As a rule of thumb, try the square root of the sample size as the number of bins, then adjust visually. Different bin widths can make the same data look symmetric or skewed, which is why analysts often try several before settling on one.

Reading histogram **shapes** connects to the distributions you'll encounter in statistical inference. A **symmetric, bell-shaped** histogram suggests normality — the mean, median, and mode are all close together. A **right-skewed** histogram has a long tail to the right, with the mean pulled higher than the median (a few large values drag the mean up). A **left-skewed** histogram mirrors this. A **bimodal** histogram has two peaks, suggesting two subpopulations in the data. Finally, **density histograms** rescale the y-axis so that bar areas (not heights) sum to 1, making them directly comparable to probability density functions — a key bridge between exploratory data analysis and the theoretical distributions you'll encounter in inference.
