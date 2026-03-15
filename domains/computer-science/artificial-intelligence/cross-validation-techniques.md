---
id: cross-validation-techniques
title: Cross-Validation Techniques
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: supervised-learning-intro
  type: hard
- id: bias-variance-tradeoff
  type: hard
- id: probability-axioms
  type: soft
builds-toward:
- hyperparameter-optimization
tags:
- evaluation
- hyperparameter-tuning
- overfitting-prevention
- model-selection
stage: advanced
status: draft
---

# Cross-Validation Techniques

## Core Idea
Cross-validation partitions data into train/test folds to estimate generalization error and tune hyperparameters without wasting data on a separate validation set. Stratified k-fold preserves class distribution; time-series splits respect temporal order; cross-validation reduces variance in error estimates compared to a single train/test split.

## How It's Best Learned
Implement k-fold cross-validation and observe how error estimates vary with fold size and how folds affect hyperparameter selection.
