---
id: asymptotic-normality-regression
title: Asymptotic Normality of Regression Estimators
domain: economics
course: econometrics
prerequisites:
- id: estimator-consistency-unbiasedness
  type: hard
- id: hypothesis-testing-regression
  type: hard
- id: central-limit-theorem
  type: soft
- id: convergence-in-distribution
  type: hard
builds-toward:
- confidence-intervals-regression
tags:
- asymptotic-theory
- inference
- clt
stage: formal-systems
status: draft
---

# Asymptotic Normality of Regression Estimators

## Core Idea
Under standard regularity conditions, the OLS estimator is asymptotically normally distributed around the true parameter. This central limit result enables hypothesis testing and confidence interval construction using t-statistics and F-tests, which is essential for econometric inference in practice.

## How It's Best Learned
Understand the central limit theorem for sums, then apply it to the OLS estimator written as a weighted sum of outcome variables.

## Common Misconceptions
Asymptotic normality doesn't require the errors to be normally distributed; it holds under much weaker conditions through the CLT.

## Explainer

The OLS estimator β̂ can be written as a function of the data. From your study of estimator consistency, you know that β̂ converges in probability to the true β as sample size grows — it gets close in a probabilistic sense. But for doing inference — running t-tests, constructing confidence intervals — you need more: you need to know the *shape* of the sampling distribution, not just where it's centered. Knowing the estimator is consistent tells you it lands near the right answer in large samples, but it doesn't tell you how to quantify the uncertainty around it.

This is where the **central limit theorem** enters. You know from the CLT that sums of independent random variables converge to a normal distribution as the sample grows, regardless of the underlying distribution. The OLS estimator can be written as a weighted sum of the outcome variable y_i (specifically, β̂ = β + (X'X)⁻¹X'ε). The numerator (X'ε) is a sum of terms x_i·ε_i. Under standard regularity conditions — finite variance, regressors that behave well — these terms satisfy the conditions needed for a CLT to apply.

The key result is: √n(β̂ − β) converges **in distribution** to a normal random variable, which you recognize from your prerequisite on convergence in distribution. This is what asymptotic normality means — the *standardized* estimator converges in distribution. Notice what this does and does not claim: it is an approximation valid in large samples, not an exact finite-sample statement. The normality emerges from the averaging process, not from any assumption about the shape of ε_i.

The practical payoff is enormous. Because the standardized OLS estimator is asymptotically normal, t-statistics constructed from the estimator follow approximately standard normal (or t) distributions in large samples. This validates all the hypothesis testing procedures you already know — the test statistics are only approximately valid in finite samples, with the approximation improving as n grows. The asymptotic variance of β̂ determines the standard errors, which you can estimate from the data, enabling you to compute confidence intervals and p-values without knowing the true error distribution.

Crucially, this does not require the error term ε_i to be normally distributed — the CLT does the work even when errors follow some non-normal distribution, as long as they have finite variance. This is the core correction to the misconception: standard OLS inference (t-tests, F-tests) does not assume normal errors in large samples. It assumes the CLT is operative. In small samples, where the CLT approximation may be poor, the normal-errors assumption becomes more important as a justification for exact finite-sample results. This distinction between asymptotic and exact finite-sample inference is fundamental to understanding when econometric tools are reliable.
