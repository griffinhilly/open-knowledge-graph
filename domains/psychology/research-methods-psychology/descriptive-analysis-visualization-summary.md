---
id: descriptive-analysis-visualization-summary
title: Descriptive Statistics and Data Visualization
domain: psychology
course: research-methods-psychology
prerequisites:
- id: data-preparation-screening-quality
  type: hard
- id: normal-distribution
  type: soft
builds-toward:
- statistical-inference-significance-testing
tags:
- descriptive-statistics
- visualization
- summary-statistics
- data-presentation
stage: formal-systems
status: draft
---

# Descriptive Statistics and Data Visualization

## Core Idea
Descriptive statistics (means, medians, standard deviations, percentiles) summarize data; visualizations (histograms, boxplots, scatterplots) reveal distributions and relationships. Appropriate summary and visual selection depends on data type and research question. Good graphics are clear, accurate, and accessible; they reveal patterns without distorting them.

## How It's Best Learned
Calculate and report descriptive statistics for a dataset. Create multiple visualizations of the same data and evaluate which best communicates the findings. Critique published figures for clarity, accuracy, and appropriateness.

## Common Misconceptions
- Descriptive statistics only matter in exploratory phases; - All distributions are normal; - Outliers always warrant summary-independent statistics; - Visual appeal is more important than accuracy.

## Explainer

After cleaning and screening your data — the prerequisite step — you face a deceptively simple question: *what does this data actually look like?* Descriptive statistics and visualizations are the tools for answering that question, and they matter at every stage of analysis, not just at the beginning. A single mean and standard deviation rarely tells the whole story; the goal is to understand the distribution as a whole before reaching for inferential tests.

**Central tendency** and **spread** are the two core dimensions of any numerical summary. The mean is the balance point of a distribution — mathematically convenient and sensitive to all values. The median is the middle value — robust to outliers and skew. Your prerequisite on the normal distribution gives you the key insight: for a perfectly symmetric, bell-shaped distribution, the mean and median coincide. The moment they diverge, you are looking at skew, and that matters for choosing your summary. Income distributions, reaction times, and many real psychological variables are right-skewed — a small number of extreme high values pulls the mean upward, making it a misleading "typical value." In those cases, the median is more informative. The **standard deviation** (and its square, variance) quantifies spread around the mean; the **interquartile range** does the same for the median. Match your spread statistic to your central tendency statistic.

The right visualization depends on what you want to reveal and what type of data you have. A **histogram** shows the shape of a continuous distribution — whether it is symmetric, skewed, bimodal, or has fat tails. A **boxplot** compresses the same information into five numbers (minimum, Q1, median, Q3, maximum) and makes outliers visible as individual points; it is especially useful for comparing multiple groups side by side. A **scatterplot** reveals the relationship between two continuous variables — direction, strength, linearity, and the presence of clusters or outliers. Bar charts summarize categorical data. Each type reveals something different, which is why the same dataset often deserves multiple visualizations.

Good data graphics have one job: reveal the data honestly. Edward Tufte's concept of **data-ink ratio** captures this — every visual element should carry information, and anything that doesn't should be removed (unnecessary gridlines, decorative 3D effects, gradient fills). Misleading graphics typically distort through truncated axes, inappropriate scale, or cherry-picked comparisons. The criterion for a good graph is not whether it looks professional; it is whether a reader who did not collect the data can understand exactly what was measured, what was found, and what the uncertainty is. That standard — clarity, accuracy, accessibility — is what makes visualization a scientific activity rather than a design exercise.


