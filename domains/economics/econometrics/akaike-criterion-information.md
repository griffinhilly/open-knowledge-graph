---
id: akaike-criterion-information
title: 'Information Criteria: AIC and BIC for Model Selection'
domain: economics
course: econometrics
prerequisites:
- id: model-specification-testing
  type: hard
- id: maximum-likelihood-econometrics
  type: soft
builds-toward:
- quasi-maximum-likelihood-estimation
tags:
- model-selection
- information-criteria
stage: formal-systems
status: draft
---

# Information Criteria: AIC and BIC for Model Selection

## Core Idea
The Akaike Information Criterion (AIC) and Bayesian Information Criterion (BIC) provide data-driven methods for comparing non-nested models by balancing goodness-of-fit against parameter count. BIC penalizes complexity more heavily; both help select parsimonious models that generalize well to out-of-sample data.

## How It's Best Learned
Apply AIC/BIC to compare multiple specifications of the same relationship and observe how the information criteria penalize additional regressors.

## Common Misconceptions
Information criteria values are not interpretable on their own absolute scale—only differences between models matter; lower AIC/BIC is better.
