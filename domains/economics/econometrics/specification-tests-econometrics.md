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
status: validated
---

# Specification Tests: Ramsey RESET and Hausman Tests

## Core Idea
Specification tests formally check whether key assumptions hold. The RESET test detects omitted nonlinearities by adding powers of fitted values; Hausman tests compare two estimators to detect endogeneity or misspecification.

## Questions

```yaml
- question: "You run a RESET test on your regression model and reject the null hypothesis at the 5% level. What can you correctly conclude?"
  type: multiple-choice
  options:
    - "Your model suffers from omitted variable bias and you should add more control variables"
    - "The functional form of your model is likely misspecified — something nonlinear belongs in the regression — but RESET does not tell you what to add"
    - "At least one of your explanatory variables is endogenous and correlated with the error term"
    - "Your standard errors are heteroskedastic and need to be corrected with robust standard errors"
  answer: 1
  explanation: "The RESET test detects functional form misspecification by testing whether powers of the fitted values (ŷ², ŷ³) have joint explanatory power. Rejecting the null means the model is misspecified — the relationship is likely nonlinear — but the test is a general alarm: it tells you something is wrong without specifying what. It does not directly diagnose endogeneity, omitted variables, or heteroskedasticity. The next step is to think about what transformation or variable might capture the nonlinearity."

- question: "In a Hausman test comparing OLS and IV estimates, what is the null hypothesis, and what does rejecting it imply?"
  type: multiple-choice
  options:
    - "Null: both OLS and IV are biased; rejection implies you should use a different estimator entirely"
    - "Null: OLS is consistent (regressors are exogenous); rejection implies OLS is inconsistent due to endogeneity and IV should be preferred"
    - "Null: the IV instrument is invalid; rejection implies you have found a valid instrument"
    - "Null: the model has the correct functional form; rejection implies nonlinearity"
  answer: 1
  explanation: "The Hausman test exploits the fact that OLS and IV converge to the same value under exogeneity (null), but diverge under endogeneity (alternative). Under the null, OLS is consistent and efficient; IV is consistent but less efficient. If the two estimates differ systematically — which the test formalizes — the best explanation is that OLS is inconsistent because one or more regressors are correlated with the error term, and IV should be preferred."

- question: "The RESET test can detect functional form misspecification without requiring the researcher to know in advance which variable or transformation is missing from the model."
  type: true-false
  answer: true
  explanation: "This is Ramsey's key insight: if the functional form is wrong, the fitted values ŷ contain information about the missing structure. Adding powers of ŷ (ŷ², ŷ³) and testing their joint significance effectively checks for any systematic nonlinearity in the residuals, regardless of its source. The test serves as a general-purpose diagnostic before you know what the problem is — a signal to investigate further, not a prescription for what to add."

- question: "If the Hausman test fails to reject the null hypothesis, this proves that OLS is unbiased."
  type: true-false
  answer: false
  explanation: "Failing to reject the null provides evidence that OLS is consistent (that regressors are approximately exogenous), but it does not prove unbiasedness. OLS can be consistent without being unbiased in finite samples. Moreover, the Hausman test's power depends critically on having a valid instrument — if the instrument is weak or invalid, the test may lack the power to detect real endogeneity. A non-rejection is evidence, not proof."

- question: "Explain the logic of the Hausman test. Why does comparing two estimators reveal information about endogeneity?"
  type: short-answer
  answer: "The Hausman test exploits the fact that OLS and IV have different properties under endogeneity. Under exogeneity (null), both are consistent and should produce similar estimates — any difference is just sampling noise. Under endogeneity (alternative), OLS is inconsistent (it absorbs the correlation between regressor and error into the coefficient), but IV remains consistent if the instrument is valid. A systematic difference between the two estimates is therefore evidence that OLS is inconsistent — i.e., that endogeneity is present. The test formalizes this comparison using the asymptotic variance of the difference."
  explanation: "The beauty of the Hausman approach is that it doesn't require knowing the source of endogeneity — it only requires a valid instrument and the observation that two estimators 'should agree' under the null. This same logic generalizes: any time you have two estimators that agree under the null but differ under the alternative, you can construct a Hausman-style test. The random effects vs. fixed effects test in panel data follows exactly this structure."
```

## Explainer

Your work on hypothesis testing in regression gave you the tools to test whether individual coefficients are zero. Specification tests take that logic up a level: instead of testing a coefficient, you test whether the model itself is correctly formulated. The two most important tools — the **Ramsey RESET test** and the **Hausman test** — each target a different type of misspecification.

The RESET test (Regression Equation Specification Error Test) addresses **functional form misspecification**. Your prerequisites covered omitted variable bias: if a variable belongs in the model but isn't included, OLS estimates are biased. Ramsey's insight was that you don't need to know what the omitted variable is — if the functional form is wrong, the fitted values ŷ will contain information about the missing structure. The procedure: run your original regression, save the fitted values, then add ŷ², ŷ³ (and optionally ŷ⁴) to the model and test their joint significance with an F-test. If those powers are significant, the original model is misspecified — something nonlinear belongs in the regression. The RESET test is a general-purpose alarm: it tells you something is wrong, but not what to add. It's useful as a quick check before reporting results.

The **Hausman test** operates on a different principle: comparing two estimators that both converge to the same value under the null hypothesis but differ under the alternative. The most common application is testing for **endogeneity**. OLS is efficient under exogeneity; instrumental variables (IV) is consistent even under endogeneity but less efficient. Under the null that OLS is consistent, the OLS and IV estimates should be close. If they differ systematically — which the Hausman statistic formalizes — that's evidence that OLS is inconsistent due to endogeneity, and IV should be preferred. The test statistic is (β̂_IV - β̂_OLS)'[Var(β̂_IV) - Var(β̂_OLS)]⁻¹(β̂_IV - β̂_OLS), which is chi-squared distributed under the null.

The broader lesson is that regression results should be reported alongside a suite of diagnostics, not just coefficients and standard errors. A model that passes the RESET test provides more credibility that the functional form is correct. A model where OLS and a valid IV give similar results provides evidence against endogeneity. Neither test is foolproof — the RESET test can miss certain misspecifications, and the Hausman test requires a valid instrument — but together they constitute a minimum standard for responsible empirical work.
