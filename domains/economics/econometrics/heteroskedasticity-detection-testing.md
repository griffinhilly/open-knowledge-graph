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

## Questions

```yaml
- question: "After running a regression of consumption on income, you plot residuals against fitted values and see a clear funnel shape — variance increasing with fitted values. Which formal test is most appropriate to confirm this, and what would rejection indicate?"
  type: multiple-choice
  options:
    - "An F-test for joint significance; rejection means some regressors are not significant"
    - "A Breusch-Pagan test; rejection means error variance is systematically related to the regressors"
    - "A Durbin-Watson test; rejection means residuals are correlated across observations"
    - "A Hausman test; rejection means the regressors are endogenous"
  answer: 1
  explanation: "The funnel shape is the classic visual signature of heteroskedasticity — variance growing with fitted values. The Breusch-Pagan test formalizes this: it runs an auxiliary regression of squared OLS residuals on the original regressors and tests whether any coefficient is nonzero (i.e., whether residual size is predictable from the regressors). Rejection confirms that error variance depends on at least one regressor. The other tests detect different problems: F-tests for joint significance, Durbin-Watson for serial autocorrelation, Hausman for endogeneity."

- question: "A researcher uses White's test instead of Breusch-Pagan. What is the main reason White's test might be preferred, and what is its key limitation?"
  type: multiple-choice
  options:
    - "White's test is preferred because it has higher power in all sample sizes; its limitation is it requires specifying the functional form for variance"
    - "White's test is preferred because it does not require assuming which regressors drive variance; its limitation is lower power in small samples due to using more degrees of freedom"
    - "White's test is preferred for detecting serial correlation; its limitation is it cannot detect heteroskedasticity in cross-sectional data"
    - "White's test is preferred because it is computationally simpler; its limitation is it only works for continuous regressors"
  answer: 1
  explanation: "White's test uses fitted values and their squares as auxiliary regressors rather than the original regressors, making it agnostic about the functional form of heteroskedasticity. This generality lets it catch patterns that Breusch-Pagan misses when variance depends on nonlinear combinations of regressors. The cost is consuming more degrees of freedom, which reduces statistical power in small samples. Breusch-Pagan is preferred when theory suggests which specific variable drives variance; White's test is the safer diagnostic when there are no strong priors."

- question: "The Breusch-Pagan test works by regressing squared OLS residuals on the original explanatory variables and testing whether the coefficients are jointly zero."
  type: true-false
  answer: true
  explanation: "This is an accurate description of the Breusch-Pagan procedure. If error variance is constant (homoskedasticity), squared residuals should be unrelated to any regressor — the auxiliary regression should have no explanatory power. The test statistic is n × R² from this auxiliary regression, distributed chi-squared under the null. A significant result means at least one regressor predicts residual size, which is exactly what heteroskedasticity means: variance is not constant but systematically related to the regressors."

- question: "Because OLS coefficient estimates are unbiased under heteroskedasticity, detecting heteroskedasticity requires no change to the estimation or inference procedure."
  type: true-false
  answer: false
  explanation: "This is a critical misconception. OLS coefficients are indeed unbiased under heteroskedasticity — the estimates of β are numerically correct. But the standard errors are wrong: OLS standard errors assume constant variance, so they are too small or too large under heteroskedasticity, making t-statistics and confidence intervals unreliable. Hypothesis tests based on incorrect standard errors can badly mislead. Detecting heteroskedasticity is a signal to switch to heteroskedasticity-robust standard errors or weighted least squares to restore valid inference."

- question: "What is the null hypothesis of the Breusch-Pagan test, and what does rejection tell you about the need to change your estimation strategy?"
  type: short-answer
  answer: "The null hypothesis is homoskedasticity: error variance is constant and unrelated to any regressor. Rejection means at least one regressor predicts the magnitude of the errors. OLS coefficient estimates remain unbiased, but standard errors are inconsistent, making t-statistics and confidence intervals unreliable. Rejection indicates you should switch to heteroskedasticity-robust standard errors or weighted least squares."
  explanation: "It's important to distinguish what rejection does and does not imply. The coefficients (β̂) are still correct point estimates — heteroskedasticity does not bias them. What's broken is the precision estimate: OLS standard errors assume Var(ε) = σ²I, so they are systematically wrong when variance differs across observations. Robust standard errors (e.g., HC3) correct the inference problem without changing the coefficients. Weighted least squares is more efficient if you can correctly specify the variance function."
```

## Explainer

From your study of heteroskedasticity, you know the core problem: when error variance is not constant across observations, OLS estimates remain unbiased but lose efficiency, and — critically — the standard errors become wrong, making t-tests and confidence intervals unreliable. Before choosing a remedy, you need to *detect* the problem. Testing for heteroskedasticity translates an abstract concern about non-constant variance into a concrete empirical question.

The simplest first step is graphical: after running a regression, plot the residuals (or squared residuals) against fitted values or against each explanatory variable. In homoskedastic data, this scatter should look like a random horizontal band with no pattern. **Heteroskedasticity** reveals itself as a funnel shape — residuals spreading wider as fitted values increase — or as distinct clusters of high versus low variance. This visual inspection is fast and often decisive; many experienced econometricians start here before running formal tests.

The **Breusch-Pagan test** formalizes this intuition. It runs a secondary regression with the squared OLS residuals as the dependent variable and the original regressors (or some function of them) as predictors. If error variance truly is unrelated to the regressors, this auxiliary regression should have no explanatory power — all coefficients should be zero, and R² should be near zero. The test statistic is n times R² from this auxiliary regression, which follows a chi-squared distribution under the null of homoskedasticity. A significant result means at least one regressor is predicting how large the errors are, which is exactly the definition of heteroskedasticity.

**White's test** is a more general version that doesn't assume a specific functional form for the variance. Instead of using the raw regressors, it uses the fitted values and their squares — a compact way to capture both linear and quadratic variance patterns without specifying them in advance. White's test catches forms of heteroskedasticity that Breusch-Pagan might miss. The tradeoff is that White's test uses more degrees of freedom and has lower power in small samples. In practice: if you have prior theory about which variable drives variance (e.g., income usually drives variance in consumption data), use Breusch-Pagan. If you're doing general diagnostics without strong priors, White's test is safer. Rejection from either test is a signal to move to robust standard errors or weighted least squares — the topics that follow directly from this one.
