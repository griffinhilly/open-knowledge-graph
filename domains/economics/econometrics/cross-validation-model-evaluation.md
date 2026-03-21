---
id: cross-validation-model-evaluation
title: Cross-Validation and Out-of-Sample Model Evaluation
domain: economics
course: econometrics
prerequisites:
- id: multiple-regression-model
  type: hard
- id: r-squared-and-model-fit
  type: hard
tags:
- cross-validation
- out-of-sample
- model-evaluation
stage: formal-systems
status: draft
---

# Cross-Validation and Out-of-Sample Model Evaluation

## Core Idea
K-fold and leave-one-out cross-validation assess out-of-sample predictive performance by iteratively holding out data, fitting on the remainder, and testing on the holdout. This prevents overfitting and provides honest estimates of generalization error.

## Questions

```yaml
- question: "A researcher compares two models: Model A has 3 predictors and in-sample R² = 0.73. Model B has 25 predictors and R² = 0.91. Model B's 10-fold cross-validation error is 60% higher than Model A's. For a forecasting application, which model should they choose?"
  type: multiple-choice
  options:
    - "Model B — higher R² always indicates a better-fitting, more accurate model"
    - "Model A — lower CV error means it generalizes better to new data"
    - "Model B — more predictors capture more real variation in the data"
    - "It depends on which individual coefficients are statistically significant"
  answer: 1
  explanation: "Model B's high R² likely reflects overfitting — its 25 predictors have learned the noise in the training sample rather than the true underlying pattern. A 60% higher CV error means Model B performs much worse on data it hasn't seen. For forecasting, cross-validation error — not in-sample R² — is the correct performance metric. This is the central lesson: R² measures how well the model describes the past; CV error estimates how well it predicts the future."

- question: "What specific problem does cross-validation detect that in-sample R² cannot?"
  type: multiple-choice
  options:
    - "Whether the model's coefficients are statistically significant at the 5% level"
    - "Whether the model has overfitted — fitting noise specific to the sample rather than the true underlying pattern"
    - "Whether omitted variable bias is affecting the coefficient estimates"
    - "Whether the error terms satisfy the Gauss-Markov homoskedasticity assumption"
  answer: 1
  explanation: "In-sample R² is measured on the same data used to estimate the model. Adding any variable — even pure noise — will improve R². This means R² rewards complexity regardless of whether that complexity reflects real signal. Cross-validation simulates out-of-sample prediction by actually withholding data during estimation: a model that overfit will nail the training folds but fail on the held-out fold, and this shows up as high CV error. R² cannot detect this because it never tests the model on data it didn't train on."

- question: "Adding more predictor variables to a regression always improves out-of-sample predictive performance because additional variables cannot reduce the model's explanatory power."
  type: true-false
  answer: false
  explanation: "This confuses in-sample and out-of-sample performance. Adding variables always improves (or at worst maintains) in-sample R², because more parameters give the model more flexibility to fit the existing data. But out-of-sample, additional variables can hurt by fitting noise specific to the training sample — when the model encounters new data where that noise pattern doesn't repeat, its predictions worsen. Cross-validation reveals this by actually measuring performance on held-out data."

- question: "A model selected by minimizing cross-validation error will typically outperform a model selected by maximizing in-sample R² when making predictions on new data."
  type: true-false
  answer: true
  explanation: "This is precisely the purpose of cross-validation. Maximizing in-sample R² tends to select overly complex models that fit the sample's idiosyncrasies. Minimizing CV error selects models that perform well on data they haven't seen — which is the definition of good generalization. The two selection criteria agree only when models don't overfit; when they disagree, CV error is the more reliable guide for prediction tasks."

- question: "Explain why in-sample R² is a misleading measure of a model's predictive quality, and what cross-validation reveals instead."
  type: short-answer
  answer: "R² is measured on the same data used to fit the model, so it rewards complexity: any additional variable improves R² even if it's pure noise. A model with as many parameters as observations achieves R² = 1.0 while predicting new data no better than chance. Cross-validation simulates out-of-sample prediction by holding out portions of the data during estimation and measuring error on what the model never saw. This penalizes complexity automatically — overfit models perform well on training folds but fail on held-out folds."
  explanation: "The key distinction is what each metric is measuring. R² answers: 'How well does the model describe this data?' CV error answers: 'How well will the model predict data it hasn't seen?' For forecasting, the second question is what matters. This is why modern machine learning and econometric forecasting practice uses CV error (or related metrics like AIC/BIC that penalize complexity) rather than R² as the model selection criterion."
```

## Explainer

You already know that R² measures how well a regression fits the data in your sample. The problem is that R² is measured on the same data used to estimate the model — and any model, no matter how badly specified, can be made to fit better simply by adding more variables. A model with as many parameters as observations will have R² = 1.0 while predicting new data no better than random noise. This pathology is called **overfitting**: the model has learned the quirks of your particular sample rather than the underlying pattern.

Cross-validation is the solution. The core idea is to simulate what happens when you use the model on new data — by actually withholding some data during estimation and testing the model on what it never saw. In **k-fold cross-validation**, you divide the dataset into k roughly equal groups (folds). You train the model on k−1 folds, then measure prediction error on the held-out fold. Repeat this k times, each time holding out a different fold. The average prediction error across all k held-out folds is your **cross-validation error** — an honest estimate of how well the model generalizes. With k = n (one observation held out each time), you get **leave-one-out cross-validation (LOOCV)**, the most thorough variant but computationally expensive.

The key insight is what this procedure reveals that in-sample R² hides. Suppose you compare a simple 3-variable model to a complex 15-variable model. In-sample, the 15-variable model almost always wins on R². But out-of-sample, the simpler model often wins — because the extra variables in the complex model were fitting noise specific to your sample. Cross-validation penalizes this complexity automatically: models that overfit perform well on training folds but poorly on the held-out fold, which drags down the average CV error.

Cross-validation also provides a disciplined method for **model selection**. When choosing between competing specifications — different sets of regressors, different functional forms, or different regularization strengths — pick the model with the lowest cross-validation error rather than the highest in-sample R². This connects directly to your earlier understanding of R²: a high R² tells you how well the model describes the past; a low CV error tells you how well the model predicts the future. In causal economic research, you often care more about unbiased estimates than prediction, but in forecasting applications — GDP growth, asset prices, demand — cross-validated predictive performance is the primary scorecard.
