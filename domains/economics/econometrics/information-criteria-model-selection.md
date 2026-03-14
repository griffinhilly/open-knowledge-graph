---
id: information-criteria-model-selection
title: 'Information Criteria: AIC and BIC for Model Selection'
domain: economics
course: econometrics
prerequisites:
- id: multiple-regression-model
  type: hard
- id: r-squared-and-model-fit
  type: hard
tags:
- model-selection
- information-criteria
- aic
- bic
stage: formal-systems
status: draft
---

# Information Criteria: AIC and BIC for Model Selection

## Core Idea
AIC and BIC are criteria that balance fit and parsimony when choosing among competing models. Both penalize the number of parameters, with BIC imposing a stronger penalty that favors simpler models. Lower values indicate better models.

## How It's Best Learned
Compare models of different complexities using AIC or BIC. Understand that AIC asymptotically selects the best predictor, while BIC is consistent for model selection when the true model is in the candidate set.

## Common Misconceptions
AIC and BIC are not goodness-of-fit measures; lower values don't mean the model fits well, only that it's better relative to alternatives in the comparison set. The absolute values cannot be compared across different samples or response transformations.
