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

## Explainer

Your prerequisite — maximum likelihood estimation — gives you the machinery to fit models where assumptions about the error distribution can be made explicit. Now consider a type of outcome that violates every OLS assumption: counts. How many hospital visits did a patient have last year? How many patents did a firm file? These outcomes are non-negative integers, they cluster near zero, and their variance tends to grow with the mean. Applying OLS to such data produces nonsensical predictions (including negative counts) and invalid standard errors.

**Poisson regression** is the natural starting point. It assumes the outcome Y follows a Poisson distribution with conditional mean λ = exp(Xβ). The exponential link ensures predicted counts are always non-negative — a necessary constraint. You can read the coefficients as effects on log(λ): a one-unit increase in x multiplies the expected count by exp(β). This is the count-data analog of the log-linear interpretation you may have seen in OLS with logged outcomes. Estimation proceeds by maximizing the Poisson log-likelihood, which you already know how to do.

The Poisson model imposes one distinctive restriction: the mean equals the variance (**equidispersion**). In practice, count data is almost always **overdispersed** — the observed variance exceeds the Poisson mean. Think of emergency room visits: most people have zero or one visit per year, but a small, chronically ill population has very many, inflating the variance far above the mean. If you fit Poisson to overdispersed data, the standard errors are too small and t-statistics are inflated, leading to false significance.

**Negative binomial regression** relaxes equidispersion by introducing an extra dispersion parameter α. When α = 0, the negative binomial collapses to Poisson — you can formally test this restriction. The NB model can be derived by treating each observation as drawn from a Poisson distribution whose own mean varies across individuals according to a gamma distribution. The intuition is that individuals have unobserved heterogeneity in their base rate of the count outcome, and this unobserved variation inflates the variance. In practice, testing whether the negative binomial significantly improves on Poisson is one of the first diagnostics to run on any count dataset.

A further extension worth knowing is the **zero-inflated** count model, which handles data with far more zeros than any Poisson or negative binomial distribution can accommodate. This arises when zeros come from two distinct processes — for example, lifelong non-smokers who can never have a smoking-related diagnosis, versus smokers who happen to have zero incidents this period. Zero-inflated models combine a binary component (is the outcome structurally zero?) with a count component (given non-zero, how many?), letting each process have its own covariates.
