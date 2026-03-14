---
id: propensity-score-analysis
title: Propensity Score Analysis
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: confounding-epidemiology
  type: hard
- id: multivariable-regression-epi
  type: hard
builds-toward:
- inverse-probability-weighting
- g-estimation-causal-effects
tags:
- causal-inference
- confounding
- observational-studies
stage: advanced
status: draft
---

# Propensity Score Analysis

## Core Idea
Propensity score analysis estimates the probability that an individual receives an exposure conditional on observed confounders. By matching, stratifying, or weighting on propensity scores, analysts can simulate randomization and reduce confounding bias in observational studies without explicitly adjusting for every confounder.

## How It's Best Learned
Start with a simple observational dataset and manually calculate propensity scores using logistic regression, then compare crude vs. adjusted estimates. Practice with real data using matching and weighting approaches in sequence.

## Common Misconceptions
- Propensity scores eliminate all confounding (they only control measured confounders). - Using propensity scores requires 1:1 matching (matching is one option; weighting and stratification are alternatives). - Overlap/common support is not required (perfect overlap is ideal but not always necessary).
