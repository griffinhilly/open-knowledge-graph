---
id: matching-methods-causal-inference
title: Matching Methods for Causal Inference
domain: economics
course: econometrics
prerequisites:
- id: causal-inference-econometrics
  type: hard
- id: potential-outcomes-framework
  type: hard
builds-toward:
- propensity-score-methods
tags:
- matching
- causal-inference
- observational
stage: formal-systems
status: draft
---

# Matching Methods for Causal Inference

## Core Idea
Matching estimators pair treated and control units with similar pre-treatment characteristics. Nearest-neighbor, caliper, and kernel matching select matches differently, balancing bias and variance in treatment effect estimation.

## Explainer

From the potential outcomes framework, you know the **fundamental problem of causal inference**: each unit is either treated or untreated — you never observe both Y(1) and Y(0) for the same person at the same time. To estimate the average treatment effect (ATT or ATE), you need to approximate the counterfactual: what would treated units have experienced if they hadn't been treated? Matching builds this counterfactual by substituting control units that look similar to the treated unit before treatment. The logic is simple: if two students have identical test scores, family income, and prior grades, and one goes to a private school while the other doesn't, the latter is a reasonable counterfactual for the former.

The key assumption that makes matching valid is **conditional independence** (also called "selection on observables" or the CIA): conditional on observable pre-treatment characteristics X, treatment assignment is independent of potential outcomes. Written as Y(0), Y(1) ⊥ D | X. In plain language: once you account for all the measured covariates, treated and untreated units with the same X values are similar enough that any difference in outcomes can be attributed to the treatment. This is a strong assumption — it fails whenever important confounders are unobserved — but in settings where you have rich administrative data (detailed demographics, prior outcomes, institutional records), it is often plausible.

The three matching algorithms differ in how they select the counterfactual comparison. **Nearest-neighbor matching** pairs each treated unit with the single control unit closest in covariate space (often using Euclidean distance or Mahalanobis distance). It's computationally simple and unbiased in large samples but can produce poor matches when the nearest neighbor is still far away. **Caliper matching** imposes a maximum distance threshold: treated units without a sufficiently close match are dropped from the analysis entirely. This reduces bias from bad matches but can shrink the sample significantly, potentially introducing selection if the matched sample is unrepresentative of all treated units. **Kernel matching** weights every control unit by a kernel function of its distance to the treated unit — nearby controls receive high weight, distant controls near-zero weight. It uses more data than nearest-neighbor, reducing variance, but the choice of kernel bandwidth introduces a smoothing decision.

The bias-variance tradeoff across these methods follows a clear pattern. One-to-one nearest-neighbor matching is low-bias (when matches are good) but high-variance (few observations, noisy estimates). Kernel matching is lower variance but can introduce bias when distant, poor matches receive positive weight. Caliper matching controls bias by removing bad matches, at the cost of external validity. Practitioners often run multiple methods as a robustness check: if treatment effect estimates are similar across methods, the result is less sensitive to the specific matching algorithm chosen.

The critical limitation of all matching methods is that they handle **observed confounding** only. If there is an unobserved variable that predicts both treatment selection and outcomes — innate ability in education studies, health consciousness in nutrition studies, location quality in housing studies — matching on observed characteristics cannot eliminate this bias. The identifying assumption is untestable directly; researchers typically assess it with placebo tests, sensitivity analyses (like Rosenbaum bounds), and by arguing the economic mechanism behind selection. When unobserved confounding is a serious concern, matching should be combined with or replaced by methods that exploit external variation, such as instrumental variables or difference-in-differences.
