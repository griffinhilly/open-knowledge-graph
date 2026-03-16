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

## Explainer

You already know that linear regression models the expected value of a continuous outcome as a linear function of predictors. The problem with applying this directly to a binary outcome — voted or didn't, employed or not, sick or healthy — is that predicted values can fall outside [0,1], probabilities are bounded, and the relationship between predictors and the probability of an event is almost never linear across the full range. **Logistic regression** solves this by modeling the **log-odds** of the outcome rather than the probability directly. The log-odds (also called the **logit**) is the natural logarithm of the odds ratio, and it can range from negative to positive infinity — making it a natural target for linear modeling.

The key transformation is the **logistic function**: it maps any real number to a value strictly between 0 and 1, producing an S-shaped curve. When your predictor increases, the predicted probability rises steeply in the middle of the range and flattens near 0 and 1. This S-curve is not a quirk of the model — it captures the realistic compression that happens as probabilities approach their bounds. Estimating logistic regression means finding the coefficients that maximize the likelihood of observing the actual binary outcomes in your data (maximum likelihood estimation), rather than minimizing squared residuals as in OLS.

The hardest part of logistic regression is interpreting coefficients. A logistic regression coefficient is not the change in probability per unit increase in a predictor — it is the change in the **log-odds**. Because log-odds are unintuitive, researchers typically convert them to **odds ratios** by exponentiating the coefficient (e^β). An odds ratio of 1.5 means the odds of the outcome are 50% higher for a one-unit increase in the predictor. But odds ratios are also slippery: they are not the same as relative risks, and they can be misleading when baseline probabilities are high. The most interpretable quantities are often **predicted probabilities** at substantively meaningful values of the predictors — computed by plugging values into the logistic function directly. These are more honest about the non-linearity and should accompany any substantive interpretation.

**Model fit** in logistic regression cannot be assessed with R². Instead, you use a combination of the **likelihood ratio test** (comparing your model to a null model), classification metrics like accuracy and the **area under the ROC curve** (AUC), and pseudo-R² statistics like McFadden's R² — but the last of these should never be interpreted on the 0–1 scale of OLS R². AUC is particularly useful in social science applications: a value of 0.7 means the model correctly ranks 70% of all outcome-present/outcome-absent pairs, which is often a more meaningful summary than raw accuracy.

Extensions matter for social science work. **Multinomial logistic regression** applies when the outcome has more than two unordered categories (e.g., voted Democratic, Republican, third-party, abstained). **Ordinal logistic regression** — the proportional odds model — applies when categories have a meaningful order (e.g., low/medium/high) and assumes that the same set of predictors shifts the cumulative odds proportionally across all thresholds. These two are not interchangeable: ordinal logit is more parsimonious when ordering is meaningful, but its proportional odds assumption should always be tested.
