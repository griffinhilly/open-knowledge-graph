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

## Questions

```yaml
- question: "A researcher fits a simple linear regression and obtains β̂₁ = 0.45 with SE(β̂₁) = 0.18 and n = 30. The p-value for H₀: β₁ = 0 is 0.018. What is the correct interpretation of this p-value?"
  type: multiple-choice
  options:
    - "There is a 1.8% probability that β₁ = 0 in the population"
    - "If β₁ = 0, the probability of observing a t-statistic at least as extreme as the one observed is 1.8%"
    - "The regression explains 98.2% of the variation in Y"
    - "There is a 98.2% probability that the true slope is positive"
  answer: 1
  explanation: "A p-value is the probability of observing data at least as extreme as what was observed, assuming the null hypothesis is true. It is not the probability that the null hypothesis is true (option A), not a measure of model fit (option C), and not a posterior probability about the parameter (option D). Under H₀: β₁ = 0, a t-statistic this large would arise only 1.8% of the time by chance, so we reject H₀ at the 5% level."

- question: "A confidence interval for the mean response E[Y|X=x*] and a prediction interval for a new observation at the same x* are computed. Which statement correctly describes their relationship?"
  type: multiple-choice
  options:
    - "They are the same width, since both use the same regression equation"
    - "The confidence interval is wider, because it must account for uncertainty in both β̂₀ and β̂₁"
    - "The prediction interval is wider, because it must also account for the irreducible scatter of individual observations around the true line"
    - "The confidence interval is wider near X̄ but the prediction interval is wider far from X̄"
  answer: 2
  explanation: "Prediction intervals are always wider than confidence intervals for the mean at the same X value. A confidence interval captures only parameter uncertainty — how precisely we've estimated the true mean response at x*. A prediction interval must also account for residual variation: even if we knew the true line exactly, individual observations scatter around it with variance σ². This additional source of uncertainty makes prediction intervals irreducibly wider."

- question: "A 95% confidence interval for β₁ that does not include zero is equivalent to rejecting H₀: β₁ = 0 at the 5% significance level."
  type: true-false
  answer: true
  explanation: "A confidence interval at level (1−α) and a hypothesis test at level α are two perspectives on the same question. The confidence interval contains exactly those values of β₁ that would not be rejected by a two-sided test at level α. If zero is not in the interval, then zero would be rejected — which is identical to rejecting H₀: β₁ = 0 at level α. Both approaches yield the same conclusion about statistical significance."

- question: "Both confidence intervals for the mean response and prediction intervals for new observations are narrowest at the extreme ends of the observed X range."
  type: true-false
  answer: false
  explanation: "Both intervals are narrowest at X = X̄, the mean of the predictor values, and widen as X moves away from X̄ in either direction. The OLS regression line is pinned by the data's centroid — the estimate of the mean response is most precise there. As X moves toward the extremes or into extrapolation territory, uncertainty in the slope estimate compounds, widening both intervals. The extremes of the X range are where the intervals are widest, not narrowest."

- question: "Why does the t-test for the regression slope β₁ use n − 2 degrees of freedom rather than n − 1?"
  type: short-answer
  answer: "Two parameters are estimated from the data — the intercept β̂₀ and the slope β̂₁ — and each estimated parameter costs one degree of freedom. Starting with n observations, we lose 2 degrees of freedom for the two estimated parameters, leaving n − 2 for the residual variance estimate s². The t-statistic uses s in its denominator, so it follows a t-distribution with n − 2 degrees of freedom under H₀."
  explanation: "Degrees of freedom count the number of independent pieces of information remaining after estimating parameters. A one-sample t-test uses n − 1 df because only the mean is estimated. Simple linear regression estimates two parameters (intercept and slope), so n − 2 df remain. Multiple regression with p predictors (plus intercept) uses n − p − 1 df for the same reason. This matters for the critical value and p-value of the test."
```

## Explainer

From simple linear regression you know how to compute β̂₁ — the OLS estimate of the slope — from a sample of n observations. But β̂₁ is a statistic, not a parameter. Every new sample would give a slightly different slope. The central insight of regression inference is that β̂₁ has its own **sampling distribution**: under standard assumptions (linearity, constant variance, uncorrelated errors), β̂₁ is normally distributed with mean equal to the true population slope β₁ and standard error SE(β̂₁) = s / √(Σ(xᵢ − x̄)²), where s is the residual standard error. We cannot observe β₁ directly, but we can reason probabilistically about where it lies.

The most common question is whether the predictor matters at all — does X have a linear relationship with Y in the population? This is formalized as H₀: β₁ = 0. The **t-statistic** T = β̂₁ / SE(β̂₁) measures how many standard errors the estimate is from zero. Under H₀, T follows a t-distribution with n − 2 degrees of freedom (we lose two for estimating β₀ and β₁). A large |T| means the slope is far from zero relative to its sampling uncertainty, giving evidence against H₀. The p-value is the probability of observing a t-statistic at least as extreme, assuming H₀ is true. If p < α, we reject H₀ and conclude that X is a statistically significant linear predictor of Y.

A **confidence interval** for β₁ — β̂₁ ± t_{n−2, α/2} · SE(β̂₁) — inverts the same logic. Rather than asking whether a specific hypothesized value is plausible, the interval reports all values that would not be rejected at level α. An interval that excludes zero is equivalent to rejecting H₀: β₁ = 0 at that level. The **F-test** for the overall model generalizes to multiple predictors: it tests whether all slopes are simultaneously zero. In simple regression, the F-statistic equals T², so both tests are equivalent and give identical p-values.

**Prediction intervals** address a different question: where will a *new individual observation* fall, given a particular X value? Unlike a confidence interval for the mean response (which only captures uncertainty about the population mean at X = x*), a prediction interval must also account for residual variation — the irreducible scatter of individual points around the true line. As a result, prediction intervals are always wider than confidence intervals for the mean. Both intervals are narrowest at X = X̄ and widen as X moves away from the mean, because the OLS line is pinned by the data centroid — extrapolation increases uncertainty. The more residual variation in the data (larger s), the wider both intervals become, reflecting genuine uncertainty about the underlying relationship.
