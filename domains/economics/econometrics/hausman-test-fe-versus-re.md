---
id: hausman-test-fe-versus-re
title: 'Hausman Test: Fixed Effects vs. Random Effects'
domain: economics
course: econometrics
prerequisites:
- id: hausman-specification-test
  type: hard
- id: fixed-effects-within-transformation
  type: hard
- id: random-effects-error-components
  type: hard
tags:
- panel-data
- model-selection
- hypothesis-testing
stage: formal-systems
status: draft
---

# Hausman Test: Fixed Effects vs. Random Effects

## Core Idea
The Hausman test compares FE and RE estimators under H₀: Cov(αᵢ, X) = 0 (RE is valid). The test statistic H = (β̂_FE - β̂_RE)' Var̂(β̂_FE - β̂_RE)⁻¹ (β̂_FE - β̂_RE) ~ χ²ₖ. Rejection favors FE; failure to reject can justify the more efficient RE.
