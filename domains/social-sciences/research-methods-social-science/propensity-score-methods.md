---
id: propensity-score-methods
title: Propensity Score Methods
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: causal-inference-observational-data
  type: hard
- id: logistic-regression-binary-outcomes
  type: hard
- id: probability-distributions
  type: hard
- id: conditional-distributions-of-random-variables
  type: hard
- id: probability-mass-functions
  type: soft
- id: conditional-probability
  type: soft
- id: probability-axioms
  type: soft
- id: logistic-regression-binary-categorical
  type: soft
tags:
- propensity-score
- matching
- stratification
- weighting
stage: professional-practice
status: draft
---

# Propensity Score Methods

## Core Idea
Introduces propensity score methods to balance treatment and control groups in observational studies by matching on probability of treatment. Covers PS estimation, matching algorithms (1:1, caliper, replacement), stratification, inverse probability weighting, and sensitivity analysis for hidden bias.

## How It's Best Learned
Estimate propensity scores, create balance diagnostics before/after matching, try different matching algorithms, conduct sensitivity analysis with hidden bias parameters.

## Common Misconceptions
- Matching on propensity scores solves confounding
- Perfect balance is achievable and necessary
- Propensity score matching always improves inference
