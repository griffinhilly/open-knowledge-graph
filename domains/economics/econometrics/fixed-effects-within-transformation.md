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
status: validated
---

# Fixed Effects: Within Transformation

## Core Idea
The within (fixed effects) estimator removes time-invariant unobserved heterogeneity αᵢ by demeaning: Yᵢₜ - Ȳᵢ = β(Xᵢₜ - X̄ᵢ) + (uᵢₜ - ūᵢ). Equivalent to including individual dummies, FE is consistent under conditional exogeneity E[uᵢₜ|Xᵢ] = 0 even if αᵢ correlates with X.

## Questions

```yaml
- question: "A researcher uses the within transformation (fixed effects) to study how exercise hours affect health scores using a panel of 500 individuals over 10 years. She also wants to estimate the effect of biological sex on health outcomes. What happens to the sex variable?"
  type: multiple-choice
  options:
    - "Sex is estimated with higher precision than time-varying variables, since it doesn't change and creates no measurement noise"
    - "The sex coefficient cannot be estimated — demeaning eliminates time-invariant variables because they have zero within-unit variation"
    - "Sex's coefficient is estimated using cross-sectional variation between male and female participants"
    - "Sex's effect is absorbed into the individual-specific intercept and can be recovered separately afterward"
  answer: 1
  explanation: "Time-invariant variables are eliminated by demeaning: if sex = 1 for all t for individual i, then (sex_it − sex̄_i) = (1 − 1) = 0. The variable vanishes identically. This is not a flaw — it is the price of eliminating all time-invariant confounders, including observed ones. Options C and D describe what random effects (or separate OLS regressions) could do, not within-transformation FE."

- question: "In a panel dataset of schools tracked over 8 years, the within (fixed effects) estimator identifies the effect of class size on test scores by comparing:"
  type: multiple-choice
  options:
    - "High-performing schools to low-performing schools across the full sample"
    - "Each school's test scores in years when its class sizes were unusually small relative to that school's own history"
    - "Schools in wealthy districts to schools in poor districts, controlling for observable differences"
    - "Average test scores across all schools for each calendar year"
  answer: 1
  explanation: "The within transformation subtracts each school's time-mean from every observation. The estimator uses only the variation within each school over time — asking whether a school scores better in years when its class sizes are below its own average. This eliminates all fixed school characteristics (wealth, neighborhood, historical culture) that confound the cross-school comparison in option A. Options C and D describe between-school comparisons, which are what FE is designed to avoid."

- question: "The within (fixed effects) transformation is mathematically equivalent to including a dummy variable for every individual in the panel, but demeaning is more computationally efficient when N is large."
  type: true-false
  answer: true
  explanation: "Including N individual dummies (LSDV — Least Squares Dummy Variables) produces identical coefficient estimates on the time-varying regressors as demeaning. The equivalence follows from the Frisch-Waugh-Lovell theorem: partialing out the individual dummies is the same as regressing on demeaned data. LSDV requires inverting an (N + K) × (N + K) matrix; demeaning only requires inverting a K × K matrix, a major computational advantage when N is thousands or millions."

- question: "Fixed effects estimation remains consistent even when the idiosyncratic error uᵢₜ is correlated with future values of Xᵢₜ, as long as the fixed effect αᵢ is successfully eliminated by demeaning."
  type: true-false
  answer: false
  explanation: "The identifying assumption for fixed effects is *strict exogeneity*: E[uᵢₜ | Xᵢ₁, Xᵢ₂, ..., XᵢT] = 0. The idiosyncratic error must be uncorrelated with regressors across *all* time periods, not just the current one. Anticipation effects (units adjusting X in response to future outcomes) and lagged dependent variable specifications both violate strict exogeneity and make FE inconsistent, even though αᵢ is eliminated. The key distinction: FE handles correlation between αᵢ and X freely, but demands the residual uᵢₜ be clean across all periods."

- question: "Explain in plain language what the within transformation 'removes' from the data, and why this allows the fixed effect αᵢ to correlate freely with the regressors Xᵢₜ."
  type: short-answer
  answer: "The within transformation subtracts each unit's time-average from its observations, removing everything that is constant for that unit across time. The fixed effect αᵢ is by definition time-invariant — it represents stable, unobserved characteristics like a school's neighborhood quality or a person's innate ability. When you subtract the unit mean, αᵢ − αᵢ = 0: the fixed effect cancels out exactly, regardless of how large it is or how strongly it correlates with X. Once αᵢ is gone, the remaining variation is purely within-unit over time, and OLS on this demeaned data is consistent. The correlation between αᵢ and X that would bias OLS no longer matters because αᵢ is not in the equation."
  explanation: "The intuition is: we don't need to know the value of αᵢ or control for it with observables — we just need to eliminate it algebraically. Demeaning achieves this by exploiting the fact that αᵢ is constant; a constant minus its own mean is always zero. This is the power and the limitation of fixed effects: anything time-invariant is equally eliminated, whether you wanted to eliminate it (the confounders) or not (observed time-invariant regressors you care about)."
```

## Explainer

From your panel data prerequisite, you know you have repeated observations on the same entities over time — N individuals observed across T periods. From fixed effects models, you know the conceptual problem: each entity i has an unobserved characteristic αᵢ (ability, neighborhood quality, firm culture) that affects outcomes and may correlate with your regressors. OLS ignores αᵢ and is biased. The within transformation is how you mechanically eliminate these fixed effects without estimating each one directly.

The key operation is **demeaning**: for each entity i, subtract that entity's time mean from every observation. If unit i has average outcome Ȳᵢ across T periods, the demeaned outcome is Yᵢₜ − Ȳᵢ. Because αᵢ is constant across all t, when you subtract the mean you get αᵢ − αᵢ = 0. The fixed effect cancels algebraically. You're left with Yᵢₜ − Ȳᵢ = β(Xᵢₜ − X̄ᵢ) + (uᵢₜ − ūᵢ). Regressing demeaned outcomes on demeaned regressors is the within estimator — it uses only the variation within each unit over time, not the variation between units.

An important practical consequence: **time-invariant variables are eliminated by demeaning**. If you want to study the effect of race, country of birth, or any fixed characteristic, the within estimator cannot identify it — these variables have zero within-unit variation and vanish under demeaning. This is not a flaw; it's the price of eliminating omitted variable bias from time-invariant unobservables. Numerically, the within estimator is equivalent to including a separate dummy variable for every entity (Least Squares Dummy Variables, LSDV), but direct demeaning is far more computationally efficient when N is large.

The **identifying assumption** is strict exogeneity: the idiosyncratic error uᵢₜ must be uncorrelated with Xᵢₛ for all time periods s, not just the current one. Notice what this allows: αᵢ can be correlated with Xᵢₜ in any way — that's the whole point. But the time-varying residual must be uncorrelated with the regressors across all periods. This rules out anticipation effects (where units adjust X in response to future outcomes) and lagged dependent variable specifications (where a past Y on the right-hand side violates strict exogeneity).

A concrete example makes this tangible. Suppose you want to estimate how class size affects test scores using a panel of schools over several years. Wealthier schools have smaller classes and also score higher for unrelated reasons — classic omitted variable bias. The within transformation computes each school's deviation from its own mean class size and mean test score. You're now asking: in years when a particular school had unusually small classes relative to its own history, did it score unusually well? This comparison eliminates all fixed school characteristics — wealth, neighborhood, historical culture — that were biasing the OLS estimate. Only the within-school variation over time identifies β.
