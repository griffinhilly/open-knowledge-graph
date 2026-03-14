---
id: f-statistic-overall-significance
title: F-Statistic for Overall Model Significance
domain: economics
course: econometrics
prerequisites:
- id: normal-linear-regression-model
  type: hard
- id: f-test-joint-significance
  type: soft
tags:
- hypothesis-testing
- inference
- model-fit
stage: formal-systems
status: draft
---

# F-Statistic for Overall Model Significance

## Core Idea
The F-statistic F = (ESS/k) / (RSS/(n-k-1)) tests H₀: all slopes equal zero; it follows an F(k, n-k-1) distribution under the null. High F values indicate the model explains significant variation, though this does not imply causal effects.
