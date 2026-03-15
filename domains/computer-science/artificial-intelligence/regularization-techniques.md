---
id: regularization-techniques
title: Regularization Techniques
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: bias-variance-tradeoff
  type: hard
- id: constrained-optimization
  type: soft
- id: partial-derivatives
  type: soft
- id: optimization-problems
  type: soft
tags:
- learning-theory
- overfitting-prevention
stage: advanced
status: draft
---

# Regularization Techniques

## Core Idea
Regularization reduces overfitting by penalizing model complexity. L1 (Lasso) encourages sparsity; L2 (Ridge) shrinks weights. Early stopping halts at validation peak. Dropout randomly removes neurons; batch normalization stabilizes activations. Data augmentation increases effective samples.
