---
id: standard-error-of-estimators
title: Standard Error of Estimators
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: sampling-distributions
  type: hard
builds-toward:
- confidence-intervals-framework
- hypothesis-test-framework
tags:
- estimation
- inference
- standard-error
stage: formal-systems
status: draft
---

# Standard Error of Estimators

## Core Idea
The standard error is the standard deviation of an estimator's sampling distribution. It quantifies the variability of estimates across samples. For the sample mean from N(μ,σ²): SE = σ/√n. Smaller SE indicates more precise estimation.

## Explainer

From your study of sampling distributions, you know that an estimator like the sample mean x̄ is not a fixed number — it is a random variable that takes a different value in each possible sample. The **standard error** (SE) is simply the standard deviation of that sampling distribution. It measures how spread out the estimator's values are across all possible samples of size n drawn from the same population.

For the sample mean from a population with standard deviation σ, the standard error is SE(x̄) = σ/√n. This follows directly from basic variance rules: Var(x̄) = Var((X₁+...+Xn)/n) = nσ²/n² = σ²/n, so the standard deviation is σ/√n. The key insight is the √n denominator: with more observations, the sample mean varies less because random errors partially cancel. As n grows, estimates cluster tighter and tighter around the true parameter value.

Different estimators have different standard errors. The sample proportion p̂ has SE = √(p(1-p)/n). The difference between two sample means has SE = √(σ₁²/n₁ + σ₂²/n₂). In each case, the SE is derived from the sampling distribution of that specific estimator. A smaller SE signals a more **precise** estimator — not necessarily a more accurate one (that depends on bias), but one whose estimates are more repeatable across samples.

In practice, σ is usually unknown, so you estimate SE by substituting the sample standard deviation s in place of σ. The estimated standard error ŜE = s/√n appears in every confidence interval formula and every test statistic as the denominator. When you compute a t-statistic as (x̄ − μ₀)/ŜE, the SE is answering: given the typical variability of x̄ across samples, how many standard errors is this estimate from the null hypothesis? Understanding SE as a property of the estimator's sampling distribution — not of the raw data directly — is the conceptual shift that ties all of statistical inference together.
