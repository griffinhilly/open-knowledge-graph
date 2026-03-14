---
id: multivariable-regression-epi
title: Multivariable Regression in Epidemiology
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: stratification-and-adjustment
  type: hard
- id: biostatistics-in-public-health
  type: hard
builds-toward:
- cox-proportional-hazards
- meta-analysis-methods
tags:
- logistic-regression
- linear-regression
- adjustment
- multicollinearity
stage: advanced
status: draft
---

# Multivariable Regression in Epidemiology

## Core Idea
Multivariable regression simultaneously models associations between an outcome and multiple exposures/confounders, providing adjusted effect estimates. Linear regression is used for continuous outcomes; logistic regression for binary outcomes; Cox regression for time-to-event. Regression assumes specific functional forms, handles interactions explicitly, and is flexible for many confounders, but requires careful model specification and diagnostics.
