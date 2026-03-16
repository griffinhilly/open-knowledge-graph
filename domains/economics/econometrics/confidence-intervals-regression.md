---
id: confidence-intervals-regression
title: Confidence Intervals and Hypothesis Tests in Regression
domain: economics
course: econometrics
prerequisites:
- id: asymptotic-normality-regression
  type: hard
- id: hypothesis-testing-regression
  type: hard
builds-toward:
- prediction-intervals-regression
tags:
- inference
- hypothesis-testing
- intervals
stage: formal-systems
status: draft
---

# Confidence Intervals and Hypothesis Tests in Regression

## Core Idea
Confidence intervals quantify uncertainty around parameter estimates using estimated standard errors and critical values from the t-distribution; hypothesis tests evaluate whether parameters equal specific values. Both rely on asymptotic normality and require valid estimates of standard errors, accounting for any heteroskedasticity or serial correlation.

## Explainer

You already know from asymptotic normality that the OLS estimator β̂ is approximately normally distributed in large samples: (β̂ − β) / se(β̂) → N(0,1). A **confidence interval** uses this fact directly — it constructs a range around β̂ that, under repeated sampling, would contain the true β in 95% of cases (for a 95% interval). The formula is β̂ ± t* · se(β̂), where t* is the critical value from the t-distribution with n − k − 1 degrees of freedom. In large samples, t* ≈ 1.96 for 95% confidence. The interval does not mean "there is a 95% chance β is inside this range" — β is a fixed (unknown) constant, not a random variable. What varies across samples is β̂ itself.

The **t-statistic** for hypothesis testing is the same building block rearranged. To test H₀: βⱼ = c (typically c = 0, the hypothesis that variable j has no effect), compute t = (β̂ⱼ − c) / se(β̂ⱼ). Under H₀, this statistic follows an approximate t-distribution. A large absolute value of t means the estimate is many standard errors from the hypothesized value — unlikely if H₀ were true. The **p-value** converts this to a probability: it is the probability of observing a t-statistic at least as extreme as yours if H₀ were true. A p-value below your chosen significance level (commonly 0.05) leads to rejection of H₀.

The confidence interval and hypothesis test are two sides of the same coin: β̂ ± t* · se(β̂) contains exactly the values c for which a two-sided test would fail to reject H₀: βⱼ = c. If zero is inside the 95% confidence interval, the t-test at 5% significance fails to reject H₀: βⱼ = 0. If zero is outside, you reject. This duality gives you two ways to communicate the same inference — the interval conveys both significance and effect magnitude, while the test gives a clean binary decision.

The critical ingredient in all of this is se(β̂) — the estimated standard error. You know from your prerequisites that if errors are heteroskedastic or serially correlated, the classical OLS standard errors are inconsistent; they typically understate the true uncertainty, producing confidence intervals that are too narrow and t-statistics that are too large. This is why valid inference requires using **heteroskedasticity-robust** or **cluster-robust** standard errors whenever those problems are present. The formula for β̂ does not change — only the standard errors you attach to it do. Getting this right is not a technical nicety; it is the difference between inference you can trust and inference that will mislead you.
