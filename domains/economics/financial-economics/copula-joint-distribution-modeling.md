---
id: copula-joint-distribution-modeling
title: Copulas and Modeling Asset Dependence
domain: economics
course: financial-economics
prerequisites:
- id: expected-return-and-variance-of-assets
  type: hard
builds-toward:
- expected-shortfall-tail-risk
tags:
- dependence
- correlation
- copulas
- risk-modeling
stage: formal-systems
status: draft
---

# Copulas and Modeling Asset Dependence

## Core Idea
Copulas separate dependence structure from marginal distributions, allowing modeling of non-linear relationships and tail dependence that constant correlations miss. Gaussian copulas assume tail independence (correlations are low in extreme moves), while student-t copulas allow tail dependence. The 2008 crisis revealed that assuming Gaussian structure underestimates joint tail risk.
