---
id: prediction-intervals-regression-probability-and-statistics
title: Prediction Intervals in Regression
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: inference-in-linear-regression
  type: hard
tags:
- regression
- prediction
- inference
stage: formal-systems
status: draft
---

# Prediction Intervals in Regression

## Core Idea
A prediction interval estimates where a new individual observation will fall; a confidence interval estimates the mean response. Prediction intervals are wider because they include both uncertainty in estimating the mean and natural variation around the mean.

## Explainer

From your work with inference in linear regression, you know that the fitted line ŷ = β̂₀ + β̂₁x is itself uncertain — it's estimated from data, so it wobbles depending on which sample you draw. A **confidence interval for the mean response** captures exactly this uncertainty: at a given x value, where might the true population mean μ_Y|x lie? That interval shrinks as sample size grows, because with more data the estimated line stabilizes around the truth.

A **prediction interval** asks a different and harder question: where will the *next single observation* at that x value land? Even if you knew the regression line perfectly — even with infinite data — individual observations would still scatter around it. That scatter is the irreducible noise term ε, with variance σ². A prediction interval must account for *both* sources of uncertainty: the estimation uncertainty in the mean (which goes to zero as n → ∞) and the irreducible observation-to-observation variance (which does not).

Mathematically, the prediction interval at a given x* is ŷ* ± t* · SE_pred, where SE_pred² = s²(1 + h), with h capturing the leverage of x* and the "1" term being the irreducible variance contribution. The "1 +" is the essential difference: the confidence interval uses SE² = s² · h alone, without the leading 1. Because SE_pred > SE_mean always, prediction intervals are always wider — often substantially so, especially for small samples.

The practical lesson is to match the interval to the question. If you want to know the expected height of all 40-year-old men in a population, use a confidence interval for the mean. If you want to know where one specific 40-year-old man's height will fall, use a prediction interval. Confusing them leads to either false precision (using a confidence interval when you need a prediction interval) or unnecessary alarm (the opposite direction). The confidence interval tells you about the center of a distribution; the prediction interval tells you about the distribution itself.

As x* moves away from x̄ (the center of your data), both interval types widen — leverage h increases the farther you extrapolate. But the prediction interval widens more slowly in relative terms because the "1" dominates when h is small. Near the center of the data, prediction intervals are roughly twice as wide as confidence intervals; far into extrapolation territory, both balloon together. This is why extrapolation with a prediction interval makes caution concrete: you can literally see how much uncertainty you're projecting onto a single future observation.
