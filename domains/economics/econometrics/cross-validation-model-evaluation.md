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

## Explainer

You already know that R² measures how well a regression fits the data in your sample. The problem is that R² is measured on the same data used to estimate the model — and any model, no matter how badly specified, can be made to fit better simply by adding more variables. A model with as many parameters as observations will have R² = 1.0 while predicting new data no better than random noise. This pathology is called **overfitting**: the model has learned the quirks of your particular sample rather than the underlying pattern.

Cross-validation is the solution. The core idea is to simulate what happens when you use the model on new data — by actually withholding some data during estimation and testing the model on what it never saw. In **k-fold cross-validation**, you divide the dataset into k roughly equal groups (folds). You train the model on k−1 folds, then measure prediction error on the held-out fold. Repeat this k times, each time holding out a different fold. The average prediction error across all k held-out folds is your **cross-validation error** — an honest estimate of how well the model generalizes. With k = n (one observation held out each time), you get **leave-one-out cross-validation (LOOCV)**, the most thorough variant but computationally expensive.

The key insight is what this procedure reveals that in-sample R² hides. Suppose you compare a simple 3-variable model to a complex 15-variable model. In-sample, the 15-variable model almost always wins on R². But out-of-sample, the simpler model often wins — because the extra variables in the complex model were fitting noise specific to your sample. Cross-validation penalizes this complexity automatically: models that overfit perform well on training folds but poorly on the held-out fold, which drags down the average CV error.

Cross-validation also provides a disciplined method for **model selection**. When choosing between competing specifications — different sets of regressors, different functional forms, or different regularization strengths — pick the model with the lowest cross-validation error rather than the highest in-sample R². This connects directly to your earlier understanding of R²: a high R² tells you how well the model describes the past; a low CV error tells you how well the model predicts the future. In causal economic research, you often care more about unbiased estimates than prediction, but in forecasting applications — GDP growth, asset prices, demand — cross-validated predictive performance is the primary scorecard.
