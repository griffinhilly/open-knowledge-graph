---
id: specification-error-reset-test
title: 'Specification Error: RESET Test'
domain: economics
course: econometrics
prerequisites:
- id: multiple-regression-model
  type: hard
- id: hypothesis-testing-regression
  type: hard
tags:
- specification-error
- functional-form
- testing
stage: formal-systems
status: draft
---

# Specification Error: RESET Test

## Core Idea
The Regression Specification Error Test (RESET) adds powers of fitted values Ŷ to the regression and tests their joint significance. Rejection suggests omitted nonlinearity or wrong functional form, though RESET does not identify the specific misspecification.

## Explainer

You have learned to estimate multiple regression models and to test hypotheses using F-statistics. The RESET test is a clever application of that same F-test machinery, turned inward: instead of testing whether certain external variables matter, it tests whether your own model's predictions can predict *themselves better* with a nonlinear adjustment. The insight is that if you have specified the correct functional form, the fitted values Ŷ already summarize everything the regressors can tell you about Y. Any remaining systematic pattern in Y — anything left for Ŷ², Ŷ³, or higher powers to explain — is evidence that the linear model is leaving structure on the table.

The mechanics work as follows. Estimate your original model: Y = β₀ + β₁X₁ + β₂X₂ + ... + u, and save the fitted values Ŷ. Then run an augmented regression that adds Ŷ² (and optionally Ŷ³) as additional regressors: Y = β₀ + β₁X₁ + β₂X₂ + ... + γ₁Ŷ² + γ₂Ŷ³ + u. The null hypothesis is γ₁ = γ₂ = 0 — the powers add nothing. Test this with an **F-statistic** comparing restricted (original) to unrestricted (augmented) models. Rejection of the null at conventional significance levels is a signal of **functional form misspecification**: the linear model is not capturing the true shape of the relationship between Y and the regressors.

What is RESET detecting? It is sensitive to several problems simultaneously. Omitting a relevant variable that enters nonlinearly shows up as unexplained curvature, which Ŷ² and Ŷ³ can partially absorb. Using a linear form when the true relationship is log-linear, quadratic, or otherwise curved triggers rejection. Missing interaction terms between regressors can also show up. This breadth makes RESET a useful screening test — a positive test should prompt you to reconsider your specification. The limitation is the same breadth: RESET does not tell you which of these problems you have, only that something is wrong.

A useful mental model: Ŷ is a linear combination of your regressors, so Ŷ² is a sum of all pairwise products and squared terms from those regressors. When RESET rejects, it is essentially saying that some combination of quadratic and interaction terms among your existing regressors would improve the fit. Common remedies include adding squared terms for regressors that might have diminishing or accelerating effects, adding interaction terms, transforming variables (log, square root), or reconsidering whether the outcome variable itself should be transformed. RESET is the diagnostic; what to do after rejection requires substantive judgment about the underlying economic relationship.
