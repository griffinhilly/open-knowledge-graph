---
id: heteroskedasticity-types-causes
title: 'Heteroskedasticity: Types and Causes'
domain: economics
course: econometrics
prerequisites:
- id: ols-assumptions
  type: hard
builds-toward:
- heteroskedasticity-detection-testing
tags:
- heteroskedasticity
- assumptions
- diagnostics
stage: formal-systems
status: draft
---

# Heteroskedasticity: Types and Causes

## Core Idea
Heteroskedasticity (non-constant error variance) occurs when Var(u|X) depends on X. Common sources include measurement error increasing with variable magnitude, omitted variables correlated with X, or model misspecification. Heteroskedasticity does not bias OLS but inflates standard errors.

## Explainer

One of the OLS assumptions you learned is **homoskedasticity**: the variance of the error term is the same at every value of X, written Var(u|X) = σ². Heteroskedasticity is simply the violation of that assumption — the spread of errors around the regression line is not constant, but fans out (or contracts) as X changes. Visualize a scatter plot of residuals against fitted values: homoskedastic data produces a random cloud with uniform width; heteroskedastic data produces a funnel shape, a wedge, or some other pattern where variance grows or shrinks.

The intuition for why this happens in economic data is usually about scale. Consider a cross-sectional regression of household consumption on income. Poor households have limited options — their spending is tightly clustered near a predictable floor. Wealthy households have far more discretion; two households with the same income might spend very differently. So errors grow with income. Similarly, if you model firm profits as a function of revenue, errors in estimating the profit margin for a small firm are measured in thousands while errors for a large firm are measured in millions — even if the percentage error is the same, the absolute variance differs dramatically. This type, where variance grows with the scale of X, is the most common form in applied economics.

Other causes are subtler. **Omitted variables** cause heteroskedasticity when the omitted factor's influence is correlated with X — the omission introduces a non-random component into the error that varies with X. **Model misspecification** (for example, fitting a linear model to a relationship that is truly quadratic) can produce a systematic pattern in residuals that mimics heteroskedasticity. **Subgroup differences** also cause it: if your sample contains a mix of large and small firms, or urban and rural households, the error process may differ structurally across groups even at the same X value.

The critical practical consequence is what heteroskedasticity does — and does not — do to OLS. The estimates β̂ remain **unbiased** and **consistent**: on average, they still point at the right population parameters. What breaks is the variance formula. The standard formula for Var(β̂) assumes homoskedasticity; when that assumption fails, the formula gives the wrong answer, which means your standard errors, t-statistics, and confidence intervals are all wrong. Typically the standard errors are underestimated and t-statistics are inflated, making results look more statistically significant than they really are. Recognizing the types and causes of heteroskedasticity is the first step toward diagnosing and correcting it — which is why testing for it and using robust standard errors are standard practice in applied work.
