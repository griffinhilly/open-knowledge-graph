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

## Questions

```yaml
- question: "You compare three models on the same dataset. Model A: AIC=450, BIC=480. Model B: AIC=440, BIC=510. Model C: AIC=460, BIC=465. What does the disagreement between AIC and BIC for Model B suggest?"
  type: multiple-choice
  options:
    - "Model B has a computational error — AIC and BIC should always agree"
    - "Model B fits the data best in absolute terms since it has the lowest AIC"
    - "Model B likely has more parameters; BIC penalizes them more harshly, so AIC favors it for prediction while BIC prefers a simpler alternative"
    - "Model B should be rejected outright because the two criteria disagree"
  answer: 2
  explanation: "Disagreement between AIC and BIC is common when a model adds parameters that improve fit substantially. AIC penalizes each parameter by 2; BIC penalizes by ln(n), which exceeds 2 for any n > 8. Model B's lowest AIC means it best balances fit and complexity for prediction purposes, but BIC's harsher penalty discourages its extra parameters. The right choice depends on whether you prioritize predictive accuracy (AIC) or identifying the true model structure (BIC)."

- question: "A researcher fits a model predicting Y (AIC = 300) and a model predicting log(Y) (AIC = 250), and concludes the log-linear model is better. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — lower AIC always indicates a better model regardless of the response variable"
    - "AIC cannot be used for log-linear models, only for ordinary linear regression"
    - "AIC values are only comparable when models use the same response variable on the same dataset; the two likelihoods live on different scales"
    - "The researcher should use BIC instead, which corrects for response variable transformations"
  answer: 2
  explanation: "This is a critical caveat of information criteria: AIC and BIC can only be compared across models with the same response variable on the same dataset. When you predict log(Y) instead of Y, the likelihood function changes fundamentally — it is computed in the space of log(Y). The AIC=250 and AIC=300 are not on the same scale and cannot be meaningfully compared. To compare log and non-log specifications, a different approach is needed (e.g., cross-validation on the original scale)."

- question: "A model that achieves the lowest AIC in a comparison set can be considered a well-fitting model in an absolute sense."
  type: true-false
  answer: false
  explanation: "False. AIC and BIC are relative comparison tools — a lower AIC means a model is better than its competitors in the candidate set, but says nothing about absolute fit. All models in the comparison could be terrible, and the 'winner' by AIC is merely the least bad. This is why information criteria must always be paired with residual diagnostics and substantive scrutiny: winning a comparison does not certify a model's adequacy."

- question: "For any sample size larger than approximately 8 observations, BIC imposes a stricter penalty per additional parameter than AIC does."
  type: true-false
  answer: true
  explanation: "True. AIC penalizes each parameter by 2. BIC penalizes each parameter by ln(n). Since ln(8) ≈ 2.08, for n > 8 we have ln(n) > 2, so BIC's per-parameter penalty exceeds AIC's. For large samples (e.g., n = 1000, ln(n) ≈ 6.9), BIC is substantially harsher. This is why BIC consistently selects simpler models than AIC when sample sizes are moderate to large."

- question: "What is the fundamental difference in theoretical motivation between AIC and BIC, and when would you prefer each?"
  type: short-answer
  answer: "AIC is motivated by minimizing predictive error: it selects the model that best predicts new data from the same generating process. BIC is motivated by identifying the true model: it is consistent, meaning it selects the true model with probability 1 as n → ∞ if the true model is among the candidates. Prefer AIC when building a predictive tool; prefer BIC when testing theoretical structure and you believe the true model is in your candidate set."
  explanation: "These different motivations matter in practice. A researcher testing competing economic theories wants BIC: given enough data, BIC will identify the correct model structure. A forecasting practitioner wants AIC: it optimizes for out-of-sample prediction accuracy even when the 'true' model is never in the candidate set. Neither criterion is universally correct — the right choice depends on the scientific question being asked."
```

## Explainer

From your study of R² and adjusted R², you already know the central tension in model selection: adding regressors always improves in-sample fit, but not all of those regressors improve genuine explanatory power. Adjusted R² penalizes for extra parameters, but only for linear models estimated by OLS. **Information criteria** — principally AIC (Akaike Information Criterion) and BIC (Bayesian Information Criterion) — generalize this principle to any model estimated by maximum likelihood, making them applicable to logit, probit, count models, survival models, or any likelihood-based estimation.

Both criteria share the same structure: they reward fit and penalize complexity. Specifically, AIC = −2 ln(L̂) + 2k and BIC = −2 ln(L̂) + k ln(n), where L̂ is the maximized likelihood, k is the number of estimated parameters, and n is the sample size. A larger log-likelihood means better fit (less negative, so AIC and BIC go down). More parameters push AIC and BIC up. You want the model with the **lowest** AIC or BIC — lower means a better balance of fit and parsimony.

The key difference is the size of the penalty. BIC penalizes each parameter by ln(n) rather than 2. For any sample larger than about 8 observations, ln(n) > 2, so BIC penalizes additional parameters more harshly than AIC does. In practice, BIC tends to select simpler models. Theoretically, AIC is motivated by minimizing predictive error (it targets the approximation that best predicts new data), while BIC is motivated by identifying the true model from the candidate set (it is consistent: as n → ∞, BIC selects the true model with probability 1, if it is among the candidates). Neither goal is universally correct — the right criterion depends on whether you are building a predictive tool or testing a theoretical structure.

Two critical caveats prevent misuse. First, AIC and BIC can only be compared across models fit to the **same dataset with the same response variable**. Comparing AIC from a model of log(Y) to one of Y is invalid — the likelihoods live on different scales. Second, a lower AIC or BIC means only that one model is relatively better than another; it says nothing about whether either model fits well in an absolute sense. A model with AIC = 500 may be far better than AIC = 600, yet both may be terrible. Information criteria are selection tools, not validation tools — always pair them with residual diagnostics and substantive scrutiny of the winning model.
