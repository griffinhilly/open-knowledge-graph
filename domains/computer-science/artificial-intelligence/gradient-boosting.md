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
- id: critical-points-extrema
  type: soft
- id: expected-value
  type: soft
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

## Explainer

From ensemble methods, you know that combining multiple weak models often outperforms any single strong model. From gradient descent, you know how to minimize a loss function by iteratively stepping in the direction of steepest descent. **Gradient boosting** unifies these ideas in an elegant way: it performs gradient descent in function space, where each step is a new weak learner (typically a small decision tree) fitted to the negative gradient of the loss. Instead of adjusting numerical parameters, gradient boosting adjusts the prediction function itself, one additive correction at a time.

Here is the concrete procedure. Start with a simple initial prediction — for regression, the mean of all target values. Compute the **residuals**: the differences between the true targets and current predictions. These residuals tell you exactly where and by how much the current model is wrong. Now fit a small decision tree (a "weak learner") to predict these residuals. Add this tree's predictions to the current model, scaled by a **learning rate** (typically 0.01–0.3). The model has now corrected some of its errors. Repeat: compute new residuals from the updated predictions, fit another tree to those residuals, add it in. After hundreds or thousands of such iterations, the ensemble of small trees collectively produces highly accurate predictions. Each tree is simple (often just 4–8 terminal nodes), but their cumulative effect is powerful.

The connection to gradient descent becomes clear when you generalize beyond squared-error loss. For squared error, the residual (y − ŷ) happens to equal the negative gradient of the loss with respect to the prediction. For other loss functions — absolute error, log-loss for classification, quantile loss for prediction intervals — the residuals are replaced by the **negative gradient of the loss function** evaluated at each data point's current prediction. The new tree is always fitted to these pseudo-residuals. This is why the method is called gradient boosting: it performs gradient descent in function space, and the "gradient" is computed pointwise across the dataset. This generality means gradient boosting works with any differentiable loss function, making it applicable to regression, classification, ranking, and survival analysis.

The practical dominance of gradient boosting in applied machine learning (especially on tabular data) comes from implementations like **XGBoost**, **LightGBM**, and **CatBoost** that add critical engineering and regularization. XGBoost introduced second-order Taylor expansion of the loss (using both gradient and Hessian) for better split finding, plus L1 and L2 regularization on leaf weights to prevent overfitting. LightGBM made training dramatically faster with histogram-based splitting and leaf-wise tree growth instead of level-wise. Key hyperparameters to tune are learning rate (smaller = more trees needed but better generalization), tree depth (deeper = more complex interactions captured), and number of trees (controlled by early stopping on a validation set). The learning rate and number of trees trade off directly: halving the learning rate roughly doubles the number of trees needed, but often improves final accuracy. Gradient boosting remains the default choice for structured/tabular prediction tasks, consistently winning Kaggle competitions and powering production ML systems across industry.
