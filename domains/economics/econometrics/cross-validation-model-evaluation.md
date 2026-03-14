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
