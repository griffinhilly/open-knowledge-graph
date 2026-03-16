---
id: endogeneity
title: Endogeneity
domain: economics
course: econometrics
prerequisites:
- id: omitted-variable-bias
  type: hard
- id: ols-assumptions
  type: hard
builds-toward:
- instrumental-variables
- panel-data-basics
tags:
- endogeneity
- simultaneity
- measurement-error
- bias
stage: formal-systems
status: validated
---

# Endogeneity

## Core Idea
Endogeneity is a general term for any situation where a regressor is correlated with the error term, making OLS biased and inconsistent. There are three main sources: omitted variable bias (a confound is excluded from the model), simultaneity (y and x are jointly determined, as when price and quantity are both endogenous in a supply-demand system), and measurement error (x is measured with noise, attenuating its coefficient toward zero via 'attenuation bias'). Endogeneity is the central identification problem in applied economics, and most advanced methods — instrumental variables, panel fixed effects, regression discontinuity, difference-in-differences — are designed to address specific forms of it.

## How It's Best Learned
Work through three separate examples, one for each source of endogeneity, and derive the direction of bias for each. The supply-demand simultaneity example is essential for macroeconomics applications.

## Common Misconceptions
- Endogeneity is not about the dependent variable being 'determined inside a model'; it specifically means Cov(xⱼ, u) ≠ 0.
- Measurement error in y does not cause endogeneity; only measurement error in x creates attenuation bias.

## Explainer

From your study of OLS assumptions, you know that the zero-conditional-mean assumption E(u|X) = 0 is what makes OLS unbiased. **Endogeneity** is the collective name for anything that violates this assumption — any situation where your regressor X is correlated with the error term u. When Cov(X, u) ≠ 0, OLS does not recover the true causal effect; instead it picks up a blend of the causal effect and the confounding relationship between X and u. The bias does not shrink with sample size — endogeneity is a consistency problem, not just a precision problem.

The three sources each have a distinct mechanism. You already understand the first from **omitted variable bias**: if a variable Z affects Y and is correlated with X but is left out of the model, Z ends up in the error term, making u correlated with X. The classic example is estimating the returns to education: ability affects wages and is correlated with education, so omitting ability inflates the estimated education coefficient. The direction of bias follows a simple formula: the product of the sign of (Z's effect on Y) and the sign of (Z's correlation with X). Second, **simultaneity** arises when X and Y jointly determine each other. Trying to estimate a demand curve using market data is the canonical case: both price and quantity are simultaneously set by the intersection of supply and demand, so price is correlated with the demand error. Running OLS on price and quantity gives neither a supply curve nor a demand curve — it gives a jumbled blend of both.

The third source, **measurement error in X**, is subtler but important. Suppose you're estimating the effect of true ability (X*) on wages, but you only observe test scores (X = X* + v) where v is random noise. The noise v ends up in the error term and is negatively correlated with the mismeasured X, because X absorbs part of v while the remaining v creates negative covariance with u. The result is **attenuation bias**: your estimated coefficient is biased toward zero — you understate the true relationship. The magnitude of attenuation equals the reliability ratio, the fraction of X's variance that is true signal rather than noise.

All the major tools of applied econometrics — instrumental variables, difference-in-differences, regression discontinuity, panel fixed effects — exist specifically to address one or more forms of endogeneity. Instrumental variables finds a variable Z that shifts X but has no direct effect on Y and no correlation with the error, allowing you to use only the exogenous variation in X for identification. Panel fixed effects remove time-invariant omitted variables by differencing out each unit's average. Understanding endogeneity is therefore not an isolated topic — it is the central diagnostic question behind every causal regression design. Before trusting any OLS estimate, ask: is there any reason my regressor might be correlated with the error? If yes, identify the source and select the appropriate remedy.
