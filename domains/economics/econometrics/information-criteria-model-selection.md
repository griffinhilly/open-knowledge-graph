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

## Explainer

From your study of R² and adjusted R², you already know the central tension in model selection: adding regressors always improves in-sample fit, but not all of those regressors improve genuine explanatory power. Adjusted R² penalizes for extra parameters, but only for linear models estimated by OLS. **Information criteria** — principally AIC (Akaike Information Criterion) and BIC (Bayesian Information Criterion) — generalize this principle to any model estimated by maximum likelihood, making them applicable to logit, probit, count models, survival models, or any likelihood-based estimation.

Both criteria share the same structure: they reward fit and penalize complexity. Specifically, AIC = −2 ln(L̂) + 2k and BIC = −2 ln(L̂) + k ln(n), where L̂ is the maximized likelihood, k is the number of estimated parameters, and n is the sample size. A larger log-likelihood means better fit (less negative, so AIC and BIC go down). More parameters push AIC and BIC up. You want the model with the **lowest** AIC or BIC — lower means a better balance of fit and parsimony.

The key difference is the size of the penalty. BIC penalizes each parameter by ln(n) rather than 2. For any sample larger than about 8 observations, ln(n) > 2, so BIC penalizes additional parameters more harshly than AIC does. In practice, BIC tends to select simpler models. Theoretically, AIC is motivated by minimizing predictive error (it targets the approximation that best predicts new data), while BIC is motivated by identifying the true model from the candidate set (it is consistent: as n → ∞, BIC selects the true model with probability 1, if it is among the candidates). Neither goal is universally correct — the right criterion depends on whether you are building a predictive tool or testing a theoretical structure.

Two critical caveats prevent misuse. First, AIC and BIC can only be compared across models fit to the **same dataset with the same response variable**. Comparing AIC from a model of log(Y) to one of Y is invalid — the likelihoods live on different scales. Second, a lower AIC or BIC means only that one model is relatively better than another; it says nothing about whether either model fits well in an absolute sense. A model with AIC = 500 may be far better than AIC = 600, yet both may be terrible. Information criteria are selection tools, not validation tools — always pair them with residual diagnostics and substantive scrutiny of the winning model.
