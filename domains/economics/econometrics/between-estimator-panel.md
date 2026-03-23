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
status: validated
---

# Between and Random Effects Estimators for Panel Data

## Core Idea
The random effects estimator assumes unobserved heterogeneity is uncorrelated with regressors, treating the unit-specific effect as random. When this orthogonality condition holds, random effects is more efficient than fixed effects because it exploits both within-unit and between-unit variation; the between estimator uses only cross-sectional variation.

## Questions

```yaml
- question: "You are studying the effect of job training programs on wages using panel data. You suspect that workers who self-select into training are systematically more motivated — and motivation is unobserved but positively correlated with wages. Which estimator should you use?"
  type: multiple-choice
  options:
    - "The between estimator, since it uses cross-sectional differences between trained and untrained workers"
    - "The random effects estimator, which is more efficient than fixed effects"
    - "The within (fixed effects) estimator, which removes time-invariant unobserved heterogeneity including motivation"
    - "OLS on pooled data, since motivation averages out across the full sample"
  answer: 2
  explanation: "The motivation-wage correlation means the orthogonality assumption (αᵢ ⊥ Xᵢₜ) fails: the unobserved unit-specific component (motivation) is correlated with the regressor (training). Both the between estimator and random effects would be inconsistent in this case — they rely on cross-unit variation in training, which is confounded with cross-unit variation in motivation. The within estimator removes all time-invariant unit-level effects by demeaning, including the unobserved motivation component, isolating only within-worker variation in training over time. This is the key strength of fixed effects."

- question: "The between estimator for panel data is computed by:"
  type: multiple-choice
  options:
    - "Regressing each observation's deviation from its unit time-mean on the within-unit deviation of regressors"
    - "Running OLS on the time-averaged observations for each unit (group means)"
    - "Running OLS on first differences between consecutive time periods"
    - "Applying GLS weights that blend within- and between-unit variation"
  answer: 1
  explanation: "The between estimator collapses each unit's panel observations into a single row of time-averaged values (ȳᵢ, X̄ᵢ) and then runs OLS on those averages. The result is estimated entirely from cross-sectional variation — how units with higher average X differ from units with lower average X. This is the 'opposite' of fixed effects: where fixed effects removes between-unit variation by demeaning, the between estimator uses only between-unit variation and discards the within-unit time-series information entirely."

- question: "The random effects estimator is more efficient than fixed effects when the unit-specific effect is uncorrelated with all regressors."
  type: true-false
  answer: true
  explanation: "When αᵢ ⊥ Xᵢₜ holds, both fixed effects and random effects are consistent, but random effects uses more information. Fixed effects discards all between-unit variation (by demeaning), throwing away valid identifying variation. Random effects uses GLS to optimally combine both within- and between-unit variation, producing more precise estimates. The efficiency gain is real and can be substantial when between-unit variation is large — but it disappears entirely if the orthogonality assumption fails."

- question: "If random effects and fixed effects produce very similar coefficient estimates, this is evidence that the orthogonality assumption (αᵢ ⊥ Xᵢₜ) has likely failed."
  type: true-false
  answer: false
  explanation: "This is the reverse of the correct logic. The Hausman test detects failure of the orthogonality assumption by asking whether random effects and fixed effects estimates are *statistically different*. When the assumption holds, both estimators are consistent and should converge to similar values — similar estimates are evidence the assumption is satisfied. A large, statistically significant difference between the two estimates is the warning sign that random effects may be inconsistent and fixed effects should be trusted."

- question: "Explain the trade-off between random effects and fixed effects estimators. Under what condition does random effects fail, and why does fixed effects remain valid in that case?"
  type: short-answer
  answer: "Random effects assumes the unit-specific effect αᵢ is uncorrelated with all regressors (αᵢ ⊥ Xᵢₜ). When this holds, random effects uses GLS to blend within- and between-unit variation, yielding more efficient estimates than fixed effects. When the assumption fails — when unobserved unit characteristics are correlated with the regressors (e.g., unobserved firm quality correlated with investment) — random effects is inconsistent, meaning its estimates are biased even in large samples. Fixed effects remains valid because it eliminates αᵢ entirely by demeaning: the within transformation ÿᵢₜ = yᵢₜ − ȳᵢ removes all time-invariant unit-level variation, including the unobserved correlated component. The cost is that you lose all information from cross-unit differences and cannot estimate coefficients on time-invariant regressors."
  explanation: "The trade-off is efficiency vs. robustness. Random effects wins on efficiency (uses more variation) but requires a strong assumption. Fixed effects is more robust (doesn't require the orthogonality assumption) but wastes potentially valid identifying variation. The Hausman test helps choose between them empirically."
```

## Explainer

When you learned the within estimator (fixed effects), you demean each unit's observations over time, stripping out all time-invariant variation — including everything you can't observe about each unit. That is exactly its strength when unobserved heterogeneity might bias estimates, but also its cost: you throw away all the information in cross-unit differences. The **between estimator** makes the opposite bet. It collapses each unit's data to a single time-averaged observation and runs OLS on those group means. The result is estimated entirely from variation *across* units — how much, on average, do units with higher X differ from units with lower X?

The **random effects estimator** occupies the middle ground. Rather than eliminating unit-specific effects (within) or ignoring them (between), random effects assumes the unit-specific component αᵢ is a random draw from a distribution that is *uncorrelated* with all regressors. Under this assumption, αᵢ is just another part of the error term, and you can use Generalized Least Squares (GLS) to combine within- and between-variation optimally. The GLS weighting θ determines how much between-variation to use: when within-variation is relatively informative, θ is large and random effects resembles fixed effects; when between-variation is informative, θ is smaller and the estimator draws more from cross-unit differences.

The efficiency gain from random effects over fixed effects is real but conditional. Think of it as a bet: random effects stakes its unbiasedness on the orthogonality assumption αᵢ ⊥ Xᵢₜ. If that assumption holds — say you're studying outcomes across hospitals where hospital-level effects are plausibly random with respect to your covariates — you get more precise estimates by not throwing away between-unit information. If the assumption fails — say unobserved firm quality is correlated with the firm's investment choices — random effects is inconsistent while fixed effects remains valid.

This is precisely why the Hausman test is the natural follow-up to this topic. Under the null hypothesis that αᵢ ⊥ Xᵢₜ, both fixed effects and random effects are consistent, but random effects is more efficient. Under the alternative, fixed effects is consistent and random effects is not. The Hausman test formalizes this comparison by asking: are the coefficient estimates from the two methods statistically distinguishable? A significant difference signals that the orthogonality assumption has failed, and you should trust fixed effects. Understanding the between estimator as its own object — not just a failed version of fixed effects — sharpens your intuition for what the Hausman test is actually detecting.
