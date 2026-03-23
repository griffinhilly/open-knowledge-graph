---
id: reduced-form-equations
title: Reduced Form and First-Stage Equations
domain: economics
course: econometrics
prerequisites:
- id: two-stage-least-squares-procedure
  type: hard
builds-toward:
- overidentification-test
tags:
- instrumental-variables
- reduced-form
- first-stage
stage: formal-systems
status: validated
---

# Reduced Form and First-Stage Equations

## Core Idea
The first-stage equation (X regressed on Z) is the reduced form for X, showing how exogenous variation in Z translates to variation in the endogenous X. Weak first-stage (low R² or t-statistics) indicates weak instruments; guidance suggests F-statistic > 10 for instrument strength diagnostics.

## Questions

```yaml
- question: "A researcher uses an IV strategy where the first-stage F-statistic is 4.2. The IV estimate is large and statistically significant at p < 0.01. What is the most appropriate conclusion?"
  type: multiple-choice
  options:
    - "The results are reliable — statistical significance of the IV estimate confirms the instrument works"
    - "The large IV estimate itself validates the first stage, since a weak instrument would produce a near-zero estimate"
    - "The weak instrument undermines the IV estimate — even small violations of the exclusion restriction could be severely amplified"
    - "An F-statistic of 4.2 is borderline; the researcher should report it but the results are still trustworthy"
  answer: 2
  explanation: "A weak first stage (F < 10) is disqualifying regardless of the IV estimate's size or significance. With a weak instrument, IV estimates have severe finite-sample bias that can be worse than OLS, and the confidence intervals are unreliable. A large IV estimate with a weak instrument may simply reflect amplified noise or an exclusion restriction violation. Statistical significance of the IV estimate does not validate the instrument — it just means the noise is too small relative to the (possibly biased) signal. The F > 10 threshold exists precisely because finite-sample behavior is poor below it."

- question: "The Wald estimator in instrumental variables is the ratio of:"
  type: multiple-choice
  options:
    - "The OLS coefficient on X divided by the first-stage coefficient on Z"
    - "The reduced-form coefficient on Z divided by the first-stage coefficient on Z"
    - "The first-stage coefficient on Z divided by the reduced-form coefficient on Z"
    - "The IV residual variance divided by the OLS residual variance"
  answer: 1
  explanation: "The Wald estimator is: (coefficient of Z in the y-on-Z regression) / (coefficient of Z in the X-on-Z regression). The numerator is the reduced-form: how much does y change when Z changes by one unit? The denominator is the first-stage: how much does X change when Z changes by one unit? Dividing removes the Z-to-X scaling, leaving the causal effect of X on y. This ratio logic makes IV transparent: the instrument affects y only through X, so the y-response is just the X-response scaled by the effect of X on y."

- question: "A strong first-stage F-statistic (F > 10) is sufficient to validate an instrumental variables strategy."
  type: true-false
  answer: false
  explanation: "A strong first stage is necessary but not sufficient. The instrument must also satisfy the exclusion restriction: Z must affect y only through X, not through any direct channel. This is a theoretical requirement that cannot be tested when you have exactly one instrument and one endogenous variable. A strong F-statistic tells you the instrument is relevant (Z strongly predicts X), but it says nothing about validity (Z ↛ y except through X). Both conditions are required for consistent IV estimation."

- question: "When first-stage F is very small (near 1), IV estimates can actually be more biased than OLS estimates, even if the instrument is theoretically valid."
  type: true-false
  answer: true
  explanation: "With a weak instrument, the IV estimator has poor finite-sample properties: it can have enormous variance and bias that far exceeds OLS bias from the endogeneity it was meant to correct. Intuitively, a weak instrument barely shifts X, so the IV estimate amplifies both signal and noise. Even a tiny violation of the exclusion restriction (Z has a small direct effect on y) gets amplified into a large bias when the first-stage coefficient is small. This is why weak instruments represent a complete failure of IV, not just reduced precision."

- question: "Explain the logic of the Wald estimator: why does dividing the reduced-form coefficient by the first-stage coefficient recover the causal effect of X on y?"
  type: short-answer
  answer: "The instrument Z affects y only through X (by the exclusion restriction). The reduced-form coefficient measures the total effect of Z on y, which is: (effect of Z on X) × (effect of X on y). The first-stage coefficient measures the effect of Z on X. Dividing removes the Z-to-X scaling: (effect of Z on y) / (effect of Z on X) = (effect of Z on X × effect of X on y) / (effect of Z on X) = effect of X on y. This is the causal effect we want — the instrument acts as a natural experiment, and the Wald ratio scales the outcome shift by the treatment shift."
  explanation: "The Wald estimator makes IV intuitive: it asks 'how much did y change per unit change in X that was induced by Z?' The first stage tells you how much X was induced; the reduced form tells you how much y moved in response. Their ratio is the causal effect. This logic breaks down with a weak first stage — if Z barely moves X, any noise in the reduced form gets magnified enormously."
```

## Explainer

From your study of two-stage least squares (2SLS), you know the core idea: when X is endogenous (correlated with the error in the structural equation), you find an instrument Z that affects X but has no direct effect on y. The **first-stage equation** is the regression of X on Z (and any other controls): X = π₀ + π₁Z + controls + v. This is sometimes called the reduced form for X because it expresses the endogenous variable purely as a function of exogenous variables — no endogenous regressors appear on the right-hand side.

The **reduced form for y** is what you get by substituting the first-stage relationship all the way through: regress y directly on Z and controls, bypassing X entirely. The coefficient on Z in this regression captures the total effect of the instrument on the outcome, working through X. The ratio of the reduced-form coefficient on Z to the first-stage coefficient on Z gives you the IV estimate of the structural effect of X on y — this is precisely the Wald estimator, and it makes the logic of instrumental variables transparent. The instrument only matters to the outcome because it shifts X; the IV estimate recovers the causal effect of X by scaling the outcome shift by the X shift.

**Instrument strength** is not a minor technical detail — it determines whether your IV estimates are reliable at all. A weak instrument is one where Z barely shifts X, meaning the first-stage F-statistic is small. The commonly cited threshold is F > 10 (from Staiger and Stock, 1997). When instruments are weak, even small violations of the exclusion restriction get amplified in the IV estimate, and finite-sample bias can be severe — the IV estimate may actually be worse than OLS. You can always check instrument strength simply by running the first-stage regression and examining the F-statistic on the excluded instruments. A large first-stage F is necessary but not sufficient for valid IV: the instrument must also satisfy the exclusion restriction (Z ↛ y except through X), which is a theoretical judgment, not testable when you have exactly one instrument.

The distinction between first-stage and reduced-form equations also clarifies the overidentification test (the topic this builds toward). When you have more instruments than endogenous variables, you can test whether all instruments give the same IV estimate — if they don't, at least one instrument may be violating the exclusion restriction. The reduced-form equations for each instrument must all point to the same structural coefficient for the overidentifying restrictions to hold. Thinking systematically in terms of first-stage and reduced-form regressions gives you a coherent framework for designing, diagnosing, and stress-testing any instrumental variables strategy.
