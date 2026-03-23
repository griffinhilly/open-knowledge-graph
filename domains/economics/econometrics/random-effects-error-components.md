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
status: validated
---

# Random Effects: Error Component Model

## Core Idea
The RE model specifies errors as uᵢₜ = αᵢ + εᵢₜ, where αᵢ ~ N(0,σ²ₐ) is time-invariant and εᵢₜ ~ N(0,σ²ₑ) is idiosyncratic. RE assumes Cov(αᵢ, Xᵢ) = 0; when valid, RE is more efficient than FE. Estimation uses feasible GLS accounting for both error components.

## Questions

```yaml
- question: "Researchers study how capital investment affects firm productivity using panel data. They believe better-managed firms both invest more in capital AND are more productive — but management quality is unobservable. Which estimator is most appropriate?"
  type: multiple-choice
  options:
    - "Random effects, because management quality varies over time and will be captured in the time-varying error term"
    - "Fixed effects, because management quality is a time-invariant unobserved characteristic likely correlated with capital investment, violating the RE assumption"
    - "Random effects, because it uses both within-unit and between-unit variation, making it more efficient"
    - "Pooled OLS, because it uses all variation without imposing unnecessary assumptions"
  answer: 1
  explanation: "If management quality (αᵢ) is correlated with capital investment (Xᵢₜ), the RE assumption Cov(αᵢ, Xᵢₜ) = 0 is violated. Using RE would load the management quality effect onto the capital coefficient, biasing it upward. Fixed effects sweeps out αᵢ entirely through the within transformation, eliminating this bias. Option C's efficiency reasoning is correct about RE in general, but efficiency is irrelevant when the estimator is biased."

- question: "In the RE partial demeaning formula, the parameter θ approaches 1 as σ²ₐ becomes very large relative to σ²ₑ. What does this imply about the RE estimator?"
  type: multiple-choice
  options:
    - "RE becomes less efficient than pooled OLS as unit-specific variance dominates"
    - "RE approaches the fixed effects estimator, since nearly all of each unit's mean is subtracted out"
    - "RE becomes identical to pooled OLS because unit-specific effects are negligible"
    - "RE breaks down and should be replaced with a structural model"
  answer: 1
  explanation: "The parameter θ = 1 − σ_ε / √(Tσ²ₐ + σ²ₑ) measures what fraction of the unit mean is subtracted. When σ²ₐ is large, θ → 1 and RE subtracts the entire unit mean — exactly what fixed effects does via the within transformation. When permanent unit-level variation dominates idiosyncratic noise, you must remove most of the unit mean to get consistent estimates, and RE and FE converge to the same solution."

- question: "The random effects estimator uses both within-unit variation (how each unit changes over time) and between-unit variation (cross-sectional differences), while the fixed effects estimator uses only within-unit variation."
  type: true-false
  answer: true
  explanation: "Fixed effects removes all between-unit variation by fully demeaning each unit's observations — it is entirely identified by within-unit change over time. RE only partially removes the unit mean (by factor θ < 1), so cross-sectional differences between units also contribute to the estimates. This is why RE is more efficient when Cov(αᵢ, Xᵢₜ) = 0 holds — it uses more information. When that assumption fails, the between-unit variation is contaminated by the αᵢ–Xᵢₜ correlation, and RE's extra efficiency becomes bias."

- question: "The random effects assumption Cov(αᵢ, Xᵢₜ) = 0 is automatically satisfied whenever the panel dataset is balanced (every unit observed the same number of periods)."
  type: true-false
  answer: false
  explanation: "Whether a panel is balanced is a feature of data collection design, not of the relationship between unobserved unit characteristics and regressors. Cov(αᵢ, Xᵢₜ) = 0 is a substantive assumption about whether unmeasured permanent unit factors (management quality, innate ability, institutional strength) correlate with covariates. A perfectly balanced panel with correlated unit effects still violates the RE assumption and produces biased estimates. The Hausman test — which compares RE and FE coefficients — is the standard empirical check."

- question: "Why does the fixed effects estimator lose information about time-invariant regressors (like a person's race or a firm's founding year), while the random effects estimator does not?"
  type: short-answer
  answer: "Fixed effects identifies coefficients purely from within-unit variation over time — it fully demeans each unit, removing any variable that is constant within a unit. A time-invariant regressor (like race) takes the same value in every period for the same person; after demeaning it becomes identically zero, providing no variation to estimate a coefficient. Random effects only partially demeans (by θ < 1), so between-unit variation in time-invariant regressors still provides identifying information."
  explanation: "This is the fundamental FE–RE tradeoff: FE consistently estimates effects of time-varying regressors regardless of whether αᵢ correlates with Xᵢₜ, but cannot estimate effects of fixed characteristics. RE can estimate both, but only consistently when Cov(αᵢ, Xᵢₜ) = 0 holds. Researchers who need to estimate effects of time-invariant characteristics (e.g., the gender wage gap) must use RE or IV-based approaches while accepting the risk of bias from unobserved unit heterogeneity."
```

## Explainer

From your panel data basics, you know that panel data gives you repeated observations on the same units — firms, individuals, countries — over time. A core challenge is that each unit likely has permanent characteristics that affect the outcome but that you cannot directly observe or measure. The random effects model is one way to handle this, and understanding its structure carefully reveals both its power and its critical weakness.

The **error component decomposition** splits the composite error term into two parts. The term αᵢ is a unit-specific, time-invariant disturbance — think of it as everything permanently different about unit i: management quality for firms, innate ability for workers, institutional strength for countries. The term εᵢₜ is the ordinary idiosyncratic shock that varies both across units and over time. This two-part structure means observations on the same unit are correlated across time — knowing that a firm had a high α₁ in period one predicts it will also have a high α₁ in period two, because it is the same firm. Ignoring this within-unit correlation and running pooled OLS treats these errors as independent, which gives inefficient estimates and wrong standard errors.

The RE estimator handles this correlation through **feasible GLS**. It first estimates σ²ₐ and σ²ₑ by examining the within-unit and between-unit variance in the residuals, then uses those estimates to perform a partial demeaning. Unlike fixed effects (which removes the unit mean entirely), RE subtracts only a fraction θ = 1 − σ_ε / √(Tσ²ₐ + σ²ₑ) of the unit mean. When σ²ₐ is large relative to σ²ₑ, θ approaches 1 and RE approaches fixed effects. When σ²ₐ is negligible, θ approaches 0 and RE approaches pooled OLS. RE lives between these extremes, and its estimate uses both within-unit variation over time and between-unit cross-sectional variation.

This is where the critical assumption bites. RE is valid only when **Cov(αᵢ, Xᵢₜ) = 0** — the unobserved unit characteristic must be uncorrelated with your regressors. For firms, αᵢ might represent management quality. If better managers also invest more in capital (your regressor), management quality and capital are correlated, and the RE assumption fails. The α for better-managed firms gets partially loaded onto the capital coefficient, biasing it upward. Fixed effects avoids this by sweeping out αᵢ entirely through the within transformation — at the cost of losing all information from time-invariant regressors (like a firm's industry or a person's race) that also get swept out. The choice between RE and FE is therefore fundamentally about whether you trust the Cov(αᵢ, Xᵢₜ) = 0 assumption, which the Hausman test you will encounter next formalizes as a statistical test.
