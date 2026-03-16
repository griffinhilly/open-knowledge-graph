---
id: descriptive-statistics-overview
title: 'Descriptive Statistics: Summarizing Data'
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: categorical-vs-quantitative-data
  type: soft
builds-toward:
- quantiles-and-percentiles
- distribution-shape-skewness-kurtosis
tags:
- descriptive-statistics
- data-summary
stage: formal-systems
status: draft
---

# Descriptive Statistics: Summarizing Data

## Core Idea
Descriptive statistics summarize a dataset using measures of center (mean, median, mode), spread (range, variance, standard deviation), and shape. These summaries provide a concise picture of the data before formal inference.

## How It's Best Learned
Calculate all measures on real datasets. Compare how different measures respond to outliers and skewed data. Use software to compute and visualize these statistics for various datasets.

## Explainer

Statistics begins with a basic problem: you have a collection of numbers — test scores, temperatures, incomes, reaction times — and you need to communicate something useful about that collection without listing every value. **Descriptive statistics** are the vocabulary for this compression. The goal is to capture the most important features of a distribution using just a few numbers: where is the center, how spread out are the values, and what shape does the distribution take?

**Measures of center** answer "what's a typical value?" The **mean** (average) is the sum of all values divided by the count — it balances the distribution like a fulcrum, in the sense that the signed deviations above and below it sum to zero. The **median** is the middle value when all observations are sorted; exactly half the data falls above it and half below. The **mode** is the most frequently occurring value, most useful for categorical data or discrete distributions with a clear peak. For symmetric, bell-shaped data these three coincide. For skewed data they diverge: if a few very high incomes pull the mean rightward while most people earn modest amounts, the median is a more representative "typical" income. The choice of center measure depends on whether you want sensitivity to extreme values (mean) or resistance to them (median).

**Measures of spread** answer "how variable are the values?" The **range** (max minus min) is intuitive but highly sensitive to outliers — one extreme value can make a tight dataset look wildly dispersed. The **variance** averages the squared deviations from the mean: s² = Σ(xᵢ − x̄)² / (n − 1). Squaring ensures positive and negative deviations don't cancel, and also amplifies large deviations, making variance sensitive to outliers too. The **standard deviation** s is the square root of variance, restoring the original units and making it interpretable: a dataset with mean 50 and standard deviation 5 has most observations clustered near the mean, while one with standard deviation 20 is far more dispersed. The division by n − 1 (rather than n) produces an **unbiased estimator** of the population variance — a correction for the fact that using the sample mean x̄ slightly underestimates the true spread.

Shape is the third dimension of a distribution's summary. A **symmetric** distribution has roughly matching tails on both sides and mean ≈ median. A **right-skewed** distribution has a long tail stretching toward high values — the mean is pulled above the median by a few large observations. A **left-skewed** distribution tails toward low values. **Outliers** — observations far from the bulk — are visible in histograms and boxplots and disproportionately affect the mean and standard deviation while leaving the median and interquartile range nearly unchanged. Comparing mean and median gives a quick diagnostic: when they diverge substantially, something asymmetric is shaping the data. Descriptive statistics do not test hypotheses or make inferences about populations — that is inferential statistics — but they are always the first step: understand what your data look like before drawing any conclusions from them.
