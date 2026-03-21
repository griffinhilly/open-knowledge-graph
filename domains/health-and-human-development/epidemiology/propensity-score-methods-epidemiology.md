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

## Questions

```yaml
- question: "After a propensity-score-matched study finds no difference in mortality between treated and untreated groups, a reviewer argues that propensity scoring 'essentially randomized' the groups so the result can be trusted as causal evidence. What is the most important flaw in this reasoning?"
  type: multiple-choice
  options:
    - "Propensity scores cannot be used for binary outcomes like mortality"
    - "Matching reduces sample size and thus statistical power"
    - "Propensity scores only balance measured covariates, leaving unmeasured confounding intact"
    - "The propensity model must be estimated with logistic regression specifically"
  answer: 2
  explanation: "Unlike randomization — which balances both observed and unobserved covariates by design — propensity score methods only control for confounders that were measured and included in the model. Unmeasured confounding remains fully intact regardless of how well the propensity model is specified. This is the fundamental limitation that prevents propensity score analyses from claiming the same causal guarantees as an RCT."

- question: "A researcher assesses covariate balance before and after propensity-score matching using p-values from t-tests, declaring 'balance achieved' when most p-values become non-significant. What is wrong with this approach?"
  type: multiple-choice
  options:
    - "Balance should be assessed using standardized mean differences, not p-values"
    - "Matching can only be validated using propensity score distribution histograms"
    - "Only the treated group should be checked for balance after matching"
    - "P-values are appropriate for continuous covariates but not for categorical ones"
  answer: 0
  explanation: "P-values are sensitive to sample size, not just covariate imbalance. After matching, sample size is typically reduced, which inflates p-values even when meaningful imbalance remains. Standardized mean differences (SMDs) quantify the magnitude of imbalance independent of sample size and are the appropriate tool for assessing whether matching succeeded in creating comparable groups."

- question: "A propensity score model that perfectly predicts treatment assignment would be the ideal tool for causal inference in an observational study."
  type: true-false
  answer: false
  explanation: "A perfect predictor of treatment assignment means there is no overlap — every subject is deterministically treated or untreated based on measured covariates. This violates the positivity assumption: the counterfactual outcome is unobservable for every person. Perfect prediction destroys the possibility of causal inference rather than enabling it. Causal estimation requires common support — regions of the covariate space where both treated and untreated individuals exist."

- question: "In a propensity-score-matched analysis, covariate balance should be assessed after matching, not only before."
  type: true-false
  answer: true
  explanation: "Pre-matching balance assessment describes the confounding problem; post-matching balance assessment tells you whether the solution worked. The purpose of matching is to create comparable groups, so checking balance after matching — using standardized mean differences across all covariates included in the propensity model — is the diagnostic that validates the analysis. Pre-match imbalance is expected; post-match imbalance indicates the matching failed."

- question: "Why can propensity score methods never fully replicate the causal guarantees of a randomized controlled trial, no matter how well the propensity model is specified?"
  type: short-answer
  answer: "Because propensity scores only balance covariates that were measured and included in the model. A randomized trial balances all confounders — measured and unmeasured — by design, because treatment assignment is independent of all subject characteristics. In an observational study, unmeasured variables (unknown to the researcher or simply not collected) may still differ between groups after propensity-score adjustment, leaving residual confounding that no statistical method can remove."
  explanation: "This is the irreducible limitation of all observational study designs. The quality of a propensity score analysis is bounded by the quality and completeness of the measured confounders. Sensitivity analyses (e.g., E-values) can quantify how strong unmeasured confounding would need to be to explain away a finding, but they cannot rule out its existence."
```

## Explainer

Your counterfactual framework prerequisite establishes the fundamental problem of causal inference: we observe each person under only one treatment condition, never both. The ideal is a randomized experiment where treatment assignment is independent of all covariates. In observational data, exposed and unexposed groups differ systematically — sicker patients get treated, wealthier neighborhoods receive more resources — and those differences confound the exposure-outcome relationship. Propensity score methods offer a strategy for handling this: instead of directly controlling for every confounder, summarize the entire confounding picture in a single number.

The **propensity score** is defined as the conditional probability of receiving the exposure given the observed baseline covariates: e(X) = P(A=1 | X). The key theorem, due to Rosenbaum and Rubin, is that conditioning on the propensity score is sufficient to remove confounding by all *measured* covariates — you don't need to model each covariate separately. Intuitively, if two individuals have the same propensity score (same probability of being treated), they are comparable across all covariates that went into estimating that score, even if their individual covariate values differ. This makes them pseudo-randomly assigned: within a stratum of equal propensity, treatment assignment is approximately independent of covariates.

There are four main implementations. **Matching**: for each treated subject, find an untreated subject with the same (or very close) propensity score and compare outcomes. This creates a matched sample that mirrors a randomized design. **Stratification**: divide the propensity score range into 5–10 strata and estimate the exposure effect within each stratum, then pool. **Inverse probability of treatment weighting (IPTW)**: weight each individual by 1/e(X) if treated and 1/(1−e(X)) if untreated, creating a pseudo-population where treatment is balanced across covariates. **Regression adjustment**: include the propensity score as a covariate in a regression model. Each method has different assumptions, efficiency, and sensitivity to model misspecification.

The critical limitation — which your multivariable regression background should make intuitive — is that propensity scores only balance **measured** confounders. Unlike randomization, which balances both observed and unobserved characteristics, propensity score methods leave unmeasured confounding fully intact. Before accepting a propensity score analysis, always ask: what unmeasured variables might still differ between groups? The practical standard is to assess **covariate balance** after matching or weighting using standardized mean differences (not p-values) and to report how much overlap exists in the propensity score distributions — because in regions of non-overlap, the counterfactual comparison is purely model-dependent and potentially unreliable.
