---
id: regression-diagnostics-assumption-violations
title: 'Regression Diagnostics: Checking Assumptions and Violations'
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: linear-regression-social-science
  type: hard
- id: validity-construct-internal-external
  type: soft
builds-toward:
- multilevel-hierarchical-modeling-nesting
- missing-data-mechanisms-imputation
tags:
- regression
- diagnostics
- assumptions
- robustness
stage: advanced
status: draft
---

# Regression Diagnostics: Checking Assumptions and Violations

## Core Idea
Ordinary least squares regression assumes linearity, homoscedasticity, independence, normality, and no multicollinearity. Real data often violate these. Diagnostic techniques—residual plots, tests, robust standard errors—detect violations and guide corrections.

## Explainer

From linear regression, you know that OLS minimizes the sum of squared residuals to find the best-fitting line. What "best" means depends critically on a set of assumptions built into the math. When those assumptions hold, OLS is **BLUE** — the Best Linear Unbiased Estimator. When they fail, your coefficient estimates may still be unbiased, but your standard errors — and therefore your p-values, confidence intervals, and hypothesis tests — may be completely wrong. Regression diagnostics are the practice of checking which assumptions hold and deciding what to do when they don't.

The five core assumptions are worth knowing as a checklist. **Linearity** means the relationship between X and Y is actually linear — violations show up as systematic curves in a residuals-vs-fitted plot. **Homoscedasticity** means the variance of residuals is constant across all values of X — violations (called **heteroscedasticity**) make residual plots fan out or funnel in. **Independence** means observations are not correlated with each other — violated by clustered data (students within schools), panel data (repeated measures), or spatial data. **Normality of residuals** is the least consequential assumption for large samples by the central limit theorem, but matters in small samples when you need accurate p-values. **No multicollinearity** means predictors aren't so highly correlated that the model can't distinguish their separate effects — diagnosed using the **variance inflation factor** (VIF); high VIF inflates standard errors.

The primary diagnostic tool is the **residual plot**: a scatterplot of residuals against fitted values (or against each predictor). Patterns in this plot are informative: a random cloud means the linearity and homoscedasticity assumptions look okay; a curve suggests a nonlinear relationship you've missed; a fan shape signals heteroscedasticity. A **Q-Q plot** of residuals against the normal distribution diagnoses normality — points deviating from the 45-degree line indicate non-normality. For influential observations, Cook's distance measures how much coefficient estimates would change if a particular point were removed; high-leverage points can disproportionately determine your results.

The good news is that violations don't always require starting over — they often have tractable remedies. Heteroscedasticity can be addressed with **robust standard errors** (also called sandwich estimators or HC standard errors), which give valid inference even when variance isn't constant, without changing coefficient estimates. Nonlinearity can be addressed by adding polynomial terms, log-transforming variables, or including interaction terms. Multicollinearity can sometimes be reduced by centering variables or reconsidering model specification. Clustered observations call for cluster-robust standard errors or multilevel models. The diagnostic step tells you what's wrong; it doesn't automatically tell you the fix, which depends on understanding *why* the violation is occurring in your data. That interpretive step connects back to your knowledge of measurement validity and research design — violations often signal substantive modeling problems, not just statistical technicalities.
