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
- id: adjusted-r-squared-model-comparison
  type: soft
- id: hausman-test-fe-versus-re
  type: soft
builds-toward:
- quasi-maximum-likelihood-estimation
tags:
- model-selection
- information-criteria
stage: advanced
status: validated
---
# Information Criteria: AIC and BIC for Model Selection

## Core Idea
The Akaike Information Criterion (AIC) and Bayesian Information Criterion (BIC) provide data-driven methods for comparing non-nested models by balancing goodness-of-fit against parameter count. BIC penalizes complexity more heavily; both help select parsimonious models that generalize well to out-of-sample data.

## How It's Best Learned
Apply AIC/BIC to compare multiple specifications of the same relationship and observe how the information criteria penalize additional regressors.

## Common Misconceptions
Information criteria values are not interpretable on their own absolute scale—only differences between models matter; lower AIC/BIC is better.

## Questions

```yaml
- question: "A researcher estimates Model A on one dataset and gets AIC = −150. She estimates Model B on a different dataset and gets AIC = −200. She concludes Model B fits its data better. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "AIC can only be used when models are nested; non-nested models require a different criterion"
    - "She should compare BIC values instead of AIC for cross-dataset comparisons"
    - "AIC values are not comparable across different datasets — only differences between models estimated on the same data are meaningful"
    - "A lower AIC always indicates worse fit, so Model A is actually the better model"
  answer: 2
  explanation: "AIC values have no meaningful absolute interpretation. The scale depends on the dataset, the likelihood function, and the number of observations. Comparing AIC = −150 from one study to AIC = −200 from another is like comparing exam scores from two different tests with different grading scales. Only *differences* in AIC between models fitted to the exact same dataset can guide model selection. This is stated explicitly in the Common Misconceptions section and is the most frequent misuse of information criteria in practice."

- question: "You are comparing five regression models on the same dataset. Their AIC values are −410, −408, −397, −385, and −420. Using the standard rule of thumb (|ΔAIC| < 2 suggests equivalent models, |ΔAIC| > 10 suggests strong evidence), which pair of models is effectively equivalent?"
  type: multiple-choice
  options:
    - "AIC = −410 and AIC = −408 (difference = 2)"
    - "AIC = −408 and AIC = −397 (difference = 11)"
    - "AIC = −397 and AIC = −385 (difference = 12)"
    - "AIC = −420 and AIC = −410 (difference = 10)"
  answer: 0
  explanation: "By the rule of thumb, a difference of ≤ 2 in AIC indicates the models are roughly equivalent in their fit-complexity tradeoff — neither is clearly preferred. The pair with AIC = −410 and −408 has a difference of exactly 2, placing it at the edge of equivalence. The pairs with differences of 10–12 represent moderate to strong evidence in favor of the lower-AIC model. Note that the model with AIC = −420 is the best overall — lower (more negative) AIC is always better."

- question: "BIC penalizes each additional parameter more heavily than AIC when the sample size is larger than about 8 observations, because its complexity penalty grows with the logarithm of sample size."
  type: true-false
  answer: true
  explanation: "AIC's penalty for each additional parameter is a fixed 2 regardless of sample size. BIC's penalty is ln(n) per parameter, which exceeds 2 once n > e² ≈ 7.4. For typical econometric datasets with hundreds or thousands of observations (ln(1000) ≈ 6.9), BIC imposes roughly 3–4 times the per-parameter penalty of AIC. This is why BIC consistently selects sparser models than AIC in large samples, and why the two criteria increasingly disagree as sample size grows."

- question: "A model with AIC = −400 is preferable to one with AIC = −200, regardless of which dataset each was estimated on."
  type: true-false
  answer: false
  explanation: "AIC values from different datasets cannot be compared. The absolute value of AIC depends on the number of observations, the scale of the likelihood, and the distributional assumptions — none of which are held constant across different datasets. Only within-dataset comparisons are meaningful. This is perhaps the most common misuse of information criteria: treating AIC as an absolute measure of model quality rather than a relative tool for comparing models on the same data."

- question: "A researcher is building a model to predict next quarter's GDP growth and wants to select among several specifications. A colleague is trying to identify which macroeconomic variables are 'truly' causal drivers of growth. Should they use the same criterion (AIC or BIC)? Explain why or why not."
  type: short-answer
  answer: "No. The prediction-focused researcher should use AIC, which is calibrated to minimize out-of-sample prediction error and tolerates slightly more complex models. The causal-identification researcher should use BIC, which under certain conditions selects the 'true' model (the data-generating process) with higher probability, especially in large samples, because its heavier penalty avoids including spurious variables. The goals differ: minimizing forecast error versus identifying the correct structural relationships."
  explanation: "AIC and BIC optimize for different things. AIC minimizes expected Kullback-Leibler divergence between the fitted model and the true data-generating process — a measure of predictive accuracy. BIC is derived from Bayesian model selection and, under regularity conditions, is consistent: as sample size grows, BIC selects the true model (if it is in the candidate set) with probability approaching 1. When they disagree, the choice of criterion should reflect the researcher's actual goal, not a default preference."
```

## Explainer

Every time you add a variable to a regression, the model fits the sample data better — the residuals shrink and R² rises. But that improvement might be pure noise: the variable captures random patterns in this dataset that won't repeat in new data. Model selection criteria like **AIC** (Akaike Information Criterion) and **BIC** (Bayesian Information Criterion) formalize the tradeoff between fit and parsimony. From your work on model specification testing, you already know that overfitting is a real danger. AIC and BIC give you a principled way to penalize it.

Both criteria follow the same logic: start with a measure of fit (typically the log-likelihood from maximum likelihood estimation, which you've already learned) and subtract a penalty proportional to the number of parameters. The formula is AIC = −2 ln(L̂) + 2k and BIC = −2 ln(L̂) + k ln(n), where L̂ is the maximized likelihood, k is the number of parameters, and n is the sample size. The first term rewards fit; the second penalizes complexity. Lower values are better, and you choose the model with the lowest criterion value. Because AIC's penalty is 2k regardless of sample size, while BIC's penalty k ln(n) grows with n, **BIC penalizes additional parameters more heavily**, especially in large samples — it leans toward simpler models.

The intuition is clearest when comparing two nested models: a restricted model with fewer parameters and an unrestricted one with more. Adding a variable decreases −2 ln(L̂) by some amount. If that decrease exceeds the penalty (2 for AIC, ln(n) for BIC), the richer model wins; otherwise, the simpler model is preferred. In this sense, AIC and BIC are like automatic hypothesis tests, but they don't require a single null hypothesis — you can compare any set of models, **including non-nested specifications** like different functional forms or different regressor sets, which standard F-tests cannot handle.

One crucial point the Core Idea flags: AIC and BIC values have no meaningful absolute interpretation. A model with AIC = −340 is not "worse" than one with AIC = −200 from a different dataset — the scales are incomparable. What matters is the *difference* between criteria for models estimated on the same data. As a rough rule of thumb, differences in AIC of less than 2 suggest the models are roughly equivalent; differences greater than 10 suggest strong evidence favoring the lower-AIC model. Because AIC favors predictive accuracy while BIC favors the "true" model (under certain assumptions), they will sometimes disagree — when they do, the choice depends on your goal: prediction (use AIC) or identifying the data-generating process (use BIC).
