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

## Questions

```yaml
- question: "A researcher regresses crime rates on police deployment across cities and finds a positive coefficient — more police, more crime. The most likely explanation is:"
  type: multiple-choice
  options:
    - "Measurement error in the crime rate variable attenuates the true negative coefficient"
    - "Simultaneous causality: high-crime cities deploy more police, so police deployment is correlated with the error term"
    - "The model is correctly specified; police presence genuinely increases crime"
    - "Omitting income as a control variable causes the police coefficient to flip sign"
  answer: 1
  explanation: "This is a classic simultaneous causality problem. Crime causes police deployment (cities respond to crime), while police may also affect crime — both causal arrows run simultaneously. OLS cannot distinguish them and produces a biased estimate. The positive coefficient likely reflects the reverse causation (high crime → more police) dominating the estimate, not evidence that police cause crime. More data won't fix this; the regressor is endogenous by design."

- question: "What distinguishes endogeneity bias from ordinary sampling variance?"
  type: multiple-choice
  options:
    - "Endogeneity bias affects only small samples; it disappears with larger datasets"
    - "Endogeneity produces wider confidence intervals but an unbiased point estimate"
    - "Endogeneity makes OLS inconsistent — the estimator converges to the wrong value even with unlimited data"
    - "Endogeneity bias is larger in magnitude but still correctable through heteroskedasticity-robust standard errors"
  answer: 2
  explanation: "This is the key distinction. Sampling variance shrinks as n grows — more data averages out random noise. Endogeneity causes inconsistency: the OLS estimator converges to a value that is systematically wrong (not the true causal coefficient), because Cov(X, u) ≠ 0 is a structural feature of the model, not a sampling accident. Collecting more data makes you more confidently wrong. This is why endogeneity requires a fix at the design level — instrumental variables, randomization, or natural experiments — not just a larger sample."

- question: "In a wage regression that omits individual ability, the OLS coefficient on education will be biased upward because ability is positively correlated with both education and wages."
  type: true-false
  answer: true
  explanation: "The direction-of-bias formula confirms this: the omitted variable bias is approximately Cov(education, ability) / Var(education) × (effect of ability on wages). Both terms are positive — more-able workers tend to get more education, and ability directly raises wages — so the bias is positive. OLS attributes to education some of the wage premium that actually belongs to ability, inflating the education coefficient."

- question: "Classical measurement error in the dependent variable Y (rather than in a regressor X) causes endogeneity bias in the OLS coefficient estimates."
  type: true-false
  answer: false
  explanation: "Measurement error in Y adds noise to the error term but does not correlate with the regressors X (under classical assumptions), so OLS remains unbiased — just less precise. Endogeneity bias arises from measurement error in a REGRESSOR X, not in Y. When the measured X* = X + ε, the true X and the measurement error ε both enter the model, making the observed regressor correlated with the error term. This causes attenuation bias — coefficients are biased toward zero."

- question: "Why does endogeneity make OLS inconsistent rather than merely imprecise, and why does this distinction matter practically?"
  type: short-answer
  answer: "Inconsistency means the estimator does not converge to the true parameter as sample size grows — it converges to a wrong value. This happens because Cov(X, u) ≠ 0 is a systematic feature: OLS attributes variation in Y to X even when that variation actually comes from the correlated error. More data amplifies the false signal rather than averaging it away. Practically, this means you cannot fix endogeneity by gathering more observations; you must address the source of correlation — through instrumental variables that isolate exogenous variation in X, through randomization that breaks the X-u correlation, or through a research design that eliminates the confounding path."
  explanation: "The contrast with imprecision is crucial for research strategy. An imprecise estimate is still correct on average — you need more data to narrow the confidence interval. An inconsistent estimate is wrong on average, and gathering more data only makes you more confident in the wrong answer. This motivates the entire instrumental variables literature: find a variable that moves X but is uncorrelated with u, so it extracts only the clean, exogenous variation in X that OLS cannot isolate on its own."
```

## Explainer

You already know from omitted variable bias that leaving out a relevant predictor contaminates OLS estimates. Endogeneity generalizes that problem: any time a regressor is correlated with the error term — for *any* reason — the OLS estimator attributes to that regressor variation that actually belongs elsewhere. The result is a coefficient that is not just imprecise but **systematically wrong**, biased even in large samples. This is the distinction from sampling variance: more data does not fix endogeneity, because the estimator is inconsistent — it converges to the wrong value.

The three main sources of endogeneity are worth treating separately. **Omitted confounders** are the case you know: variable Z affects both X and Y but is left out of the model, so its influence shows up in the residual u, which is then correlated with X. **Simultaneous causality** is different: X causes Y, but Y also causes X, so the regressor and the outcome are jointly determined. A classic example is police presence and crime — more crime leads to more police deployment, but more police may reduce crime. Regressing crime on police gives a coefficient contaminated by both causal arrows. **Measurement error** in the regressor is the third source: if we observe X* = X + ε instead of the true X, the classical errors-in-variables problem creates a downward bias in the coefficient magnitude (attenuation bias), because the measured X is partially just noise.

The direction of bias follows from a simple formula. For a bivariate regression, the bias in the OLS coefficient is approximately Cov(Xⱼ, u) / Var(Xⱼ). If the omitted variable is positively correlated with both X and Y, OLS overstates the effect of X. If it is positively correlated with X but negatively correlated with Y, OLS understates (or reverses) the effect. Working through the sign of the bias is a practical skill: in a wage regression omitting ability, if more-able workers are hired more (positive Cov(education, ability)) and ability raises wages (positive direct effect), the omitted variable biases the education coefficient upward. This directional reasoning lets you anticipate which way your estimates are off, even before finding a fix.

The deeper lesson is that endogeneity is a **violation of the identification assumption**, not merely a nuisance. OLS estimates a causal effect only when the regression design isolates exogenous variation in X — variation that is not driven by other determinants of Y. When endogeneity is present, the variation in X is contaminated by feedback from Y, confounders, or measurement noise, and the coefficient estimate no longer has a causal interpretation. This motivates the instrumental variables framework you will study next: find a variable that shifts X but affects Y only through X, thereby isolating the clean, exogenous variation needed for causal inference.
