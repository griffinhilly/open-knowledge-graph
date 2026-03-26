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
stage: advanced
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

## Questions

```yaml
- question: "A logit model of employment predicts a coefficient of 0.5 on years of education. A researcher reports: 'One additional year of education increases the probability of employment by 50 percentage points.' What is wrong?"
  type: multiple-choice
  options:
    - "The coefficient should be divided by 100 to convert from log-odds to probability"
    - "The logit coefficient measures change in log-odds, not probability; marginal effects — which vary across individuals — must be computed separately"
    - "The interpretation would be correct only if all other variables are held at their means"
    - "The interpretation is correct for probit but not logit due to their different link functions"
  answer: 1
  explanation: "A logit coefficient β on variable X means a one-unit increase in X raises the log-odds by β — not the probability. The probability change (the marginal effect) is β × F'(X'β), where F' is the derivative of the logistic function. This varies across observations because F' depends on the value of X'β. A coefficient of 0.5 could imply a marginal effect of 0.01 (near the extremes where the curve is flat) or 0.125 (near the middle where the curve is steepest). The raw coefficient is not interpretable as a probability change regardless of what units it's in."

- question: "Why do logit and probit models replace OLS (the linear probability model) for binary outcomes?"
  type: multiple-choice
  options:
    - "OLS cannot converge when Y is binary because the design matrix becomes singular"
    - "Binary outcomes have zero variance, so OLS has nothing to explain"
    - "OLS can predict probabilities below 0 and above 1, and produces heteroskedastic errors by construction; logit and probit constrain predictions to (0,1)"
    - "OLS requires normally distributed dependent variables, and binary data follow a Bernoulli distribution that violates this assumption"
  answer: 2
  explanation: "The linear probability model's core problem is geometric: a line extending infinitely in both directions will eventually predict probabilities below 0 or above 1 for sufficiently extreme values of X. It also has built-in heteroskedasticity because Var(Y|X) = p(1-p), which changes with X. Logit and probit squeeze the linear index X'β through an S-shaped link function that maps (−∞, +∞) into (0,1), guaranteeing valid probability predictions. Option D is a common misconception — OLS assumptions concern the errors, not Y itself, and the normality assumption is not strictly required."

- question: "Because logit and probit models produce nearly identical fitted values in practice, you can directly compare the magnitudes of their coefficients to determine which model fits better."
  type: true-false
  answer: false
  explanation: "Logit and probit coefficients cannot be compared in magnitude because they are on different scales. The logit model uses the logistic function and the probit model uses the standard normal CDF, which have different variances. Logit coefficients are typically about 1.6–1.8 times larger than probit coefficients for the same data, simply due to the scale difference between the two link functions. To compare model fit, use log-likelihood or information criteria (AIC/BIC), not coefficient magnitudes. Marginal effects from the two models ARE comparable because they are in probability units."

- question: "In a logit model, the marginal effect of a predictor variable on P(Y=1) is constant across most observations, analogous to a slope coefficient in linear regression."
  type: true-false
  answer: false
  explanation: "The marginal effect in a logit model is dP/dX = F'(X'β) × β, where F' is the derivative of the logistic function. F' equals p(1-p), which reaches its maximum of 0.25 when p = 0.5 and approaches 0 near the extremes. This means the marginal effect is largest when predicted probability is near 0.5 and nearly zero when probability is near 0 or 1. A predictor that shifts probability from 0.49 to 0.51 has a much larger marginal effect than one shifting probability from 0.01 to 0.03, even if the coefficient is the same. This non-constancy is why marginal effects must be computed — and why 'effect at the mean' and 'average marginal effect' can differ."

- question: "Why must researchers compute and report marginal effects rather than just reporting the raw logit or probit coefficients? What do the raw coefficients actually measure?"
  type: short-answer
  answer: "Raw logit coefficients measure changes in log-odds per unit increase in the predictor — a quantity that is hard to interpret intuitively. Raw probit coefficients measure changes in the standard normal z-score. Neither is directly interpretable as a probability change. Marginal effects convert the coefficient into probability units (the change in P(Y=1) per unit change in X) by multiplying by the derivative of the link function at each observation's values. Because this derivative varies with X'β, the marginal effect differs across individuals, so researchers report either the marginal effect at the mean X or the average marginal effect across all observations."
  explanation: "The deeper issue is that logit and probit models are inherently nonlinear: the same coefficient β implies a larger probability change near p = 0.5 than near p = 0 or 1. Reporting only β hides this nonlinearity and can mislead readers about the practical significance of the predictor. Marginal effects translate the statistical output into policy-relevant terms — 'an additional year of schooling raises the probability of employment by approximately 3 percentage points at the mean' is informative in a way that 'the logit coefficient on schooling is 0.5' is not."
```

## Explainer

You already know how OLS regression models E[Y|X] as a linear function of the predictors. When Y is continuous, this works well. When Y is binary — someone either has a job or doesn't, a firm defaults or doesn't, a patient survives or doesn't — OLS produces the **linear probability model (LPM)**, which models P(Y=1|X) directly as X'β. The problem is that a linear function has no natural boundaries: it can predict probabilities below 0 or above 1 for extreme values of X, and its constant marginal effects ignore the fact that it is much easier to shift probability near the middle of the distribution (around 0.5) than near the extremes. The LPM also has errors that are heteroskedastic by construction — since Y can only take two values, the variance of the error is p(1-p), which varies with X.

The solution is to squeeze the linear index X'β through a function that maps the entire real line into (0,1). The **logistic function** F(z) = 1/(1+e^{-z}) does this: it outputs values strictly between 0 and 1, is symmetric around 0.5, approaches 1 asymptotically for large positive z, and 0 for large negative z. This gives the logit model: P(Y=1|X) = 1/(1+e^{-X'β}). The **probit model** uses the standard normal CDF Φ(X'β) instead, which has the same shape — both produce an S-curve, and in practice they give nearly identical fitted values. The choice between them is mostly conventional; economists often prefer probit, biostatisticians logit.

Because these models are nonlinear, you cannot use OLS to estimate them. Instead, you maximize the **log-likelihood**: for each observation, the model predicts a probability pᵢ = F(X'ᵢβ), and the likelihood contribution is pᵢ if Yᵢ=1 or (1−pᵢ) if Yᵢ=0. Maximizing the sum of log contributions finds the β that makes the observed data most probable under the model. The resulting estimator is consistent and asymptotically normal, so standard errors and hypothesis tests work in the usual way.

The trickiest part is interpreting the coefficients. A logit coefficient β_j does not mean "a one-unit increase in Xⱼ raises P(Y=1) by β_j." It means a one-unit increase in Xⱼ raises the **log-odds** — log(p/(1-p)) — by β_j. Log-odds are not intuitive. To get something interpretable, you compute **marginal effects**: dP/dXⱼ = F'(X'β) × βⱼ, where F' is the derivative of the link function. Because F' depends on X, the marginal effect varies across observations. Standard practice is to report either the **marginal effect at the mean** (evaluate at the average X) or the **average marginal effect** (compute for each observation and average). These give the actual probability change associated with a unit increase in Xⱼ, and are the quantities to report in applied work.

An important distinction from OLS: the logit model's coefficients and marginal effects are not separately identified. Coefficients can only be interpreted relative to the scale of the index X'β, which is fixed by the distributional assumption (logistic or normal). This is why you cannot directly compare the magnitude of logit coefficients across different samples or models that include different variables — the scale changes. You can compare signs and significance, and you can compare marginal effects, but not raw coefficient magnitudes between models.


