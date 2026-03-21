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

## Questions

```yaml
- question: "A researcher fits a regression model with n = 10,000 observations and reports a very tight 95% confidence interval for the mean response at x = 5. A colleague says this means they can predict any individual patient's outcome with high precision. What is wrong with this claim?"
  type: multiple-choice
  options:
    - "Nothing — a tight confidence interval implies a tight prediction interval for the same data"
    - "The confidence interval estimates the population mean response, not individual outcomes; a prediction interval would be much wider due to irreducible person-to-person variation"
    - "The colleague should use a 99% confidence level instead of 95% for medical applications"
    - "The model must be misspecified if individual predictions are not as precise as the confidence interval"
  answer: 1
  explanation: "This is the core confusion the topic addresses. A confidence interval for the mean response narrows with more data because estimation uncertainty shrinks. But a prediction interval also includes σ² — the irreducible scatter of individual observations around the population mean — which does not shrink with more data. Even with a perfect knowledge of the regression line, patients would still vary around it. Option A is exactly the misconception: the tight CI does not imply a tight PI."

- question: "As sample size n approaches infinity, what happens to a 95% prediction interval for a new observation?"
  type: multiple-choice
  options:
    - "It collapses to zero width, as all intervals do with sufficient data"
    - "It narrows to zero only if the true error variance σ² equals zero"
    - "It approaches a fixed non-zero width determined by the irreducible observation variance σ²"
    - "It becomes equivalent to the confidence interval for the mean response"
  answer: 2
  explanation: "As n → ∞, the estimation uncertainty in the mean (the h term in SE_pred²) vanishes, but the '1' term — representing individual-to-individual variance σ² — remains. The prediction interval approaches ŷ ± z* · σ, a fixed width determined by the true noise in the data-generating process. Option A applies to confidence intervals, not prediction intervals. Option D is incorrect: they converge to different limits."

- question: "A confidence interval for the mean response and a prediction interval for a new observation answer the same underlying statistical question."
  type: true-false
  answer: false
  explanation: "They answer fundamentally different questions. A CI asks: 'Where does the population mean μ_Y|x lie?' — a question about a fixed but unknown parameter. A PI asks: 'Where will the next individual observation at x fall?' — a question about a random variable with inherent scatter. The CI width goes to zero as n → ∞ because the parameter can be pinned down; the PI width has a lower bound because individual observations always vary around the mean."

- question: "Prediction intervals are always wider than confidence intervals at the same x value and confidence level."
  type: true-false
  answer: true
  explanation: "This follows directly from the formulas: SE_pred² = s²(1 + h) while SE_mean² = s² · h. The '1 +' in the prediction interval formula adds the irreducible variance component that is always positive, so SE_pred > SE_mean always, and therefore the prediction interval is always wider. The gap is largest near the center of the data (where h is small and the '1' dominates) and smallest far into extrapolation (where h is large for both)."

- question: "Explain why a prediction interval cannot shrink to zero width even with an arbitrarily large sample, while a confidence interval for the mean response can."
  type: short-answer
  answer: "A confidence interval captures estimation uncertainty — the wobble in the fitted line due to working from a finite sample. With more data, the estimated line converges to the true population line, and this uncertainty vanishes. A prediction interval also includes σ², the irreducible scatter of individual observations around any regression line, even a perfectly known one. That scatter reflects genuine person-to-person (or observation-to-observation) variation in the outcome, which is a property of the data-generating process, not of estimation. It cannot be reduced by collecting more data."
  explanation: "The mathematical marker of this distinction is the '1' in SE_pred² = s²(1 + h). The 'h' term captures estimation uncertainty (shrinks with n); the '1' captures irreducible observation variance (does not shrink). A PI is a statement about a random variable; a CI is a statement about a fixed parameter. Confusing them leads to false precision — acting as if the tight CI tells you where individual outcomes will fall when it only tells you where their mean is."
```

## Explainer

From your work with inference in linear regression, you know that the fitted line ŷ = β̂₀ + β̂₁x is itself uncertain — it's estimated from data, so it wobbles depending on which sample you draw. A **confidence interval for the mean response** captures exactly this uncertainty: at a given x value, where might the true population mean μ_Y|x lie? That interval shrinks as sample size grows, because with more data the estimated line stabilizes around the truth.

A **prediction interval** asks a different and harder question: where will the *next single observation* at that x value land? Even if you knew the regression line perfectly — even with infinite data — individual observations would still scatter around it. That scatter is the irreducible noise term ε, with variance σ². A prediction interval must account for *both* sources of uncertainty: the estimation uncertainty in the mean (which goes to zero as n → ∞) and the irreducible observation-to-observation variance (which does not).

Mathematically, the prediction interval at a given x* is ŷ* ± t* · SE_pred, where SE_pred² = s²(1 + h), with h capturing the leverage of x* and the "1" term being the irreducible variance contribution. The "1 +" is the essential difference: the confidence interval uses SE² = s² · h alone, without the leading 1. Because SE_pred > SE_mean always, prediction intervals are always wider — often substantially so, especially for small samples.

The practical lesson is to match the interval to the question. If you want to know the expected height of all 40-year-old men in a population, use a confidence interval for the mean. If you want to know where one specific 40-year-old man's height will fall, use a prediction interval. Confusing them leads to either false precision (using a confidence interval when you need a prediction interval) or unnecessary alarm (the opposite direction). The confidence interval tells you about the center of a distribution; the prediction interval tells you about the distribution itself.

As x* moves away from x̄ (the center of your data), both interval types widen — leverage h increases the farther you extrapolate. But the prediction interval widens more slowly in relative terms because the "1" dominates when h is small. Near the center of the data, prediction intervals are roughly twice as wide as confidence intervals; far into extrapolation territory, both balloon together. This is why extrapolation with a prediction interval makes caution concrete: you can literally see how much uncertainty you're projecting onto a single future observation.
