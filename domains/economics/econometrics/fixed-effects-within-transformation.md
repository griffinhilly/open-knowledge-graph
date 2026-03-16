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

## Explainer

From your panel data prerequisite, you know you have repeated observations on the same entities over time — N individuals observed across T periods. From fixed effects models, you know the conceptual problem: each entity i has an unobserved characteristic αᵢ (ability, neighborhood quality, firm culture) that affects outcomes and may correlate with your regressors. OLS ignores αᵢ and is biased. The within transformation is how you mechanically eliminate these fixed effects without estimating each one directly.

The key operation is **demeaning**: for each entity i, subtract that entity's time mean from every observation. If unit i has average outcome Ȳᵢ across T periods, the demeaned outcome is Yᵢₜ − Ȳᵢ. Because αᵢ is constant across all t, when you subtract the mean you get αᵢ − αᵢ = 0. The fixed effect cancels algebraically. You're left with Yᵢₜ − Ȳᵢ = β(Xᵢₜ − X̄ᵢ) + (uᵢₜ − ūᵢ). Regressing demeaned outcomes on demeaned regressors is the within estimator — it uses only the variation within each unit over time, not the variation between units.

An important practical consequence: **time-invariant variables are eliminated by demeaning**. If you want to study the effect of race, country of birth, or any fixed characteristic, the within estimator cannot identify it — these variables have zero within-unit variation and vanish under demeaning. This is not a flaw; it's the price of eliminating omitted variable bias from time-invariant unobservables. Numerically, the within estimator is equivalent to including a separate dummy variable for every entity (Least Squares Dummy Variables, LSDV), but direct demeaning is far more computationally efficient when N is large.

The **identifying assumption** is strict exogeneity: the idiosyncratic error uᵢₜ must be uncorrelated with Xᵢₛ for all time periods s, not just the current one. Notice what this allows: αᵢ can be correlated with Xᵢₜ in any way — that's the whole point. But the time-varying residual must be uncorrelated with the regressors across all periods. This rules out anticipation effects (where units adjust X in response to future outcomes) and lagged dependent variable specifications (where a past Y on the right-hand side violates strict exogeneity).

A concrete example makes this tangible. Suppose you want to estimate how class size affects test scores using a panel of schools over several years. Wealthier schools have smaller classes and also score higher for unrelated reasons — classic omitted variable bias. The within transformation computes each school's deviation from its own mean class size and mean test score. You're now asking: in years when a particular school had unusually small classes relative to its own history, did it score unusually well? This comparison eliminates all fixed school characteristics — wealth, neighborhood, historical culture — that were biasing the OLS estimate. Only the within-school variation over time identifies β.
