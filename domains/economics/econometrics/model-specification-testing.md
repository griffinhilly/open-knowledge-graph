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
status: draft
---

# Model Specification Testing and Diagnostics

## Core Idea
Model specification testing evaluates whether chosen functional form, regressor sets, and error structure assumptions are appropriate for the data. Common tests include Ramsey RESET for functional form misspecification and comparison of nested models through F-tests; diagnostic checks examine residuals for deviations from white noise.

## Explainer

From your work on multiple regression and hypothesis testing, you know how to estimate a model and test whether individual coefficients are statistically significant. But there is a prior question: is the model itself correctly specified? Significance tests assume the model's functional form is right, the relevant variables are included, and the errors are well-behaved. If those assumptions fail, your t-statistics and F-statistics are meaningless — you are testing hypotheses in a model that misrepresents the data-generating process. Specification testing addresses exactly this: how do we detect when the model is wrong before trusting what it tells us?

The broadest class of specification tests asks whether the **functional form** is appropriate. The most common is the **Ramsey RESET test** (Regression Specification Error Test). The logic is elegant: if your linear model is correctly specified, the fitted values Ŷ should already capture all systematic variation in Y, and powers of Ŷ (like Ŷ² and Ŷ³) should have no additional predictive power. The RESET test adds these powers as auxiliary regressors and uses an F-test to check whether they are jointly significant. A rejection is a signal that the original linear model is missing something — possibly a nonlinear relationship, an interaction term, or an omitted variable that enters nonlinearly. What it cannot tell you is *what* is wrong; RESET is a diagnostic, not a prescription.

Testing **nested models** via F-tests is the second major tool. A restricted model is nested inside an unrestricted model when the restricted model imposes specific parameter constraints (usually setting some coefficients to zero). The F-statistic compares how much explanatory power is lost by imposing the restriction. If the restricted model fits nearly as well — if the loss in R² is small relative to the degrees of freedom consumed — the restriction is not rejected. This framework allows principled comparison of competing specifications that differ in which variables are included.

**Residual diagnostics** complement formal tests by revealing patterns that indicate model failure. If residuals exhibit **heteroskedasticity** — variance that changes with fitted values or a regressor — the standard errors are wrong even if the coefficients are unbiased. If residuals are **autocorrelated** — systematically positive or negative in runs — this often signals a missing dynamic structure. If residuals are non-normal, inference in small samples is unreliable. Plots of residuals against fitted values, against each regressor, and over time (for time-series data) are the first-line tools. Formal tests (Breusch-Pagan for heteroskedasticity, Durbin-Watson for autocorrelation) add statistical precision. Together, specification testing and residual diagnostics form the discipline of checking your model before trusting it.
