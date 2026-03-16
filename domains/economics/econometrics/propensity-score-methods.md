---
id: propensity-score-methods
title: Propensity Score Methods and Estimation
domain: economics
course: econometrics
prerequisites:
- id: matching-methods-causal-inference
  type: hard
- id: logit-probit-models
  type: hard
tags:
- propensity-score
- treatment-effects
- observational
stage: formal-systems
status: draft
---

# Propensity Score Methods and Estimation

## Core Idea
The propensity score is the probability of treatment given covariates. Propensity score methods balance treated and control groups on observed characteristics through matching, stratification, weighting, or regression adjustment.

## Explainer

From matching methods, you know the fundamental problem of causal inference: treated and control units may differ systematically in ways that affect both who receives treatment and what outcomes they'd achieve. Direct matching on observed covariates works when you have a small number of variables, but it breaks down fast. If units differ on five or ten variables, finding a "close match" in that high-dimensional space becomes nearly impossible — the **curse of dimensionality**. Propensity score methods solve this by collapsing all those covariates into a single number.

The **propensity score** p(X) = P(D=1 | X) is the conditional probability that a unit receives treatment given its observed characteristics. The key theoretical result (Rosenbaum and Rubin, 1983) is the balancing property: conditional on the propensity score, treated and control units have the same distribution of observed covariates. In other words, if two units have the same propensity score, they are comparable — even if they differ on individual covariates. This reduces a high-dimensional matching problem to a one-dimensional one.

In practice, you estimate the propensity score using logit or probit — your prerequisite from binary choice models. You regress treatment status D on all observed covariates X, and the fitted probabilities are your estimated propensity scores. Once you have scores, you can apply them in four ways: **propensity score matching** pairs each treated unit to the control unit with the closest score; **stratification** (subclassification) divides the score distribution into bins and compares averages within each bin; **inverse probability of treatment weighting (IPTW)** reweights the sample so treated and control groups look like they came from the same population; **regression adjustment** includes the score as a control variable in an outcome regression.

The critical assumption underlying all propensity score methods is **unconfoundedness** (also called conditional independence or selection on observables): conditional on observed covariates, treatment assignment is independent of potential outcomes. This assumption is untestable — if there are unobserved variables that affect both treatment and outcomes, propensity scores cannot remove that bias, no matter how carefully estimated. This is why checking covariate balance *after* applying the method is essential: good balance means treated and control groups look similar on observed characteristics. It doesn't guarantee good balance on unobserved ones, but poor observed balance is a definitive sign the method has failed. Sensitivity analysis tools (like Rosenbaum bounds) help assess how robust conclusions are to potential hidden confounders.
