---
id: statistical-methods-analytical
title: Error Analysis and Statistics in Analytical Chemistry
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: analytical-chemistry-intro
  type: hard
- id: mean-median-mode
  type: soft
- id: measures-of-spread
  type: soft
builds-toward:
- calibration-curve-methods
- method-validation
- quality-assurance-analytical
tags:
- statistics
- error analysis
- precision
- accuracy
- confidence intervals
stage: advanced
status: draft
---

# Error Analysis and Statistics in Analytical Chemistry

## Core Idea
Every analytical measurement carries uncertainty arising from random (indeterminate) and systematic (determinate) errors. Statistical tools — mean, standard deviation, relative standard deviation, confidence intervals, and significance tests such as the t-test and F-test — allow chemists to characterize measurement uncertainty and compare results rigorously. Propagation of uncertainty describes how errors in individual measurements combine in calculated quantities. Outlier identification using the Q-test or Grubbs' test maintains data integrity.

## How It's Best Learned
Practice computing confidence intervals and propagating uncertainty through multi-step calculations by hand before relying on spreadsheet functions. Simulating datasets with known parameters builds intuition for how sample size and variability affect conclusions.

## Common Misconceptions
- Standard deviation describes spread among replicates, not the uncertainty of the mean — that is the standard error.
- A result reported with many significant figures is not necessarily more accurate; significant figures should reflect actual measurement precision.
