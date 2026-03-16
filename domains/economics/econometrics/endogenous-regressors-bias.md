---
id: endogenous-regressors-bias
title: 'Endogenous Regressors: Bias and Consequences'
domain: economics
course: econometrics
prerequisites:
- id: endogeneity
  type: hard
- id: omitted-variable-bias
  type: hard
builds-toward:
- instrumental-variables-validity
tags:
- endogeneity
- causality
- bias
stage: formal-systems
status: draft
---

# Endogenous Regressors: Bias and Consequences

## Core Idea
Endogeneity—when E[Xⱼuᵢ] ≠ 0—causes OLS bias and inconsistency. Sources include omitted confounders, simultaneous causality, and measurement error in regressors. Even weak correlation between Xⱼ and u induces substantial bias; direction and magnitude depend on signs and magnitudes of correlations.

## Explainer

You already know from omitted variable bias that leaving out a relevant predictor contaminates OLS estimates. Endogeneity generalizes that problem: any time a regressor is correlated with the error term — for *any* reason — the OLS estimator attributes to that regressor variation that actually belongs elsewhere. The result is a coefficient that is not just imprecise but **systematically wrong**, biased even in large samples. This is the distinction from sampling variance: more data does not fix endogeneity, because the estimator is inconsistent — it converges to the wrong value.

The three main sources of endogeneity are worth treating separately. **Omitted confounders** are the case you know: variable Z affects both X and Y but is left out of the model, so its influence shows up in the residual u, which is then correlated with X. **Simultaneous causality** is different: X causes Y, but Y also causes X, so the regressor and the outcome are jointly determined. A classic example is police presence and crime — more crime leads to more police deployment, but more police may reduce crime. Regressing crime on police gives a coefficient contaminated by both causal arrows. **Measurement error** in the regressor is the third source: if we observe X* = X + ε instead of the true X, the classical errors-in-variables problem creates a downward bias in the coefficient magnitude (attenuation bias), because the measured X is partially just noise.

The direction of bias follows from a simple formula. For a bivariate regression, the bias in the OLS coefficient is approximately Cov(Xⱼ, u) / Var(Xⱼ). If the omitted variable is positively correlated with both X and Y, OLS overstates the effect of X. If it is positively correlated with X but negatively correlated with Y, OLS understates (or reverses) the effect. Working through the sign of the bias is a practical skill: in a wage regression omitting ability, if more-able workers are hired more (positive Cov(education, ability)) and ability raises wages (positive direct effect), the omitted variable biases the education coefficient upward. This directional reasoning lets you anticipate which way your estimates are off, even before finding a fix.

The deeper lesson is that endogeneity is a **violation of the identification assumption**, not merely a nuisance. OLS estimates a causal effect only when the regression design isolates exogenous variation in X — variation that is not driven by other determinants of Y. When endogeneity is present, the variation in X is contaminated by feedback from Y, confounders, or measurement noise, and the coefficient estimate no longer has a causal interpretation. This motivates the instrumental variables framework you will study next: find a variable that shifts X but affects Y only through X, thereby isolating the clean, exogenous variation needed for causal inference.
