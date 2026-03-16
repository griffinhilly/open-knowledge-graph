---
id: elastic-net-ridge-lasso-regression
title: Ridge, Lasso, and Elastic Net Regression
domain: economics
course: econometrics
prerequisites:
- id: multiple-regression-model
  type: hard
- id: multicollinearity
  type: hard
tags:
- regularization
- ridge
- lasso
- elastic-net
stage: formal-systems
status: draft
---

# Ridge, Lasso, and Elastic Net Regression

## Core Idea
Ridge (L2), Lasso (L1), and Elastic Net add penalty terms to OLS loss. Ridge shrinks all coefficients; Lasso zeros out weak variables; Elastic Net combines both. These methods address multicollinearity and perform variable selection.

## How It's Best Learned
Fit models with varying penalty parameters (lambda) and plot coefficient paths. Use cross-validation to choose the optimal lambda that balances fit and parsimony.

## Explainer

Standard OLS finds the coefficient vector that minimizes the sum of squared residuals — it fits the data as closely as possible, with no other constraint. When you have many predictors, especially correlated ones (multicollinearity, your prerequisite), OLS develops a problem: it will assign large and opposite-signed coefficients to correlated variables, chasing noise in the sample to marginally improve fit. The estimates become numerically unstable and virtually useless for interpretation or prediction on new data. **Regularization** is the solution — deliberately accept a little more bias in exchange for much lower variance.

Ridge regression adds a penalty term to the OLS loss function: instead of minimizing Σ(yᵢ - ŷᵢ)², it minimizes Σ(yᵢ - ŷᵢ)² + **λ**Σβⱼ² (the L2 penalty). The λ parameter controls how harsh the penalty is. When λ = 0, you get standard OLS. As λ increases, coefficients are pulled ("shrunk") toward zero. Crucially, ridge shrinks all coefficients proportionally but never eliminates any entirely — you always retain p predictors in the model. This makes ridge ideal when many variables each contribute a small signal and you want to dampen their collective noise.

**Lasso** (Least Absolute Shrinkage and Selection Operator) uses an L1 penalty instead: Σ(yᵢ - ŷᵢ)² + λΣ|βⱼ|. The absolute value rather than squared penalty has a geometric consequence: the constraint region has corners at the axes, and the optimal solution often sits exactly at a corner where some βⱼ = 0. Lasso therefore performs **automatic variable selection** — it zeros out weak predictors entirely, producing sparse models. If you believe only a subset of your variables genuinely matter, lasso is the more appropriate tool.

**Elastic Net** blends both penalties: λ₁Σ|βⱼ| + λ₂Σβⱼ². It inherits lasso's sparsity property while retaining ridge's ability to handle groups of correlated predictors (lasso arbitrarily picks one from a correlated group; elastic net can retain all of them with dampened coefficients). In practice, the choice among the three depends on the problem: many small signals favor ridge, a sparse signal favors lasso, and correlated predictors with an unknown structure favor elastic net.

The key insight unifying all three is the **bias-variance tradeoff**. Increasing λ introduces bias (coefficients drift from their true values) but reduces variance (the model responds less to sample-specific noise). The optimal λ is typically found through k-fold cross-validation: fit the model at many λ values, evaluate out-of-sample prediction error at each, and choose the λ that minimizes that error. This is where the discipline of regularization lives — not in the penalty algebra, but in the principled use of held-out data to tune the tradeoff.
