---
id: heteroskedasticity
title: Heteroskedasticity
domain: economics
course: econometrics
prerequisites:
- id: ols-assumptions
  type: hard
- id: variance-of-random-variables
  type: hard
- id: residuals-and-goodness-of-fit
  type: soft
- id: probability-axioms
  type: soft
builds-toward:
- robust-standard-errors
tags:
- heteroskedasticity
- variance
- Breusch-Pagan
- White-test
stage: formal-systems
status: validated
---

# Heteroskedasticity

## Core Idea
Heteroskedasticity means the variance of the regression error u is not constant across observations: Var(u|x) ≠ σ². This violates the Gauss-Markov homoskedasticity assumption, so OLS remains unbiased but is no longer efficient, and reported standard errors are incorrect (usually too small), making inference invalid. It is common in cross-sectional economic data — for instance, expenditure variance typically rises with income. The Breusch-Pagan and White tests formally detect heteroskedasticity. The practical remedy is heteroskedasticity-robust standard errors, which produce valid inference without changing the coefficient estimates.

## How It's Best Learned
Plot residuals against fitted values — a fan-shaped pattern indicates heteroskedasticity. Compare conventional and robust standard errors on real data to see how inference changes.

## Common Misconceptions
- Heteroskedasticity does not bias β̂, only its standard errors — so point estimates may still be meaningful.
- Weighted least squares (WLS) is optimal under known heteroskedasticity structure, but robust standard errors are preferred when the form is unknown.

## Questions

```yaml
- question: "A researcher runs OLS regression and detects heteroskedasticity using a Breusch-Pagan test. What is the most accurate conclusion about their results?"
  type: multiple-choice
  options:
    - "The coefficient estimates β̂ are biased and must be re-estimated using WLS or GLS"
    - "The coefficient estimates β̂ are still unbiased, but the standard errors are incorrect and inference is invalid"
    - "Both the coefficient estimates and standard errors are unreliable and the regression must be discarded"
    - "The regression is fine as long as the sample size is large enough for asymptotic normality to hold"
  answer: 1
  explanation: "Heteroskedasticity does not bias β̂. Bias comes from E[β̂] − β, which depends on whether E[u|x] = 0 — a condition unrelated to variance. What heteroskedasticity destroys is efficiency (OLS is no longer BLUE) and the validity of the standard error formula (which assumes constant σ²). The practical remedy is heteroskedasticity-robust standard errors, which correct the inference without changing β̂ at all."

- question: "A regression of food expenditure on income yields β̂_income = 0.35. The residual plot shows a clear fan shape (wider spread at higher incomes). A colleague argues the estimate of 0.35 is biased by the heteroskedasticity. What is wrong with this claim?"
  type: multiple-choice
  options:
    - "Nothing — a fan-shaped residual plot is evidence of both heteroskedasticity and omitted variable bias"
    - "The colleague is right that 0.35 is biased, but only if the fan shape is statistically significant by a formal test"
    - "Heteroskedasticity affects standard errors and inference, not the point estimate β̂ — 0.35 remains an unbiased estimate"
    - "The claim would be correct only if the heteroskedasticity were correlated with the regressor (income)"
  answer: 2
  explanation: "Unbiasedness of OLS depends on E[u|x] = 0 (mean independence of errors from regressors), which is entirely separate from the variance condition Var(u|x) = σ². The fan shape indicates that error variance increases with income — a violation of homoskedasticity — but this says nothing about whether errors have zero mean given income. The coefficient estimate of 0.35 remains unbiased. What the fan shape invalidates is the standard error (and therefore the t-statistic and p-value) attached to that estimate."

- question: "Under heteroskedasticity, OLS coefficient estimates remain unbiased, but the reported standard errors are typically too small, causing t-statistics to be inflated and p-values to be too low."
  type: true-false
  answer: true
  explanation: "This is the precise consequence of heteroskedasticity. The standard OLS variance formula Var(β̂) = σ²(X'X)⁻¹ assumes constant σ² across all observations. When variance is not constant, this formula underestimates the true sampling variance of β̂, producing standard errors that are too small. Smaller standard errors mean larger t-statistics and smaller p-values — so you find apparent statistical significance that isn't really there. Robust standard errors correct this by estimating the true sampling variance directly from the residuals."

- question: "Heteroskedasticity causes OLS to produce biased estimates of the regression coefficients."
  type: true-false
  answer: false
  explanation: "This is the most common misconception about heteroskedasticity. Bias in OLS (E[β̂] ≠ β) results from violations of the zero-mean error condition (E[u|x] ≠ 0), such as omitted variable bias or endogeneity — not from non-constant variance. Heteroskedasticity only violates the equal-variance assumption, leaving the zero-mean condition intact. β̂ remains an unbiased estimator of β; what fails is the efficiency guarantee (OLS is no longer BLUE) and the validity of standard error formulas."

- question: "Why does heteroskedasticity make OLS standard errors invalid even though it does not bias the coefficient estimates? What specifically breaks down in the standard error formula?"
  type: short-answer
  answer: "The standard OLS standard error formula is derived assuming Var(u|x) = σ² — the same constant variance for every observation. Under heteroskedasticity, this assumption is violated: some observations have larger error variance than others. The formula plugs in a single estimated σ² as if it applied everywhere, but the true sampling variance of β̂ depends on the pattern of error variances across observations. The result is a mismatch: the formula produces a number, but that number is not the actual variance of the estimator. It typically underestimates the true variance, making confidence intervals too narrow and p-values too small."
  explanation: "Robust standard errors solve this by directly estimating the true sampling variance of β̂ from the squared residuals, without assuming any particular structure for how variance varies. They are consistent estimators of Var(β̂) under general forms of heteroskedasticity. The coefficient β̂ itself is unchanged — only the uncertainty quantification around it is corrected."
```

