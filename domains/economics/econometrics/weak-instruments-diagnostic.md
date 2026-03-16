---
id: weak-instruments-diagnostic
title: 'Weak Instruments: Diagnosis and Solutions'
domain: economics
course: econometrics
prerequisites:
- id: instrumental-variables
  type: hard
- id: two-stage-least-squares
  type: hard
tags:
- weak-instruments
- iv
- first-stage
stage: formal-systems
status: draft
---

# Weak Instruments: Diagnosis and Solutions

## Core Idea
Weak instruments have low correlation with the endogenous regressor in the first stage, leading to large standard errors and biased inference. The F-statistic on excluded instruments and Stock-Yogo critical values diagnose weakness.

## Explainer

You already understand why instrumental variables (IV) estimation is valuable: when a regressor is endogenous — correlated with the error term due to omitted variables, reverse causality, or measurement error — OLS is inconsistent. IV solves this by finding an instrument that is correlated with the endogenous regressor (relevance) but uncorrelated with the outcome except through that regressor (exclusion restriction). Two-stage least squares (2SLS) then uses the instrument to isolate exogenous variation. The catch you're now confronting: what happens when the instrument is only weakly correlated with the endogenous regressor? The answer is severe — and counterintuitive — problems.

The problem with **weak instruments** is that a tiny amount of violation of the exclusion restriction gets magnified dramatically. To see why, think about 2SLS intuitively: the first stage extracts the variation in the endogenous regressor that is explained by the instrument, and the second stage uses only that extracted variation. If the instrument barely moves the regressor (weak first stage), then almost all the variation in the second-stage "instrumented" regressor comes from noise, not clean exogenous signal. The 2SLS estimator is pulled toward the OLS estimator (and its bias) rather than correcting it. Standard confidence intervals are misleading — they don't cover the true parameter at their nominal rate, even in large samples.

Diagnosis centers on the **first-stage F-statistic** — the F-test of the joint significance of excluded instruments in the first-stage regression of the endogenous regressor on instruments and controls. The Stock-Yogo (2005) critical values give you the threshold for acceptable weakness. The standard rule of thumb is F > 10 for a single instrument, though this can be conservative; Stock-Yogo provide exact critical values for desired maximum relative bias (e.g., no more than 10% of OLS bias) and maximum size distortion of t-tests. With one instrument, F > 10 approximately ensures 2SLS bias is less than 10% of OLS bias. With multiple instruments, the relevant statistic is the **Cragg-Donald F-statistic** (or its heteroskedasticity-robust analogue, the Kleibergen-Paap statistic).

When instruments are weak, the remedies depend on context. If you have multiple weak instruments, combining them via 2SLS actually worsens the problem relative to using fewer — more instruments means more first-stage overfitting. Better alternatives include **LIML** (limited information maximum likelihood), which is median-unbiased under weak instruments and performs better than 2SLS in most simulations, and **Anderson-Rubin confidence sets**, which remain valid under weak instruments by inverting a test rather than relying on the first stage. The most honest response is sometimes to acknowledge that available instruments are too weak for reliable inference and that the research design requires stronger instruments — a better natural experiment, a more predictive policy assignment rule, or additional sources of exogenous variation.
