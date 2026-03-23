---
id: two-stage-least-squares-procedure
title: 'Two-Stage Least Squares: Procedure and Inference'
domain: economics
course: econometrics
prerequisites:
- id: two-stage-least-squares
  type: hard
- id: instrumental-variables-validity
  type: hard
- id: matrix-operations
  type: hard
- id: linear-regression-simple-theory
  type: soft
builds-toward:
- overidentification-test
tags:
- instrumental-variables
- two-stage
- estimation
stage: formal-systems
status: validated
---

# Two-Stage Least Squares: Procedure and Inference

## Core Idea
2SLS: Stage 1 regresses X on Z to obtain X̂; Stage 2 regresses Y on X̂. This yields consistent and asymptotically normal causal effect estimates under IV assumptions. Standard errors must account for first-stage estimation, typically using robust sandwich formulas.

## Questions

```yaml
- question: "A researcher manually runs Stage 1 of 2SLS, saves the predicted values X̂, then runs a separate OLS regression of Y on X̂. She reports the standard errors from this second regression. What is wrong with her inference?"
  type: multiple-choice
  options:
    - "Nothing is wrong — this is exactly what 2SLS instructs you to do"
    - "The coefficient estimate β̂₁ is biased because she did not use purpose-built software"
    - "The standard errors are too small because they ignore the sampling uncertainty from estimating Stage 1, making her confidence intervals too narrow and t-statistics too large"
    - "The standard errors are too large because she is using predicted values rather than actual values of X"
  answer: 2
  explanation: "The coefficient estimates from manual two-step regression match those from purpose-built 2SLS packages, but the standard errors are incorrect. Manual OLS in Stage 2 treats X̂ as if it were directly observed data — it ignores the fact that X̂ was itself estimated with sampling error in Stage 1. This underestimates the true variability of β̂₁, producing standard errors that are too small, t-statistics that are too large, and confidence intervals that are too narrow. All inference becomes overconfident. The correct fix is to use commands like Stata's ivregress or R's ivreg, which implement the corrected sandwich formula."

- question: "What does Stage 1 of the 2SLS procedure accomplish?"
  type: multiple-choice
  options:
    - "It tests whether the instrument Z satisfies the exclusion restriction"
    - "It removes the endogenous variation from X by retaining only the variation driven by the instrument Z"
    - "It estimates the reduced-form effect of Z on Y"
    - "It orthogonalizes the instrument Z with respect to the controls W"
  answer: 1
  explanation: "Stage 1 regresses X on Z (and any controls W) to get predicted values X̂. These predicted values capture only the variation in X that is driven by Z — and by the exclusion restriction, Z's effect on Y runs only through X, not directly. So X̂ strips out whatever correlation existed between X and the structural error term, retaining the 'clean' exogenous variation. This is why Stage 2 OLS on X̂ satisfies the exogeneity condition: not by assumption about the original data, but by construction. Option A describes a separate diagnostic test (the Sargan/Hansen test); option C is related but describes a different regression."

- question: "In 2SLS, the Stage 2 exogeneity condition is satisfied by construction, not because the original regressor X is uncorrelated with the error term."
  type: true-false
  answer: true
  explanation: "This is the core insight of 2SLS. X is endogenous — correlated with the error term u — which is why OLS fails. But X̂ (the Stage 1 predicted values) contains only Z-driven variation, and by the exclusion restriction, Z does not directly affect Y. Therefore X̂ is uncorrelated with u by construction. Stage 2 OLS on X̂ then satisfies OLS's exogeneity assumption not because of anything about the original data, but because of how X̂ was constructed."

- question: "If Stage 1 of 2SLS has a very high R², weak instrument problems are effectively eliminated."
  type: true-false
  answer: false
  explanation: "Weak instrument problems are determined by whether Z is a strong predictor of X — specifically by the F-statistic on Z in Stage 1, not by the overall R² of the Stage 1 regression. A high R² could result from other predictors (controls W) fitting X well, even if Z itself adds little explanatory power. The relevant diagnostic is the first-stage F-statistic on the excluded instruments: by convention, F < 10 suggests weak instruments. High overall R² from good controls can mask a weak first stage."

- question: "Why does Stage 1 of 2SLS 'clean' the endogenous regressor X, and what exactly is being removed?"
  type: short-answer
  answer: "Stage 1 regresses X on the instrument Z (and any controls). The predicted values X̂ represent the variation in X that is attributable to Z. Since the exclusion restriction requires Z to affect Y only through X, this Z-driven variation is exogenous — uncorrelated with the structural error term u. What is 'removed' is the remaining variation in X: the part correlated with u that made X endogenous in the first place. X̂ keeps the 'good' (exogenous) variation and discards the 'bad' (endogenous) variation."
  explanation: "This is what makes 2SLS work: it uses the instrument to surgically separate the endogenous variation in X (which would bias OLS) from the exogenous variation (which identifies the causal effect). If the instrument is weak, there is very little Z-driven variation to keep, and the resulting X̂ is a poor proxy for X, which is why weak instruments cause severe problems."
```

## Explainer

You already understand why instrumental variables are needed: when the regressor X is endogenous — correlated with the error term — OLS is biased and inconsistent, and no sample size will save you. You also know the validity requirements for an instrument Z: relevance (Z must predict X) and exclusion (Z must affect Y only through X, not directly). Two-stage least squares is the procedure that turns a valid instrument into a usable estimator, and understanding each stage mechanically helps you see what the method is actually doing.

**Stage 1** regresses the endogenous regressor X on the instrument Z (and any exogenous controls W already in the model): X = π₀ + π₁Z + γW + v. The predicted values X̂ from this regression are the "cleaned" version of X — they retain only the variation in X that is driven by Z, which by the exclusion restriction is variation uncorrelated with the structural error. Intuitively, you're keeping the good variation (the exogenous push from Z) and throwing away the bad variation (whatever correlation existed between X and the error term). If Z is weak — if π₁ ≈ 0 and the first stage R² is low — X̂ won't track X well, and all the problems of weak instruments emerge.

**Stage 2** regresses Y on X̂ (and the same controls W): Y = β₀ + β₁X̂ + γW + u. The coefficient β₁ is your 2SLS estimate of the causal effect. The logic is that X̂ is uncorrelated with u by construction (since it only contains Z-driven variation, and Z doesn't directly affect Y). So this second regression satisfies the OLS exogeneity condition — not because we assumed it, but because we engineered it. In this way, 2SLS is OLS applied to a purified regressor.

The critical warning about **standard errors** is easy to miss. If you naively run Stage 1 in one regression and Stage 2 in another, saving the predicted values manually and feeding them in, most software will compute standard errors as if X̂ were directly observed — ignoring the sampling uncertainty from Stage 1. This produces standard errors that are too small, making you overconfident. Any competent econometrics package (Stata's `ivregress 2sls`, R's `ivreg`, Python's `linearmodels`) implements the correct sandwich formula that accounts for first-stage estimation error. Always use these purpose-built commands, not manual two-step estimation, unless you're willing to calculate corrected standard errors yourself. This seemingly technical detail determines whether your inference is valid.

