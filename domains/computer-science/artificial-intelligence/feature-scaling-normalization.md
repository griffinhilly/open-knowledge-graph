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

## Explainer

From your work on feature engineering, you know that the raw features in a dataset can vary wildly in their numeric ranges. A dataset might include age (0–100), income (20,000–500,000), and a binary indicator (0 or 1). Most machine learning algorithms treat these numbers at face value, and when one feature's range is thousands of times larger than another's, it can dominate the model's behavior in unintended ways. **Feature scaling** transforms all features to comparable ranges so that no single feature overwhelms the others simply because of its units or magnitude.

The two most common techniques are **standardization** and **min-max normalization**. Standardization (also called z-score normalization, which you have seen in statistics) subtracts the mean and divides by the standard deviation, producing features with zero mean and unit variance. Min-max normalization rescales each feature to a fixed range, typically [0, 1], by subtracting the minimum and dividing by the range. Standardization is generally preferred when the data contains outliers, because it does not bound the output to a fixed range — an outlier becomes a large z-score rather than compressing all other values into a tiny slice of [0, 1]. Min-max normalization is useful when you need bounded values, such as for neural network inputs that expect values in [0, 1].

Why does scaling matter? **Distance-based algorithms** like k-nearest neighbors and support vector machines compute distances between data points. If income ranges from 20,000 to 500,000 and age ranges from 0 to 100, the distance calculation is almost entirely determined by income — a difference of 10,000 in income swamps a difference of 50 in age, even though both might be equally important. Scaling puts both features on an equal footing. **Gradient-based methods** like neural networks and logistic regression are also sensitive: features with large magnitudes produce large gradients, causing the optimization to oscillate along those dimensions while creeping along others. Scaling creates a smoother, more symmetric loss surface that gradient descent can navigate efficiently.

A critical practical rule is that scaling parameters must be computed from the **training set only** and then applied identically to the test set. If you compute the mean and standard deviation using all available data (including the test set), you leak information from the test set into the training process — this is **data leakage**, and it produces overly optimistic performance estimates that do not hold on truly unseen data. In practice, this means fitting a scaler object on the training data and using its `transform` method on both training and test data, never calling `fit` on the test set. This discipline extends to cross-validation: scaling must happen inside each fold, not before the split.
