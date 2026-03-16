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

## Explainer

Every time you add a variable to a regression, the model fits the sample data better — the residuals shrink and R² rises. But that improvement might be pure noise: the variable captures random patterns in this dataset that won't repeat in new data. Model selection criteria like **AIC** (Akaike Information Criterion) and **BIC** (Bayesian Information Criterion) formalize the tradeoff between fit and parsimony. From your work on model specification testing, you already know that overfitting is a real danger. AIC and BIC give you a principled way to penalize it.

Both criteria follow the same logic: start with a measure of fit (typically the log-likelihood from maximum likelihood estimation, which you've already learned) and subtract a penalty proportional to the number of parameters. The formula is AIC = −2 ln(L̂) + 2k and BIC = −2 ln(L̂) + k ln(n), where L̂ is the maximized likelihood, k is the number of parameters, and n is the sample size. The first term rewards fit; the second penalizes complexity. Lower values are better, and you choose the model with the lowest criterion value. Because AIC's penalty is 2k regardless of sample size, while BIC's penalty k ln(n) grows with n, **BIC penalizes additional parameters more heavily**, especially in large samples — it leans toward simpler models.

The intuition is clearest when comparing two nested models: a restricted model with fewer parameters and an unrestricted one with more. Adding a variable decreases −2 ln(L̂) by some amount. If that decrease exceeds the penalty (2 for AIC, ln(n) for BIC), the richer model wins; otherwise, the simpler model is preferred. In this sense, AIC and BIC are like automatic hypothesis tests, but they don't require a single null hypothesis — you can compare any set of models, **including non-nested specifications** like different functional forms or different regressor sets, which standard F-tests cannot handle.

One crucial point the Core Idea flags: AIC and BIC values have no meaningful absolute interpretation. A model with AIC = −340 is not "worse" than one with AIC = −200 from a different dataset — the scales are incomparable. What matters is the *difference* between criteria for models estimated on the same data. As a rough rule of thumb, differences in AIC of less than 2 suggest the models are roughly equivalent; differences greater than 10 suggest strong evidence favoring the lower-AIC model. Because AIC favors predictive accuracy while BIC favors the "true" model (under certain assumptions), they will sometimes disagree — when they do, the choice depends on your goal: prediction (use AIC) or identifying the data-generating process (use BIC).
