---
id: regression-model-assumptions
title: Assumptions in Linear Regression
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: linear-regression
  type: hard
builds-toward:
- regression-diagnostics
- inference-in-linear-regression
tags:
- regression
- assumptions
- diagnostics
stage: formal-systems
status: draft
---

# Assumptions in Linear Regression

## Core Idea
Standard linear regression assumes: linearity (relationship is linear), independence of observations, homoscedasticity (constant error variance), and normality of errors. Violations affect validity of inferential procedures. Residual plots help diagnose violations.

## How It's Best Learned
Create residual plots for various datasets and identify assumption violations. Compare behavior of regression under satisfied vs. violated assumptions. Use transformations to stabilize variance or linearize relationships.

## Common Misconceptions
Assuming regression works automatically without checking assumptions. Thinking normality is most important (independence violations are often more problematic). Fitting regression to inherently nonlinear relationships and ignoring residual patterns.
