---
id: distribution-shape-skewness-kurtosis
title: 'Distribution Shape: Skewness and Kurtosis'
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: quantiles-and-percentiles
  type: soft
- id: descriptive-statistics-overview
  type: soft
builds-toward:
- normal-distribution-intro
tags:
- distribution-shape
- descriptive-statistics
stage: formal-systems
status: draft
---

# Distribution Shape: Skewness and Kurtosis

## Core Idea
Skewness measures asymmetry in a distribution: positive skew has a long right tail, negative skew has a long left tail. Kurtosis measures tail heaviness or peakedness. These concepts help identify when data deviates from symmetry.

## How It's Best Learned
Examine histograms and identify visual skewness and kurtosis. Calculate sample skewness and kurtosis. Compare skewed and symmetric distributions side-by-side.

## Common Misconceptions
Thinking skewness measures departure from normality (it measures asymmetry specifically). Confusing positive skew direction (right tail, not left). Using sample skewness as a formal test for normality without appropriate context.

## Questions

```yaml
- question: "A dataset of household incomes shows mean = $85,000 and median = $60,000. Which best describes the shape of this distribution?"
  type: multiple-choice
  options:
    - "Symmetric — mean and median are both valid measures of center"
    - "Negatively skewed — the median is lower than the mean"
    - "Positively skewed — extreme high incomes pull the mean above the median"
    - "Leptokurtic — the gap between mean and median indicates heavy tails"
  answer: 2
  explanation: "When extreme high values pull the mean above the median, the distribution is positively skewed (right-skewed) — the long tail stretches rightward. Income is a classic example: most households earn moderate amounts, but a small number of very high earners pull the mean upward while the median stays near the typical value. Option B names the relationship correctly (median < mean) but labels it backwards — that ordering IS positive skew. Option D confuses skewness with kurtosis."

- question: "Kurtosis primarily measures which property of a distribution?"
  type: multiple-choice
  options:
    - "The degree of asymmetry — how far the peak is shifted left or right"
    - "How peaked the distribution is — the height of the central peak"
    - "The heaviness of the tails — how often extreme values occur"
    - "The spread of the distribution relative to its mean"
  answer: 2
  explanation: "Kurtosis measures tail weight — how much of the distribution's variance comes from extreme values, relative to a normal distribution. High kurtosis (leptokurtic) means heavier tails and more frequent extreme events, not necessarily a taller peak. The 'peakedness' interpretation is the most common misconception. Asymmetry is measured by skewness, not kurtosis. Spread is measured by standard deviation or IQR."

- question: "In a positively skewed distribution, the mean is greater than the median."
  type: true-false
  answer: true
  explanation: "Positive skew means a long right tail — a few extreme high values. These extreme values drag the mean upward (since the mean uses all values) while the median (the middle value) is much less affected. The result is mean > median > mode in a right-skewed distribution. This relationship between mean and median is one of the most reliable practical indicators of skew direction when examining summary statistics."

- question: "A leptokurtic distribution (high kurtosis) is characterized primarily by a tall, narrow peak at the center."
  type: true-false
  answer: false
  explanation: "Kurtosis primarily measures tail heaviness, not peak height. A leptokurtic distribution has heavier tails than a normal distribution — extreme events occur more frequently than the normal model predicts. The central peak may appear taller as a visual consequence (since probability mass shifted to the tails must come from somewhere), but this is secondary. Financial return distributions are leptokurtic because they produce more crashes and booms than a normal distribution would predict, which is a statement about tails, not peaks."

- question: "Why do the mean and standard deviation alone fail to fully describe a distribution, and what do skewness and kurtosis add?"
  type: short-answer
  answer: "Two distributions can have identical means and variances but completely different shapes. Skewness captures asymmetry — which tail is longer and by how much — which determines whether the mean is a reliable center summary. Kurtosis captures tail heaviness — how often extreme values occur — which determines whether variance-based methods like t-tests and confidence intervals are reliable. Together they reveal shape characteristics that determine whether standard statistical tools are appropriate for the data."
  explanation: "This is the practical motivation for shape descriptors: before applying any parametric method, you need to know not just where the distribution is centered and how spread out it is, but whether it is symmetric and whether its tails are well-behaved. Strong skewness may call for a median-based analysis or a log transformation; high kurtosis may invalidate p-values computed under the normal assumption."
```

## Explainer

From your study of descriptive statistics, you know that a distribution can be summarized by its center (mean, median) and spread (standard deviation, IQR). But two distributions can have identical means and variances and still look completely different. **Skewness** and **kurtosis** are the shape descriptors that capture what the mean and standard deviation miss — asymmetry and tail behavior.

**Skewness** measures how far a distribution departs from left-right symmetry. The key is to think about which tail is longer, not where the peak sits. A distribution is **positively skewed** (right-skewed) when the right tail stretches further than the left — think of income distributions, where most people earn moderate amounts but a small number earn extremely high incomes. A distribution is **negatively skewed** (left-skewed) when the left tail is longer — think of scores on an easy exam, where most people score high but a few score very low. The practical test: in a right-skewed distribution, the mean is pulled up by the extreme high values and sits above the median, which sits above the mode. In a left-skewed distribution, the order reverses. Your knowledge of quantiles is directly useful here — the relative positions of the median (50th percentile), mean, and mode reveal the direction of skew.

**Kurtosis** measures how heavy the tails of a distribution are compared to a normal distribution. High kurtosis (**leptokurtic**) means more data in the tails and a sharper peak — think of financial returns, which often exhibit more extreme events than a normal distribution would predict. Low kurtosis (**platykurtic**) means thinner tails and a flatter, more spread-out peak. The normal distribution has kurtosis of 3, so many formulas report **excess kurtosis** = kurtosis − 3, making the normal the reference point at zero. A common misconception is that kurtosis measures peakedness — it actually primarily measures tail weight, and the visual appearance of the peak is a secondary effect.

These two measures matter in practice because most classical statistical methods (t-tests, ANOVA, linear regression) assume the data or errors are approximately normally distributed — symmetric, with thin tails. When your data is strongly skewed, the mean is a misleading summary and variance-based methods lose their justification. When your data has heavy tails (high kurtosis), rare extreme events occur far more often than the normal model predicts, which can invalidate confidence intervals and p-values. Checking skewness and kurtosis histograms before choosing an analysis method is part of responsible data exploration — it tells you how far from normality your data sits and whether transformations (like log or square root) might bring it into better shape.
