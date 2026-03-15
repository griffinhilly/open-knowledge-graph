---
id: feature-scaling-normalization
title: Feature Scaling and Normalization
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: feature-engineering-selection
  type: hard
- id: mean-median-mode
  type: soft
- id: standard-normal-z-scores-theory
  type: soft
builds-toward:
- gradient-descent-optimization
- neural-networks-intro
tags:
- scaling
- normalization
- standardization
stage: advanced
status: draft
---

# Feature Scaling and Normalization

## Core Idea
Feature scaling transforms features to comparable ranges (standardization: zero mean and unit variance; normalization: [0, 1] range). Distance-based algorithms (KNN, SVM) and gradient-based methods (neural networks) are sensitive to feature scale. Improper scaling causes slow convergence and numerical instability.

## How It's Best Learned
Fit scalers on training data only, then apply consistently to test data. Compare model performance with and without scaling across different algorithms.

## Common Misconceptions
Scaling means the same thing as one-hot encoding; improperly applying test-set scaling introduces data leakage.
