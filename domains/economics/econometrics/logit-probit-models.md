---
id: logit-probit-models
title: Logit and Probit Models for Binary Outcomes
domain: economics
course: econometrics
prerequisites:
- id: multiple-regression-model
  type: hard
- id: maximum-likelihood-econometrics
  type: hard
- id: normal-distribution-intro
  type: soft
- id: continuous-random-variables
  type: soft
tags:
- logit
- probit
- binary-outcome
- MLE
- marginal-effects
stage: formal-systems
status: validated
---

# Logit and Probit Models for Binary Outcomes

## Core Idea
When the dependent variable is binary (y ∈ {0,1}), the linear probability model (OLS on a dummy) can predict probabilities outside [0,1] and has heteroskedastic errors by construction. Logit and probit models instead model P(y=1|x) = F(x'β) where F is the logistic function (logit) or the standard normal CDF (probit), ensuring predicted probabilities lie in (0,1). Both are estimated by maximum likelihood, not OLS. Coefficients are not directly interpretable as marginal effects; marginal effects (dP/dx evaluated at the mean or averaged over the sample) are reported instead. Logit and probit produce similar results in practice; the choice is usually conventional.

## How It's Best Learned
Estimate a labor force participation model (binary) using LPM, logit, and probit on the same data. Compare predicted probabilities near 0 and 1 to see where LPM fails. Compute average marginal effects for the logit model.

## Common Misconceptions
- Logit coefficients are log-odds ratios, not probability changes — always compute and report marginal effects.
- Pseudo-R² statistics (McFadden, Nagelkerke) are not comparable to OLS R² and should not be interpreted as 'fraction of variance explained'.

## Explainer

You already know how OLS regression models E[Y|X] as a linear function of the predictors. When Y is continuous, this works well. When Y is binary — someone either has a job or doesn't, a firm defaults or doesn't, a patient survives or doesn't — OLS produces the **linear probability model (LPM)**, which models P(Y=1|X) directly as X'β. The problem is that a linear function has no natural boundaries: it can predict probabilities below 0 or above 1 for extreme values of X, and its constant marginal effects ignore the fact that it is much easier to shift probability near the middle of the distribution (around 0.5) than near the extremes. The LPM also has errors that are heteroskedastic by construction — since Y can only take two values, the variance of the error is p(1-p), which varies with X.

The solution is to squeeze the linear index X'β through a function that maps the entire real line into (0,1). The **logistic function** F(z) = 1/(1+e^{-z}) does this: it outputs values strictly between 0 and 1, is symmetric around 0.5, approaches 1 asymptotically for large positive z, and 0 for large negative z. This gives the logit model: P(Y=1|X) = 1/(1+e^{-X'β}). The **probit model** uses the standard normal CDF Φ(X'β) instead, which has the same shape — both produce an S-curve, and in practice they give nearly identical fitted values. The choice between them is mostly conventional; economists often prefer probit, biostatisticians logit.

Because these models are nonlinear, you cannot use OLS to estimate them. Instead, you maximize the **log-likelihood**: for each observation, the model predicts a probability pᵢ = F(X'ᵢβ), and the likelihood contribution is pᵢ if Yᵢ=1 or (1−pᵢ) if Yᵢ=0. Maximizing the sum of log contributions finds the β that makes the observed data most probable under the model. The resulting estimator is consistent and asymptotically normal, so standard errors and hypothesis tests work in the usual way.

The trickiest part is interpreting the coefficients. A logit coefficient β_j does not mean "a one-unit increase in Xⱼ raises P(Y=1) by β_j." It means a one-unit increase in Xⱼ raises the **log-odds** — log(p/(1-p)) — by β_j. Log-odds are not intuitive. To get something interpretable, you compute **marginal effects**: dP/dXⱼ = F'(X'β) × βⱼ, where F' is the derivative of the link function. Because F' depends on X, the marginal effect varies across observations. Standard practice is to report either the **marginal effect at the mean** (evaluate at the average X) or the **average marginal effect** (compute for each observation and average). These give the actual probability change associated with a unit increase in Xⱼ, and are the quantities to report in applied work.

An important distinction from OLS: the logit model's coefficients and marginal effects are not separately identified. Coefficients can only be interpreted relative to the scale of the index X'β, which is fixed by the distributional assumption (logistic or normal). This is why you cannot directly compare the magnitude of logit coefficients across different samples or models that include different variables — the scale changes. You can compare signs and significance, and you can compare marginal effects, but not raw coefficient magnitudes between models.


