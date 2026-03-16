---
id: bootstrap-inference-econometrics
title: Bootstrap Methods for Statistical Inference
domain: economics
course: econometrics
prerequisites:
- id: hypothesis-testing-regression
  type: hard
- id: robust-standard-errors
  type: soft
- id: probability-theory
  type: hard
- id: sampling-distributions-theory
  type: hard
builds-toward:
- sensitivity-analysis-econometrics
tags:
- bootstrap
- inference
- resampling
stage: formal-systems
status: draft
---

# Bootstrap Methods for Statistical Inference

## Core Idea
Bootstrap methods construct empirical sampling distributions by repeatedly resampling from the data. They provide standard errors, confidence intervals, and p-values without requiring strong distributional assumptions.

## How It's Best Learned
Start with the nonparametric bootstrap: resample observations with replacement, recompute the estimator, and repeat many times. Compare bootstrap standard errors to parametric assumptions to assess robustness.

## Explainer

Your study of sampling distributions established a fundamental problem: we want to know the variability of an estimator across repeated samples, but in practice we only have one sample. The classical solution is to derive the sampling distribution mathematically — assuming normality, invoking the central limit theorem, or exploiting known distributional properties. The bootstrap offers an alternative: use the data itself to simulate repeated sampling. If your single sample of 500 observations approximates the population, then drawing 500 observations with replacement from your sample approximates drawing a new sample from the population. Do this 10,000 times, compute your estimator each time, and you have an empirical approximation to the sampling distribution.

The mechanics of the **nonparametric bootstrap** are straightforward. Given a dataset of n observations, create a bootstrap sample by drawing n observations with replacement — some original observations will appear multiple times, others not at all. Compute the statistic of interest (a coefficient, a median, a ratio, any estimator you like). Repeat B times (typically B = 999 or B = 4,999). The standard deviation of the B bootstrap estimates is your **bootstrap standard error**. The 2.5th and 97.5th percentiles of the bootstrap distribution form a 95% **bootstrap confidence interval**. No formula derivation required — the data does the work.

The crucial insight is what the bootstrap buys you relative to your hypothesis-testing prerequisites. Classical inference requires assumptions about the error distribution (usually normality) or relies on asymptotic arguments that may be poor approximations in small samples. Bootstrap standard errors are valid under much weaker conditions: they work for complex estimators with no closed-form variance formula, for statistics based on ratios or nonlinear transformations, and for settings where the classical standard error formula is known to be misspecified. When you learned about robust standard errors, you were correcting standard errors for heteroskedasticity; the bootstrap corrects them for almost anything, including unknown forms of heteroskedasticity or non-normality.

Bootstrap methods have limits. The bootstrap requires that the sample is representative of the population — it cannot manufacture information that is not in the data. It also requires stationarity for time-series applications: resampling observations that are serially correlated violates the independence assumption of the standard bootstrap, requiring modifications like the block bootstrap. For hypothesis testing, the bootstrap p-value is constructed by centering the bootstrap distribution under the null hypothesis — a subtlety that matters for small samples. The **parametric bootstrap** is a related variant where instead of resampling the data, you simulate from an estimated parametric model, useful when the distributional form is known but the standard error derivation is complex. Understanding when to use each variant — and recognizing the bootstrap's assumptions — is what separates mechanical application from genuine statistical fluency.
