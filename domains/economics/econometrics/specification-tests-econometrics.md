---
id: specification-tests-econometrics
title: 'Specification Tests: Ramsey RESET and Hausman Tests'
domain: economics
course: econometrics
prerequisites:
- id: hypothesis-testing-regression
  type: hard
- id: omitted-variable-bias
  type: hard
tags:
- specification
- hypothesis-testing
- model-diagnostics
stage: formal-systems
status: draft
---

# Specification Tests: Ramsey RESET and Hausman Tests

## Core Idea
Specification tests formally check whether key assumptions hold. The RESET test detects omitted nonlinearities by adding powers of fitted values; Hausman tests compare two estimators to detect endogeneity or misspecification.

## Explainer

Your work on hypothesis testing in regression gave you the tools to test whether individual coefficients are zero. Specification tests take that logic up a level: instead of testing a coefficient, you test whether the model itself is correctly formulated. The two most important tools — the **Ramsey RESET test** and the **Hausman test** — each target a different type of misspecification.

The RESET test (Regression Equation Specification Error Test) addresses **functional form misspecification**. Your prerequisites covered omitted variable bias: if a variable belongs in the model but isn't included, OLS estimates are biased. Ramsey's insight was that you don't need to know what the omitted variable is — if the functional form is wrong, the fitted values ŷ will contain information about the missing structure. The procedure: run your original regression, save the fitted values, then add ŷ², ŷ³ (and optionally ŷ⁴) to the model and test their joint significance with an F-test. If those powers are significant, the original model is misspecified — something nonlinear belongs in the regression. The RESET test is a general-purpose alarm: it tells you something is wrong, but not what to add. It's useful as a quick check before reporting results.

The **Hausman test** operates on a different principle: comparing two estimators that both converge to the same value under the null hypothesis but differ under the alternative. The most common application is testing for **endogeneity**. OLS is efficient under exogeneity; instrumental variables (IV) is consistent even under endogeneity but less efficient. Under the null that OLS is consistent, the OLS and IV estimates should be close. If they differ systematically — which the Hausman statistic formalizes — that's evidence that OLS is inconsistent due to endogeneity, and IV should be preferred. The test statistic is (β̂_IV - β̂_OLS)'[Var(β̂_IV) - Var(β̂_OLS)]⁻¹(β̂_IV - β̂_OLS), which is chi-squared distributed under the null.

The broader lesson is that regression results should be reported alongside a suite of diagnostics, not just coefficients and standard errors. A model that passes the RESET test provides more credibility that the functional form is correct. A model where OLS and a valid IV give similar results provides evidence against endogeneity. Neither test is foolproof — the RESET test can miss certain misspecifications, and the Hausman test requires a valid instrument — but together they constitute a minimum standard for responsible empirical work.
