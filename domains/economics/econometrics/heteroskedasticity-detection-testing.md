---
id: heteroskedasticity-detection-testing
title: Testing for Heteroskedasticity
domain: economics
course: econometrics
prerequisites:
- id: heteroskedasticity
  type: hard
- id: heteroskedasticity-types-causes
  type: hard
builds-toward:
- robust-standard-errors
tags:
- heteroskedasticity
- testing
- diagnostics
stage: formal-systems
status: draft
---

# Testing for Heteroskedasticity

## Core Idea
Tests for heteroskedasticity include: residual scatter plots vs fitted values, Breusch-Pagan regression of squared residuals on X, and White's test using fitted values and squares. Each detects dependence of error variance on regressors; rejection indicates correction is needed.

## Explainer

From your study of heteroskedasticity, you know the core problem: when error variance is not constant across observations, OLS estimates remain unbiased but lose efficiency, and — critically — the standard errors become wrong, making t-tests and confidence intervals unreliable. Before choosing a remedy, you need to *detect* the problem. Testing for heteroskedasticity translates an abstract concern about non-constant variance into a concrete empirical question.

The simplest first step is graphical: after running a regression, plot the residuals (or squared residuals) against fitted values or against each explanatory variable. In homoskedastic data, this scatter should look like a random horizontal band with no pattern. **Heteroskedasticity** reveals itself as a funnel shape — residuals spreading wider as fitted values increase — or as distinct clusters of high versus low variance. This visual inspection is fast and often decisive; many experienced econometricians start here before running formal tests.

The **Breusch-Pagan test** formalizes this intuition. It runs a secondary regression with the squared OLS residuals as the dependent variable and the original regressors (or some function of them) as predictors. If error variance truly is unrelated to the regressors, this auxiliary regression should have no explanatory power — all coefficients should be zero, and R² should be near zero. The test statistic is n times R² from this auxiliary regression, which follows a chi-squared distribution under the null of homoskedasticity. A significant result means at least one regressor is predicting how large the errors are, which is exactly the definition of heteroskedasticity.

**White's test** is a more general version that doesn't assume a specific functional form for the variance. Instead of using the raw regressors, it uses the fitted values and their squares — a compact way to capture both linear and quadratic variance patterns without specifying them in advance. White's test catches forms of heteroskedasticity that Breusch-Pagan might miss. The tradeoff is that White's test uses more degrees of freedom and has lower power in small samples. In practice: if you have prior theory about which variable drives variance (e.g., income usually drives variance in consumption data), use Breusch-Pagan. If you're doing general diagnostics without strong priors, White's test is safer. Rejection from either test is a signal to move to robust standard errors or weighted least squares — the topics that follow directly from this one.
