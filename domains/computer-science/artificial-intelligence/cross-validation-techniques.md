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
- id: sampling
  type: soft
- id: statistics-descriptive
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

## Explainer

From your study of the bias-variance tradeoff, you know that a model's performance on training data is an optimistic estimate of how it will perform on unseen data. The naive solution is to hold out a separate test set, but this wastes precious data — in a dataset of 500 examples, reserving 100 for testing means training on only 400, which may yield a worse model. **Cross-validation** addresses this by systematically rotating which data serves as the test set, so every example is used for both training and evaluation.

In **k-fold cross-validation**, you partition the data into k equally sized subsets (folds). You train the model k times, each time holding out one fold as the test set and training on the remaining k−1 folds. The k test-set error estimates are then averaged to produce a single performance metric. With k = 5, for example, each model trains on 80% of the data and tests on 20%, and every data point appears in exactly one test fold. This gives you a much more reliable error estimate than a single random split, because the variance of the estimate decreases — you are averaging over k independent evaluations rather than depending on the luck of one particular partition.

The choice of k involves its own bias-variance tradeoff. Large k (approaching leave-one-out, where k = n) uses nearly all data for training, reducing bias in the error estimate, but the k training sets overlap heavily, making the individual estimates highly correlated and increasing variance. Small k (like k = 2) produces more independent estimates but trains on less data, introducing bias. **k = 5 or k = 10** has emerged as a practical default because it balances these concerns well. **Stratified** k-fold ensures each fold preserves the class distribution of the full dataset, which is important when classes are imbalanced — without stratification, a fold might accidentally contain no examples of a rare class. For time-series data, standard k-fold violates temporal ordering (training on future data to predict the past), so **time-series splits** use expanding or sliding windows that always train on past data and test on future data.

Cross-validation's most important application is **model selection and hyperparameter tuning**. When choosing between, say, a decision tree with max depth 5 versus depth 10, you cannot compare their training errors (the deeper tree will always win on training data). Instead, you compare their cross-validated errors, which estimate generalization performance. You select the hyperparameters that minimize cross-validated error, then retrain the final model on all available data using those hyperparameters. This workflow — cross-validate to select, then retrain on everything — extracts maximum value from limited data while providing honest performance estimates that guard against overfitting.
