---
id: count-data-models
title: 'Count Data Models: Poisson and Negative Binomial Regression'
domain: economics
course: econometrics
prerequisites:
- id: maximum-likelihood-econometrics
  type: hard
tags:
- count-data
- poisson
- negative-binomial
stage: advanced
status: draft
---

# Count Data Models: Poisson and Negative Binomial Regression

## Core Idea
Poisson regression models count outcomes by linking the conditional mean to covariates, with the constraint that mean equals variance. Negative binomial relaxes this restriction, allowing overdispersion when variance exceeds the mean.

## Questions

```yaml
- question: "A researcher fits a Poisson regression to the number of hospital visits per patient and gets highly significant coefficients. A reviewer suspects the results may be invalid. What should the reviewer check first?"
  type: multiple-choice
  options:
    - "Whether the log-likelihood is maximized at the estimated parameters"
    - "Whether the data is overdispersed — if variance exceeds the mean, Poisson standard errors will be too small and significance will be inflated"
    - "Whether the outcome variable has any zero values, which Poisson cannot handle"
    - "Whether the coefficients are positive, since count outcomes cannot decrease"
  answer: 1
  explanation: "The Poisson model imposes equidispersion (mean = variance). Real count data is almost always overdispersed — a small, high-utilization subgroup inflates the variance far above the mean. When the Poisson model is fit to overdispersed data, it underestimates standard errors and overstates statistical significance. The first diagnostic is to test for overdispersion (e.g., compare mean vs. sample variance, or test whether the negative binomial dispersion parameter α is significantly different from 0)."

- question: "What is the key parametric difference between Poisson and negative binomial regression?"
  type: multiple-choice
  options:
    - "Negative binomial uses a log link while Poisson uses an identity link"
    - "Negative binomial adds a dispersion parameter α that allows variance to exceed the mean; when α = 0 it reduces to Poisson"
    - "Negative binomial models the log of the outcome while Poisson models the outcome directly"
    - "Negative binomial uses ordinary least squares while Poisson uses maximum likelihood"
  answer: 1
  explanation: "Both models use a log link and maximum likelihood estimation. The essential difference is the dispersion parameter α in the negative binomial. Poisson fixes variance = mean; negative binomial allows variance = mean + α·mean² (NB2 parameterization), with α estimated from the data. When α = 0, the negative binomial collapses to Poisson, which is why you can formally test Poisson vs. negative binomial by testing H₀: α = 0."

- question: "In Poisson regression, the exponential link function means the model can predict negative counts for extreme covariate values."
  type: true-false
  answer: false
  explanation: "The exponential link is specifically chosen to guarantee non-negative predictions. The model predicts λ = exp(Xβ), and since exp(·) > 0 for all finite inputs, predicted counts are always positive. This is one of the key advantages of Poisson regression over OLS for count data: OLS can produce nonsensical negative predictions, while the exponential link ensures the prediction is always a valid (non-negative) count."

- question: "When Poisson regression is fit to overdispersed count data, the estimated coefficients are biased, making them unreliable even if standard errors were correct."
  type: true-false
  answer: false
  explanation: "The primary problem with Poisson on overdispersed data is invalid standard errors, not biased coefficients. The coefficient estimates themselves are still consistent under overdispersion (this is the QMLE / quasi-Poisson result). What fails is the standard error formula, which assumes mean = variance — so t-statistics and p-values are inflated, but the point estimates remain useful. This is why robust standard errors (sandwich estimator) can fix inference without switching to a different model."

- question: "Explain why overdispersion is specifically dangerous for inference (not just model fit) when using Poisson regression on real count data."
  type: short-answer
  answer: "Poisson regression's standard error formula is derived assuming variance = mean. When actual variance exceeds the mean (overdispersion), the model 'sees' less spread in the data than is truly there, and estimates standard errors that are too small. This makes t-statistics and z-statistics artificially large and p-values artificially small — so coefficients appear statistically significant when they may not be. The danger is incorrect inference: you may publish results claiming strong, reliable associations when the apparent precision is an artifact of the misspecified error structure."
  explanation: "The fix is either to switch to negative binomial regression (which models overdispersion explicitly), use quasi-Poisson with sandwich standard errors, or test for overdispersion before finalizing results. This is one of the most common sources of false positives in applied research using count outcomes."
```

## Explainer

Your prerequisite — maximum likelihood estimation — gives you the machinery to fit models where assumptions about the error distribution can be made explicit. Now consider a type of outcome that violates every OLS assumption: counts. How many hospital visits did a patient have last year? How many patents did a firm file? These outcomes are non-negative integers, they cluster near zero, and their variance tends to grow with the mean. Applying OLS to such data produces nonsensical predictions (including negative counts) and invalid standard errors.

**Poisson regression** is the natural starting point. It assumes the outcome Y follows a Poisson distribution with conditional mean λ = exp(Xβ). The exponential link ensures predicted counts are always non-negative — a necessary constraint. You can read the coefficients as effects on log(λ): a one-unit increase in x multiplies the expected count by exp(β). This is the count-data analog of the log-linear interpretation you may have seen in OLS with logged outcomes. Estimation proceeds by maximizing the Poisson log-likelihood, which you already know how to do.

The Poisson model imposes one distinctive restriction: the mean equals the variance (**equidispersion**). In practice, count data is almost always **overdispersed** — the observed variance exceeds the Poisson mean. Think of emergency room visits: most people have zero or one visit per year, but a small, chronically ill population has very many, inflating the variance far above the mean. If you fit Poisson to overdispersed data, the standard errors are too small and t-statistics are inflated, leading to false significance.

**Negative binomial regression** relaxes equidispersion by introducing an extra dispersion parameter α. When α = 0, the negative binomial collapses to Poisson — you can formally test this restriction. The NB model can be derived by treating each observation as drawn from a Poisson distribution whose own mean varies across individuals according to a gamma distribution. The intuition is that individuals have unobserved heterogeneity in their base rate of the count outcome, and this unobserved variation inflates the variance. In practice, testing whether the negative binomial significantly improves on Poisson is one of the first diagnostics to run on any count dataset.

A further extension worth knowing is the **zero-inflated** count model, which handles data with far more zeros than any Poisson or negative binomial distribution can accommodate. This arises when zeros come from two distinct processes — for example, lifelong non-smokers who can never have a smoking-related diagnosis, versus smokers who happen to have zero incidents this period. Zero-inflated models combine a binary component (is the outcome structurally zero?) with a count component (given non-zero, how many?), letting each process have its own covariates.
