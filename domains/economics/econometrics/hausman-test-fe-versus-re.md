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

## Explainer

When you work with panel data — observations on multiple units (firms, countries, individuals) over time — a fundamental modeling choice is how to treat the unobserved heterogeneity across units. Your prerequisite study of fixed effects (FE) and random effects (RE) laid out the tradeoff. Fixed effects are conservative: they absorb all unit-level variation, including anything correlated with your regressors, by transforming away the unit means. Random effects are efficient: by treating unit effects as random draws uncorrelated with regressors, they can use between-unit variation and produce smaller standard errors. The catch is that RE is only valid if that correlation assumption actually holds. The **Hausman test** is the formal tool for deciding between them.

The logic exploits a comparison of two estimators that have different properties under the null. Under H₀ (the RE assumption holds), both FE and RE are consistent, but RE is more efficient — it uses more variation. Under H₁ (the unit effects correlate with regressors), FE is still consistent, but RE is inconsistent — it suffers omitted variable bias. If the null is true, β̂_FE and β̂_RE should be close to each other (apart from sampling noise). If the null is false, they should diverge systematically because they are estimating different quantities. The test statistic measures this divergence, weighting it by the precision of the difference.

The test statistic H = (β̂_FE − β̂_RE)' [Var(β̂_FE − β̂_RE)]⁻¹ (β̂_FE − β̂_RE) follows a χ² distribution with k degrees of freedom (where k is the number of time-varying regressors) under H₀. A useful property: because RE is efficient under H₀, the variance of the difference simplifies to Var(β̂_FE) − Var(β̂_RE), which means you only need the two individual variance matrices to compute it. **Rejection** of H₀ (large H statistic) means the coefficient estimates differ enough to reject the RE assumption — use FE. **Failure to reject** means RE's efficiency gains are defensible.

Two practical caveats are worth knowing. First, the Hausman test is a test of RE's validity conditional on FE being correct — it does not test whether either model is well-specified. If you have omitted time-varying confounders, FE won't save you. Second, in small samples the test can have low power, meaning it may fail to reject RE even when mild endogeneity is present. A modern alternative is the cluster-robust Hausman test or the Mundlak approach, which adds group means of time-varying regressors to the RE specification — a rejection there is equivalent to the Hausman conclusion but with robust inference. The key takeaway: the Hausman test is not about which model is "better" in the abstract. It is specifically about whether the efficiency gains of RE come at the cost of consistency.
