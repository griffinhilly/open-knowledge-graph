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
