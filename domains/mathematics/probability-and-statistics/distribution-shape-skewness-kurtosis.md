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

## Explainer

From your study of descriptive statistics, you know that a distribution can be summarized by its center (mean, median) and spread (standard deviation, IQR). But two distributions can have identical means and variances and still look completely different. **Skewness** and **kurtosis** are the shape descriptors that capture what the mean and standard deviation miss — asymmetry and tail behavior.

**Skewness** measures how far a distribution departs from left-right symmetry. The key is to think about which tail is longer, not where the peak sits. A distribution is **positively skewed** (right-skewed) when the right tail stretches further than the left — think of income distributions, where most people earn moderate amounts but a small number earn extremely high incomes. A distribution is **negatively skewed** (left-skewed) when the left tail is longer — think of scores on an easy exam, where most people score high but a few score very low. The practical test: in a right-skewed distribution, the mean is pulled up by the extreme high values and sits above the median, which sits above the mode. In a left-skewed distribution, the order reverses. Your knowledge of quantiles is directly useful here — the relative positions of the median (50th percentile), mean, and mode reveal the direction of skew.

**Kurtosis** measures how heavy the tails of a distribution are compared to a normal distribution. High kurtosis (**leptokurtic**) means more data in the tails and a sharper peak — think of financial returns, which often exhibit more extreme events than a normal distribution would predict. Low kurtosis (**platykurtic**) means thinner tails and a flatter, more spread-out peak. The normal distribution has kurtosis of 3, so many formulas report **excess kurtosis** = kurtosis − 3, making the normal the reference point at zero. A common misconception is that kurtosis measures peakedness — it actually primarily measures tail weight, and the visual appearance of the peak is a secondary effect.

These two measures matter in practice because most classical statistical methods (t-tests, ANOVA, linear regression) assume the data or errors are approximately normally distributed — symmetric, with thin tails. When your data is strongly skewed, the mean is a misleading summary and variance-based methods lose their justification. When your data has heavy tails (high kurtosis), rare extreme events occur far more often than the normal model predicts, which can invalidate confidence intervals and p-values. Checking skewness and kurtosis histograms before choosing an analysis method is part of responsible data exploration — it tells you how far from normality your data sits and whether transformations (like log or square root) might bring it into better shape.
