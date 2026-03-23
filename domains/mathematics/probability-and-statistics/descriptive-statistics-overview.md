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
status: validated
---

# Descriptive Statistics: Summarizing Data

## Core Idea
Descriptive statistics summarize a dataset using measures of center (mean, median, mode), spread (range, variance, standard deviation), and shape. These summaries provide a concise picture of the data before formal inference.

## How It's Best Learned
Calculate all measures on real datasets. Compare how different measures respond to outliers and skewed data. Use software to compute and visualize these statistics for various datasets.

## Questions

```yaml
- question: "A company reports its employees' average salary as $85,000, but a typical employee earns only $52,000. What most likely explains this gap?"
  type: multiple-choice
  options:
    - "The mean was calculated incorrectly"
    - "A few very high executive salaries pull the mean far above the median"
    - "The median is not a valid measure of center for salary data"
    - "The standard deviation is unusually low, compressing the mean"
  answer: 1
  explanation: "In right-skewed distributions like income, a small number of very large values pull the mean upward while the median stays near the bulk of the data. $85,000 is the mean (sensitive to extreme values); $52,000 is the median (resistant). This divergence is a diagnostic signal that the distribution is skewed, and the median better represents a typical employee's salary."

- question: "A dataset of 10 values has a mean of 50 and a standard deviation of 3. One additional value of 500 is added. What happens?"
  type: multiple-choice
  options:
    - "Both the mean and median increase substantially"
    - "The mean increases substantially, but the median increases only slightly"
    - "The median increases substantially, but the mean increases only slightly"
    - "Neither the mean nor median changes because 500 is an outlier and is excluded"
  answer: 1
  explanation: "The mean is the balance point of all values, so the extreme outlier of 500 dramatically pulls it upward. The median, however, is determined only by rank order — adding one large value shifts the middle position by at most one spot, causing a minor change. This illustrates the key contrast: mean is sensitive to outliers, median is resistant. Option D is wrong — outliers are not automatically excluded from standard calculations."

- question: "For a strongly right-skewed distribution, the mean is typically greater than the median."
  type: true-false
  answer: true
  explanation: "In a right-skewed distribution, the long tail stretches toward high values. Those extreme values pull the mean — which balances all observations — upward toward the tail. The median is determined only by rank order and is resistant to extreme values, so it stays closer to the bulk of the data. The rule of thumb: mean > median signals right skew; mean < median signals left skew."

- question: "Dividing by n (rather than n − 1) when computing sample variance gives an unbiased estimate of the population variance."
  type: true-false
  answer: false
  explanation: "Dividing by n produces a biased estimator that systematically underestimates population variance. This happens because the sample mean x̄ is computed from the same data, causing the sum of squared deviations to be slightly smaller than it would be around the true population mean μ. Dividing by n − 1 (Bessel's correction) compensates for this bias. Division by n is appropriate only when computing variance for a complete population, not a sample."

- question: "Why is the standard deviation preferred over the variance as a reported measure of spread, and what does a 'large' standard deviation actually mean?"
  type: short-answer
  answer: "Standard deviation is the square root of variance, which restores the original units of measurement. Variance is in squared units (e.g., dollars² for income data), making it hard to interpret directly. A 'large' standard deviation means observations are widely dispersed around the mean; a 'small' one means they cluster tightly. Whether a standard deviation is 'large' is always context-dependent — a SD of 5 is large if the mean is 10, but negligible if the mean is 10,000."
  explanation: "This targets practical understanding: statistics are tools for communication, and units matter. The transition from variance to standard deviation is not cosmetic — it is what makes the number interpretable in the domain's original units. The follow-up about 'large' targets the common error of evaluating spread in isolation from the scale of the data."
```

## Explainer

Statistics begins with a basic problem: you have a collection of numbers — test scores, temperatures, incomes, reaction times — and you need to communicate something useful about that collection without listing every value. **Descriptive statistics** are the vocabulary for this compression. The goal is to capture the most important features of a distribution using just a few numbers: where is the center, how spread out are the values, and what shape does the distribution take?

**Measures of center** answer "what's a typical value?" The **mean** (average) is the sum of all values divided by the count — it balances the distribution like a fulcrum, in the sense that the signed deviations above and below it sum to zero. The **median** is the middle value when all observations are sorted; exactly half the data falls above it and half below. The **mode** is the most frequently occurring value, most useful for categorical data or discrete distributions with a clear peak. For symmetric, bell-shaped data these three coincide. For skewed data they diverge: if a few very high incomes pull the mean rightward while most people earn modest amounts, the median is a more representative "typical" income. The choice of center measure depends on whether you want sensitivity to extreme values (mean) or resistance to them (median).

**Measures of spread** answer "how variable are the values?" The **range** (max minus min) is intuitive but highly sensitive to outliers — one extreme value can make a tight dataset look wildly dispersed. The **variance** averages the squared deviations from the mean: s² = Σ(xᵢ − x̄)² / (n − 1). Squaring ensures positive and negative deviations don't cancel, and also amplifies large deviations, making variance sensitive to outliers too. The **standard deviation** s is the square root of variance, restoring the original units and making it interpretable: a dataset with mean 50 and standard deviation 5 has most observations clustered near the mean, while one with standard deviation 20 is far more dispersed. The division by n − 1 (rather than n) produces an **unbiased estimator** of the population variance — a correction for the fact that using the sample mean x̄ slightly underestimates the true spread.

Shape is the third dimension of a distribution's summary. A **symmetric** distribution has roughly matching tails on both sides and mean ≈ median. A **right-skewed** distribution has a long tail stretching toward high values — the mean is pulled above the median by a few large observations. A **left-skewed** distribution tails toward low values. **Outliers** — observations far from the bulk — are visible in histograms and boxplots and disproportionately affect the mean and standard deviation while leaving the median and interquartile range nearly unchanged. Comparing mean and median gives a quick diagnostic: when they diverge substantially, something asymmetric is shaping the data. Descriptive statistics do not test hypotheses or make inferences about populations — that is inferential statistics — but they are always the first step: understand what your data look like before drawing any conclusions from them.
