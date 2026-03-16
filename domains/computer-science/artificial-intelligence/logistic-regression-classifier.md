---
id: logistic-regression-classifier
title: Logistic Regression for Classification
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: linear-regression-ml
  type: hard
- id: probability-basics
  type: hard
- id: probability-axioms
  type: soft
- id: derivatives-of-exponential-functions
  type: soft
- id: partial-derivatives
  type: soft
- id: derivatives-of-logarithmic-functions
  type: soft
- id: conditional-probability
  type: soft
- id: probability-rules-for-events
  type: soft
tags:
- supervised-learning
- classification
- probabilistic
stage: advanced
status: draft
---

# Logistic Regression for Classification

## Core Idea
Logistic regression outputs class probabilities via the logistic function applied to linear combinations of features. Cross-entropy loss is minimized via gradient descent. Despite its name, it is a classification algorithm modeling P(y=1|x).

## How It's Best Learned
Implement logistic regression with cross-entropy loss, visualize decision boundaries on 2D data, and compare ROC curves.

## Common Misconceptions
Logistic regression outputs probabilities, not binary labels; thresholding is needed for classification. It assumes linear separability; overlapping classes degrade performance.

## Explainer

You already know how linear regression fits a line to predict a continuous value. Logistic regression starts from the same foundation — a linear combination of features, w₁x₁ + w₂x₂ + ... + b — but asks a different question: instead of "what value?", it asks "which class?" The problem is that a raw linear combination can produce any real number, while a probability must stay between 0 and 1. The **logistic function** (also called the sigmoid), σ(z) = 1/(1 + e⁻ᶻ), solves this by squashing any real-valued input into the (0, 1) range. Feed the linear combination through the sigmoid, and you get P(y = 1 | x) — the model's estimated probability that the input belongs to the positive class.

This probabilistic output is what makes logistic regression fundamentally different from just drawing a dividing line. The model does not output "yes" or "no" directly; it outputs a number like 0.82, meaning "82% chance of class 1." You choose a **decision threshold** (typically 0.5) to convert this probability into a hard prediction, but the threshold is a separate design choice. Moving it up or down trades off precision against recall — something you can visualize with an ROC curve. The decision boundary itself — the set of points where P(y = 1 | x) = 0.5 — is always a straight line (or hyperplane in higher dimensions), because it corresponds to the set of inputs where the linear combination equals zero.

Training logistic regression means finding the weights that make the model's predicted probabilities match the observed labels as closely as possible. The right loss function here is **cross-entropy loss** (also called log loss), not squared error. Cross-entropy penalizes confident wrong predictions severely: if the model says P(y = 1) = 0.99 but the true label is 0, the loss is enormous. This is derived from maximum likelihood estimation — you are maximizing the likelihood of the observed data under the model. Since the sigmoid and logarithm are both differentiable, you can compute gradients of the cross-entropy loss with respect to each weight using the chain rule, and then apply gradient descent to update the weights iteratively.

Despite its simplicity, logistic regression is a powerful and interpretable baseline. Each weight tells you how much a one-unit increase in that feature shifts the log-odds of the positive class. It works well when the true decision boundary is approximately linear, scales efficiently to large datasets, and rarely overfits when properly regularized. Its limitations are equally instructive: because the decision boundary must be linear, logistic regression cannot capture XOR-like patterns or complex nonlinear boundaries without manual feature engineering. This limitation is precisely what motivates the move to neural networks — which you can think of as stacking many logistic-regression-like units together with nonlinearities between them.
