---
id: fixed-effects-within-transformation
title: 'Fixed Effects: Within Transformation'
domain: economics
course: econometrics
prerequisites:
- id: fixed-effects-models
  type: hard
- id: panel-data-basics
  type: hard
builds-toward:
- hausman-test-fe-versus-re
tags:
- panel-data
- fixed-effects
- within-transformation
stage: formal-systems
status: draft
---

# Fixed Effects: Within Transformation

## Core Idea
The within (fixed effects) estimator removes time-invariant unobserved heterogeneity αᵢ by demeaning: Yᵢₜ - Ȳᵢ = β(Xᵢₜ - X̄ᵢ) + (uᵢₜ - ūᵢ). Equivalent to including individual dummies, FE is consistent under conditional exogeneity E[uᵢₜ|Xᵢ] = 0 even if αᵢ correlates with X.
