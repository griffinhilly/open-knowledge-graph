---
id: fixed-effects-models
title: Fixed Effects Models
domain: economics
course: econometrics
prerequisites:
- id: panel-data-basics
  type: hard
- id: dummy-variables-regression
  type: hard
- id: linear-algebra
  type: hard
builds-toward:
- random-effects-models
- difference-in-differences
tags:
- fixed-effects
- within-estimator
- demeaning
- panel
stage: formal-systems
status: validated
---

# Fixed Effects Models

## Core Idea
The fixed effects (FE) estimator eliminates time-invariant unobserved heterogeneity by transforming the data so that unit means are removed — the 'within' transformation: ÿ_it = y_it − ȳᵢ. Regressing demeaned outcomes on demeaned regressors uses only within-unit variation over time, making α_i irrelevant. Equivalently, FE adds a dummy variable for each unit. Because FE uses only within-unit variation, it cannot estimate the effects of time-invariant regressors (e.g., gender, race). Two-way fixed effects adds time fixed effects, controlling for aggregate shocks common to all units.

## How It's Best Learned
Manually demean a small panel dataset and run OLS on the demeaned data — verify the results match software FE output. Then try including a time-invariant variable and see that it perfectly collinears with unit dummies.

## Common Misconceptions
- Fixed effects do not eliminate all bias — if the regressor changes within units for endogenous reasons (e.g., wage increases causing workers to move), FE still produces biased estimates.
- FE 'controls for' unobservables in the sense of absorbing them; it does not estimate them.
