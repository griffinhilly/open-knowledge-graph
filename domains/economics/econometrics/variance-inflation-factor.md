---
id: variance-inflation-factor
title: Variance Inflation Factor and Multicollinearity Diagnosis
domain: economics
course: econometrics
prerequisites:
- id: multicollinearity
  type: hard
- id: multiple-regression-model
  type: soft
builds-toward:
- generalized-least-squares
tags:
- multicollinearity
- diagnostics
- vif
stage: formal-systems
status: draft
---

# Variance Inflation Factor and Multicollinearity Diagnosis

## Core Idea
The Variance Inflation Factor (VIF) quantifies how much a coefficient's variance is inflated by multicollinearity: VIF = 1/(1 - Rⱼ²), where Rⱼ² comes from regressing regressor j on all others. VIF values above 5–10 typically indicate problematic multicollinearity requiring remediation.

## Explainer

From your study of multicollinearity, you know the problem: when two or more regressors are highly linearly related, OLS cannot cleanly attribute variation in Y to one variable versus the other. The estimates are still unbiased — OLS is not broken — but they become imprecise. Standard errors blow up, t-statistics shrink, and coefficients can appear statistically insignificant even when the variables genuinely matter. What you need is a way to measure how severe this imprecision is for each coefficient individually. That is exactly what the **Variance Inflation Factor** provides.

The logic behind the VIF formula is elegant. For regressor j, run a separate regression: regress Xⱼ on all the *other* regressors and record the R² from that auxiliary regression, calling it Rⱼ². This Rⱼ² measures how well the other regressors can predict Xⱼ — in other words, how redundant Xⱼ is given the rest of the model. The VIF is then 1/(1 − Rⱼ²). When Rⱼ² = 0 (Xⱼ is completely unrelated to the other regressors), VIF = 1: no inflation, the coefficient's variance is exactly what it would be in a simple regression. When Rⱼ² = 0.9 (90% of Xⱼ's variation is explained by the others), VIF = 10: the variance of β̂ⱼ is ten times larger than it would be without multicollinearity. The standard error is thus √10 ≈ 3.16 times wider, dramatically shrinking t-statistics.

The conventional thresholds — VIF > 5 causes concern, VIF > 10 indicates serious problems — are rules of thumb, not mathematical cutoffs. What they communicate is that once VIF exceeds these values, your coefficient estimates are so imprecise that meaningful inference is difficult. A VIF of 25 means the standard error is five times larger than it would be in an orthogonal design; you would need a sample roughly 25 times larger to achieve the same precision. Understanding this relationship makes the diagnosis concrete: a high VIF is not a mysterious pathology but a quantitative statement about how much statistical power you are losing.

Remedies depend on the source of multicollinearity. If two regressors measure nearly the same thing conceptually, you can drop one or combine them into an index. If multicollinearity arises from the functional form (including both X and X² creates high correlation), centering the variable before squaring often helps. If you must retain both variables because theory requires them, the practical implication is humility: wide confidence intervals are honest, and you should report them as such rather than over-interpreting coefficient magnitudes. VIF does not tell you what to do, but it gives you the quantitative basis for understanding why your estimates are uncertain and how much worse the problem would have to get before the model becomes uninformative.
