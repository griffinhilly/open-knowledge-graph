---
id: selection-bias-econometrics
title: Selection Bias
domain: economics
course: econometrics
prerequisites:
- id: potential-outcomes-framework
  type: hard
- id: endogeneity
  type: hard
builds-toward:
- difference-in-differences
- instrumental-variables
tags:
- selection-bias
- self-selection
- observational-data
- non-random-treatment
stage: formal-systems
status: draft
---

# Selection Bias

## Core Idea
Selection bias occurs when the units who receive treatment systematically differ from controls in ways that also affect the outcome, making the treated group a non-representative counterfactual for the untreated. A classic example: estimating returns to job training by comparing trainees to non-trainees, when those who chose to train were already more motivated. Selection on observables (confounding) can be addressed by controlling for all relevant characteristics; selection on unobservables requires an instrument, a discontinuity, or a differencing strategy. Heckman's selection model handles selection into a sample from a latent participation equation.

## Common Misconceptions
- Matching on observables does not solve selection on unobservables — it only balances measured covariates.
- Selection bias and attrition bias are related but distinct: attrition bias arises from non-random dropout from a study.
