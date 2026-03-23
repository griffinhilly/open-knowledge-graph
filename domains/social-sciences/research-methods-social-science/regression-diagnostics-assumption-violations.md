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
stage: expert
status: draft
---

# Regression Diagnostics: Checking Assumptions and Violations

## Core Idea
Ordinary least squares regression assumes linearity, homoscedasticity, independence, normality, and no multicollinearity. Real data often violate these. Diagnostic techniques—residual plots, tests, robust standard errors—detect violations and guide corrections.

## Questions

```yaml
- question: "A residual plot shows a clear fan shape — residuals spread out as fitted values increase. The most important consequence of ignoring this is:"
  type: multiple-choice
  options:
    - "The coefficient estimates will be biased toward zero"
    - "The model will underfit the data and miss real patterns"
    - "The standard errors, p-values, and confidence intervals will be unreliable, even though the coefficient estimates themselves may still be correct"
    - "The R² will be inflated, making the model appear stronger than it is"
  answer: 2
  explanation: "A fan shape signals heteroscedasticity — non-constant variance across fitted values. Under heteroscedasticity, OLS coefficient estimates remain unbiased (they still identify the conditional mean correctly), but the standard errors are wrong. This invalidates all inference: p-values may indicate significance where none exists, confidence intervals will be too narrow or wide, and hypothesis tests will have incorrect Type I error rates. The remedy is robust (sandwich) standard errors — not refitting the model — which is why recognizing that coefficients and standard errors are separable consequences is the key insight."

- question: "A researcher finds a variance inflation factor (VIF) of 15 for one predictor. The most appropriate interpretation is:"
  type: multiple-choice
  options:
    - "The predictor must be dropped immediately — VIF above 10 invalidates any model"
    - "Robust standard errors should be applied to address the inflated variance"
    - "This predictor's coefficient estimate is unstable due to high correlation with other predictors; standard errors are inflated and the model specification should be reconsidered"
    - "VIF measures collinearity but has no effect on OLS coefficient estimates or standard errors"
  answer: 2
  explanation: "High VIF means the predictor is highly collinear with other predictors, making it difficult for the model to disentangle their individual effects. This inflates standard errors (making coefficient estimates unstable — small data changes produce large estimate changes) and reduces interpretability. Option B is wrong because robust SE addresses heteroscedasticity, not multicollinearity. Option D is wrong because VIF does affect standard errors. Option A overstates the case — the appropriate response depends on whether prediction or interpretation is the goal."

- question: "If OLS regression assumptions are violated, the coefficient estimates are always biased."
  type: true-false
  answer: false
  explanation: "This overstates the consequences. Heteroscedasticity and autocorrelation, for example, leave coefficient estimates unbiased — OLS still correctly estimates the conditional mean — but they invalidate standard errors and inference. Only specific violations produce biased estimates: omitted variable bias (relevant predictor excluded), endogeneity (predictor correlated with the error), or measurement error in predictors. Knowing *which* assumption is violated and *what its specific consequences are* is exactly the point of regression diagnostics — a single blanket response ('my estimates are biased') is often incorrect."

- question: "A Q-Q plot of regression residuals is used to assess the normality assumption: points that deviate from the 45-degree reference line indicate non-normality."
  type: true-false
  answer: true
  explanation: "A Q-Q plot plots the quantiles of the observed residual distribution against the quantiles expected from a theoretical normal distribution. When residuals are normally distributed, the points fall approximately on the 45-degree line. Systematic deviations — S-curves (skewness), heavy tails, or gaps — indicate non-normality. For large samples, normality violations matter less (by the central limit theorem), but in small samples, non-normal residuals can distort p-values and confidence intervals substantially."

- question: "Why is it important to identify *which* OLS assumption has been violated before choosing a remedy, rather than applying a single catch-all fix?"
  type: short-answer
  answer: "Different assumption violations have different consequences and require different remedies. Heteroscedasticity leaves coefficients unbiased but invalidates standard errors — the remedy is robust (sandwich) standard errors, not model re-specification. Nonlinearity biases coefficient estimates — the remedy is transformations, polynomial terms, or interaction effects. Multicollinearity inflates standard errors without biasing estimates — robust SE doesn't help; reconsidering which variables to include might. Clustered observations require cluster-robust SE or multilevel models. Applying the wrong remedy can be harmful: using robust SE when the real problem is omitted variable bias leaves the bias in place while giving false confidence that inference is valid. The diagnostic step tells you what is wrong; understanding why guides the appropriate substantive fix."
  explanation: "Regression diagnostics connect technical checks to substantive modeling decisions. Violations often signal that the model is misspecified — missing a nonlinear relationship, ignoring clustering structure, or including highly redundant predictors. The remedy therefore depends on understanding the research context, not just applying a statistical correction formula."
```

## Explainer

From linear regression, you know that OLS minimizes the sum of squared residuals to find the best-fitting line. What "best" means depends critically on a set of assumptions built into the math. When those assumptions hold, OLS is **BLUE** — the Best Linear Unbiased Estimator. When they fail, your coefficient estimates may still be unbiased, but your standard errors — and therefore your p-values, confidence intervals, and hypothesis tests — may be completely wrong. Regression diagnostics are the practice of checking which assumptions hold and deciding what to do when they don't.

The five core assumptions are worth knowing as a checklist. **Linearity** means the relationship between X and Y is actually linear — violations show up as systematic curves in a residuals-vs-fitted plot. **Homoscedasticity** means the variance of residuals is constant across all values of X — violations (called **heteroscedasticity**) make residual plots fan out or funnel in. **Independence** means observations are not correlated with each other — violated by clustered data (students within schools), panel data (repeated measures), or spatial data. **Normality of residuals** is the least consequential assumption for large samples by the central limit theorem, but matters in small samples when you need accurate p-values. **No multicollinearity** means predictors aren't so highly correlated that the model can't distinguish their separate effects — diagnosed using the **variance inflation factor** (VIF); high VIF inflates standard errors.

The primary diagnostic tool is the **residual plot**: a scatterplot of residuals against fitted values (or against each predictor). Patterns in this plot are informative: a random cloud means the linearity and homoscedasticity assumptions look okay; a curve suggests a nonlinear relationship you've missed; a fan shape signals heteroscedasticity. A **Q-Q plot** of residuals against the normal distribution diagnoses normality — points deviating from the 45-degree line indicate non-normality. For influential observations, Cook's distance measures how much coefficient estimates would change if a particular point were removed; high-leverage points can disproportionately determine your results.

The good news is that violations don't always require starting over — they often have tractable remedies. Heteroscedasticity can be addressed with **robust standard errors** (also called sandwich estimators or HC standard errors), which give valid inference even when variance isn't constant, without changing coefficient estimates. Nonlinearity can be addressed by adding polynomial terms, log-transforming variables, or including interaction terms. Multicollinearity can sometimes be reduced by centering variables or reconsidering model specification. Clustered observations call for cluster-robust standard errors or multilevel models. The diagnostic step tells you what's wrong; it doesn't automatically tell you the fix, which depends on understanding *why* the violation is occurring in your data. That interpretive step connects back to your knowledge of measurement validity and research design — violations often signal substantive modeling problems, not just statistical technicalities.
