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
status: validated
---

# Heteroskedasticity: Types and Causes

## Core Idea
Heteroskedasticity (non-constant error variance) occurs when Var(u|X) depends on X. Common sources include measurement error increasing with variable magnitude, omitted variables correlated with X, or model misspecification. Heteroskedasticity does not bias OLS but inflates standard errors.

## Questions

```yaml
- question: "A researcher estimates a regression of household consumption on income and finds evidence of heteroskedasticity. What is the most important consequence for their results?"
  type: multiple-choice
  options:
    - "The coefficient estimates β̂ are now biased and no longer point at the true population parameters"
    - "The coefficient estimates β̂ remain unbiased, but the standard errors are wrong, making t-statistics and confidence intervals unreliable"
    - "The R² statistic becomes meaningless under heteroskedasticity"
    - "OLS will fail to converge and produce no estimates at all"
  answer: 1
  explanation: "Heteroskedasticity does NOT bias OLS coefficients — β̂ remains unbiased and consistent. What breaks is the variance formula for β̂. The standard OLS formula for Var(β̂) assumes homoskedasticity; when that assumption fails, the formula gives wrong standard errors. Typically these are underestimated, making t-statistics too large and results appear more statistically significant than they really are. The distinction between biased estimates and wrong inference is the central practical lesson of this topic."

- question: "A regression of firm profits on revenue shows residuals that are small for small firms but very large for large firms. What is the most likely explanation?"
  type: multiple-choice
  options:
    - "The regression model is misspecified and should include a quadratic revenue term"
    - "Heteroskedasticity driven by scale: variance in profit grows with firm size because large firms have more discretion in how they allocate revenue"
    - "The large firms are outliers that should be removed before estimation"
    - "The error variance is constant — large residuals for large firms simply reflect larger absolute values, not different variance"
  answer: 1
  explanation: "This is the classic scale-driven heteroskedasticity pattern. Large firms generate larger absolute errors because discretion in allocating revenue grows with firm size — two firms with the same large revenue might have very different profits. The variance of the residual genuinely differs across the range of X. Option D confuses levels with variance: large firms having larger absolute residuals is exactly what heteroskedasticity looks like. Option A is possible but not the most likely explanation given a systematic fan-out pattern."

- question: "In a regression with heteroskedasticity, OLS coefficient estimates are biased toward zero."
  type: true-false
  answer: false
  explanation: "Heteroskedasticity does not bias OLS coefficient estimates. Unbiasedness only requires that errors have zero conditional mean — E(u|X) = 0 — which is a separate assumption from homoskedasticity. Heteroskedasticity violates the 'Best' part of Gauss-Markov (OLS is no longer the minimum-variance unbiased estimator) and breaks the standard error formula, but the estimates themselves remain unbiased and consistent. Bias would require the errors to be systematically correlated with X — that is endogeneity, a different violation."

- question: "Heteroskedasticity typically causes OLS standard errors to be underestimated, making t-statistics appear larger than they should be."
  type: true-false
  answer: true
  explanation: "When residual variance grows with X (the common fan-out pattern), the true variance of β̂ is larger than what the standard OLS formula reports. OLS assumes constant variance — it effectively averages variance across all observations. When high-X observations have much more variance than accounted for, the formula underestimates uncertainty. The result is standard errors that are too small, t-statistics that are too large, and p-values that are too small — spuriously significant results. This is why using robust standard errors is standard practice."

- question: "Why does heteroskedasticity break statistical inference (standard errors, t-tests) without biasing the OLS coefficient estimates themselves?"
  type: short-answer
  answer: "OLS minimizes the sum of squared residuals, which finds the best linear predictor of Y given X regardless of whether error variance is constant. Unbiasedness requires only that errors average to zero conditional on X — a property preserved under heteroskedasticity. But the formula for the standard error of β̂ is derived under the assumption that all errors have the same variance σ². When variance differs across X values, this formula gives the wrong answer. The coefficient converges to the right value; it's the uncertainty measure around that coefficient that is miscalculated."
  explanation: "Think of it this way: the coefficient captures the average relationship between X and Y, and OLS finds that average correctly. But standard errors measure how much you should trust your coefficient estimate — and that depends on how noisy each data point is. Heteroskedasticity means some data points are much noisier than others. The standard formula treats all observations as equally informative, which misrepresents actual uncertainty. Robust standard errors correct this by accounting for the actual pattern of residual variance."
```

## Explainer

One of the OLS assumptions you learned is **homoskedasticity**: the variance of the error term is the same at every value of X, written Var(u|X) = σ². Heteroskedasticity is simply the violation of that assumption — the spread of errors around the regression line is not constant, but fans out (or contracts) as X changes. Visualize a scatter plot of residuals against fitted values: homoskedastic data produces a random cloud with uniform width; heteroskedastic data produces a funnel shape, a wedge, or some other pattern where variance grows or shrinks.

The intuition for why this happens in economic data is usually about scale. Consider a cross-sectional regression of household consumption on income. Poor households have limited options — their spending is tightly clustered near a predictable floor. Wealthy households have far more discretion; two households with the same income might spend very differently. So errors grow with income. Similarly, if you model firm profits as a function of revenue, errors in estimating the profit margin for a small firm are measured in thousands while errors for a large firm are measured in millions — even if the percentage error is the same, the absolute variance differs dramatically. This type, where variance grows with the scale of X, is the most common form in applied economics.

Other causes are subtler. **Omitted variables** cause heteroskedasticity when the omitted factor's influence is correlated with X — the omission introduces a non-random component into the error that varies with X. **Model misspecification** (for example, fitting a linear model to a relationship that is truly quadratic) can produce a systematic pattern in residuals that mimics heteroskedasticity. **Subgroup differences** also cause it: if your sample contains a mix of large and small firms, or urban and rural households, the error process may differ structurally across groups even at the same X value.

The critical practical consequence is what heteroskedasticity does — and does not — do to OLS. The estimates β̂ remain **unbiased** and **consistent**: on average, they still point at the right population parameters. What breaks is the variance formula. The standard formula for Var(β̂) assumes homoskedasticity; when that assumption fails, the formula gives the wrong answer, which means your standard errors, t-statistics, and confidence intervals are all wrong. Typically the standard errors are underestimated and t-statistics are inflated, making results look more statistically significant than they really are. Recognizing the types and causes of heteroskedasticity is the first step toward diagnosing and correcting it — which is why testing for it and using robust standard errors are standard practice in applied work.
