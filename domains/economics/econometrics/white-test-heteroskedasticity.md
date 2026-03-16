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
builds-toward:
- generalized-least-squares
tags:
- heteroskedasticity
- testing
- diagnostics
stage: formal-systems
status: draft
---

# White Test and Detection of Heteroskedasticity

## Core Idea
White's test detects heteroskedasticity by regressing squared residuals on all regressors and their interactions, testing whether these variables explain squared residuals. Unlike Breusch-Pagan, it is robust to specific forms of heteroskedasticity, making it practical for applied work when the source of heteroskedasticity is unknown.

## Explainer

You know from studying heteroskedasticity that the problem is non-constant error variance — Var(u|X) depends on X. You also know from the F-test that you can test joint significance of a group of variables: does including these regressors significantly improve fit? White's test combines these two ideas into a single diagnostic: it asks whether the squared residuals — your proxy for the unobservable error variance — are systematically explained by the regressors in your model.

The mechanics of White's test follow a structured three-step procedure. First, run your original OLS regression and save the **residuals** ê. Second, construct a new regression where the dependent variable is ê² and the regressors are all the original X variables, all their squares (X₁², X₂², ...), and all their pairwise cross-products (X₁·X₂, X₁·X₃, ...). Third, test whether this auxiliary regression has any explanatory power, using the test statistic nR² from the auxiliary regression, which follows a chi-squared distribution under the null of homoskedasticity. The null hypothesis is that none of these terms explains variance in ê², meaning heteroskedasticity is absent.

The key advantage of White's test over simpler alternatives like Breusch-Pagan is its **generality**. Breusch-Pagan assumes that if heteroskedasticity exists, it is a linear function of X — a specific functional form. White's test is nonparametric in its approach: by including squares and interactions, it captures nonlinear and interactive patterns in error variance without assuming a particular structure. This is what "robust to specific forms of heteroskedasticity" means — you do not have to guess how variance depends on X; the test searches broadly.

The practical downside is a trade-off between power and parsimony. With many regressors, the auxiliary regression can include a very large number of terms (k regressors produce up to k + k + k(k−1)/2 auxiliary variables), consuming degrees of freedom and potentially generating spurious detections. An important caution: White's test can reject homoskedasticity even when the true problem is **model misspecification** rather than genuine heteroskedasticity — a misspecified functional form also produces systematic residual patterns. If White's test triggers, the appropriate diagnostic question is not just "should I use robust standard errors?" but also "is my model correctly specified in the first place?"
