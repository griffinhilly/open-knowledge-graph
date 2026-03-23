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
stage: expert
status: draft
---

# Logistic Regression and Generalized Linear Models

## Core Idea
When outcomes are categorical, ordinary regression is inappropriate. Logistic regression transforms probabilities to log-odds scale. Generalized linear models extend this framework to count data, ordinal outcomes, and non-normal distributions, providing proper inference for categorical outcomes.

## Questions

```yaml
- question: "A logistic regression predicting employment (1 = employed, 0 = not) finds that holding a college degree has an odds ratio of 2.0. A researcher reports: 'College graduates are twice as likely to be employed.' This conclusion is:"
  type: multiple-choice
  options:
    - "Correct — an odds ratio of 2.0 means the probability of employment doubles for college graduates"
    - "Incorrect — an odds ratio of 2.0 means the odds of employment double, and this equals a probability doubling only when baseline probability is very small"
    - "Correct — odds ratios are always interpretable as probability ratios in logistic regression"
    - "Incorrect — odds ratios greater than 1 indicate a negative association in logistic regression"
  answer: 1
  explanation: "This is the most common misinterpretation of logistic regression output. An odds ratio of 2.0 means the odds (p/(1−p)) are twice as large for degree holders, not the probability itself. If baseline employment probability is 0.5, the odds are 1.0; an OR of 2 gives odds of 2.0, which corresponds to a probability of 0.67 — a 17 percentage-point increase, not a doubling. Only when the baseline probability is very small (the 'rare outcome assumption') do odds ratios approximate probability ratios. In social science research with common outcomes, conflating ORs and relative risks systematically overstates effect sizes."

- question: "A criminologist is modeling the number of arrests each respondent accumulated over five years — a count ranging from 0 to 12. Which model is most appropriate?"
  type: multiple-choice
  options:
    - "OLS linear regression, since the count can be treated as a continuous outcome"
    - "Binary logistic regression after recoding to 0 vs. 1+ arrests"
    - "Poisson GLM with a log link, because the outcome is a non-negative count"
    - "Ordinal logistic regression, since the count values can be ranked"
  answer: 2
  explanation: "Count outcomes require a model that respects their distributional properties: non-negative integers, typically right-skewed, with variance that scales with the mean. OLS is inappropriate because it can generate negative predictions and assumes constant variance. Binary recoding discards information about how many arrests occurred. Ordinal logistic regression is for ordered categorical outcomes, not continuous counts. Poisson GLM with a log link is the standard choice — the log link ensures predicted counts are always positive, and the Poisson distribution models event counts that accumulate over exposure time. If the data show overdispersion (variance > mean), a negative binomial GLM is the natural extension."

- question: "In a logistic regression, the maximum likelihood estimates of the coefficients cannot be solved analytically and must be found through iterative numerical optimization."
  type: true-false
  answer: true
  explanation: "Unlike OLS, which has a closed-form normal equations solution (β = (X'X)⁻¹X'y), the log-likelihood of a logistic regression has no closed-form maximizer. Coefficients are estimated via iteratively reweighted least squares (IRWLS) or gradient-based methods that converge to the MLE numerically. This is why GLMs 'may fail to converge' — a warning that OLS never produces — and why sparse data or perfect separation (a predictor that perfectly predicts the outcome) causes problems."

- question: "If a logistic regression coefficient for predictor X is positive, increasing X by one unit always increases the predicted probability of the outcome by a constant amount, regardless of the current value of X or the baseline probability."
  type: true-false
  answer: false
  explanation: "The logit link makes the effect of X on probability nonlinear. The same one-unit change in X produces a constant change in log-odds, but the corresponding change in probability depends on the current probability level: the sigmoid curve is steepest near p = 0.5 and flattens near p = 0 or p = 1. So the marginal effect of X on probability is largest at moderate probabilities and smallest at extreme probabilities. This is why researchers report marginal effects (change in predicted probability at specified baseline values) rather than raw coefficients when communicating to non-technical audiences."

- question: "Explain why an odds ratio of 1.5 does NOT mean that the probability of the outcome is 50% higher for a one-unit increase in a predictor."
  type: short-answer
  answer: "An odds ratio of 1.5 means the odds (p/(1−p)) increase by 50%, not the probability. The relationship between odds and probability is nonlinear: probability = odds/(1 + odds). So if the baseline probability is 0.50 (odds = 1.0), an OR of 1.5 gives odds of 1.5 and probability of 0.60 — a 10 percentage-point increase, not 50%. The conversion from odds ratios to probability differences depends entirely on the baseline probability, and misreading ORs as probability ratios systematically overstates effect sizes when outcomes are common."
  explanation: "The rare-outcome approximation — where OR ≈ relative risk — only holds when the baseline probability is small (roughly below 10%). For common outcomes in social science research (employment, health status, voting), odds ratios substantially exaggerate relative risks. This is not merely a technical detail: policy-relevant communication of risk requires converting ORs to absolute probability differences or relative risks, which demands knowing or specifying the baseline probability."
```