## Explainer

You know from OLS assumptions that the Gauss-Markov theorem requires Var(uᵢ|xᵢ) = σ² — the same constant variance for every observation. **Heteroskedasticity** is the violation of this assumption: the spread of errors is not constant but varies systematically with the regressors or some other observable. Think of household expenditure: higher-income families have far more discretionary spending and thus more variance in their food budgets than low-income families. If you regress food spending on income, the residuals will fan out as income rises — a classic heteroskedastic pattern.

Here is what heteroskedasticity actually does and does not do. It does **not** bias OLS coefficient estimates. β̂ remains an unbiased estimator of the true β because bias comes from E[β̂] − β, which depends on whether E[u|x] = 0 — not on variance. What heteroskedasticity destroys is the efficiency claim: OLS is no longer the Best Linear Unbiased Estimator (BLUE), because it gives equal weight to all observations when unequal weighting would be better. More importantly, the standard formula for Var(β̂) — which assumes constant σ² — is simply wrong under heteroskedasticity. It usually underestimates the true variance, making standard errors too small, t-statistics too large, and p-values too low. You end up finding significance that isn't there.

Detection is straightforward. The most direct method is a residual plot: after estimating your regression, plot the squared residuals (or absolute residuals) against fitted values or individual regressors. A random horizontal scatter suggests homoskedasticity; a fan shape or systematic curve reveals heteroskedasticity. Formal tests operationalize this. The **Breusch-Pagan test** regresses squared residuals on the original regressors and tests whether all slope coefficients are zero. The **White test** is more general — it includes squares and cross-products of all regressors to capture nonlinear forms of heteroskedasticity. Both tests produce a chi-squared statistic; rejection means heteroskedasticity is present.

The modern remedy is **heteroskedasticity-robust standard errors** (also called White or Eicker-Huber-White standard errors). Rather than assuming a specific structure for how variance changes, robust standard errors directly estimate the true sampling variance of β̂ from the data. The point estimate β̂ is unchanged — you are only adjusting how you quantify uncertainty around it. In practice, most applied economists use robust standard errors by default, treating them as insurance against an assumption that is rarely tested and often violated in cross-sectional data. Weighted least squares (WLS) can be more efficient if you know the exact form of heteroskedasticity, but since this is rarely known, robust standard errors offer a robust, low-cost alternative that requires no structural assumption about Var(u|x).
