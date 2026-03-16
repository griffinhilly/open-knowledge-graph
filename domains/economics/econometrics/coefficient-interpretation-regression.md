---
id: coefficient-interpretation-regression
title: Interpreting Regression Coefficients
domain: economics
course: econometrics
prerequisites:
- id: multiple-regression-model
  type: hard
- id: logarithms-intro
  type: soft
builds-toward:
- hypothesis-testing-regression
- dummy-variables-regression
tags:
- interpretation
- log-linear
- elasticity
- ceteris-paribus
stage: formal-systems
status: validated
---

# Interpreting Regression Coefficients

## Core Idea
The interpretation of a regression coefficient depends on the functional form. In a level-level model (y on x), β₁ gives the change in y per unit change in x. In a log-level model (log y on x), 100·β₁ gives the approximate percentage change in y per unit change in x. In a log-log model, β₁ is the elasticity — the percentage change in y per 1% change in x. Dummy variable coefficients compare a group mean to the omitted reference group, holding other covariates constant. Correct interpretation always includes the ceteris paribus qualifier.

## How It's Best Learned
Practice translating coefficient estimates into plain-language economic statements across different functional forms. The wage-education regression in log form is a canonical exercise.

## Common Misconceptions
- A coefficient of 0.05 in a log-level regression means a 5 percentage point change, not a 5% change — the distinction matters for large effects.
- Standardized beta coefficients answer a different question than raw coefficients; mixing them up leads to incorrect comparisons.

## Explainer

You already know that a multiple regression coefficient captures the relationship between one regressor and the outcome after holding all other regressors constant — the **ceteris paribus** effect. Now the question is: what units is that effect expressed in? The answer depends entirely on how you have transformed your variables, and getting this wrong turns a correct regression into a meaningless number.

In a **level-level model** — both Y and X in their natural units — the coefficient β₁ is the simplest case: a one-unit increase in X is associated with a β₁-unit change in Y. If wages (in dollars per hour) are regressed on years of education, a coefficient of 1.50 means an additional year of education predicts $1.50 more per hour. Straightforward. The level-level model is the right baseline interpretation to understand before the log transformations.

Log transformations change the units from levels to percentages, which is often more natural for economic variables that grow proportionally. In a **log-level model** (log Y on X, X still in levels), the coefficient β₁ means that a one-unit increase in X is associated with approximately a 100·β₁ percent change in Y. If log wages are regressed on years of education and β₁ = 0.08, then each additional year of schooling raises wages by roughly 8%. This approximation is exact for small changes but overstates the true percentage for large β values. In a **log-log model** (both in logs), β₁ is the **elasticity**: a 1% increase in X is associated with a β₁ percent change in Y. Log-log models appear constantly in demand analysis precisely because elasticity is the natural unit there.

**Dummy variable** coefficients follow the level-level rule but have a specific meaning: the coefficient compares the group mean of the dummy-coded group to the **reference group** (the omitted category), holding everything else constant. If you include a Female indicator in a wage regression and the coefficient is −0.12 in a log-level model, this says women earn approximately 12% less than men after controlling for the other variables in the model. The choice of reference group is arbitrary but affects which comparisons are directly readable from the output. Every interpretation must end with "holding other covariates constant" — without that qualifier, you are not reading a ceteris paribus effect; you are reading something else entirely.
