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
