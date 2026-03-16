---
id: regression-inference-hypothesis-tests
title: Hypothesis Tests and Inference in Regression
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: linear-regression-simple-theory
  type: hard
builds-toward:
- regression-diagnostics
tags:
- regression-inference
stage: formal-systems
status: draft
---

# Hypothesis Tests and Inference in Regression

## Core Idea
Test H₀:β₁=0 using T=(β₁−0)/SE(β₁) with n−2 df. Confidence interval for β₁: β₁±t_{n-2,α/2}·SE(β₁). F-test for overall model. Prediction intervals widen with distance from X̄ and with increased residual variation.

## Explainer

From simple linear regression you know how to compute β̂₁ — the OLS estimate of the slope — from a sample of n observations. But β̂₁ is a statistic, not a parameter. Every new sample would give a slightly different slope. The central insight of regression inference is that β̂₁ has its own **sampling distribution**: under standard assumptions (linearity, constant variance, uncorrelated errors), β̂₁ is normally distributed with mean equal to the true population slope β₁ and standard error SE(β̂₁) = s / √(Σ(xᵢ − x̄)²), where s is the residual standard error. We cannot observe β₁ directly, but we can reason probabilistically about where it lies.

The most common question is whether the predictor matters at all — does X have a linear relationship with Y in the population? This is formalized as H₀: β₁ = 0. The **t-statistic** T = β̂₁ / SE(β̂₁) measures how many standard errors the estimate is from zero. Under H₀, T follows a t-distribution with n − 2 degrees of freedom (we lose two for estimating β₀ and β₁). A large |T| means the slope is far from zero relative to its sampling uncertainty, giving evidence against H₀. The p-value is the probability of observing a t-statistic at least as extreme, assuming H₀ is true. If p < α, we reject H₀ and conclude that X is a statistically significant linear predictor of Y.

A **confidence interval** for β₁ — β̂₁ ± t_{n−2, α/2} · SE(β̂₁) — inverts the same logic. Rather than asking whether a specific hypothesized value is plausible, the interval reports all values that would not be rejected at level α. An interval that excludes zero is equivalent to rejecting H₀: β₁ = 0 at that level. The **F-test** for the overall model generalizes to multiple predictors: it tests whether all slopes are simultaneously zero. In simple regression, the F-statistic equals T², so both tests are equivalent and give identical p-values.

**Prediction intervals** address a different question: where will a *new individual observation* fall, given a particular X value? Unlike a confidence interval for the mean response (which only captures uncertainty about the population mean at X = x*), a prediction interval must also account for residual variation — the irreducible scatter of individual points around the true line. As a result, prediction intervals are always wider than confidence intervals for the mean. Both intervals are narrowest at X = X̄ and widen as X moves away from the mean, because the OLS line is pinned by the data centroid — extrapolation increases uncertainty. The more residual variation in the data (larger s), the wider both intervals become, reflecting genuine uncertainty about the underlying relationship.
