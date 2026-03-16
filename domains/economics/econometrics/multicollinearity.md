---
id: multicollinearity
title: Multicollinearity
domain: economics
course: econometrics
prerequisites:
- id: multiple-regression-model
  type: hard
- id: correlation-coefficient
  type: hard
- id: matrices-intro
  type: soft
- id: r-squared-and-model-fit
  type: soft
builds-toward:
- robust-standard-errors
tags:
- multicollinearity
- variance-inflation
- VIF
- identification
stage: formal-systems
status: validated
---
# Multicollinearity

## Core Idea
Multicollinearity arises when two or more regressors are highly (but not perfectly) correlated, making it difficult for OLS to separately identify their individual effects. It inflates standard errors, widens confidence intervals, and makes individual t-tests unreliable — but it does not bias the coefficient estimates. Variance Inflation Factors (VIFs) quantify how much each regressor's standard error is inflated relative to the case of no correlation. Perfect multicollinearity (e.g., including both a variable and its exact linear combination) makes (X'X) singular and OLS undefined.

## Common Misconceptions
- Multicollinearity is a data problem, not a model misspecification — it does not violate any Gauss-Markov assumption.
- Dropping a correlated variable 'fixes' multicollinearity but may introduce omitted variable bias.

## Explainer

Suppose you are regressing a worker's wage on both years of education and a cognitive test score. These two variables are positively correlated — people with more education tend to score higher. Now imagine you ask OLS to tell you: "How much does an extra year of education raise wages, holding the test score fixed?" The model must find observations where education increases but test scores do not change — comparisons that may be rare in the data because the two variables tend to move together. When the variables are highly correlated, OLS struggles to separately attribute wage variation to education versus the test score. This is the essence of **multicollinearity**: not a model error, but a data problem — the information needed to cleanly identify separate effects is thin.

The consequence shows up in the **standard errors**, not in the estimates themselves. OLS coefficient estimates remain unbiased and consistent even under severe multicollinearity — the Gauss-Markov conditions are not violated, so OLS is still BLUE. But the estimates become imprecise. Intuitively, when the model cannot distinguish education's effect from the test score's effect, it produces wide confidence intervals around both. You'll see large standard errors, high p-values that fail to reject H₀ for individual coefficients, and wide confidence intervals — even though R² and the overall F-statistic may remain high. This pattern is a diagnostic fingerprint: statistically insignificant individual coefficients paired with a significant overall F-test often indicates multicollinearity.

The **Variance Inflation Factor (VIF)** quantifies this precisely. For each regressor, VIF measures how much its variance (squared standard error) is inflated relative to what it would be if that regressor were uncorrelated with all others. A VIF of 1 means no inflation; a VIF of 10 means the standard error is √10 ≈ 3.16 times larger than it would be in an ideal orthogonal design. The formula is VIF_j = 1 / (1 - R²_j), where R²_j is the R-squared from regressing variable j on all other regressors. High R²_j means variable j is nearly a linear combination of the others — exactly the problem.

The response to multicollinearity requires care. The naive fix — dropping one of the correlated variables — does reduce standard errors, but at the cost of omitted variable bias if the dropped variable actually belongs in the model. The cleaner solutions are: collect more data (larger samples improve precision even when correlation persists), use ridge regression or other shrinkage methods that trade some bias for variance reduction, or reconsider whether the model is asking for a finer distinction than the data can support. Sometimes multicollinearity is telling you that two theoretical constructs are operationally inseparable in your dataset — a substantive finding, not just a statistical nuisance.
