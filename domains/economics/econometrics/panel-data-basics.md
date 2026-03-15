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
