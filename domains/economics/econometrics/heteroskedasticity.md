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

## Explainer

You know from OLS assumptions that the Gauss-Markov theorem requires Var(uᵢ|xᵢ) = σ² — the same constant variance for every observation. **Heteroskedasticity** is the violation of this assumption: the spread of errors is not constant but varies systematically with the regressors or some other observable. Think of household expenditure: higher-income families have far more discretionary spending and thus more variance in their food budgets than low-income families. If you regress food spending on income, the residuals will fan out as income rises — a classic heteroskedastic pattern.

Here is what heteroskedasticity actually does and does not do. It does **not** bias OLS coefficient estimates. β̂ remains an unbiased estimator of the true β because bias comes from E[β̂] − β, which depends on whether E[u|x] = 0 — not on variance. What heteroskedasticity destroys is the efficiency claim: OLS is no longer the Best Linear Unbiased Estimator (BLUE), because it gives equal weight to all observations when unequal weighting would be better. More importantly, the standard formula for Var(β̂) — which assumes constant σ² — is simply wrong under heteroskedasticity. It usually underestimates the true variance, making standard errors too small, t-statistics too large, and p-values too low. You end up finding significance that isn't there.

Detection is straightforward. The most direct method is a residual plot: after estimating your regression, plot the squared residuals (or absolute residuals) against fitted values or individual regressors. A random horizontal scatter suggests homoskedasticity; a fan shape or systematic curve reveals heteroskedasticity. Formal tests operationalize this. The **Breusch-Pagan test** regresses squared residuals on the original regressors and tests whether all slope coefficients are zero. The **White test** is more general — it includes squares and cross-products of all regressors to capture nonlinear forms of heteroskedasticity. Both tests produce a chi-squared statistic; rejection means heteroskedasticity is present.

The modern remedy is **heteroskedasticity-robust standard errors** (also called White or Eicker-Huber-White standard errors). Rather than assuming a specific structure for how variance changes, robust standard errors directly estimate the true sampling variance of β̂ from the data. The point estimate β̂ is unchanged — you are only adjusting how you quantify uncertainty around it. In practice, most applied economists use robust standard errors by default, treating them as insurance against an assumption that is rarely tested and often violated in cross-sectional data. Weighted least squares (WLS) can be more efficient if you know the exact form of heteroskedasticity, but since this is rarely known, robust standard errors offer a robust, low-cost alternative that requires no structural assumption about Var(u|x).
