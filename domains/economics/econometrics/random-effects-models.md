---
id: random-effects-models
title: Random Effects Models
domain: economics
course: econometrics
prerequisites:
- id: fixed-effects-models
  type: hard
tags:
- random-effects
- GLS
- Hausman-test
- panel
stage: formal-systems
status: validated
---

# Random Effects Models

## Core Idea
The random effects (RE) model treats the unit-specific component α_i as a random variable drawn from a distribution, rather than a fixed unknown parameter. RE estimation uses Generalized Least Squares (GLS), which exploits both within-unit and between-unit variation, yielding more efficient estimates than FE when the key assumption holds: the individual effect α_i must be uncorrelated with the regressors. Unlike FE, RE can estimate the effects of time-invariant covariates. The Hausman test compares FE and RE estimates — a significant difference indicates the RE assumption is violated and FE is preferred.

## How It's Best Learned
Apply the Hausman test to a panel dataset, interpret the test result, and explain why FE is preferred when the null is rejected. Understanding what 'correlation between α_i and x_it' means economically is the key insight.

## Common Misconceptions
- Random effects does not mean the effects are random in a colloquial sense — it is a modeling assumption about the distribution of unit heterogeneity.
- The Hausman test rejects the null when RE is inconsistent, but a failure to reject does not guarantee RE is correct — it may just be low-powered.

## Explainer

You already know fixed effects (FE) models, which handle unit heterogeneity by absorbing α_i — the stable, unobserved characteristics of each unit — as unit-specific constants that get differenced away. FE is consistent regardless of whether those unobserved characteristics are correlated with your regressors, and that is its great virtue. Its great cost is that it discards all between-unit variation and cannot estimate coefficients on time-invariant variables (like a country's legal system or a person's gender). The **random effects model** is the alternative that attempts to recover that lost efficiency and information, at the price of an additional assumption.

Where FE treats α_i as a fixed constant to be estimated, RE treats it as a **random draw from a distribution** — specifically, as part of a composite error term vᵢₜ = α_i + uᵢₜ. Because α_i is now in the error, the estimator uses **Generalized Least Squares (GLS)**, which accounts for the fact that observations on the same unit share a common component (α_i) and are therefore correlated. GLS is more efficient than OLS or the within-estimator when the model is correctly specified, using both the variation within units over time and the variation between units across the sample.

The critical assumption that unlocks this efficiency gain is that **α_i is uncorrelated with all regressors**. Think about what this requires economically. If you are studying wages and include education as a regressor, RE assumes that unobserved individual ability (the α_i) is uncorrelated with education. That is a strong claim — more able people typically get more education, so ability and education are correlated. When this assumption fails, the RE estimator is inconsistent for the same reason that omitting a variable correlated with the regressor biases OLS. FE does not make this assumption and remains consistent.

The **Hausman test** operationalizes this comparison. Under the null hypothesis, RE is correctly specified — α_i is uncorrelated with regressors — and both FE and RE estimates converge to the same true parameter, but RE is more efficient. Under the alternative, RE is misspecified and its estimates are biased, while FE remains consistent. The test statistic measures the systematic divergence between the two estimators: if they differ substantially, RE is likely picking up correlated heterogeneity and FE should be preferred. A practical heuristic: use FE when you are worried about unobserved individual characteristics influencing your regressors (most economic applications involving people or firms), and use RE when panel structure is primarily a statistical efficiency consideration and unit effects are plausibly independent of the covariates.
