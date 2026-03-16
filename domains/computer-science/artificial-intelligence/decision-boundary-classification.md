---
id: decision-boundary-classification
title: Decision Boundaries in Classification
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: supervised-learning-intro
  type: hard
- id: linear-regression-ml
  type: hard
tags:
- classification
- geometry
- model-interpretation
stage: advanced
status: draft
---

# Decision Boundaries in Classification

## Core Idea
A decision boundary separates the feature space into regions for different classes; decision boundaries may be linear (logistic regression, SVMs with linear kernels) or nonlinear (neural networks, decision trees, SVMs with nonlinear kernels). Understanding decision boundaries reveals model assumptions and limitations, such as whether a model can represent disjoint classes or capture nonlinear patterns.

## How It's Best Learned
Visualize decision boundaries in 2D for different classifiers (logistic regression, k-NN, decision trees, SVMs) to understand how they partition the space differently.

## Explainer

From your study of supervised learning and linear regression, you know that a model learns a mapping from input features to outputs. In classification, the output is a discrete class label rather than a continuous value, and the **decision boundary** is the surface in feature space where the model switches from predicting one class to predicting another. Understanding what this boundary looks like — its shape, its flexibility, and its relationship to the data — is one of the most powerful ways to understand what a classifier is actually doing.

Start with the simplest case: a linear classifier in two dimensions. Imagine plotting data points on a plane with two features as axes, colored by class. A linear model like logistic regression finds a single straight line (or, in higher dimensions, a hyperplane) that best separates the classes. On one side of the line, the model predicts class A; on the other, class B. The line's position and angle are determined by the learned weights — the same coefficients you encountered in linear regression, but now passed through a sigmoid function to produce class probabilities. The boundary itself is the set of points where the predicted probability is exactly 50%. This simplicity is both the strength and the limitation: linear boundaries are fast to compute and resistant to overfitting, but they cannot capture situations where the classes are interleaved or separated by a curved surface.

**Nonlinear decision boundaries** arise from models with more expressive capacity. A decision tree partitions the space with axis-aligned splits, producing a boundary that looks like a staircase — a series of horizontal and vertical cuts. A k-nearest-neighbors classifier creates an irregular, locally adaptive boundary that follows the contours of the data, because the class prediction at any point depends only on its nearest labeled neighbors. Support vector machines with nonlinear kernels (like the radial basis function kernel) project the data into a higher-dimensional space where a linear separator exists, producing smooth curved boundaries in the original space. Neural networks, with their layers of nonlinear activations, can learn arbitrarily complex boundaries — curves, islands, and disconnected regions.

The shape of the decision boundary directly reveals the model's **inductive bias** — its built-in assumptions about the structure of the problem. A model with a linear boundary assumes the classes are linearly separable; if they are not, it will misclassify points near the boundary regardless of how much data you provide. A model with a highly flexible boundary can fit complex patterns but risks **overfitting**: the boundary may contort to accommodate noise in the training data, creating jagged or fragmented regions that do not generalize. Visualizing decision boundaries in 2D makes this tradeoff concrete — you can literally see a simple model underfitting by drawing too straight a line, and a complex model overfitting by carving out tiny islands around individual training points. This geometric intuition carries directly into higher dimensions, where the tradeoff between boundary complexity and generalization remains the central challenge of classification.
