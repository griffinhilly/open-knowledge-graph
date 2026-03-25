---
id: white-test-heteroskedasticity
title: White Test and Detection of Heteroskedasticity
domain: economics
course: econometrics
prerequisites:
- id: heteroskedasticity
  type: hard
- id: f-test-joint-significance
  type: hard
- id: heteroskedasticity-detection-testing
  type: soft
- id: specification-error-reset-test
  type: soft
builds-toward:
- generalized-least-squares
tags:
- heteroskedasticity
- testing
- diagnostics
stage: formal-systems
status: validated
---
# White Test and Detection of Heteroskedasticity

## Core Idea
White's test detects heteroskedasticity by regressing squared residuals on all regressors and their interactions, testing whether these variables explain squared residuals. Unlike Breusch-Pagan, it is robust to specific forms of heteroskedasticity, making it practical for applied work when the source of heteroskedasticity is unknown.

## Questions

```yaml
- question: "You run White's test on your regression and reject the null hypothesis at the 5% level. What is the most important diagnostic question to ask before switching to robust standard errors?"
  type: multiple-choice
  options:
    - "Whether your sample size is large enough for the chi-squared approximation to be valid"
    - "Whether your model is correctly specified, since misspecification can also produce systematic residual patterns that White's test detects"
    - "Whether you should use Breusch-Pagan instead to confirm the result"
    - "Whether the auxiliary regression's R² is above 0.5"
  answer: 1
  explanation: "White's test detects whether squared residuals are systematically explained by the regressors. Both genuine heteroskedasticity and model misspecification (e.g., omitting a quadratic term) produce systematic patterns in residuals. White's test cannot distinguish between the two causes. If the real problem is a misspecified functional form, switching to robust standard errors leaves the bias from misspecification untreated. The correct first response is to interrogate the model specification, not automatically apply a correction for heteroskedasticity."

- question: "How does White's test fundamentally differ from Breusch-Pagan in its approach to detecting heteroskedasticity?"
  type: multiple-choice
  options:
    - "White's test uses F-statistics, while Breusch-Pagan uses chi-squared statistics"
    - "White's test includes squared regressors and cross-products in the auxiliary regression, making it general rather than assuming a specific linear form for the heteroskedasticity"
    - "White's test requires a larger sample size because it tests a different null hypothesis"
    - "Breusch-Pagan is the general test and White's is a restricted special case"
  answer: 1
  explanation: "Breusch-Pagan tests whether error variance is a linear function of the regressors — it assumes heteroskedasticity, if present, takes a specific linear form. White's test makes no such assumption: by adding squared terms and cross-products of all regressors, it searches for nonlinear and interactive patterns in error variance. This generality is its main advantage when you don't know how variance relates to the regressors. The downside is that more auxiliary variables consume more degrees of freedom."

- question: "In White's test, the dependent variable in the auxiliary regression is the squared OLS residual ê²."
  type: true-false
  answer: true
  explanation: "Since the true error variance Var(u|X) is unobservable, the squared residual ê² serves as a proxy. The auxiliary regression asks: do the regressors, their squares, and their cross-products explain variation in ê²? If yes (significant R²), the null of homoskedasticity is rejected. The test statistic nR² follows a chi-squared distribution under the null."

- question: "Rejecting the null in White's test conclusively establishes that the model has heteroskedastic errors rather than a misspecified functional form."
  type: true-false
  answer: false
  explanation: "White's test cannot distinguish between these two causes. A misspecified model — for example, fitting a straight line to a relationship that is actually quadratic — will produce residuals with systematic patterns that depend on the regressors. White's test will detect this and reject the null, even though the issue is misspecification, not heteroskedasticity. This is why the test should trigger a model-specification check first, not an automatic switch to heteroskedasticity corrections."

- question: "Why might White's test reject the null of homoskedasticity even when the true error variance is constant? What alternative explanation should you investigate first?"
  type: short-answer
  answer: "White's test uses squared residuals as a proxy for error variance and tests whether the regressors, their squares, and their cross-products explain those squared residuals. But systematic patterns in squared residuals are not unique to heteroskedasticity — they also arise when the model is misspecified (wrong functional form, omitted variables, incorrect link function). A misspecified model produces residuals that systematically vary with the regressors, which White's test detects. The first step after rejection should be to check model specification: add polynomial terms, inspect residual plots, and consider whether the functional form is appropriate before concluding that heteroskedasticity is the problem."
  explanation: "This caution is practically important. Applying robust standard errors to a misspecified model still leaves the specification bias in the coefficient estimates — it only addresses inference. Fixing the model specification is the more fundamental correction. White's test rejection is a diagnostic signal, not a definitive diagnosis."
```

## Explainer

You know from studying heteroskedasticity that the problem is non-constant error variance — Var(u|X) depends on X. You also know from the F-test that you can test joint significance of a group of variables: does including these regressors significantly improve fit? White's test combines these two ideas into a single diagnostic: it asks whether the squared residuals — your proxy for the unobservable error variance — are systematically explained by the regressors in your model.

The mechanics of White's test follow a structured three-step procedure. First, run your original OLS regression and save the **residuals** ê. Second, construct a new regression where the dependent variable is ê² and the regressors are all the original X variables, all their squares (X₁², X₂², ...), and all their pairwise cross-products (X₁·X₂, X₁·X₃, ...). Third, test whether this auxiliary regression has any explanatory power, using the test statistic nR² from the auxiliary regression, which follows a chi-squared distribution under the null of homoskedasticity. The null hypothesis is that none of these terms explains variance in ê², meaning heteroskedasticity is absent.

The key advantage of White's test over simpler alternatives like Breusch-Pagan is its **generality**. Breusch-Pagan assumes that if heteroskedasticity exists, it is a linear function of X — a specific functional form. White's test is nonparametric in its approach: by including squares and interactions, it captures nonlinear and interactive patterns in error variance without assuming a particular structure. This is what "robust to specific forms of heteroskedasticity" means — you do not have to guess how variance depends on X; the test searches broadly.

The practical downside is a trade-off between power and parsimony. With many regressors, the auxiliary regression can include a very large number of terms (k regressors produce up to k + k + k(k−1)/2 auxiliary variables), consuming degrees of freedom and potentially generating spurious detections. An important caution: White's test can reject homoskedasticity even when the true problem is **model misspecification** rather than genuine heteroskedasticity — a misspecified functional form also produces systematic residual patterns. If White's test triggers, the appropriate diagnostic question is not just "should I use robust standard errors?" but also "is my model correctly specified in the first place?"
