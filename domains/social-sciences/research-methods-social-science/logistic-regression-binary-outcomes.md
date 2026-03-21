---
id: logistic-regression-binary-outcomes
title: Logistic Regression for Binary Outcomes
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: linear-regression-social-science
  type: hard
- id: matrices-intro
  type: soft
- id: probability-mass-functions
  type: soft
- id: logarithmic-functions-review
  type: soft
builds-toward:
- structural-equation-modeling-latent
tags:
- logistic
- binary
- odds-ratios
- probability
stage: advanced
status: draft
---

# Logistic Regression for Binary Outcomes

## Core Idea
Applies logistic regression to binary and categorical outcomes common in social research, including voting, employment, health behaviors, and participation. Covers odds ratio interpretation, predicted probabilities, model fit, and extensions to multinomial outcomes. Emphasizes differences from linear regression.

## How It's Best Learned
Estimate logistic models on social outcomes, calculate and interpret odds ratios, create predicted probability plots, compare with linear probability models.

## Common Misconceptions
- Coefficients in logistic regression are like regression coefficients
- Pseudo R-squared values are comparable across datasets
- Multinomial logit and ordinal logit are the same

## Questions

```yaml
- question: "A researcher reports that a logistic regression coefficient for education (in years) on voting behavior is β = 0.15. A colleague concludes that each additional year of education raises the probability of voting by 15 percentage points. What is wrong with this interpretation?"
  type: multiple-choice
  options:
    - "Nothing is wrong — logistic regression coefficients directly represent probability changes"
    - "The coefficient 0.15 represents a change in log-odds, not probability; the actual probability change is non-constant and depends on the baseline probability"
    - "The coefficient must first be squared before interpreting it as a probability change"
    - "The interpretation is wrong because logistic regression reports marginal effects at the mean automatically"
  answer: 1
  explanation: "Logistic regression coefficients are changes in log-odds per unit increase in the predictor — not probability changes. Because the logistic function is S-shaped, the same log-odds change corresponds to very different probability changes depending on where you are on the curve. Near 50% probability, a 0.15 log-odds change might shift probability ~3–4 points; near 5% or 95% it shifts much less. To communicate results honestly, researchers should report predicted probabilities at substantively meaningful predictor values."

- question: "Why does logistic regression model the log-odds of an outcome rather than the probability directly?"
  type: multiple-choice
  options:
    - "Log-odds are easier to compute than probabilities on modern hardware"
    - "It is a historical convention with no mathematical justification"
    - "Predicted probabilities from a linear model can fall outside [0,1], and the relationship between predictors and probability is rarely linear across the full range"
    - "The logistic function eliminates the need for maximum likelihood estimation, simplifying inference"
  answer: 2
  explanation: "A linear model applied directly to a binary outcome has two fatal flaws: it can predict probabilities below 0 or above 1, and it assumes the effect of a predictor on probability is constant from 0% to 100%, which is unrealistic. Probabilities compress near their bounds. The logistic function maps any real-valued linear predictor to (0,1) and produces an S-shaped curve that naturally captures this compression. The log-odds transformation is the mathematical device that converts the bounded probability scale to the unbounded real line where linear modeling is valid."

- question: "An odds ratio greater than 1 for a predictor in a logistic regression model means that subjects with higher values of that predictor are more likely than not (probability > 50%) to experience the outcome."
  type: true-false
  answer: false
  explanation: "An odds ratio greater than 1 means the odds of the outcome *increase* with the predictor — relative to a baseline. Whether the outcome probability exceeds 50% depends on the baseline probability, which is not captured by the odds ratio alone. For example, if the baseline probability is 5%, an OR of 3.0 raises the odds from 0.053 to 0.158, corresponding to a probability of ~14% — still well below 50%. Odds ratios are relative measures; absolute probability requires knowing where you start."

- question: "A logistic regression coefficient can be converted to an odds ratio by exponentiating it (e^β)."
  type: true-false
  answer: true
  explanation: "This is exactly correct. The logistic regression model is log(odds) = β₀ + β₁X, so β₁ = log(odds₁) − log(odds₀) = log(odds₁/odds₀). Exponentiating both sides gives e^β₁ = odds₁/odds₀ — the odds ratio. An OR of 1.5 means the odds are 50% higher for a one-unit increase in X. This transformation is standard in reporting logistic regression results, though predicted probabilities are often more interpretable."

- question: "Why are predicted probabilities often more informative than odds ratios when communicating logistic regression results to a non-technical audience?"
  type: short-answer
  answer: "Odds ratios are relative measures that depend on a baseline and are often misread as relative risks (which they are not, especially when baseline probabilities are high). Predicted probabilities, computed by plugging specific predictor values into the logistic function, give concrete, bounded quantities — 'a person with 16 years of education has a 73% predicted probability of voting' — that are intuitive and honest about the non-linearity of the relationship. They make the S-shaped nature of the model visible and avoid the common misinterpretation of OR as a percentage change in probability."
  explanation: "The non-linearity of logistic regression means that a predictor's effect on probability is large in the middle of the distribution and small at the extremes. Odds ratios hide this variation. Predicted probabilities at representative or meaningful values of the predictors (e.g., average-income vs. high-income voter) show the practical magnitude of the effect in ways that are directly interpretable."
```

