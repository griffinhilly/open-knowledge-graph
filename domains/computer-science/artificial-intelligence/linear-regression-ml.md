---
id: linear-regression-ml
title: Linear Regression in Machine Learning
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: linear-algebra-basics
  type: hard
- id: probability-basics
  type: soft
- id: matrices-intro
  type: soft
- id: eigenvalues-and-eigenvectors
  type: soft
- id: linear-transformations
  type: soft
- id: linear-systems-notation
  type: soft
- id: expected-value
  type: soft
- id: least-squares-approximation
  type: soft
- id: matrix-operations
  type: soft
- id: statistics-descriptive
  type: soft
- id: expected-value-and-variance
  type: soft
tags:
- supervised-learning
- regression
- optimization
stage: advanced
status: draft
---

# Linear Regression in Machine Learning

## Core Idea
Linear regression models continuous outputs as linear combinations of input features. Least squares minimizes squared error; solutions are computed analytically via normal equations or iteratively via gradient descent. Extensions include regularization and polynomial features.

## Questions

```yaml
- question: "Which statement best describes what the ordinary least squares (OLS) objective minimizes?"
  type: multiple-choice
  options: ["The sum of absolute differences between predicted and actual values", "The sum of squared differences between predicted and actual values", "The maximum single prediction error across all training examples", "The difference between the largest and smallest predicted values"]
  answer: 1
  explanation: "OLS minimizes the sum of squared residuals (SSR = Σ(yᵢ - ŷᵢ)²). Squaring errors penalizes large errors disproportionately and makes the objective differentiable, enabling the closed-form normal equation solution β = (XᵀX)⁻¹Xᵀy and gradient-based optimization. Minimizing absolute differences (L1) leads to median regression, not OLS."

- question: "Linear regression can only model truly linear relationships between input features and the target variable."
  type: true-false
  answer: false
  explanation: "Linear regression is linear in its parameters, not necessarily in the input features. By adding polynomial features (x², x³) or interaction terms (x₁·x₂) to the feature matrix, linear regression can model curved and complex relationships. The model remains 'linear' because ŷ is a linear combination of the (now transformed) features, and all OLS theory still applies."

- question: "When would you choose gradient descent over the normal equations to fit a linear regression model?"
  type: short-answer
  answer: "When the number of features (p) is very large, because the normal equations require inverting a p×p matrix, which is O(p³) in time and O(p²) in memory. Gradient descent scales much better with large feature sets and is the standard approach when p can be thousands or millions."
  explanation: "The normal equation β = (XᵀX)⁻¹Xᵀy requires forming and inverting the p×p matrix XᵀX. For small datasets with few features this is fast and exact. But for high-dimensional problems, matrix inversion is computationally prohibitive. Gradient descent iteratively updates parameters using the loss gradient, costing only O(n·p) per step, making it far more scalable."
```

## Explainer

Linear regression is the foundational model of supervised learning: given input features and continuous output labels, find the linear combination of features that best predicts the output. Despite its simplicity, understanding it deeply — why it works, how it's solved, and when it fails — provides the conceptual scaffolding for nearly every more advanced method.

The model is ŷ = Xβ, where X is the feature matrix (n examples × p features, with a column of ones for the intercept), β is the parameter vector to learn, and ŷ is the prediction vector. The goal is to choose β minimizing the sum of squared residuals. This objective has a unique minimum (assuming XᵀX is invertible) given by the normal equations: β = (XᵀX)⁻¹Xᵀy. This is an exact, closed-form solution — no iteration required. The matrix XᵀX captures the covariance structure of the features, and its inverse "un-rotates" and "un-stretches" the feature space to align predictions with targets.

For large feature sets, computing (XᵀX)⁻¹ becomes too expensive — inverting a p×p matrix scales as O(p³). Gradient descent is the practical alternative: start with arbitrary β, compute the gradient of the loss with respect to β, and take a small step in the direction that reduces the loss. Repeat until convergence. Each step costs O(n·p), scaling gracefully to millions of features. This is the same mechanism used to train neural networks, which is why understanding gradient descent in the linear regression setting is non-negotiable before moving to deeper models.

A common misconception is that "linear regression can only model straight-line relationships." The linearity refers to the parameters, not the features. Adding x², log(x), or interaction terms to the feature matrix allows linear regression to fit curves and interactions. The model is still "linear" because ŷ = β₀ + β₁x + β₂x² is linear in the parameters (β₀, β₁, β₂), and all OLS theory still applies. This is the basis of polynomial regression and illustrates why feature engineering matters as much as model selection.

Regularization addresses a practical limitation of OLS: when features are highly correlated (multicollinearity) or when p is close to n, (XᵀX)⁻¹ becomes numerically unstable and the model overfits. Ridge regression adds a penalty λ‖β‖² to the objective, shrinking coefficients toward zero and stabilizing the solution. Lasso adds λ‖β‖₁, which drives some coefficients exactly to zero, performing automatic feature selection. Both are still "linear regression" in the same model class — same structure, different objective function — and both are solved efficiently with gradient descent.