## Explainer

You already understand logistic regression for binary outcomes — that a probability bounded between 0 and 1 cannot be modeled with an unbounded linear predictor, so we apply the **logit transformation** (log-odds: ln[p/(1−p)]) to map probabilities to the real line. This transformation is invertible via the **sigmoid function**, and your background with exponential functions and graphs helps you see why: e^x / (1 + e^x) produces the characteristic S-curve that squeezes any linear combination of predictors into the (0,1) interval. The key interpretive fact is that logistic regression coefficients represent changes in log-odds, which can be exponentiated to **odds ratios** — a more interpretable but still nonlinear quantity. An odds ratio of 1.5 means the odds of the outcome are 50% higher per unit increase in the predictor, not that the probability increases by 50 percentage points.

The **Generalized Linear Model (GLM)** framework unifies logistic regression with a broader family of models for non-normal outcomes. Every GLM has three components: a **random component** (the outcome's probability distribution — Bernoulli, Poisson, binomial, gamma), a **systematic component** (the linear predictor Xβ), and a **link function** (the transformation connecting the mean of the distribution to the linear predictor). For logistic regression, the distribution is Bernoulli and the link is logit. For count data where events accumulate over time — arrest counts, hospital admissions, species occurrences — the appropriate choice is typically a **Poisson GLM** with a log link, because counts are non-negative and Poisson-distributed. This is where your background in partial derivatives becomes practically important: GLMs are fit by maximum likelihood via iteratively reweighted least squares (IRWLS), an optimization procedure that requires computing derivatives of the log-likelihood.

A common situation in social science is an outcome with more than two ordered categories — survey responses like "strongly disagree / disagree / agree / strongly agree," health status coded as poor/fair/good/excellent, or educational attainment in stages. For these, **ordinal logistic regression** (the proportional odds model) models the cumulative probability of being at or below each threshold. The key assumption is that a single set of coefficients explains the transition at every threshold — the same predictor effect governs the move from poor to fair health as the move from fair to good health. When this assumption is violated, you need a less constrained model. For unordered categorical outcomes — political party choice among three parties, choice of transportation mode — **multinomial logistic regression** models each category against a reference category simultaneously, producing a set of coefficients for each non-reference outcome.

Throughout the GLM family, **model fit** is assessed differently than in OLS. There is no direct equivalent to R². Instead, researchers compare **deviance** (analogous to residual sum of squares, based on log-likelihood ratios) between nested models using chi-squared tests, or use information criteria (AIC, BIC) to compare non-nested models penalizing for complexity. Predicted probabilities and marginal effects — the change in predicted probability for a one-unit change in a predictor, holding others at specified values — are typically more interpretable than raw coefficients, particularly for communicating findings to non-technical audiences.

The practical skill is choosing the right GLM for the right outcome structure: binary outcomes → logistic; counts → Poisson (or negative binomial if overdispersed); ordered categories → ordinal logistic; unordered categories → multinomial logistic. Each choice reflects assumptions about the data-generating process, and your background in optimization helps you understand why these models are estimated iteratively rather than analytically — unlike OLS, there is no closed-form solution for the MLE of a GLM, and convergence is not always guaranteed.
