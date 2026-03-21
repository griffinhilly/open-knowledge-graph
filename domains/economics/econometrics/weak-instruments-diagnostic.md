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

## Questions

```yaml
- question: "A researcher has an endogenous regressor and two instruments. The first-stage F-statistic is 4.2. What is the most appropriate response?"
  type: multiple-choice
  options:
    - "Proceed with 2SLS — two instruments are stronger than one"
    - "Switch to OLS, since weak instruments make IV invalid anyway"
    - "Report 2SLS results with a warning about weak instruments"
    - "Use LIML or Anderson-Rubin inference, which remain valid under weak instruments"
  answer: 3
  explanation: "F = 4.2 is well below the Stock-Yogo rule of thumb (F > 10 for approximately 10% relative bias). Standard 2SLS is problematic because the estimator is pulled toward OLS bias. Adding more instruments (option A) actually worsens first-stage overfitting. Switching to OLS (option B) abandons endogeneity correction entirely. LIML is median-unbiased under weak instruments and outperforms 2SLS in most simulations; Anderson-Rubin confidence sets remain valid by inverting a test rather than relying on the first stage."

- question: "Why does adding more weak instruments to a 2SLS regression typically worsen bias rather than helping?"
  type: multiple-choice
  options:
    - "More instruments reduce the degrees of freedom available for the second stage"
    - "More excluded instruments overfit the first stage, increasing the share of noise in the instrumented regressor"
    - "The exclusion restriction becomes harder to satisfy with more instruments"
    - "More instruments raise the Cragg-Donald F-statistic above the Stock-Yogo threshold, falsely clearing the diagnostic"
  answer: 1
  explanation: "The first stage regresses the endogenous variable on the instruments and controls. With many weak instruments, the first stage is highly overfit: predicted values are driven by noise rather than genuine signal. The second stage then uses this noisy, overfitted prediction — a regressor that is mostly measurement error — which biases 2SLS toward OLS. The Cragg-Donald F-statistic actually tends to fall with many weak instruments, flagging the problem rather than hiding it."

- question: "A high first-stage F-statistic (e.g., F > 50) guarantees that 2SLS estimates are unbiased."
  type: true-false
  answer: false
  explanation: "A high F-statistic indicates a strong instrument (high relevance), but relevance is only one of two IV requirements. The exclusion restriction — that the instrument affects the outcome only through the endogenous regressor — is not tested by the F-statistic and cannot be tested from the data alone when the model is exactly identified. A strong instrument that violates the exclusion restriction produces precise but biased estimates. The F-statistic addresses weak-instruments bias specifically, not exclusion restriction violations."

- question: "Under weak instruments, 2SLS estimates tend to be biased toward the OLS estimate rather than toward zero."
  type: true-false
  answer: true
  explanation: "Correct. The purpose of 2SLS is to isolate exogenous variation and produce consistent estimates by correcting OLS bias. With weak instruments, the first stage captures little genuine exogenous variation; most variation in the instrumented regressor comes from the endogenous component. The second stage then behaves much like OLS on the original endogenous regressor, inheriting its bias. The direction is toward OLS bias, not zero — which is insidious, since the estimates look plausible but remain contaminated by endogeneity."

- question: "Why does the first-stage F-statistic, rather than the first-stage R² or individual t-statistics, serve as the standard diagnostic for instrument weakness?"
  type: short-answer
  answer: "With multiple instruments, a researcher could have several instruments each with modest individual t-statistics that jointly provide strong first-stage prediction — or many instruments with seemingly adequate individual t-statistics that together overfit the first stage. The F-statistic tests the joint significance of all excluded instruments, capturing overall explanatory power. Crucially, Stock-Yogo (2005) derived critical values directly from the F-statistic's relationship to 2SLS relative bias, making it the natural scale for the question 'how much does weakness contaminate my estimate?' R² measures variance explained but doesn't translate to bias properties."
  explanation: "The formal result is that for a given F-value, you can bound the maximum bias of 2SLS relative to OLS bias. F > 10 corresponds approximately to 2SLS bias being no more than 10% of OLS bias for a single instrument. This directly answers the researcher's question. The Kleibergen-Paap statistic generalizes the F-statistic to heteroskedastic/clustered settings while maintaining the same interpretive framework."
```

## Explainer

You already understand why instrumental variables (IV) estimation is valuable: when a regressor is endogenous — correlated with the error term due to omitted variables, reverse causality, or measurement error — OLS is inconsistent. IV solves this by finding an instrument that is correlated with the endogenous regressor (relevance) but uncorrelated with the outcome except through that regressor (exclusion restriction). Two-stage least squares (2SLS) then uses the instrument to isolate exogenous variation. The catch you're now confronting: what happens when the instrument is only weakly correlated with the endogenous regressor? The answer is severe — and counterintuitive — problems.

The problem with **weak instruments** is that a tiny amount of violation of the exclusion restriction gets magnified dramatically. To see why, think about 2SLS intuitively: the first stage extracts the variation in the endogenous regressor that is explained by the instrument, and the second stage uses only that extracted variation. If the instrument barely moves the regressor (weak first stage), then almost all the variation in the second-stage "instrumented" regressor comes from noise, not clean exogenous signal. The 2SLS estimator is pulled toward the OLS estimator (and its bias) rather than correcting it. Standard confidence intervals are misleading — they don't cover the true parameter at their nominal rate, even in large samples.

Diagnosis centers on the **first-stage F-statistic** — the F-test of the joint significance of excluded instruments in the first-stage regression of the endogenous regressor on instruments and controls. The Stock-Yogo (2005) critical values give you the threshold for acceptable weakness. The standard rule of thumb is F > 10 for a single instrument, though this can be conservative; Stock-Yogo provide exact critical values for desired maximum relative bias (e.g., no more than 10% of OLS bias) and maximum size distortion of t-tests. With one instrument, F > 10 approximately ensures 2SLS bias is less than 10% of OLS bias. With multiple instruments, the relevant statistic is the **Cragg-Donald F-statistic** (or its heteroskedasticity-robust analogue, the Kleibergen-Paap statistic).

When instruments are weak, the remedies depend on context. If you have multiple weak instruments, combining them via 2SLS actually worsens the problem relative to using fewer — more instruments means more first-stage overfitting. Better alternatives include **LIML** (limited information maximum likelihood), which is median-unbiased under weak instruments and performs better than 2SLS in most simulations, and **Anderson-Rubin confidence sets**, which remain valid under weak instruments by inverting a test rather than relying on the first stage. The most honest response is sometimes to acknowledge that available instruments are too weak for reliable inference and that the research design requires stronger instruments — a better natural experiment, a more predictive policy assignment rule, or additional sources of exogenous variation.
