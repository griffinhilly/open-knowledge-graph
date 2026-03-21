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

## Questions

```yaml
- question: "An economist collects data on prices and quantities from competitive markets and runs OLS to estimate a demand curve. Why will this procedure produce a biased estimate?"
  type: multiple-choice
  options:
    - "Price and quantity are simultaneously determined by both supply and demand, so market price is correlated with the demand equation's error term"
    - "The sample of market observations is too small for OLS to be reliable in competitive markets"
    - "Quantity demanded is always measured with classical error in market data, attenuating the coefficient"
    - "The true demand relationship is nonlinear, making OLS the wrong estimator regardless of endogeneity"
  answer: 0
  explanation: "This is the simultaneity problem: in any market, price and quantity are jointly determined by the intersection of supply and demand. The price you observe is not set exogenously — it reflects both supply and demand conditions simultaneously. When demand shifts (a shock in the error term), price changes too, creating Cov(price, demand error) ≠ 0. OLS therefore recovers neither the demand curve nor the supply curve — it traces out a cloud of equilibrium points driven by shocks to both equations. The only solution is an instrument that shifts one curve while leaving the other unchanged."

- question: "A researcher estimates the effect of true worker productivity on wages, but productivity is measured by noisy supervisor ratings (X = X* + v, where v is random noise). Compared to the true effect, the OLS estimate will be:"
  type: multiple-choice
  options:
    - "Biased toward zero — the noise in X attenuates the estimated coefficient below the true value"
    - "Biased upward — random noise in X inflates the apparent relationship with Y"
    - "Unbiased — random noise in X averages to zero in large samples, leaving the estimate consistent"
    - "Biased toward zero, but only if the noise v is correlated with true productivity X*"
  answer: 0
  explanation: "Attenuation bias is the systematic result of classical measurement error in a regressor. The noise v ends up in the error term and creates negative covariance between the mismeasured X and the error, violating the OLS zero-conditional-mean assumption. The estimated coefficient shrinks toward zero — specifically, it equals the true coefficient multiplied by the reliability ratio (the fraction of X's variance that is true signal). This does not average away in larger samples; it is a consistency failure. Option C is wrong precisely because the endogeneity makes OLS inconsistent. Option D is wrong because attenuation occurs even when v is independent of X*."

- question: "Endogeneity is a consistency problem in OLS — the bias does not shrink as the sample size grows to infinity."
  type: true-false
  answer: true
  explanation: "This is what distinguishes endogeneity from mere imprecision. If OLS is inconsistent (as it is when Cov(X, u) ≠ 0), the estimator converges to the wrong value as n → ∞. More data does not help — it just makes you more precisely wrong. This is why endogeneity is treated as a fundamental identification problem requiring a different estimator (IV, fixed effects, RD, DiD), not as a sample-size problem that can be solved by collecting more observations."

- question: "Measurement error in the dependent variable Y causes attenuation bias in OLS estimates, just as measurement error in a regressor X does."
  type: true-false
  answer: false
  explanation: "This is a critical distinction stated in the common misconceptions. Classical measurement error in Y (the dependent variable) simply adds noise to the outcome: it inflates the error term's variance and reduces precision, but it does not create correlation between the regressors and the error. OLS remains unbiased and consistent. Only measurement error in a regressor X violates the OLS assumption E(u|X) = 0, because the noise from X ends up in the error term and is necessarily correlated with the mismeasured X. The asymmetry — error in Y is harmless, error in X is not — surprises many students."

- question: "Explain, using the concept of correlation with the error term, why omitting a relevant variable causes endogeneity — and how you can predict the direction of the resulting bias."
  type: short-answer
  answer: "When a relevant variable Z is omitted from a regression, it becomes part of the error term u. If Z is also correlated with an included regressor X, then X and u are correlated — violating E(u|X) = 0 and causing endogeneity. OLS cannot distinguish the effect of X from the effect of Z, so it attributes to X some of the variation in Y that actually comes from Z. The direction of bias follows a simple rule: bias = (Z's effect on Y) × (correlation of Z with X). If Z raises Y and is positively correlated with X, the bias is upward (X's coefficient is overstated). If Z raises Y but is negatively correlated with X, the bias is downward. This formula lets researchers predict which direction OLS will be wrong before collecting data."
  explanation: "The omitted variable bias formula — sign(bias) = sign(β_Z) × sign(Corr(Z, X)) — is one of the most useful tools in applied econometrics. It transforms endogeneity from an abstract concern into a concrete, directional prediction. In the education-wages example: ability raises wages (positive β) and is positively correlated with education, so the education coefficient is biased upward. This prediction can be tested against IV estimates and can guide the choice of instruments."
```

## Explainer

From your study of OLS assumptions, you know that the zero-conditional-mean assumption E(u|X) = 0 is what makes OLS unbiased. **Endogeneity** is the collective name for anything that violates this assumption — any situation where your regressor X is correlated with the error term u. When Cov(X, u) ≠ 0, OLS does not recover the true causal effect; instead it picks up a blend of the causal effect and the confounding relationship between X and u. The bias does not shrink with sample size — endogeneity is a consistency problem, not just a precision problem.

The three sources each have a distinct mechanism. You already understand the first from **omitted variable bias**: if a variable Z affects Y and is correlated with X but is left out of the model, Z ends up in the error term, making u correlated with X. The classic example is estimating the returns to education: ability affects wages and is correlated with education, so omitting ability inflates the estimated education coefficient. The direction of bias follows a simple formula: the product of the sign of (Z's effect on Y) and the sign of (Z's correlation with X). Second, **simultaneity** arises when X and Y jointly determine each other. Trying to estimate a demand curve using market data is the canonical case: both price and quantity are simultaneously set by the intersection of supply and demand, so price is correlated with the demand error. Running OLS on price and quantity gives neither a supply curve nor a demand curve — it gives a jumbled blend of both.

The third source, **measurement error in X**, is subtler but important. Suppose you're estimating the effect of true ability (X*) on wages, but you only observe test scores (X = X* + v) where v is random noise. The noise v ends up in the error term and is negatively correlated with the mismeasured X, because X absorbs part of v while the remaining v creates negative covariance with u. The result is **attenuation bias**: your estimated coefficient is biased toward zero — you understate the true relationship. The magnitude of attenuation equals the reliability ratio, the fraction of X's variance that is true signal rather than noise.

All the major tools of applied econometrics — instrumental variables, difference-in-differences, regression discontinuity, panel fixed effects — exist specifically to address one or more forms of endogeneity. Instrumental variables finds a variable Z that shifts X but has no direct effect on Y and no correlation with the error, allowing you to use only the exogenous variation in X for identification. Panel fixed effects remove time-invariant omitted variables by differencing out each unit's average. Understanding endogeneity is therefore not an isolated topic — it is the central diagnostic question behind every causal regression design. Before trusting any OLS estimate, ask: is there any reason my regressor might be correlated with the error? If yes, identify the source and select the appropriate remedy.
