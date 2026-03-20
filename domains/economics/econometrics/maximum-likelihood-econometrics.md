---
id: maximum-likelihood-econometrics
title: Maximum Likelihood Estimation
domain: economics
course: econometrics
prerequisites:
- id: ols-assumptions
  type: hard
- id: normal-distribution-intro
  type: hard
- id: sampling-distributions
  type: hard
- id: partial-derivatives
  type: soft
- id: probability-axioms
  type: soft
- id: optimization-problems
  type: soft
- id: natural-logarithm-and-e
  type: soft
- id: constrained-optimization
  type: soft
- id: probability-theory
  type: hard
- id: optimization-multivariable-basics
  type: soft
- id: calculus
  type: hard
builds-toward:
- logit-probit-models
tags:
- MLE
- likelihood
- log-likelihood
- consistency
- asymptotic
stage: advanced
status: validated
---

# Maximum Likelihood Estimation

## Core Idea
Maximum likelihood estimation (MLE) finds the parameter values that make the observed data most probable under a specified distributional model. The log-likelihood function ℓ(θ) = Σᵢ log f(yᵢ; θ) is maximized with respect to θ, typically requiring numerical optimization. MLE estimators are consistent and asymptotically efficient (achieving the Cramér-Rao lower bound) under correct model specification. Under normality, OLS and MLE are equivalent for linear regression. When the distributional form is wrong, MLE can be inconsistent — quasi-MLE is a robust alternative that still provides consistent estimates for certain parameters like means.

## How It's Best Learned
Derive the MLE estimator for the mean of a normal distribution by hand — this makes the logic of maximizing the likelihood concrete before applying it to more complex models like logit.

## Common Misconceptions
- MLE requires a correctly specified distributional assumption; when in doubt, OLS with robust standard errors is safer for linear models.
- The MLE is not always the most intuitive estimator — in small samples it can be biased (e.g., the MLE for the normal variance divides by n, not n−1).

## Questions

```yaml
- question: "You fit a logit model using MLE and later discover the error term is not logistically distributed. What is the most likely consequence?"
  type: multiple-choice
  options:
    - "The estimates are unaffected because MLE is always consistent"
    - "Only the standard errors are biased, but the coefficient estimates remain consistent"
    - "The estimates may be inconsistent because MLE consistency depends on correct distributional specification"
    - "The estimates are biased in small samples only, but consistent asymptotically regardless of the distribution"
  answer: 2
  explanation: "MLE consistency requires that the model is correctly specified — the true data-generating process matches the assumed distribution. If the distributional assumption is wrong, the likelihood being maximized does not correspond to the true probability of the data, and MLE may converge to the wrong parameter values (inconsistency). This contrasts with OLS for linear regression, where consistency only requires E[u|x]=0, not a specific distributional form."

- question: "When the error term is normally distributed, OLS and MLE produce identical coefficient estimates for a linear regression model."
  type: true-false
  answer: true
  explanation: "Under normality, maximizing the log-likelihood for a linear regression model is algebraically equivalent to minimizing the sum of squared residuals. Both procedures yield the same formula: β̂ = (X'X)⁻¹X'y. This equivalence is specific to the normal linear model — in non-linear models (like logit) or non-normal distributions, MLE and OLS diverge. The key implication is that OLS can be interpreted as MLE under a normality assumption."

- question: "Why do econometricians typically maximize the log-likelihood rather than the likelihood function itself?"
  type: short-answer
  answer: "The log-likelihood is computationally and mathematically more tractable: it converts the product of n probability densities into a sum, which is easier to differentiate and optimize. Because the logarithm is a monotone transformation, the parameter values that maximize the likelihood also maximize the log-likelihood."
  explanation: "For n independent observations, the likelihood is a product: L(θ) = ∏ f(yᵢ; θ). Multiplying many probabilities (each between 0 and 1) quickly produces numbers too small for computers to represent accurately (numerical underflow). Taking the log converts multiplication to addition: ℓ(θ) = Σ log f(yᵢ; θ). Since log is strictly monotone increasing, the argmax is unchanged. The resulting sum is also much easier to differentiate to find the maximum analytically or numerically."
```

## Explainer

Maximum likelihood estimation asks a deceptively simple question: given the data I observed, what parameter values would have made this data most likely to occur? If you flip a coin 10 times and get 7 heads, the MLE for the probability of heads is 0.7 — the value that assigns the highest probability to the outcome "7 heads in 10 flips." The same logic extends to any parametric model: specify a distribution for the data, write down the probability of observing your sample as a function of the parameters, and then find the parameters that maximize it.

In practice, we work with the log-likelihood rather than the likelihood itself. Because observations are assumed independent, the likelihood is a product of n terms, each between 0 and 1. This product becomes vanishingly small for large n and is prone to numerical underflow. Taking the log converts the product to a sum — ℓ(θ) = Σᵢ log f(yᵢ; θ) — which is much easier to work with analytically and numerically. Since log is a strictly increasing function, the θ that maximizes ℓ(θ) also maximizes L(θ), so nothing is lost.

One result you should know cold: for the normal linear regression model, MLE and OLS are identical. Plugging the normal density into the log-likelihood and maximizing with respect to β reduces algebraically to minimizing the sum of squared residuals — the same criterion OLS uses. This equivalence shows that OLS carries an implicit distributional assumption (normality) even though it is typically derived without one. In non-linear models like logit or Poisson regression, where OLS does not directly apply, MLE becomes the standard estimation approach.

MLE estimators have attractive large-sample (asymptotic) properties: they are consistent (converge to the true parameter as n → ∞), asymptotically normal, and asymptotically efficient — meaning they achieve the Cramér-Rao lower bound, the smallest variance any unbiased estimator can have. These properties, however, all depend on the model being correctly specified. If the assumed distribution does not match the true data-generating process, the estimator may converge to the wrong value entirely (inconsistency). This is the sharpest difference between MLE and OLS for linear regression: OLS only needs E[u|x] = 0 for consistency, while MLE needs the full distributional form to be right.

In small samples, MLE can be biased even when the model is correctly specified. The classic example is the variance of a normal distribution: the MLE divides by n rather than n−1, yielding a slightly downward-biased estimate. This finite-sample bias typically shrinks as n grows, but it is a reminder that the asymptotic efficiency of MLE does not mean it is always the best choice in small data settings.

