---
id: panel-data-basics
title: 'Panel Data: Structure and Advantages'
domain: economics
course: econometrics
prerequisites:
- id: multiple-regression-model
  type: hard
- id: endogeneity
  type: hard
- id: robust-standard-errors
  type: soft
- id: linear-algebra
  type: hard
- id: expected-value-theory
  type: soft
builds-toward:
- fixed-effects-models
- random-effects-models
tags:
- panel-data
- longitudinal
- repeated-measures
- unobserved-heterogeneity
stage: formal-systems
status: validated
---
# Panel Data: Structure and Advantages

## Core Idea
Panel data (longitudinal data) tracks the same units (individuals, firms, countries) over multiple time periods, producing observations indexed by both unit i and time t. This two-dimensional structure allows researchers to control for time-invariant unobserved characteristics (individual fixed effects) that would cause omitted variable bias in cross-sectional regressions. The key decomposition is y_it = α_i + x_it'β + u_it, where α_i captures all stable unit-specific factors. Panels can be balanced (all units observed every period) or unbalanced (missing observations). The Hausman test helps decide between fixed and random effects specifications.

## How It's Best Learned
Contrast the cross-sectional and panel estimates of the effect of union membership on wages — the panel estimate, controlling for worker fixed effects, is typically much smaller, illustrating that high-ability workers disproportionately select into unions.

## Common Misconceptions
- Panel data does not solve all endogeneity problems — only time-invariant confounders are absorbed by fixed effects; time-varying omitted variables remain a problem.
- A longer panel (more time periods) is not always better than a wider panel (more units) — the optimal dimension depends on the variation needed for identification.

## Explainer

Cross-sectional regression has a fundamental weakness you encountered in endogeneity: if the units you observe differ in some stable, unobserved way that also correlates with your treatment variable, your estimates are biased. Imagine estimating the wage premium for union membership. Union workers may systematically be higher-ability workers who would have earned more regardless. A cross-sectional regression comparing union and non-union workers cannot separate the union premium from selection — workers with better outside options may be more likely to join and also to negotiate higher wages. **Panel data** offers a different strategy: instead of comparing different people, compare the *same person to themselves* over time.

The model y_it = α_i + x_it'β + u_it formalizes this. The **individual fixed effect** α_i absorbs everything stable about person i — ability, family background, temperament, personality — regardless of whether you can measure any of it. Because α_i is constant over time, it cancels out when you look at changes within the same person. If you observe a worker before and after joining a union, their unobserved ability shows up identically in both observations and drops out of the comparison. What remains is the within-person variation in x_it (union status changed) and the within-person variation in y_it (wages changed), isolating the effect of the treatment from the stable confounders.

The two-dimensional structure (units i and time periods t) gives panel data its power through the decomposition of variation. Total variation in the data has two components: **between variation** (differences across units, like comparing different people) and **within variation** (differences within the same unit over time, like one person's changes). Fixed effects estimation uses only the within variation, making it immune to bias from time-invariant omitted variables — the α_i terms are eliminated. This is why the within estimator can be understood as applying OLS to the demeaned data: subtract each unit's time-average from every observation, and the fixed effects disappear.

The Hausman test helps navigate a fundamental choice: should α_i be treated as fixed parameters to be estimated (a **fixed effects** model), or as random draws from a population distribution that are uncorrelated with x_it (a **random effects** model)? Random effects is more efficient — it uses both within and between variation — but requires the strong assumption that the individual effects are uncorrelated with the regressors. If that assumption fails (the usual case when you're worried about omitted variable bias), random effects is inconsistent and fixed effects is required. The Hausman test checks whether the two estimates differ significantly, which would indicate that the random effects assumption is violated. Finally, note the key misconception: fixed effects removes time-invariant confounders, but time-*varying* omitted variables still cause bias — a promotion decision that precedes both union joining and wage growth would still confound your estimate even with panel data.
