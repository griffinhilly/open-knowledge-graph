---
id: quantile-regression-econometrics
title: Quantile Regression and Distributional Effects
domain: economics
course: econometrics
prerequisites:
- id: multiple-regression-model
  type: hard
- id: maximum-likelihood-econometrics
  type: soft
tags:
- quantile-regression
- distributional
- robust
stage: formal-systems
status: draft
---

# Quantile Regression and Distributional Effects

## Core Idea
Quantile regression estimates the effect of X on different quantiles (median, 25th percentile, etc.) of the conditional distribution of Y. It reveals whether relationships differ across the distribution and is robust to outliers.

## Explainer

The multiple regression model you already know estimates the **conditional mean** of Y given X — it answers: what is the average outcome for people with this set of characteristics? That is often the right question, but sometimes the mean is not the most interesting or informative part of the story. Suppose you are studying the effect of education on wages. OLS tells you the average wage return per year of schooling. But what if education raises the floor of the wage distribution much more than the ceiling? Or the opposite — what if advanced education only pays off for those who already have high earning potential? OLS cannot see this; quantile regression can.

**Quantile regression** estimates how X relates to a specific point in the conditional distribution of Y, not just the center. The **median regression** (the 50th percentile) minimizes the sum of absolute deviations instead of squared deviations, which is what makes it more robust to outliers than OLS — a handful of extreme Y values pulls the mean hard but moves the median only a little. For other quantiles (25th, 75th, 90th), the estimator minimizes an asymmetric loss function called the **check function** that penalizes under-prediction and over-prediction at different rates depending on which quantile is targeted.

The economic content of quantile regression results is richer than OLS. If you run the wage-education regression at the 10th, 50th, and 90th percentiles and find increasing coefficients (say 4%, 8%, 15%), this tells you education has a much larger effect at the top of the conditional wage distribution than at the bottom — an important finding about inequality that OLS would obscure by averaging across quantiles. Conversely, if the coefficients are similar across quantiles, the distributional effects are homogeneous and OLS captures the full story.

An important clarification: quantile regression estimates the effect of X on a **conditional quantile**, not an unconditional one. The 75th percentile in a quantile regression of wages on education is the 75th percentile of wages *given* that level of education — it is not necessarily the 75th percentile of the overall wage distribution. This distinction matters when interpreting policy implications. Quantile regression is best understood as a complement to OLS, not a replacement: use both to see whether the story is the same across the distribution or whether the mean is masking important heterogeneity.
