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
status: validated
---

# Decision Boundaries in Classification

## Core Idea
A decision boundary separates the feature space into regions for different classes; decision boundaries may be linear (logistic regression, SVMs with linear kernels) or nonlinear (neural networks, decision trees, SVMs with nonlinear kernels). Understanding decision boundaries reveals model assumptions and limitations, such as whether a model can represent disjoint classes or capture nonlinear patterns.

## How It's Best Learned
Visualize decision boundaries in 2D for different classifiers (logistic regression, k-NN, decision trees, SVMs) to understand how they partition the space differently.

## Questions

```yaml
- question: "A dataset contains two classes arranged as concentric circles — class A is the inner circle, class B is the outer ring. A logistic regression model is trained on this data. What will happen?"
  type: multiple-choice
  options:
    - "Logistic regression will find the correct circular boundary because it optimizes over all possible boundaries"
    - "Logistic regression will perfectly separate the classes once given enough training data"
    - "Logistic regression will fail to perfectly classify the data no matter how much training data is provided, because its boundary is constrained to be a straight line"
    - "Logistic regression will overfit and produce a jagged circular boundary around each class"
  answer: 2
  explanation: "Logistic regression is a linear classifier — its decision boundary is always a hyperplane (a line in 2D). Concentric circles are not linearly separable; no single straight line can correctly divide the inner circle from the outer ring. Adding more training data does not help, because the problem is with the model's inductive bias, not insufficient data. A nonlinear model (kernel SVM, neural network, or even k-NN) is required. This illustrates why understanding decision boundary shapes reveals a model's fundamental limitations."

- question: "A k-nearest-neighbors classifier trained on a small, noisy dataset produces a highly irregular decision boundary with many small islands around individual points. A second model on the same data produces a single smooth curved boundary. Which model is more likely to generalize better to new data, and why?"
  type: multiple-choice
  options:
    - "The irregular k-NN boundary, because it captures all the structure in the training data"
    - "The smooth boundary, because complex boundaries tend to overfit noise rather than capture true class structure"
    - "They will generalize equally well, because both models saw the same training data"
    - "The irregular k-NN boundary, because more complex boundaries always reflect more information"
  answer: 1
  explanation: "A decision boundary that contorts to accommodate every training point is overfitting — it is fitting noise as if it were signal. On new data, those noise-driven islands and jagged edges will misclassify points that should fall in the majority class region. The smooth boundary reflects a stronger inductive bias toward simpler structure, which tends to generalize better unless the true class boundary is genuinely complex. Visualizing decision boundaries makes this bias-variance tradeoff tangible."

- question: "A linear classifier will misclassify some points in a non-linearly separable dataset no matter how long it is trained."
  type: true-false
  answer: true
  explanation: "This is a fundamental property of linear classifiers, not a training failure. If the true decision boundary is nonlinear (classes overlap or are interleaved in ways no hyperplane can separate), the linear model's boundary cannot represent the correct partition. Training longer refines the placement of the line, but the line is still a line — it cannot curve to match a circular or spiral boundary. Adding more data also doesn't help: more examples of a problem the model cannot represent just confirms it. This is the model's inductive bias at work."

- question: "A more complex decision boundary usually leads to better classification performance because it can capture more patterns in the data."
  type: true-false
  answer: false
  explanation: "More complex boundaries can fit training data better, but they tend to overfit — capturing noise and idiosyncrasies of the training set that do not generalize to new data. A model with a very complex boundary may achieve near-perfect training accuracy while performing poorly on a held-out test set. The optimal boundary is the simplest one that correctly represents the true structure of the problem, not the most complex one that fits every training point. This is the bias-variance tradeoff: high-complexity models reduce bias but increase variance."

- question: "What does the shape of a classifier's decision boundary reveal about the model, and why is this geometrically useful for understanding classification?"
  type: short-answer
  answer: "The decision boundary's shape reveals the model's inductive bias — its built-in assumptions about the structure of the classification problem. A linear boundary assumes the classes are linearly separable; a staircase boundary (decision tree) assumes class regions align with feature axes; a smooth curved boundary (kernel SVM, neural network) assumes classes can be separated by smooth nonlinear surfaces. Visualizing the boundary in 2D makes the tradeoff between underfitting (too simple a boundary, can't capture class structure) and overfitting (too complex a boundary, memorizes noise) concrete and interpretable. It allows you to diagnose whether a model's failures are due to fundamental representational limits or excess flexibility."
  explanation: "The boundary is a geometric signature of the model. Examining where the boundary falls relative to the data reveals both what the model learned and what it cannot learn. A straight line that bisects a spiral dataset shows you immediately that the model is underfitting. A boundary that carves tiny islands around individual points shows overfitting. This geometric intuition extends to higher dimensions where direct visualization is impossible but the same underlying principles apply."
```

## Explainer

From your study of supervised learning and linear regression, you know that a model learns a mapping from input features to outputs. In classification, the output is a discrete class label rather than a continuous value, and the **decision boundary** is the surface in feature space where the model switches from predicting one class to predicting another. Understanding what this boundary looks like — its shape, its flexibility, and its relationship to the data — is one of the most powerful ways to understand what a classifier is actually doing.

Start with the simplest case: a linear classifier in two dimensions. Imagine plotting data points on a plane with two features as axes, colored by class. A linear model like logistic regression finds a single straight line (or, in higher dimensions, a hyperplane) that best separates the classes. On one side of the line, the model predicts class A; on the other, class B. The line's position and angle are determined by the learned weights — the same coefficients you encountered in linear regression, but now passed through a sigmoid function to produce class probabilities. The boundary itself is the set of points where the predicted probability is exactly 50%. This simplicity is both the strength and the limitation: linear boundaries are fast to compute and resistant to overfitting, but they cannot capture situations where the classes are interleaved or separated by a curved surface.

**Nonlinear decision boundaries** arise from models with more expressive capacity. A decision tree partitions the space with axis-aligned splits, producing a boundary that looks like a staircase — a series of horizontal and vertical cuts. A k-nearest-neighbors classifier creates an irregular, locally adaptive boundary that follows the contours of the data, because the class prediction at any point depends only on its nearest labeled neighbors. Support vector machines with nonlinear kernels (like the radial basis function kernel) project the data into a higher-dimensional space where a linear separator exists, producing smooth curved boundaries in the original space. Neural networks, with their layers of nonlinear activations, can learn arbitrarily complex boundaries — curves, islands, and disconnected regions.

The shape of the decision boundary directly reveals the model's **inductive bias** — its built-in assumptions about the structure of the problem. A model with a linear boundary assumes the classes are linearly separable; if they are not, it will misclassify points near the boundary regardless of how much data you provide. A model with a highly flexible boundary can fit complex patterns but risks **overfitting**: the boundary may contort to accommodate noise in the training data, creating jagged or fragmented regions that do not generalize. Visualizing decision boundaries in 2D makes this tradeoff concrete — you can literally see a simple model underfitting by drawing too straight a line, and a complex model overfitting by carving out tiny islands around individual training points. This geometric intuition carries directly into higher dimensions, where the tradeoff between boundary complexity and generalization remains the central challenge of classification.
