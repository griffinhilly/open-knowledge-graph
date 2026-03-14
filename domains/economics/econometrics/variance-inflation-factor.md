---
id: variance-inflation-factor
title: Variance Inflation Factor and Multicollinearity Diagnosis
domain: economics
course: econometrics
prerequisites:
- id: multicollinearity
  type: hard
- id: multiple-regression-model
  type: soft
builds-toward:
- generalized-least-squares
tags:
- multicollinearity
- diagnostics
- vif
stage: formal-systems
status: draft
---

# Variance Inflation Factor and Multicollinearity Diagnosis

## Core Idea
The Variance Inflation Factor (VIF) quantifies how much a coefficient's variance is inflated by multicollinearity: VIF = 1/(1 - Rⱼ²), where Rⱼ² comes from regressing regressor j on all others. VIF values above 5–10 typically indicate problematic multicollinearity requiring remediation.
