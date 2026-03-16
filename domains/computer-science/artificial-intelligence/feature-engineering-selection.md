---
id: feature-engineering-selection
title: Feature Engineering and Selection
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: supervised-learning-intro
  type: hard
- id: dimensionality-reduction
  type: soft
tags:
- features
- preprocessing
- dimensionality-reduction
- feature-importance
stage: advanced
status: draft
---

# Feature Engineering and Selection

## Core Idea
Feature engineering creates new features from raw data to improve model performance (e.g., polynomial features, domain-specific transformations), while feature selection removes irrelevant or redundant features. Methods range from domain knowledge and statistical tests (univariate selection) to wrapper methods (forward/backward selection) and embedded methods (regularization penalties), where the choice impacts both accuracy and generalization.

## How It's Best Learned
Compare models before and after feature engineering on a real dataset, then use embedded methods (e.g., Lasso) to identify important features.

## Explainer

From supervised learning, you know that a model learns a mapping from input features to output labels. But the quality of that mapping depends enormously on what you feed in. Raw data rarely comes in a form that makes the underlying patterns obvious to a learning algorithm. **Feature engineering** is the art of transforming raw inputs into representations that expose those patterns, and **feature selection** is the discipline of keeping only the features that help while discarding those that add noise or redundancy. Together, they often matter more than the choice of algorithm — a simple model on well-engineered features routinely outperforms a complex model on raw data.

Feature engineering creates new variables from existing ones using domain knowledge and mathematical transformations. If you are predicting house prices and have a "lot width" and "lot depth" column, creating a "lot area" feature (width × depth) gives the model a directly useful signal it would otherwise have to learn implicitly. **Polynomial features** capture nonlinear relationships — squaring an age variable lets a linear model learn that both very young and very old patients have higher risk. **Interaction features** (multiplying two variables together) capture cases where the effect of one variable depends on the value of another. **Binning** converts continuous variables into categories (age → age group), which can help when the relationship is step-like rather than smooth. The guiding question is always: "What transformation would make the pattern I expect to find linearly separable or more obvious to the model?"

Feature selection addresses the opposite problem: having too many features. Irrelevant features add noise that the model may overfit to. Redundant features (two highly correlated columns) waste capacity without adding information. There are three main families of selection methods. **Filter methods** score each feature independently using statistical tests (correlation, mutual information, chi-squared) and keep the top k — fast but blind to feature interactions. **Wrapper methods** evaluate subsets of features by training and testing the model (forward selection adds features one at a time; backward elimination removes them), capturing interactions but being computationally expensive. **Embedded methods** perform selection as part of training — **Lasso** (L1 regularization) drives unimportant feature weights to exactly zero, simultaneously fitting the model and selecting features.

A practical workflow starts with domain-driven feature engineering, then uses embedded or filter methods to prune. If you know from dimensionality reduction that your data lives on a low-dimensional manifold, feature selection can be viewed as finding the coordinate system that aligns with that manifold. One critical warning: always perform feature selection using only training data. If you compute feature importance on the full dataset (including test data) and then select features, you leak information from the test set into training, producing overly optimistic performance estimates that will not hold up on truly unseen data. This train-only rule applies equally to all selection methods and is one of the most common sources of inflated results in applied machine learning.
