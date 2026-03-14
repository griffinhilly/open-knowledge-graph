---
id: coefficient-interpretation-regression
title: Interpreting Regression Coefficients
domain: economics
course: econometrics
prerequisites:
- id: multiple-regression-model
  type: hard
- id: logarithms-intro
  type: soft
builds-toward:
- hypothesis-testing-regression
- dummy-variables-regression
tags:
- interpretation
- log-linear
- elasticity
- ceteris-paribus
stage: formal-systems
status: validated
---

# Interpreting Regression Coefficients

## Core Idea
The interpretation of a regression coefficient depends on the functional form. In a level-level model (y on x), β₁ gives the change in y per unit change in x. In a log-level model (log y on x), 100·β₁ gives the approximate percentage change in y per unit change in x. In a log-log model, β₁ is the elasticity — the percentage change in y per 1% change in x. Dummy variable coefficients compare a group mean to the omitted reference group, holding other covariates constant. Correct interpretation always includes the ceteris paribus qualifier.

## How It's Best Learned
Practice translating coefficient estimates into plain-language economic statements across different functional forms. The wage-education regression in log form is a canonical exercise.

## Common Misconceptions
- A coefficient of 0.05 in a log-level regression means a 5 percentage point change, not a 5% change — the distinction matters for large effects.
- Standardized beta coefficients answer a different question than raw coefficients; mixing them up leads to incorrect comparisons.
