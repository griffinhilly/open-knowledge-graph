---
id: support-vector-regression
title: Support Vector Regression
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: support-vector-machines
  type: hard
- id: linear-regression-ml
  type: hard
builds-toward:
- kernel-methods
- regression-techniques
tags:
- svr
- support-vector
- regression
stage: advanced
status: draft
---

# Support Vector Regression

## Core Idea
Support Vector Regression extends SVMs to regression by fitting a hyperplane while constraining prediction errors within a margin. SVR handles non-linearity via kernels and is robust to outliers. The epsilon parameter controls the trade-off between model complexity and allowable error, providing intuitive control over generalization.

## Explainer

You already know how support vector machines work for classification: find the hyperplane that separates classes with the widest margin, where only the closest points (support vectors) determine the boundary. **Support Vector Regression** (SVR) adapts this geometric intuition to continuous prediction. Instead of maximizing the margin between classes, SVR fits a function that keeps all training points within a specified distance from its predictions — and the points that sit exactly on the boundary of that distance are the support vectors that define the model.

The central idea is the **epsilon-insensitive tube**. You choose a parameter **ε** (epsilon) that defines a band around the predicted function. Any training point whose actual value falls within ε of the prediction incurs zero loss — the model considers it "close enough." Only points outside the tube contribute to the error, and they are penalized linearly by how far they fall outside. This is fundamentally different from ordinary linear regression, which penalizes every deviation from the fit. The epsilon tube means SVR ignores small noise and focuses only on significant deviations, making it naturally robust to minor fluctuations in the training data.

Points that violate the tube boundary are allowed through **slack variables**, controlled by a regularization parameter **C**. A large C penalizes violations heavily, forcing the model to fit the data more tightly (risking overfitting). A small C permits more violations, producing a smoother, more generalizable fit. This C-ε trade-off is the core tuning decision in SVR: ε controls how wide the insensitivity band is (how much noise you ignore), while C controls how much you penalize points that escape it.

Like classification SVMs, SVR can model non-linear relationships through the **kernel trick**. By mapping inputs into a higher-dimensional feature space via a kernel function (RBF, polynomial, or others), SVR fits a linear function in that space, which corresponds to a non-linear function in the original input space. The mathematical machinery — the dual formulation, kernel evaluations, support vector identification — carries over directly from classification SVMs. The result is a regression method that combines the geometric elegance of margin-based learning, the flexibility of kernel methods, and built-in robustness to noise through the epsilon tube.
