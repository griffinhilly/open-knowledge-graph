---
id: propensity-score-methods-epidemiology
title: Propensity Score Methods
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: multivariable-regression-epi
  type: hard
- id: counterfactual-framework
  type: hard
builds-toward:
- instrumental-variables-epidemiology
tags:
- confounding-control
- causal-inference
- covariate-balance
stage: advanced
status: draft
---

# Propensity Score Methods

## Core Idea
Propensity scores—the estimated probability of receiving an exposure given baseline covariates—can balance confounding without explicitly controlling for each measured covariate. They enable matching, stratification, weighting, or regression adjustment to simulate a pseudo-randomized study design. PS methods are especially useful in high-dimensional settings with many potential confounders or in observational studies with complex exposure assignment.

## How It's Best Learned
Implement PS matching on an observational dataset; assess covariate balance before and after matching using standardized mean differences.

## Common Misconceptions
Propensity score methods eliminate all bias (they only remove measured confounding). High propensity score overlap guarantees valid causal inference. Model specification is unimportant as long as the score is estimated.

## Explainer

Your counterfactual framework prerequisite establishes the fundamental problem of causal inference: we observe each person under only one treatment condition, never both. The ideal is a randomized experiment where treatment assignment is independent of all covariates. In observational data, exposed and unexposed groups differ systematically — sicker patients get treated, wealthier neighborhoods receive more resources — and those differences confound the exposure-outcome relationship. Propensity score methods offer a strategy for handling this: instead of directly controlling for every confounder, summarize the entire confounding picture in a single number.

The **propensity score** is defined as the conditional probability of receiving the exposure given the observed baseline covariates: e(X) = P(A=1 | X). The key theorem, due to Rosenbaum and Rubin, is that conditioning on the propensity score is sufficient to remove confounding by all *measured* covariates — you don't need to model each covariate separately. Intuitively, if two individuals have the same propensity score (same probability of being treated), they are comparable across all covariates that went into estimating that score, even if their individual covariate values differ. This makes them pseudo-randomly assigned: within a stratum of equal propensity, treatment assignment is approximately independent of covariates.

There are four main implementations. **Matching**: for each treated subject, find an untreated subject with the same (or very close) propensity score and compare outcomes. This creates a matched sample that mirrors a randomized design. **Stratification**: divide the propensity score range into 5–10 strata and estimate the exposure effect within each stratum, then pool. **Inverse probability of treatment weighting (IPTW)**: weight each individual by 1/e(X) if treated and 1/(1−e(X)) if untreated, creating a pseudo-population where treatment is balanced across covariates. **Regression adjustment**: include the propensity score as a covariate in a regression model. Each method has different assumptions, efficiency, and sensitivity to model misspecification.

The critical limitation — which your multivariable regression background should make intuitive — is that propensity scores only balance **measured** confounders. Unlike randomization, which balances both observed and unobserved characteristics, propensity score methods leave unmeasured confounding fully intact. Before accepting a propensity score analysis, always ask: what unmeasured variables might still differ between groups? The practical standard is to assess **covariate balance** after matching or weighting using standardized mean differences (not p-values) and to report how much overlap exists in the propensity score distributions — because in regions of non-overlap, the counterfactual comparison is purely model-dependent and potentially unreliable.
