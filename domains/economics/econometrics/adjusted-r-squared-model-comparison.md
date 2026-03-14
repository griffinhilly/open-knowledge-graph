---
id: adjusted-r-squared-model-comparison
title: Adjusted R-Squared for Model Comparison
domain: economics
course: econometrics
prerequisites:
- id: r-squared-goodness-of-fit
  type: hard
builds-toward:
- information-criteria-model-selection
tags:
- model-comparison
- model-selection
stage: formal-systems
status: draft
---

# Adjusted R-Squared for Model Comparison

## Core Idea
Adjusted R² = 1 - ((RSS/(n-k-1)) / (TSS/(n-1))) penalizes adding regressors via a degrees-of-freedom adjustment. Unlike R², it can decrease when irrelevant variables are added, making it useful for comparing non-nested models with different regressor counts.
