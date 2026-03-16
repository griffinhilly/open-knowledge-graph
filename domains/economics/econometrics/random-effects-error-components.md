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

## Explainer

From your panel data basics, you know that panel data gives you repeated observations on the same units — firms, individuals, countries — over time. A core challenge is that each unit likely has permanent characteristics that affect the outcome but that you cannot directly observe or measure. The random effects model is one way to handle this, and understanding its structure carefully reveals both its power and its critical weakness.

The **error component decomposition** splits the composite error term into two parts. The term αᵢ is a unit-specific, time-invariant disturbance — think of it as everything permanently different about unit i: management quality for firms, innate ability for workers, institutional strength for countries. The term εᵢₜ is the ordinary idiosyncratic shock that varies both across units and over time. This two-part structure means observations on the same unit are correlated across time — knowing that a firm had a high α₁ in period one predicts it will also have a high α₁ in period two, because it is the same firm. Ignoring this within-unit correlation and running pooled OLS treats these errors as independent, which gives inefficient estimates and wrong standard errors.

The RE estimator handles this correlation through **feasible GLS**. It first estimates σ²ₐ and σ²ₑ by examining the within-unit and between-unit variance in the residuals, then uses those estimates to perform a partial demeaning. Unlike fixed effects (which removes the unit mean entirely), RE subtracts only a fraction θ = 1 − σ_ε / √(Tσ²ₐ + σ²ₑ) of the unit mean. When σ²ₐ is large relative to σ²ₑ, θ approaches 1 and RE approaches fixed effects. When σ²ₐ is negligible, θ approaches 0 and RE approaches pooled OLS. RE lives between these extremes, and its estimate uses both within-unit variation over time and between-unit cross-sectional variation.

This is where the critical assumption bites. RE is valid only when **Cov(αᵢ, Xᵢₜ) = 0** — the unobserved unit characteristic must be uncorrelated with your regressors. For firms, αᵢ might represent management quality. If better managers also invest more in capital (your regressor), management quality and capital are correlated, and the RE assumption fails. The α for better-managed firms gets partially loaded onto the capital coefficient, biasing it upward. Fixed effects avoids this by sweeping out αᵢ entirely through the within transformation — at the cost of losing all information from time-invariant regressors (like a firm's industry or a person's race) that also get swept out. The choice between RE and FE is therefore fundamentally about whether you trust the Cov(αᵢ, Xᵢₜ) = 0 assumption, which the Hausman test you will encounter next formalizes as a statistical test.
