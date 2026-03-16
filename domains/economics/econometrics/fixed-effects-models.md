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

## Explainer

The fundamental problem in observational social science is that units — people, firms, countries — differ in ways we cannot measure. A student's innate ability, a firm's management culture, a country's institutional quality: these unobserved characteristics correlate with both the treatment variable (education spending, investment policy, governance reform) and the outcome (test scores, productivity, growth). Standard OLS, which you know from the normal linear regression model, will attribute to the observed regressor variation that actually comes from these hidden differences. The **fixed effects estimator** sidesteps this problem by discarding all variation *between* units and exploiting only variation *within* units over time.

The mechanics follow directly from your work on panel data and dummy variables. You can think of fixed effects as adding a dummy variable for every unit in the panel. Each dummy absorbs that unit's permanent characteristics — its average level of the outcome that can't be explained by observed regressors. Equivalently (and computationally more efficient), you **demean** the data: subtract each unit's time-average from every observation. This "within transformation" leaves only the within-unit deviations. The coefficient on regressor X is then estimated purely from periods when X changed for a given unit — not from comparing units with high X to units with low X. Because unobserved unit heterogeneity (α_i) is constant within a unit, demeaning removes it exactly.

The price of this power is the loss of cross-sectional variation. If a variable never changes within a unit — gender, country of birth, founding year of a firm — it is perfectly collinear with the unit fixed effects and drops out entirely. You cannot estimate the level effect of something that doesn't vary over time for any unit. Two-way fixed effects extend the model by also demeaning across time periods, absorbing common shocks that affect all units simultaneously (like a recession or a global commodity price spike). This leaves only variation that is both within-unit and within-time-period — the residual after removing unit means and time means.

The Common Misconceptions section flags the most important caveat: fixed effects remove *time-invariant* bias, but not all bias. If the regressor changes within a unit for reasons that are themselves correlated with the error — for instance, firms that are doing well choose to invest more, so investment correlates with productivity shocks — within-unit variation is also contaminated. Fixed effects are not a magic cure; they are a specific solution to a specific form of omitted variable bias. They work when the unobserved confounders are stable attributes of the unit. When confounders change over time, you need additional strategies like instrumental variables or difference-in-differences designs that build on the fixed effects logic.
