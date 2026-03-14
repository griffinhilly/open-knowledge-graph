---
id: instrumental-variables-epidemiology
title: Instrumental Variables for Causal Inference
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: counterfactual-framework
  type: hard
- id: confounding-epidemiology
  type: hard
- id: multivariable-regression-epi
  type: hard
builds-toward:
- mediation-analysis-epidemiology
tags:
- causal-inference
- confounding
- unmeasured-confounding
stage: advanced
status: draft
---

# Instrumental Variables for Causal Inference

## Core Idea
Instrumental variables are characteristics that influence exposure but affect the outcome only through the exposure pathway, enabling causal inference when unmeasured confounding exists. Valid instruments must satisfy three criteria: association with exposure, no direct effect on outcome, and no association with unmeasured confounders of the exposure-outcome relationship. IV analysis produces consistent causal estimates even in the presence of hidden confounding.

## How It's Best Learned
Work through genetic epidemiology examples where genetic variants serve as natural instruments; implement two-stage least squares regression.

## Common Misconceptions
Any variable correlated with exposure works as an instrumental variable. Weak instruments are nearly as valid as strong instruments (weak instruments lead to large biases). IV estimates are causal only if the exclusion restriction holds.
