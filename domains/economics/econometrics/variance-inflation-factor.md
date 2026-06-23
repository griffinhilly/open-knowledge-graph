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
tags:
- multicollinearity
- diagnostics
- vif
stage: formal-systems
status: validated
---

# Variance Inflation Factor and Multicollinearity Diagnosis

## Core Idea
The Variance Inflation Factor (VIF) quantifies how much a coefficient's variance is inflated by multicollinearity: VIF = 1/(1 - Rⱼ²), where Rⱼ² comes from regressing regressor j on all others. VIF values above 5–10 typically indicate problematic multicollinearity requiring remediation.

## Questions

```yaml
- question: "You run a regression and find VIF = 25 for the coefficient on X₃. What does this concretely mean for your estimates?"
  type: multiple-choice
  options:
    - "The coefficient on X₃ is biased upward by a factor of 25"
    - "The variance of β̂₃ is 25 times larger than it would be if X₃ were uncorrelated with the other regressors, making the standard error 5 times wider"
    - "X₃ explains 25% of the variation in Y, which exceeds acceptable limits"
    - "The OLS estimator has broken down and estimates are no longer consistent"
  answer: 1
  explanation: "VIF = 1/(1 - Rⱼ²) measures the multiplicative inflation in variance: a VIF of 25 means Var(β̂₃) is 25× what it would be in an orthogonal design. Standard errors are √25 = 5× wider, which dramatically shrinks t-statistics. Critically, OLS estimates remain unbiased (option A is wrong) and consistent (option D is wrong) — multicollinearity inflates variance without introducing bias. Option C misreads what VIF measures: Rⱼ² here is from an auxiliary regression of X₃ on the other regressors, not X₃ on Y."

- question: "A researcher includes both height_cm and height_inches in a regression predicting weight. Both variables have VIF > 1,000. What does the VIF indicate she should do?"
  type: multiple-choice
  options:
    - "Drop both variables — VIF above 10 means the variables are irrelevant"
    - "VIF diagnoses the severity of the problem but does not prescribe the fix; subject-matter reasoning determines whether to drop one, combine them, or accept wide standard errors"
    - "Use GLS instead of OLS to eliminate the multicollinearity"
    - "Increase the sample size until VIF falls below 10"
  answer: 1
  explanation: "VIF is a diagnostic, not a decision rule. It tells you how much variance inflation you have but not which variable to drop or how to fix the problem. In this case, height_cm and height_inches are perfect linear functions of each other — one should be dropped on conceptual grounds. But VIF alone doesn't tell you which. In other settings (X and X²), centering helps; in others, combining variables makes sense; in others still, you accept the imprecision because theory requires both. VIF quantifies the cost; the remedy requires judgment."

- question: "A high VIF on a coefficient indicates that the OLS estimate is imprecise but not necessarily biased."
  type: true-false
  answer: true
  explanation: "This is the crucial distinction: multicollinearity inflates the *variance* of OLS estimates without affecting their *expected value*. The Gauss-Markov theorem still applies — OLS remains BLUE (Best Linear Unbiased Estimator) under multicollinearity. What changes is the 'best' part: the minimum achievable variance is now very large because the data cannot cleanly separate the effects of collinear regressors. The estimates are centered on the truth but are spread widely around it."

- question: "If two regressors have VIF > 10, their OLS coefficient estimates are biased."
  type: true-false
  answer: false
  explanation: "Multicollinearity does not bias OLS estimates — it inflates their variance. Bias arises from omitted variables, measurement error, or endogeneity, not from correlation among included regressors. A common misconception is that high VIF 'breaks' OLS or introduces bias; the reality is that OLS still produces unbiased estimates, but with very large standard errors, making hypothesis tests unreliable and confidence intervals very wide. VIF above 10 means the estimates are imprecise, not wrong in expectation."

- question: "VIF = 1/(1 - Rⱼ²). Explain what the auxiliary regression's Rⱼ² measures and why a high value inflates the variance of β̂ⱼ."
  type: short-answer
  answer: "The auxiliary regression regresses Xⱼ on all other regressors and records the R². This R² measures how much of Xⱼ's variation is already explained by the other regressors — in other words, how redundant Xⱼ is. When Rⱼ² is high (close to 1), the data contain very little independent variation in Xⱼ that isn't already captured by the other variables. OLS estimates coefficients by comparing how Y moves when Xⱼ changes while holding the others constant, but if Xⱼ rarely moves independently of the others, there are very few such comparisons available. The coefficient estimate becomes sensitive to small perturbations in the data, resulting in a large variance."
  explanation: "The formula 1/(1 - Rⱼ²) quantifies this directly: Rⱼ² = 0.9 means only 10% of Xⱼ's variation is 'independent,' so the variance is inflated tenfold. This connects VIF to the intuitive problem: with correlated regressors, the regression cannot determine how much of Y's movement to attribute to Xⱼ versus the others — it's like trying to measure the separate effects of temperature and humidity when they always move together."
```

## Explainer

From your study of multicollinearity, you know the problem: when two or more regressors are highly linearly related, OLS cannot cleanly attribute variation in Y to one variable versus the other. The estimates are still unbiased — OLS is not broken — but they become imprecise. Standard errors blow up, t-statistics shrink, and coefficients can appear statistically insignificant even when the variables genuinely matter. What you need is a way to measure how severe this imprecision is for each coefficient individually. That is exactly what the **Variance Inflation Factor** provides.

The logic behind the VIF formula is elegant. For regressor j, run a separate regression: regress Xⱼ on all the *other* regressors and record the R² from that auxiliary regression, calling it Rⱼ². This Rⱼ² measures how well the other regressors can predict Xⱼ — in other words, how redundant Xⱼ is given the rest of the model. The VIF is then 1/(1 − Rⱼ²). When Rⱼ² = 0 (Xⱼ is completely unrelated to the other regressors), VIF = 1: no inflation, the coefficient's variance is exactly what it would be in a simple regression. When Rⱼ² = 0.9 (90% of Xⱼ's variation is explained by the others), VIF = 10: the variance of β̂ⱼ is ten times larger than it would be without multicollinearity. The standard error is thus √10 ≈ 3.16 times wider, dramatically shrinking t-statistics.

The conventional thresholds — VIF > 5 causes concern, VIF > 10 indicates serious problems — are rules of thumb, not mathematical cutoffs. What they communicate is that once VIF exceeds these values, your coefficient estimates are so imprecise that meaningful inference is difficult. A VIF of 25 means the standard error is five times larger than it would be in an orthogonal design; you would need a sample roughly 25 times larger to achieve the same precision. Understanding this relationship makes the diagnosis concrete: a high VIF is not a mysterious pathology but a quantitative statement about how much statistical power you are losing.

Remedies depend on the source of multicollinearity. If two regressors measure nearly the same thing conceptually, you can drop one or combine them into an index. If multicollinearity arises from the functional form (including both X and X² creates high correlation), centering the variable before squaring often helps. If you must retain both variables because theory requires them, the practical implication is humility: wide confidence intervals are honest, and you should report them as such rather than over-interpreting coefficient magnitudes. VIF does not tell you what to do, but it gives you the quantitative basis for understanding why your estimates are uncertain and how much worse the problem would have to get before the model becomes uninformative.
