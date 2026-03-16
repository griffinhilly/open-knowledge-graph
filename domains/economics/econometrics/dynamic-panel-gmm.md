---
id: dynamic-panel-gmm
title: Dynamic Panel Models and System GMM Estimation
domain: economics
course: econometrics
prerequisites:
- id: hausman-specification-test
  type: hard
- id: instrumental-variables
  type: hard
builds-toward:
- vector-autoregression-models
tags:
- panel-data
- dynamic
- gmm
stage: formal-systems
status: draft
---

# Dynamic Panel Models and System GMM Estimation

## Core Idea
Dynamic panels include lagged dependent variables, which correlate with fixed effects, violating strict exogeneity. Arellano-Bond and Blundell-Bond GMM estimators use internal instruments (lags of dependent variable and regressors) for consistent estimation. Arellano-Bond (difference GMM) assumes mean stationarity; Blundell-Bond (system GMM) relaxes this.

## Explainer

Start from what you know about panel fixed effects. The within estimator demeans the data to eliminate unobserved entity-specific effects (αᵢ), giving consistent estimates when strict exogeneity holds — meaning regressors are uncorrelated with the idiosyncratic error in all time periods. The problem with a **dynamic panel** is the inclusion of the lagged dependent variable yᵢ,ₜ₋₁ on the right-hand side. This lag contains information about all past values of y, which in turn are functions of αᵢ. So the regressor is mechanically correlated with the fixed effect. The within estimator is inconsistent, and the bias is large in short panels (small T) even as N grows.

The **Arellano-Bond** solution (difference GMM) first-differences the model to remove αᵢ, just like the within transformation. But now the equation is Δyᵢₜ = ρΔyᵢ,ₜ₋₁ + ΔXᵢₜβ + Δεᵢₜ. The problem is that Δyᵢ,ₜ₋₁ = yᵢ,ₜ₋₁ − yᵢ,ₜ₋₂ is still correlated with Δεᵢₜ = εᵢₜ − εᵢ,ₜ₋₁ (because Δyᵢ,ₜ₋₁ depends on εᵢ,ₜ₋₁). This is precisely the IV problem you studied: endogenous regressor in the differenced equation. The key insight is that levels of y dated t−2 and earlier are valid instruments: they are correlated with Δyᵢ,ₜ₋₁ (relevance) but uncorrelated with Δεᵢₜ provided errors are not serially correlated (exclusion). The estimator stacks these moment conditions and uses GMM to exploit all of them efficiently.

**Blundell-Bond** (system GMM) addresses a weakness of difference GMM: when y is highly persistent (ρ close to 1), lagged levels are weak instruments for the differenced equation — the correlation between yᵢ,ₜ₋₂ and Δyᵢ,ₜ₋₁ is near zero. Blundell-Bond adds the original levels equations back to the system, using lagged differences as instruments for the levels (Δyᵢ,ₜ₋₁ is a valid instrument for yᵢ,ₜ₋₁ in the levels equation if the initial conditions satisfy a stationarity restriction). The combined system gains precision, especially for persistent variables like firm size or GDP.

Two specification tests are essential for credibility. The **Sargan/Hansen test** checks whether the instruments are jointly valid (overidentification test); rejection suggests instrument proliferation or model misspecification. The **Arellano-Bond AR(2) test** checks for second-order serial correlation in the differenced residuals — if AR(2) is present, the t−2 lags are no longer valid instruments. A common failure mode is using too many instruments ("instrument proliferation"), which weakens the Hansen test and can bias coefficients. The rule of thumb is to keep the instrument count below the number of entities. Dynamic panel GMM is powerful for studying firm investment, growth regressions, and any setting where past outcomes causally determine current outcomes, but the instrument construction requires careful thought about the underlying error structure.
