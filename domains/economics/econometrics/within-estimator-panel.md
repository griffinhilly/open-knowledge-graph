---
id: within-estimator-panel
title: Within Estimator (Fixed Effects) for Panel Data
domain: economics
course: econometrics
prerequisites:
- id: panel-data-structure-advantages
  type: hard
- id: fixed-effects-models
  type: hard
builds-toward:
- between-estimator-panel
tags:
- panel-data
- fixed-effects
- within
stage: formal-systems
status: draft
---

# Within Estimator (Fixed Effects) for Panel Data

## Core Idea
The within estimator controls for unit-specific time-invariant unobserved heterogeneity by demeaning variables within each unit or including unit fixed effects. It is robust to selection based on stable individual characteristics but requires strict exogeneity: errors must be uncorrelated with past, present, and future regressors.

## Explainer

You know from panel data fundamentals that the key virtue of panel data is the ability to observe the same unit — a person, firm, or country — across multiple time periods. The **within estimator** (also called the **fixed effects estimator**) exploits this longitudinal structure to eliminate a class of confounders that would otherwise bias cross-sectional OLS: stable, unobserved unit characteristics that are correlated with the regressors.

To see why this matters, suppose you want to estimate the effect of job training on wages. Workers who seek out training may differ from those who don't — in ambition, ability, or work ethic. If you simply compare trained and untrained workers in a single cross-section, these unobserved traits confound your estimate. The within estimator sidesteps this by asking a different question: within each worker's own wage history, how does their wage change when they receive training? By focusing on changes within a unit over time, you effectively hold constant everything about that worker that doesn't change — ability, family background, personality — whether or not you can measure those things.

Mechanically, the within estimator **demeans** every variable by its unit-specific time mean. Define ȳᵢ = (1/T)∑ₜyᵢₜ. Then the regression is run on (yᵢₜ − ȳᵢ) = (xᵢₜ − x̄ᵢ)β + (εᵢₜ − ε̄ᵢ). This transformation wipes out any time-invariant component αᵢ — because αᵢ − ᾱᵢ = 0 by construction. An equivalent approach is to include a separate dummy variable for each unit (unit fixed effects); both produce the same coefficient estimates. The within estimator uses only within-unit variation in x — the fact that a given firm's investment fluctuated over time — while the **between estimator** would use across-firm variation in average investment levels.

The critical assumption is **strict exogeneity**: E[εᵢₜ | xᵢ₁, xᵢ₂, ..., xᵢT, αᵢ] = 0. This requires the error at time t to be uncorrelated with the regressors in all periods for unit i — past, present, and future. This is stronger than the contemporaneous exogeneity assumed in cross-sectional OLS. It rules out feedback effects where past outcomes influence current regressors (e.g., if last period's wage affects this period's training decision). When strict exogeneity holds, the within estimator is consistent. When it fails — for instance, due to dynamic effects or reverse causation — the estimator is inconsistent and alternative approaches like the Arellano-Bond GMM estimator are needed. Despite this limitation, fixed effects is among the most widely used tools in empirical economics precisely because it handles the most common form of omitted variable bias with minimal assumptions about the structure of unobserved heterogeneity.
