---
id: bootstrap-inference-econometrics
title: Bootstrap Methods for Statistical Inference
domain: economics
course: econometrics
prerequisites:
- id: hypothesis-testing-regression
  type: hard
- id: robust-standard-errors
  type: soft
- id: probability-theory
  type: hard
- id: sampling-distributions-theory
  type: hard
builds-toward:
- sensitivity-analysis-econometrics
tags:
- bootstrap
- inference
- resampling
stage: formal-systems
status: draft
---

# Bootstrap Methods for Statistical Inference

## Core Idea
Bootstrap methods construct empirical sampling distributions by repeatedly resampling from the data. They provide standard errors, confidence intervals, and p-values without requiring strong distributional assumptions.

## How It's Best Learned
Start with the nonparametric bootstrap: resample observations with replacement, recompute the estimator, and repeat many times. Compare bootstrap standard errors to parametric assumptions to assess robustness.
