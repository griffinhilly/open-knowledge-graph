---
id: logistic-regression-biostatistics
title: Logistic Regression in Biostatistics
domain: health-and-human-development
course: biostatistics
prerequisites:
- id: linear-regression
  type: hard
- id: study-design-biostatistics
  type: soft
- id: probability-axioms
  type: soft
builds-toward:
- diagnostic-test-evaluation
- roc-curves-biostatistics
- propensity-score-methods-biostatistics
tags:
- logistic-regression
- odds-ratio
- binary-outcome
- maximum-likelihood
stage: advanced
status: validated
---

# Logistic Regression in Biostatistics

## Core Idea
Logistic regression models binary outcomes (disease/no disease, death/survival) by relating the log-odds of the outcome to a linear combination of predictors: log(p/(1-p)) = beta_0 + beta_1*x_1 + ... + beta_k*x_k. The logit transformation maps probabilities from the bounded [0,1] interval to the unbounded real line, making linear modeling appropriate. Each coefficient beta_j represents the change in log-odds per unit increase in x_j, and exp(beta_j) gives the adjusted odds ratio — the multiplicative change in odds of the outcome for a one-unit increase in the predictor, holding all other variables constant. Logistic regression is estimated by maximum likelihood rather than least squares, and it is the workhorse model for binary health outcomes throughout clinical research and epidemiology.

## Questions

```yaml
- question: "A logistic regression model of diabetes risk includes BMI as a predictor and yields a coefficient of 0.08 for BMI. What is the correct interpretation?"
  type: multiple-choice
  options:
    - "Each 1-unit increase in BMI increases the probability of diabetes by 0.08"
    - "Each 1-unit increase in BMI increases the odds of diabetes by a factor of exp(0.08) ≈ 1.083, or about 8.3%"
    - "Each 1-unit increase in BMI increases the log-probability of diabetes by 0.08"
    - "BMI has a weak association with diabetes because the coefficient is close to zero"
  answer: 1
  explanation: "In logistic regression, coefficients are on the log-odds scale. The coefficient of 0.08 means each 1-unit increase in BMI raises the log-odds of diabetes by 0.08. Exponentiating gives the odds ratio: exp(0.08) ≈ 1.083, meaning the odds of diabetes increase by about 8.3% per BMI unit. Option A is the most common error — the coefficient is NOT a change in probability because the logit link makes the relationship nonlinear on the probability scale. A coefficient close to zero on the log-odds scale can still represent a substantial effect when the predictor has a wide range (BMI might vary by 30+ units)."

- question: "Logistic regression can be fit using ordinary least squares (OLS) by treating the binary outcome (0/1) as a continuous variable."
  type: true-false
  answer: false
  explanation: "OLS on a binary outcome (the linear probability model) can produce predicted probabilities outside [0,1], has heteroskedastic errors by construction, and does not properly model the nonlinear relationship between predictors and probability. Logistic regression uses maximum likelihood estimation, which finds the parameter values that maximize the probability of observing the actual data given the model. MLE produces consistent, asymptotically efficient estimates and naturally constrains predicted probabilities to [0,1] through the logistic function."

- question: "A study reports that smokers have an adjusted odds ratio of 3.2 for lung cancer compared to non-smokers. If the baseline probability of lung cancer is 1%, can you approximate the risk ratio from this odds ratio?"
  type: multiple-choice
  options:
    - "No — odds ratios and risk ratios are fundamentally different quantities that can never be compared"
    - "Yes — when the outcome is rare (1%), the odds ratio closely approximates the risk ratio, so the risk is approximately 3.2 times higher for smokers"
    - "Yes — the risk ratio equals the odds ratio divided by 2"
    - "No — you need the exact number of cases and controls to convert"
  answer: 1
  explanation: "When the outcome probability is low (conventionally < 10%), the odds ratio closely approximates the risk ratio. This is because odds = p/(1-p) ≈ p when p is small, so the ratio of odds approximates the ratio of probabilities. At 1% baseline probability, OR = 3.2 means the risk for smokers is approximately 3.2% — very close to what a risk ratio of 3.2 would imply. This rare-disease approximation breaks down for common outcomes, where odds ratios substantially overestimate risk ratios."

- question: "Why does logistic regression use the logit (log-odds) link function rather than modeling probability directly as a linear function of predictors?"
  type: short-answer
  answer: "Probabilities are bounded between 0 and 1, but a linear function of predictors is unbounded — it can produce values below 0 or above 1, which are nonsensical as probabilities. The logit function log(p/(1-p)) maps probabilities from [0,1] to (-infinity, +infinity), making linear modeling mathematically valid. The logistic function (the inverse of logit) then maps any linear predictor value back to a valid probability. This also produces a natural interpretation: coefficients represent log-odds ratios, which are additive on the log scale and multiplicative on the odds scale."
  explanation: "The logit link is not arbitrary — it arises naturally from the exponential family and provides the canonical link for Bernoulli distributed outcomes. It also connects logistic regression to case-control study design: because the odds ratio is invariant to outcome-based sampling, logistic regression coefficients estimated from case-control data have the same interpretation as those from cohort data (only the intercept changes). This property makes logistic regression the natural model for case-control studies."
```

## Explainer

Linear regression assumes the outcome is continuous and unbounded — systolic blood pressure, cholesterol level, or body weight. But many of the most important questions in health research involve binary outcomes: does the patient have the disease or not? Did the treatment succeed or fail? Did the patient survive five years or not? You cannot model a 0/1 outcome with ordinary linear regression because predicted values can fall outside [0,1], the errors are not normally distributed, and the variance depends on the mean. Logistic regression solves all three problems by modeling a transformed version of the outcome probability.

The **logit transformation** converts a probability p to the log-odds: logit(p) = log(p/(1-p)). If p = 0.5, the odds are 1:1 and the log-odds are 0. As p approaches 1, the log-odds go to positive infinity; as p approaches 0, they go to negative infinity. This maps the constrained probability to the entire real line, so a linear combination of predictors always produces a valid probability when passed through the inverse logit (logistic) function: p = 1/(1 + exp(-z)), where z = beta_0 + beta_1*x_1 + ... The resulting S-shaped curve ensures that predicted probabilities are always between 0 and 1, regardless of the predictor values.

The coefficients of logistic regression are interpreted on the **log-odds scale**. A coefficient of 0.5 for a predictor means that a one-unit increase raises the log-odds of the outcome by 0.5. Exponentiating gives the **odds ratio**: exp(0.5) ≈ 1.65, meaning the odds of the outcome increase by 65% per unit of the predictor. This multiplicative interpretation is constant across the predictor range on the odds scale but not on the probability scale — the change in probability for a one-unit increase depends on where you start. Moving BMI from 22 to 23 changes diabetes probability differently than moving from 35 to 36, even though the log-odds change is the same.

Logistic regression is fit by **maximum likelihood estimation** rather than least squares. MLE finds the coefficient values that make the observed data most probable under the model. There is no closed-form solution as there is for OLS; instead, iterative algorithms (typically Newton-Raphson or iteratively reweighted least squares) converge to the maximum. Model fit is assessed through deviance, the Hosmer-Lemeshow test, or information criteria rather than R-squared. For prediction, the area under the ROC curve (AUC) quantifies how well the model discriminates between cases and non-cases — a topic you will encounter next in diagnostic test evaluation.
