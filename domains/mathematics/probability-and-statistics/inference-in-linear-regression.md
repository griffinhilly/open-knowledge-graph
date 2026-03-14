---
id: inference-in-linear-regression
title: Inference in Linear Regression
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: regression-diagnostics
  type: hard
- id: t-test-for-means
  type: soft
builds-toward:
- prediction-intervals-regression
tags:
- regression
- inference
- testing
stage: formal-systems
status: draft
---

# Inference in Linear Regression

## Core Idea
Under standard regression assumptions, regression coefficients are normally distributed. We construct confidence intervals and tests for slope using t-distributions. F-test assesses overall model significance. Inference requires assumptions about errors.

## How It's Best Learned
Examine regression output with coefficients, SE, t-statistics, and p-values. Test whether slope differs from zero. Construct confidence intervals for slope and intercept. Compare F-test to t-test for single predictor.
