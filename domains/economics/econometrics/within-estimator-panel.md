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

## Questions

```yaml
- question: "A researcher studies the effect of R&D spending on firm profits using panel data. She worries about management quality — a stable, unobserved firm characteristic correlated with both R&D decisions and profits. Which feature of the within estimator addresses this concern?"
  type: multiple-choice
  options:
    - "It weights observations by firm size, reducing the influence of high-management-quality outliers"
    - "It uses variation in average R&D spending across firms, holding time trends constant"
    - "It demeans each firm's observations, removing any stable unobserved characteristic from the estimation"
    - "It includes industry dummies, which proxy for sector-level differences in management quality"
  answer: 2
  explanation: "The within estimator subtracts each firm's own time-mean from all its observations. Any stable characteristic — like management quality that doesn't change over the study period — is constant across time for a given firm, so it is completely wiped out by demeaning. The remaining variation is purely within-firm over time, where management quality is held constant by construction. This is the within estimator's core virtue: it controls for time-invariant unobservables without needing to measure them."

- question: "The within estimator and the between estimator both use the same source of variation in the panel data."
  type: multiple-choice
  options:
    - "True — both use variation in X across units to identify the effect of X on Y"
    - "False — the within estimator uses within-unit variation over time; the between estimator uses across-unit variation in unit averages"
    - "False — the within estimator uses variation across time periods; the between estimator uses variation across industries"
    - "True — both use the same demeaned data, but apply different weighting schemes"
  answer: 1
  explanation: "The within estimator identifies coefficients from how a given unit's outcome changes when its own regressor changes over time — pure within-unit variation. The between estimator identifies from differences in time-averaged outcomes across units — pure across-unit variation. These are genuinely different sources of variation, and they estimate the same population coefficient only if the model is correctly specified. The within estimator discards all cross-unit information; the between estimator discards all within-unit dynamics."

- question: "The within estimator eliminates omitted variable bias from all sources of confounding, whether or not the confounders change over time."
  type: true-false
  answer: false
  explanation: "The within estimator only eliminates bias from time-invariant confounders. If an unobserved variable changes over time and correlates with the regressor, the within estimator does not remove that bias. For example, if a firm improves its management in the same year it increases R&D spending, the within estimator cannot separate the R&D effect from the management improvement. Strict exogeneity — requiring errors to be uncorrelated with regressors in all periods — rules out such time-varying confounders."

- question: "The within estimator requires strict exogeneity: the error at time t must be uncorrelated with the regressors in all periods, not just the current period."
  type: true-false
  answer: true
  explanation: "This is stronger than the contemporaneous exogeneity assumed in cross-sectional OLS. Demeaning creates the transformed error (εᵢₜ − ε̄ᵢ), which includes the average error across all time periods for unit i. If last period's outcome affects this period's regressor (a feedback effect), then the regressor in one period is correlated with errors from other periods — violating strict exogeneity. This rules out dynamic models where lagged outcomes appear as regressors, which is why methods like Arellano-Bond GMM are needed in those settings."

- question: "Explain intuitively why the within estimator can control for an unobserved variable like 'innate worker ability' even though it never appears in the dataset."
  type: short-answer
  answer: "If innate ability doesn't change over time, it is identical across all observations for a given worker. When we subtract each worker's own time-mean from all their observations, the ability term — being constant — subtracts out completely. We are left with only within-worker variation over time, in which ability is effectively held constant. We compare each worker to their own past self, which automatically controls for everything stable about them — observed or not."
  explanation: "This is the within estimator's deepest intuition: each unit serves as its own control group. By focusing on changes within a unit rather than differences across units, we hold constant every time-invariant characteristic of that unit, whether or not we can measure it. The only confounders that survive are those that change over time — and strict exogeneity rules those out by assumption."
```

## Explainer

You know from panel data fundamentals that the key virtue of panel data is the ability to observe the same unit — a person, firm, or country — across multiple time periods. The **within estimator** (also called the **fixed effects estimator**) exploits this longitudinal structure to eliminate a class of confounders that would otherwise bias cross-sectional OLS: stable, unobserved unit characteristics that are correlated with the regressors.

To see why this matters, suppose you want to estimate the effect of job training on wages. Workers who seek out training may differ from those who don't — in ambition, ability, or work ethic. If you simply compare trained and untrained workers in a single cross-section, these unobserved traits confound your estimate. The within estimator sidesteps this by asking a different question: within each worker's own wage history, how does their wage change when they receive training? By focusing on changes within a unit over time, you effectively hold constant everything about that worker that doesn't change — ability, family background, personality — whether or not you can measure those things.

Mechanically, the within estimator **demeans** every variable by its unit-specific time mean. Define ȳᵢ = (1/T)∑ₜyᵢₜ. Then the regression is run on (yᵢₜ − ȳᵢ) = (xᵢₜ − x̄ᵢ)β + (εᵢₜ − ε̄ᵢ). This transformation wipes out any time-invariant component αᵢ — because αᵢ − ᾱᵢ = 0 by construction. An equivalent approach is to include a separate dummy variable for each unit (unit fixed effects); both produce the same coefficient estimates. The within estimator uses only within-unit variation in x — the fact that a given firm's investment fluctuated over time — while the **between estimator** would use across-firm variation in average investment levels.

The critical assumption is **strict exogeneity**: E[εᵢₜ | xᵢ₁, xᵢ₂, ..., xᵢT, αᵢ] = 0. This requires the error at time t to be uncorrelated with the regressors in all periods for unit i — past, present, and future. This is stronger than the contemporaneous exogeneity assumed in cross-sectional OLS. It rules out feedback effects where past outcomes influence current regressors (e.g., if last period's wage affects this period's training decision). When strict exogeneity holds, the within estimator is consistent. When it fails — for instance, due to dynamic effects or reverse causation — the estimator is inconsistent and alternative approaches like the Arellano-Bond GMM estimator are needed. Despite this limitation, fixed effects is among the most widely used tools in empirical economics precisely because it handles the most common form of omitted variable bias with minimal assumptions about the structure of unobserved heterogeneity.
