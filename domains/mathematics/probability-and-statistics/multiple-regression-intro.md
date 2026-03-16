---
id: multiple-regression-intro
title: Introduction to Multiple Linear Regression
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: linear-regression
  type: hard
tags:
- regression
- multiple-regression
- multivariate
stage: formal-systems
status: draft
---

# Introduction to Multiple Linear Regression

## Core Idea
Multiple linear regression extends simple regression to many predictors: E[Y|X₁,...,Xₚ] = β₀ + β₁X₁ + ... + βₚXₚ. Coefficients represent partial effects (adjusted for other predictors). Model selection and multicollinearity are key concerns.

## How It's Best Learned
Fit multiple regression models with software. Compare nested models using F-tests. Examine variance inflation factors (VIF) for multicollinearity. Interpret partial slopes as adjusted effects. Use visualization and residual diagnostics.

## Common Misconceptions
Interpreting regression coefficients causally without experimentation. Ignoring multicollinearity and its effects on interpretability. Believing all significant predictors should be included. Overfitting with too many predictors.

## Explainer

Simple linear regression asks: how does Y change with X? Multiple regression asks a harder question: how does Y change with X₁ *holding X₂, X₃, ... constant*? This "holding everything else constant" idea is the heart of the model. The equation E[Y|X₁,...,Xₚ] = β₀ + β₁X₁ + ... + βₚXₚ looks like a straight line extended to higher dimensions — a flat hyperplane through p-dimensional predictor space. Each slope βⱼ is a **partial slope**: it tells you the expected change in Y for a one-unit increase in Xⱼ when all other predictors are held fixed.

The key insight is that partial slopes can differ dramatically from simple slopes. Suppose you regress exam scores on study hours and find a positive slope. Now add a second predictor, prior GPA. The coefficient on study hours shrinks — not because study hours matter less, but because some of its apparent effect was actually attributable to GPA (better students both study more *and* score higher). Multiple regression disentangles these associations. This is called **statistical control**: by including a variable in the model, you partial out its contribution, isolating the unique relationship of each predictor with the outcome.

**Multicollinearity** occurs when predictors are strongly correlated with each other. Intuitively: if X₁ and X₂ move almost in lockstep, the model cannot tell which one is doing the work. Mathematically, the coefficient estimates become unstable — large standard errors, wildly varying slopes across similar datasets. The **variance inflation factor (VIF)** quantifies this instability for each predictor. A VIF above 5 or 10 is a warning sign. Remedies include dropping one of the correlated predictors, combining them (e.g., via PCA), or collecting more data. Multicollinearity does not bias predictions from the model as a whole; it only undermines the interpretability of individual coefficients.

Model selection — choosing which predictors to include — is one of the central practical challenges. Adding more predictors always improves R² on the training data, but can hurt predictive accuracy on new data (**overfitting**). Adjusted R², AIC, or cross-validation penalize model complexity. The deeper issue is conceptual: a model with 20 predictors and 25 observations is fitting noise, not signal. The rule of thumb is roughly 10–20 observations per predictor for stable estimates. When in doubt, prefer the simpler model that captures the essential relationships without chasing every fluctuation in the data.
