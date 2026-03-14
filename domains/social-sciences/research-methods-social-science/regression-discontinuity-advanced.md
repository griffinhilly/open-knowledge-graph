---
id: regression-discontinuity-advanced
title: Advanced Regression Discontinuity Design
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: regression-discontinuity-sharp-fuzzy
  type: hard
- id: causal-inference-observational-data
  type: soft
builds-toward:
- multi-dimensional-rdd
- spatial-discontinuity
tags:
- regression-discontinuity
- quasi-experimental
- causal
- nonparametric
stage: advanced
status: draft
---

# Advanced Regression Discontinuity Design

## Core Idea
Regression discontinuity design exploits threshold rules in policy assignment to estimate causal effects. When eligibility for treatment depends on crossing a cutoff (income threshold, test score, age), units just above and below the threshold are comparable except for treatment status. RDD requires no assumption of ignorability; instead, identification relies on the assumption that other determinants of the outcome vary smoothly across the threshold. Advanced RDD addresses multiple thresholds, bandwidth selection, and validity checks (density tests, covariate continuity).
