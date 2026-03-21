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

## Questions

```yaml
- question: "You run the RESET test on a regression of wages on years of education and experience. The F-test for Ŷ² and Ŷ³ is rejected at the 1% level. What is the correct interpretation?"
  type: multiple-choice
  options:
    - "The original regression has perfect multicollinearity and must be re-estimated"
    - "The linear model likely has functional form misspecification — the relationship may be nonlinear or missing interaction terms"
    - "Years of education and experience are jointly insignificant predictors of wages"
    - "The model has heteroskedastic errors and requires robust standard errors"
  answer: 1
  explanation: "RESET rejection means that powers of the fitted values (Ŷ², Ŷ³) have additional predictive power beyond what the linear model already captures. Since Ŷ is a linear combination of the regressors, Ŷ² implicitly tests all quadratic and interaction terms simultaneously. Rejection signals that the true relationship involves nonlinearity (e.g., wage returns to education may be convex) or missing interactions. It says nothing about multicollinearity (A), the significance of individual predictors (C), or heteroskedasticity (D) — those require separate diagnostics."

- question: "When running the RESET test for a regression Y = β₀ + β₁X₁ + β₂X₂ + u, what additional regressors are added to the augmented regression?"
  type: multiple-choice
  options:
    - "X₁² and X₂² — squares of the original predictors"
    - "X₁², X₂², and X₁X₂ — all quadratic and interaction terms"
    - "Ŷ² and optionally Ŷ³ — powers of the fitted values from the original model"
    - "û² and û³ — powers of the residuals from the original model"
  answer: 2
  explanation: "RESET adds powers of the fitted values Ŷ — specifically Ŷ² and optionally Ŷ³ — not powers of the original regressors. This is RESET's elegance: since Ŷ is a linear combination of all regressors, Ŷ² implicitly expands into all squared terms and pairwise products simultaneously, testing broadly for nonlinearity with just one or two added variables. Adding squares of individual regressors (A, B) would be a targeted test, not a general screening test. Using residuals (D) confuses RESET with other diagnostic procedures."

- question: "Failing to reject the RESET null hypothesis proves that the model's functional form is correctly specified."
  type: true-false
  answer: false
  explanation: "Failure to reject is not proof of correct specification — it is only evidence that this test did not detect a problem. RESET has limited power against certain misspecifications, such as omitted variables that enter linearly or misspecification in the error distribution. As with all hypothesis tests, failing to reject can reflect a Type II error (missing a real problem) rather than absence of a problem. The correct interpretation: 'RESET found no evidence of nonlinear functional form,' not 'the model is correctly specified.'"

- question: "RESET rejection identifies which specific regressor is causing functional form misspecification."
  type: true-false
  answer: false
  explanation: "This is RESET's key limitation. Because Ŷ² combines all regressors nonlinearly, rejection could mean any of several things — one regressor needs a quadratic term, two regressors interact, the dependent variable should be transformed, or other issues. RESET is a screening test that signals something is wrong but gives no guidance on what to fix. After rejection, diagnosing the specific problem requires substantive economic reasoning and further targeted tests. RESET detects; it does not diagnose."

- question: "Why does RESET add powers of the fitted values Ŷ rather than powers of each individual regressor directly?"
  type: short-answer
  answer: "Using Ŷ² and Ŷ³ is a parsimonious way to test for many types of nonlinearity simultaneously with just one or two added variables. Since Ŷ = β̂₀ + β̂₁X₁ + β̂₂X₂ + ..., Ŷ² expands algebraically into a sum of all squared terms and pairwise cross-products of the regressors. Adding Ŷ² therefore implicitly tests all quadratic and interaction effects at once, using a single degree of freedom in the F-test. Adding powers of each regressor individually would require many parameters, diluting the test's power and requiring more degrees of freedom."
  explanation: "The tradeoff is diagnostic resolution: the compression of all nonlinear terms into Ŷ² makes the test powerful and parsimonious, but at the cost of ambiguity when it rejects. RESET tells you that something nonlinear is missing; finding out which something requires substantive judgment."
```

## Explainer

You have learned to estimate multiple regression models and to test hypotheses using F-statistics. The RESET test is a clever application of that same F-test machinery, turned inward: instead of testing whether certain external variables matter, it tests whether your own model's predictions can predict *themselves better* with a nonlinear adjustment. The insight is that if you have specified the correct functional form, the fitted values Ŷ already summarize everything the regressors can tell you about Y. Any remaining systematic pattern in Y — anything left for Ŷ², Ŷ³, or higher powers to explain — is evidence that the linear model is leaving structure on the table.

The mechanics work as follows. Estimate your original model: Y = β₀ + β₁X₁ + β₂X₂ + ... + u, and save the fitted values Ŷ. Then run an augmented regression that adds Ŷ² (and optionally Ŷ³) as additional regressors: Y = β₀ + β₁X₁ + β₂X₂ + ... + γ₁Ŷ² + γ₂Ŷ³ + u. The null hypothesis is γ₁ = γ₂ = 0 — the powers add nothing. Test this with an **F-statistic** comparing restricted (original) to unrestricted (augmented) models. Rejection of the null at conventional significance levels is a signal of **functional form misspecification**: the linear model is not capturing the true shape of the relationship between Y and the regressors.

What is RESET detecting? It is sensitive to several problems simultaneously. Omitting a relevant variable that enters nonlinearly shows up as unexplained curvature, which Ŷ² and Ŷ³ can partially absorb. Using a linear form when the true relationship is log-linear, quadratic, or otherwise curved triggers rejection. Missing interaction terms between regressors can also show up. This breadth makes RESET a useful screening test — a positive test should prompt you to reconsider your specification. The limitation is the same breadth: RESET does not tell you which of these problems you have, only that something is wrong.

A useful mental model: Ŷ is a linear combination of your regressors, so Ŷ² is a sum of all pairwise products and squared terms from those regressors. When RESET rejects, it is essentially saying that some combination of quadratic and interaction terms among your existing regressors would improve the fit. Common remedies include adding squared terms for regressors that might have diminishing or accelerating effects, adding interaction terms, transforming variables (log, square root), or reconsidering whether the outcome variable itself should be transformed. RESET is the diagnostic; what to do after rejection requires substantive judgment about the underlying economic relationship.
