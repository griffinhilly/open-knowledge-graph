---
id: gradient-boosting
title: Gradient Boosting Machines
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: ensemble-methods-advanced
  type: hard
- id: gradient-descent-optimization
  type: hard
tags:
- ensemble
- boosting
- supervised-learning
stage: advanced
status: draft
---

# Gradient Boosting Machines

## Core Idea
Gradient boosting fits weak learners sequentially to residuals, focusing on remaining errors. Each learner reduces previous prediction errors. XGBoost and LightGBM are efficient implementations with regularization. Works with any differentiable loss function.
