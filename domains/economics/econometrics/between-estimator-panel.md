---
id: between-estimator-panel
title: Between and Random Effects Estimators for Panel Data
domain: economics
course: econometrics
prerequisites:
- id: within-estimator-panel
  type: hard
- id: random-effects-models
  type: hard
builds-toward:
- hausman-specification-test
tags:
- panel-data
- random-effects
- between
stage: formal-systems
status: draft
---

# Between and Random Effects Estimators for Panel Data

## Core Idea
The random effects estimator assumes unobserved heterogeneity is uncorrelated with regressors, treating the unit-specific effect as random. When this orthogonality condition holds, random effects is more efficient than fixed effects because it exploits both within-unit and between-unit variation; the between estimator uses only cross-sectional variation.

## Explainer

When you learned the within estimator (fixed effects), you demean each unit's observations over time, stripping out all time-invariant variation — including everything you can't observe about each unit. That is exactly its strength when unobserved heterogeneity might bias estimates, but also its cost: you throw away all the information in cross-unit differences. The **between estimator** makes the opposite bet. It collapses each unit's data to a single time-averaged observation and runs OLS on those group means. The result is estimated entirely from variation *across* units — how much, on average, do units with higher X differ from units with lower X?

The **random effects estimator** occupies the middle ground. Rather than eliminating unit-specific effects (within) or ignoring them (between), random effects assumes the unit-specific component αᵢ is a random draw from a distribution that is *uncorrelated* with all regressors. Under this assumption, αᵢ is just another part of the error term, and you can use Generalized Least Squares (GLS) to combine within- and between-variation optimally. The GLS weighting θ determines how much between-variation to use: when within-variation is relatively informative, θ is large and random effects resembles fixed effects; when between-variation is informative, θ is smaller and the estimator draws more from cross-unit differences.

The efficiency gain from random effects over fixed effects is real but conditional. Think of it as a bet: random effects stakes its unbiasedness on the orthogonality assumption αᵢ ⊥ Xᵢₜ. If that assumption holds — say you're studying outcomes across hospitals where hospital-level effects are plausibly random with respect to your covariates — you get more precise estimates by not throwing away between-unit information. If the assumption fails — say unobserved firm quality is correlated with the firm's investment choices — random effects is inconsistent while fixed effects remains valid.

This is precisely why the Hausman test is the natural follow-up to this topic. Under the null hypothesis that αᵢ ⊥ Xᵢₜ, both fixed effects and random effects are consistent, but random effects is more efficient. Under the alternative, fixed effects is consistent and random effects is not. The Hausman test formalizes this comparison by asking: are the coefficient estimates from the two methods statistically distinguishable? A significant difference signals that the orthogonality assumption has failed, and you should trust fixed effects. Understanding the between estimator as its own object — not just a failed version of fixed effects — sharpens your intuition for what the Hausman test is actually detecting.
