---
id: logistic-regression-binary-categorical
title: Logistic Regression and Generalized Linear Models
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: logistic-regression-binary-outcomes
  type: hard
- id: exponential-functions-and-graphs
  type: hard
- id: partial-derivatives
  type: hard
- id: optimization-multivariable-basics
  type: soft
builds-toward:
- count-data-regression-models
tags:
- logistic-regression
- categorical
- glm
stage: advanced
status: draft
---

# Logistic Regression and Generalized Linear Models

## Core Idea
When outcomes are categorical, ordinary regression is inappropriate. Logistic regression transforms probabilities to log-odds scale. Generalized linear models extend this framework to count data, ordinal outcomes, and non-normal distributions, providing proper inference for categorical outcomes.

## Explainer

You already understand logistic regression for binary outcomes — that a probability bounded between 0 and 1 cannot be modeled with an unbounded linear predictor, so we apply the **logit transformation** (log-odds: ln[p/(1−p)]) to map probabilities to the real line. This transformation is invertible via the **sigmoid function**, and your background with exponential functions and graphs helps you see why: e^x / (1 + e^x) produces the characteristic S-curve that squeezes any linear combination of predictors into the (0,1) interval. The key interpretive fact is that logistic regression coefficients represent changes in log-odds, which can be exponentiated to **odds ratios** — a more interpretable but still nonlinear quantity. An odds ratio of 1.5 means the odds of the outcome are 50% higher per unit increase in the predictor, not that the probability increases by 50 percentage points.

The **Generalized Linear Model (GLM)** framework unifies logistic regression with a broader family of models for non-normal outcomes. Every GLM has three components: a **random component** (the outcome's probability distribution — Bernoulli, Poisson, binomial, gamma), a **systematic component** (the linear predictor Xβ), and a **link function** (the transformation connecting the mean of the distribution to the linear predictor). For logistic regression, the distribution is Bernoulli and the link is logit. For count data where events accumulate over time — arrest counts, hospital admissions, species occurrences — the appropriate choice is typically a **Poisson GLM** with a log link, because counts are non-negative and Poisson-distributed. This is where your background in partial derivatives becomes practically important: GLMs are fit by maximum likelihood via iteratively reweighted least squares (IRWLS), an optimization procedure that requires computing derivatives of the log-likelihood.

A common situation in social science is an outcome with more than two ordered categories — survey responses like "strongly disagree / disagree / agree / strongly agree," health status coded as poor/fair/good/excellent, or educational attainment in stages. For these, **ordinal logistic regression** (the proportional odds model) models the cumulative probability of being at or below each threshold. The key assumption is that a single set of coefficients explains the transition at every threshold — the same predictor effect governs the move from poor to fair health as the move from fair to good health. When this assumption is violated, you need a less constrained model. For unordered categorical outcomes — political party choice among three parties, choice of transportation mode — **multinomial logistic regression** models each category against a reference category simultaneously, producing a set of coefficients for each non-reference outcome.

Throughout the GLM family, **model fit** is assessed differently than in OLS. There is no direct equivalent to R². Instead, researchers compare **deviance** (analogous to residual sum of squares, based on log-likelihood ratios) between nested models using chi-squared tests, or use information criteria (AIC, BIC) to compare non-nested models penalizing for complexity. Predicted probabilities and marginal effects — the change in predicted probability for a one-unit change in a predictor, holding others at specified values — are typically more interpretable than raw coefficients, particularly for communicating findings to non-technical audiences.

The practical skill is choosing the right GLM for the right outcome structure: binary outcomes → logistic; counts → Poisson (or negative binomial if overdispersed); ordered categories → ordinal logistic; unordered categories → multinomial logistic. Each choice reflects assumptions about the data-generating process, and your background in optimization helps you understand why these models are estimated iteratively rather than analytically — unlike OLS, there is no closed-form solution for the MLE of a GLM, and convergence is not always guaranteed.