## Explainer

You already know that linear regression models the expected value of a continuous outcome as a linear function of predictors. The problem with applying this directly to a binary outcome — voted or didn't, employed or not, sick or healthy — is that predicted values can fall outside [0,1], probabilities are bounded, and the relationship between predictors and the probability of an event is almost never linear across the full range. **Logistic regression** solves this by modeling the **log-odds** of the outcome rather than the probability directly. The log-odds (also called the **logit**) is the natural logarithm of the odds ratio, and it can range from negative to positive infinity — making it a natural target for linear modeling.

The key transformation is the **logistic function**: it maps any real number to a value strictly between 0 and 1, producing an S-shaped curve. When your predictor increases, the predicted probability rises steeply in the middle of the range and flattens near 0 and 1. This S-curve is not a quirk of the model — it captures the realistic compression that happens as probabilities approach their bounds. Estimating logistic regression means finding the coefficients that maximize the likelihood of observing the actual binary outcomes in your data (maximum likelihood estimation), rather than minimizing squared residuals as in OLS.

The hardest part of logistic regression is interpreting coefficients. A logistic regression coefficient is not the change in probability per unit increase in a predictor — it is the change in the **log-odds**. Because log-odds are unintuitive, researchers typically convert them to **odds ratios** by exponentiating the coefficient (e^β). An odds ratio of 1.5 means the odds of the outcome are 50% higher for a one-unit increase in the predictor. But odds ratios are also slippery: they are not the same as relative risks, and they can be misleading when baseline probabilities are high. The most interpretable quantities are often **predicted probabilities** at substantively meaningful values of the predictors — computed by plugging values into the logistic function directly. These are more honest about the non-linearity and should accompany any substantive interpretation.

**Model fit** in logistic regression cannot be assessed with R². Instead, you use a combination of the **likelihood ratio test** (comparing your model to a null model), classification metrics like accuracy and the **area under the ROC curve** (AUC), and pseudo-R² statistics like McFadden's R² — but the last of these should never be interpreted on the 0–1 scale of OLS R². AUC is particularly useful in social science applications: a value of 0.7 means the model correctly ranks 70% of all outcome-present/outcome-absent pairs, which is often a more meaningful summary than raw accuracy.

Extensions matter for social science work. **Multinomial logistic regression** applies when the outcome has more than two unordered categories (e.g., voted Democratic, Republican, third-party, abstained). **Ordinal logistic regression** — the proportional odds model — applies when categories have a meaningful order (e.g., low/medium/high) and assumes that the same set of predictors shifts the cumulative odds proportionally across all thresholds. These two are not interchangeable: ordinal logit is more parsimonious when ordering is meaningful, but its proportional odds assumption should always be tested.
