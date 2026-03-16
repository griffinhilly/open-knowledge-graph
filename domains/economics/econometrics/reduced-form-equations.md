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
status: draft
---

# Reduced Form and First-Stage Equations

## Core Idea
The first-stage equation (X regressed on Z) is the reduced form for X, showing how exogenous variation in Z translates to variation in the endogenous X. Weak first-stage (low R² or t-statistics) indicates weak instruments; guidance suggests F-statistic > 10 for instrument strength diagnostics.

## Explainer

From your study of two-stage least squares (2SLS), you know the core idea: when X is endogenous (correlated with the error in the structural equation), you find an instrument Z that affects X but has no direct effect on y. The **first-stage equation** is the regression of X on Z (and any other controls): X = π₀ + π₁Z + controls + v. This is sometimes called the reduced form for X because it expresses the endogenous variable purely as a function of exogenous variables — no endogenous regressors appear on the right-hand side.

The **reduced form for y** is what you get by substituting the first-stage relationship all the way through: regress y directly on Z and controls, bypassing X entirely. The coefficient on Z in this regression captures the total effect of the instrument on the outcome, working through X. The ratio of the reduced-form coefficient on Z to the first-stage coefficient on Z gives you the IV estimate of the structural effect of X on y — this is precisely the Wald estimator, and it makes the logic of instrumental variables transparent. The instrument only matters to the outcome because it shifts X; the IV estimate recovers the causal effect of X by scaling the outcome shift by the X shift.

**Instrument strength** is not a minor technical detail — it determines whether your IV estimates are reliable at all. A weak instrument is one where Z barely shifts X, meaning the first-stage F-statistic is small. The commonly cited threshold is F > 10 (from Staiger and Stock, 1997). When instruments are weak, even small violations of the exclusion restriction get amplified in the IV estimate, and finite-sample bias can be severe — the IV estimate may actually be worse than OLS. You can always check instrument strength simply by running the first-stage regression and examining the F-statistic on the excluded instruments. A large first-stage F is necessary but not sufficient for valid IV: the instrument must also satisfy the exclusion restriction (Z ↛ y except through X), which is a theoretical judgment, not testable when you have exactly one instrument.

The distinction between first-stage and reduced-form equations also clarifies the overidentification test (the topic this builds toward). When you have more instruments than endogenous variables, you can test whether all instruments give the same IV estimate — if they don't, at least one instrument may be violating the exclusion restriction. The reduced-form equations for each instrument must all point to the same structural coefficient for the overidentifying restrictions to hold. Thinking systematically in terms of first-stage and reduced-form regressions gives you a coherent framework for designing, diagnosing, and stress-testing any instrumental variables strategy.
