---
id: regression-inference-hypothesis-tests
title: Hypothesis Tests and Inference in Regression
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: linear-regression-simple-theory
  type: hard
builds-toward:
- regression-diagnostics
tags:
- regression-inference
stage: formal-systems
status: draft
---

# Hypothesis Tests and Inference in Regression

## Core Idea
Test H₀:β₁=0 using T=(β₁−0)/SE(β₁) with n−2 df. Confidence interval for β₁: β₁±t_{n-2,α/2}·SE(β₁). F-test for overall model. Prediction intervals widen with distance from X̄ and with increased residual variation.
