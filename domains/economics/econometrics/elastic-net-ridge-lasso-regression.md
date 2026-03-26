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
status: validated
---

# Ridge, Lasso, and Elastic Net Regression

## Core Idea
Ridge (L2), Lasso (L1), and Elastic Net add penalty terms to OLS loss. Ridge shrinks all coefficients; Lasso zeros out weak variables; Elastic Net combines both. These methods address multicollinearity and perform variable selection.

## How It's Best Learned
Fit models with varying penalty parameters (lambda) and plot coefficient paths. Use cross-validation to choose the optimal lambda that balances fit and parsimony.

## Questions

```yaml
- question: "You have a dataset with 200 candidate predictors and believe only about 20 are genuinely related to the outcome. Which regularization method is most appropriate?"
  type: multiple-choice
  options:
    - "Ridge regression, because it handles large numbers of predictors by shrinking all coefficients"
    - "OLS, because you need unbiased estimates to identify the true 20 predictors"
    - "Lasso regression, because it performs automatic variable selection by driving some coefficients to exactly zero"
    - "Elastic Net, because you always need both L1 and L2 penalties when predictors outnumber observations"
  answer: 2
  explanation: "When the true signal is sparse — only a small fraction of predictors matter — Lasso is the natural choice. Its L1 penalty produces sparse solutions by driving weak coefficients to exactly zero, effectively selecting variables automatically. Ridge retains all predictors with shrunk coefficients, better when many variables each contribute small signals. OLS with 200 predictors would overfit severely. Elastic Net is most useful when correlated predictors need to be retained or excluded in groups."

- question: "Why does Lasso drive some coefficients to exactly zero while Ridge only shrinks them toward (but never to) zero?"
  type: multiple-choice
  options:
    - "Lasso uses a larger default penalty parameter λ, forcing more shrinkage"
    - "The L1 constraint region has corners at the coordinate axes; the optimization solution often lands exactly on a corner where a coefficient is zero"
    - "Lasso uses an iterative algorithm that terminates early, leaving some coefficients unupdated"
    - "Ridge uses squared penalties which are stronger than absolute-value penalties and push coefficients further from zero"
  answer: 1
  explanation: "The geometric intuition is key. The L2 (Ridge) constraint region is a smooth sphere with no corners — the OLS loss contours touch it at a point where all coordinates are nonzero. The L1 (Lasso) constraint region is a diamond (in 2D) with corners exactly on the coordinate axes. The loss contours are likely to first touch this region at a corner, where one or more coordinates are exactly zero. This geometric property — not just the strength of the penalty — produces sparsity."

- question: "Increasing the regularization parameter λ in Ridge regression always increases the model's bias while decreasing its variance."
  type: true-false
  answer: true
  explanation: "This is the bias-variance tradeoff at the heart of regularization. Higher λ pulls coefficients further from OLS estimates (which minimize in-sample fit), introducing bias — the model no longer perfectly chases the training data's idiosyncratic patterns. At the same time, the model becomes less sensitive to the specific sample, reducing variance. At λ = 0, Ridge equals OLS (unbiased, high variance); as λ → ∞, all coefficients → 0 (maximum bias, near-zero variance). Optimal λ balances these forces."

- question: "Ridge regression is the preferred regularization method when you believe primarily a sparse subset of predictors is truly relevant to the outcome."
  type: true-false
  answer: false
  explanation: "This describes the ideal scenario for Lasso, not Ridge. Ridge shrinks all coefficients but keeps every predictor in the model — it never produces a sparse solution. When the true signal is sparse, Ridge assigns small but nonzero coefficients to all irrelevant predictors, adding noise and complicating interpretation. Lasso's automatic variable selection directly suits this scenario. Ridge is preferable when many predictors each contribute small signals and you want to dampen collective noise without eliminating any."

- question: "Explain the bias-variance tradeoff in regularization and describe how cross-validation is used to choose the optimal penalty parameter λ."
  type: short-answer
  answer: "Regularization introduces bias by penalizing large coefficients, forcing them toward zero and away from the OLS estimates that minimize in-sample fit. This bias reduces variance: the model is less sensitive to noise in the specific training sample and generalizes better to new data. The optimal λ balances these two forces. Cross-validation finds this optimum empirically: the data is split into k folds, the model is fit on k−1 folds at each λ value, and prediction error on the held-out fold is measured. The λ that minimizes average out-of-sample error is chosen."
  explanation: "In-sample fit always improves as λ decreases (more flexibility), but out-of-sample fit has a U-shape: too little regularization overfits, too much underfits. Cross-validation finds the λ at the bottom of that U-shape, making regularization a principled, data-driven procedure rather than an ad hoc tuning choice."
```

## Explainer

Standard OLS finds the coefficient vector that minimizes the sum of squared residuals — it fits the data as closely as possible, with no other constraint. When you have many predictors, especially correlated ones (multicollinearity, your prerequisite), OLS develops a problem: it will assign large and opposite-signed coefficients to correlated variables, chasing noise in the sample to marginally improve fit. The estimates become numerically unstable and virtually useless for interpretation or prediction on new data. **Regularization** is the solution — deliberately accept a little more bias in exchange for much lower variance.

Ridge regression adds a penalty term to the OLS loss function: instead of minimizing Σ(yᵢ - ŷᵢ)², it minimizes Σ(yᵢ - ŷᵢ)² + **λ**Σβⱼ² (the L2 penalty). The λ parameter controls how harsh the penalty is. When λ = 0, you get standard OLS. As λ increases, coefficients are pulled ("shrunk") toward zero. Crucially, ridge shrinks all coefficients proportionally but never eliminates any entirely — you always retain p predictors in the model. This makes ridge ideal when many variables each contribute a small signal and you want to dampen their collective noise.

**Lasso** (Least Absolute Shrinkage and Selection Operator) uses an L1 penalty instead: Σ(yᵢ - ŷᵢ)² + λΣ|βⱼ|. The absolute value rather than squared penalty has a geometric consequence: the constraint region has corners at the axes, and the optimal solution often sits exactly at a corner where some βⱼ = 0. Lasso therefore performs **automatic variable selection** — it zeros out weak predictors entirely, producing sparse models. If you believe only a subset of your variables genuinely matter, lasso is the more appropriate tool.

**Elastic Net** blends both penalties: λ₁Σ|βⱼ| + λ₂Σβⱼ². It inherits lasso's sparsity property while retaining ridge's ability to handle groups of correlated predictors (lasso arbitrarily picks one from a correlated group; elastic net can retain all of them with dampened coefficients). In practice, the choice among the three depends on the problem: many small signals favor ridge, a sparse signal favors lasso, and correlated predictors with an unknown structure favor elastic net.

The key insight unifying all three is the **bias-variance tradeoff**. Increasing λ introduces bias (coefficients drift from their true values) but reduces variance (the model responds less to sample-specific noise). The optimal λ is typically found through k-fold cross-validation: fit the model at many λ values, evaluate out-of-sample prediction error at each, and choose the λ that minimizes that error. This is where the discipline of regularization lives — not in the penalty algebra, but in the principled use of held-out data to tune the tradeoff.
