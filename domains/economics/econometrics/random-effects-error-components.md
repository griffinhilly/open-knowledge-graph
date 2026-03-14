---
id: random-effects-error-components
title: 'Random Effects: Error Component Model'
domain: economics
course: econometrics
prerequisites:
- id: random-effects-models
  type: hard
- id: panel-data-basics
  type: hard
builds-toward:
- hausman-test-fe-versus-re
tags:
- panel-data
- random-effects
- error-components
stage: formal-systems
status: draft
---

# Random Effects: Error Component Model

## Core Idea
The RE model specifies errors as uᵢₜ = αᵢ + εᵢₜ, where αᵢ ~ N(0,σ²ₐ) is time-invariant and εᵢₜ ~ N(0,σ²ₑ) is idiosyncratic. RE assumes Cov(αᵢ, Xᵢ) = 0; when valid, RE is more efficient than FE. Estimation uses feasible GLS accounting for both error components.
