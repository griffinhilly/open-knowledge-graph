---
id: sharp-regression-discontinuity-design
title: Sharp Regression Discontinuity Design
domain: economics
course: econometrics
prerequisites:
- id: regression-discontinuity
  type: hard
- id: causal-inference-econometrics
  type: hard
builds-toward:
- fuzzy-regression-discontinuity-design
tags:
- causal-inference
- regression-discontinuity
- local-treatment
stage: formal-systems
status: draft
---

# Sharp Regression Discontinuity Design

## Core Idea
In sharp RDD, treatment is a deterministic function of a running variable cᵢ, with discontinuous assignment at threshold c*. The causal effect is the discontinuity in E[Y|cᵢ] at c*. Nonparametric local regression near the cutoff or global polynomial fitting identifies this effect under continuity of potential outcomes.
