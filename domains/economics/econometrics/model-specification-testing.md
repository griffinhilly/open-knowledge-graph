---
id: model-specification-testing
title: Model Specification Testing and Diagnostics
domain: economics
course: econometrics
prerequisites:
- id: hypothesis-testing-regression
  type: hard
- id: multiple-regression-model
  type: hard
builds-toward:
- akaike-criterion-information
tags:
- model-selection
- specification
- testing
stage: formal-systems
status: validated
---

# Model Specification Testing and Diagnostics

## Core Idea
Model specification testing evaluates whether chosen functional form, regressor sets, and error structure assumptions are appropriate for the data. Common tests include Ramsey RESET for functional form misspecification and comparison of nested models through F-tests; diagnostic checks examine residuals for deviations from white noise.

## Questions

```yaml
- question: "A researcher runs a Ramsey RESET test on their OLS regression and rejects the null hypothesis at the 5% level. What can they conclude?"
  type: multiple-choice
  options:
    - "At least one of the included regressors is statistically insignificant and should be dropped"
    - "The model has a specification problem — possibly a missing nonlinear term, interaction, or omitted variable — but the test doesn't identify what is wrong"
    - "The error term is heteroskedastic and robust standard errors should be used"
    - "The model is correctly specified but the sample size is too small to estimate precisely"
  answer: 1
  explanation: "RESET is a diagnostic, not a prescription. A rejection means the fitted values' powers (Ŷ², Ŷ³) have additional explanatory power beyond the original regressors, which signals that the linear model is missing something systematic. But the test cannot identify whether the problem is a nonlinear functional form, a missing interaction term, or an omitted variable that enters nonlinearly — the researcher must investigate separately. RESET does not test for heteroskedasticity (that's Breusch-Pagan), individual regressor significance (that's t-tests), or sample size adequacy."

- question: "A researcher finds that their regression residuals show a clear fan shape — small residuals at low fitted values, large residuals at high fitted values. What is the primary concern?"
  type: multiple-choice
  options:
    - "The residuals are autocorrelated, indicating a missing lag variable"
    - "The model has omitted variable bias, inflating coefficient estimates"
    - "Heteroskedasticity is present, meaning standard errors are wrong even though coefficient estimates may be unbiased"
    - "The sample has outliers that should be removed before re-estimating"
  answer: 2
  explanation: "A fan shape in residuals vs. fitted values is the classic signature of heteroskedasticity — the error variance grows with fitted values. The coefficients themselves may still be unbiased (OLS is unbiased under heteroskedasticity), but the standard errors are incorrect, making all t-statistics, p-values, and confidence intervals invalid. This is why residual diagnostics are essential before trusting any inferential output. The fix is typically robust (heteroskedasticity-consistent) standard errors or weighted least squares."

- question: "If you run a Ramsey RESET test and fail to reject the null hypothesis, you have confirmed that your model is correctly specified."
  type: true-false
  answer: false
  explanation: "False. Failing to reject RESET means the test did not detect evidence of functional form misspecification using powers of fitted values as auxiliary regressors — it is not a confirmation of correct specification. RESET has limited power against certain alternatives (e.g., particular omitted variables), and other specification problems (heteroskedasticity, autocorrelation, wrong regressors) are not tested by RESET at all. Specification testing is a collection of diagnostics; passing one test does not certify the model."

- question: "If a regression model is misspecified — for example, if it omits a variable that belongs in the equation — then the t-statistics on included coefficients can be misleading even if they appear highly significant."
  type: true-false
  answer: true
  explanation: "True. Omitting a relevant variable typically causes omitted variable bias: the included coefficients absorb the effect of the missing variable, and their estimates are biased. More subtly, the standard errors and t-statistics are computed assuming the model is correctly specified. If the true error includes the omitted variable's variation, the error structure assumed by OLS is wrong. A t-statistic may appear large not because a true effect exists but because a correlated omitted variable is driving both. This is why specification testing must precede inferential interpretation."

- question: "Why must specification testing logically precede hypothesis testing in a regression analysis, rather than being performed afterward as a check?"
  type: short-answer
  answer: "Hypothesis testing (t-tests, F-tests, confidence intervals) assumes the model is correctly specified — that the functional form is appropriate, the right variables are included, and the error term satisfies OLS assumptions. If any of these assumptions fail, the distribution of test statistics is no longer what the formulas assume, and p-values and confidence intervals are invalid. Specification testing examines whether these prerequisites hold. Running hypothesis tests first and then checking specification afterward treats the conclusions as valid before establishing that the framework producing them is sound. The logical order is: check model validity first, then trust what the model tells you."
  explanation: "The practical consequence is that researchers who skip specification diagnostics may confidently report 'significant' results that are artifacts of misspecification — nonlinear relationships modeled as linear, autocorrelated errors treated as white noise, or heteroskedastic variance producing inflated or deflated standard errors. Each of these failures makes the reported statistics unreliable as evidence. Specification testing is the discipline of checking your instrument before trusting its readings."
```

## Explainer

From your work on multiple regression and hypothesis testing, you know how to estimate a model and test whether individual coefficients are statistically significant. But there is a prior question: is the model itself correctly specified? Significance tests assume the model's functional form is right, the relevant variables are included, and the errors are well-behaved. If those assumptions fail, your t-statistics and F-statistics are meaningless — you are testing hypotheses in a model that misrepresents the data-generating process. Specification testing addresses exactly this: how do we detect when the model is wrong before trusting what it tells us?

The broadest class of specification tests asks whether the **functional form** is appropriate. The most common is the **Ramsey RESET test** (Regression Specification Error Test). The logic is elegant: if your linear model is correctly specified, the fitted values Ŷ should already capture all systematic variation in Y, and powers of Ŷ (like Ŷ² and Ŷ³) should have no additional predictive power. The RESET test adds these powers as auxiliary regressors and uses an F-test to check whether they are jointly significant. A rejection is a signal that the original linear model is missing something — possibly a nonlinear relationship, an interaction term, or an omitted variable that enters nonlinearly. What it cannot tell you is *what* is wrong; RESET is a diagnostic, not a prescription.

Testing **nested models** via F-tests is the second major tool. A restricted model is nested inside an unrestricted model when the restricted model imposes specific parameter constraints (usually setting some coefficients to zero). The F-statistic compares how much explanatory power is lost by imposing the restriction. If the restricted model fits nearly as well — if the loss in R² is small relative to the degrees of freedom consumed — the restriction is not rejected. This framework allows principled comparison of competing specifications that differ in which variables are included.

**Residual diagnostics** complement formal tests by revealing patterns that indicate model failure. If residuals exhibit **heteroskedasticity** — variance that changes with fitted values or a regressor — the standard errors are wrong even if the coefficients are unbiased. If residuals are **autocorrelated** — systematically positive or negative in runs — this often signals a missing dynamic structure. If residuals are non-normal, inference in small samples is unreliable. Plots of residuals against fitted values, against each regressor, and over time (for time-series data) are the first-line tools. Formal tests (Breusch-Pagan for heteroskedasticity, Durbin-Watson for autocorrelation) add statistical precision. Together, specification testing and residual diagnostics form the discipline of checking your model before trusting it.
