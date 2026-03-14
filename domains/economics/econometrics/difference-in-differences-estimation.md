---
id: difference-in-differences-estimation
title: 'Difference-in-Differences: Estimation and Interpretation'
domain: economics
course: econometrics
prerequisites:
- id: difference-in-differences
  type: hard
- id: multiple-regression-model
  type: hard
builds-toward:
- parallel-trends-assumption-validity
tags:
- causal-inference
- difference-in-differences
- treatment-effects
stage: formal-systems
status: draft
---

# Difference-in-Differences: Estimation and Interpretation

## Core Idea
DD estimates the causal treatment effect by comparing outcome changes before-after in treated vs. control groups: DD = (Yₜ_treat - Ypre_treat) - (Yₜ_control - Ypre_control). This double-difference eliminates common time trends and time-invariant group differences, yielding unbiased treatment effect under parallel trends.
