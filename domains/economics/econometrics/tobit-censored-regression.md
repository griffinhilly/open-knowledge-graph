---
id: tobit-censored-regression
title: Tobit Model for Corner Solutions and Censored Data
domain: economics
course: econometrics
prerequisites:
- id: maximum-likelihood-econometrics
  type: hard
- id: logit-probit-models
  type: hard
- id: multiple-regression-model
  type: soft
- id: nonlinear-models-interpretation
  type: soft
builds-toward:
- heckman-sample-selection-correction
tags:
- limited dependent variable
- Tobit
- censoring
- corner solution
- maximum likelihood
- partial effects
stage: advanced
status: validated
---

# Tobit Model for Corner Solutions and Censored Data

## Core Idea
Many outcomes are zero for a large share of people and positive and continuous for the rest, such as hours worked, charitable donations, or spending on a durable good. The Tobit model, proposed by James Tobin in 1958, treats the outcome as y = max(0, y*), where the latent variable y* = xβ + u has a normal error. Linear regression on such data is inconsistent, whether it uses all observations or only the positive ones. Tobit estimates β and σ by maximum likelihood, combining a probit-like term for the zeros with a normal-density term for the positive values. Its coefficients describe effects on the latent variable, so effects on the observed outcome must be computed separately.

## How It's Best Learned
Plot simulated data where many observations pile up at zero, then fit OLS to all the data and to the positive data only, and show that both slopes are too flat. Next, write down the two pieces of the Tobit likelihood and connect the zero piece to the probit model students already know. Finish by computing a partial effect on E(y|x) and comparing it with the raw coefficient.

## Common Misconceptions
- Dropping the zeros and running OLS on the positive observations fixes the problem. (Conditioning on y > 0 selects observations with high errors, so the error no longer has mean zero and OLS remains biased.)
- The Tobit coefficient β_j is the effect of x_j on the expected observed outcome. (β_j is the effect on the latent y*; the effect on E(y|x) is β_j times Φ(xβ/σ), which is smaller.)
- Tobit is valid whatever the error distribution. (Its consistency relies on the error being normal and homoskedastic; if these fail, the estimates are generally inconsistent.)

## Questions

```yaml
- question: "In a Tobit model of annual hours worked, the estimated coefficient on years of education is 80, and at the average x the probability of working, Φ(xβ/σ), is 0.6. What is the approximate partial effect of one more year of education on expected hours, E(y|x)?"
  type: multiple-choice
  options: ["80 hours", "48 hours", "133 hours", "0.6 hours"]
  answer: 1
  explanation: "For the Tobit model, ∂E(y|x)/∂x_j = β_j Φ(xβ/σ) = 80 × 0.6 = 48. The raw coefficient of 80 is the effect on latent desired hours, which overstates the effect on observed hours because some people remain at zero."
- question: "OLS estimated only on observations with y > 0 gives consistent estimates of β in a Tobit setting."
  type: true-false
  answer: false
  explanation: "Among people with a given x, those with y > 0 tend to have larger errors u. So E(u | x, y > 0) is positive and depends on x, which makes OLS on the truncated sample biased and inconsistent."
- question: "For an observation with y = 0, what is its contribution to the Tobit likelihood?"
  type: multiple-choice
  options: ["The normal density at zero", "The probability that y* ≤ 0, which is 1 − Φ(xβ/σ)", "Zero, because such observations are dropped", "The logistic CDF of xβ"]
  answer: 1
  explanation: "A zero tells us only that the latent variable was at or below zero. Its probability is P(u ≤ −xβ) = Φ(−xβ/σ) = 1 − Φ(xβ/σ). Positive observations contribute the normal density (1/σ)φ((y − xβ)/σ)."
- question: "Explain the difference between a corner-solution outcome and a censored outcome, and why the distinction affects interpretation."
  type: short-answer
  answer: "A corner solution is a choice variable that truly equals zero for many people, such as hours worked, so the observed y is the quantity of interest. Censoring is a data problem, such as incomes top-coded above a threshold, where the true value exists but is not recorded, so the latent y* is the quantity of interest. A likelihood of the same form can be used, with the censoring point and direction adjusted, but with a corner solution you report effects on E(y|x), and with censoring you interpret β directly."
  explanation: "Wooldridge's introductory text stresses this distinction because the same Tobit output answers different questions in the two cases."
```

## Explainer
You know the probit model handles a binary outcome by assuming a latent variable crosses a threshold. The Tobit model extends that idea to outcomes that are zero for many observations and positive and continuous for the rest. James Tobin introduced it in 1958 to study household spending on durable goods, where many households spend nothing in a given year.

The model starts with a latent variable, y* = xβ + u, with u normally distributed with mean zero and variance σ², independent of x. We observe y = y* when y* > 0, and y = 0 otherwise. For hours worked, you can think of y* as desired hours: some people would want negative hours at the going wage if that were possible, and they appear in the data as zero.

Why not use OLS? If you regress y on x using all observations, the pile of zeros pulls the fitted line toward a flatter slope, because the true relationship is curved: E(y|x) approaches zero for low xβ and approaches xβ for high xβ. If you keep only positive observations, you select people with large errors at each x, especially at low x, which again biases the slope. Both approaches are inconsistent.

Tobit uses maximum likelihood. Each zero contributes the probability that y* was at or below zero, 1 − Φ(xβ/σ). Each positive value contributes the normal density (1/σ)φ((y − xβ)/σ). Maximizing the product over the sample yields estimates of β and σ.

Interpretation needs care. The coefficient β_j measures the effect of x_j on y*. If the outcome is a real choice with many zeros, a **corner solution**, the effect of interest is on observed y. That effect is ∂E(y|x)/∂x_j = β_j Φ(xβ/σ). Since Φ lies between zero and one, the effect on the observed mean is smaller than β_j. With a coefficient of 80 hours per year of schooling and Φ = 0.6, the effect on expected hours is 48. When the data are **censored** for recording reasons, such as top-coded incomes, the latent variable is the target and β can be read directly.

The model's main weakness is its reliance on normal, homoskedastic errors, and on a single index governing both whether y is positive and how large it is. When participation and amount depend on different factors, two-part models or Heckman's selection model are often preferred.
