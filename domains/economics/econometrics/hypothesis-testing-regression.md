---
id: hypothesis-testing-regression
title: Hypothesis Testing in Regression
domain: economics
course: econometrics
prerequisites:
- id: coefficient-interpretation-regression
  type: hard
- id: hypothesis-testing-fundamentals
  type: hard
- id: t-test-for-means
  type: hard
- id: p-values-and-significance
  type: hard
- id: confidence-intervals-means
  type: hard
builds-toward:
- f-test-joint-significance
- r-squared-and-model-fit
tags:
- t-test
- significance
- standard-errors
- hypothesis-testing
stage: formal-systems
status: draft
---

# Hypothesis Testing in Regression

## Core Idea
In regression, each coefficient β̂ⱼ has an associated standard error se(β̂ⱼ), and the t-statistic t = (β̂ⱼ − β₀)/se(β̂ⱼ) tests whether βⱼ equals some hypothesized value (usually zero) in the population. Under the null, this t-statistic follows a t-distribution with n−k−1 degrees of freedom; for large samples it approaches the standard normal. Statistical significance at the 5% level means the p-value is below 0.05, but economic significance — whether the effect size matters practically — is a separate judgment. Confidence intervals for coefficients convey both magnitude and precision.

## How It's Best Learned
Interpret regression tables from published papers, explaining each coefficient's sign, magnitude, standard error, and significance level. Practice constructing confidence intervals manually from reported standard errors.

## Common Misconceptions
- A statistically significant coefficient may be economically trivial, especially in large samples.
- Failing to reject the null does not prove the null is true — it may reflect low power from a small sample or high variance.
