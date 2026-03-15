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
