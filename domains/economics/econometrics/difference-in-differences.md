---
id: difference-in-differences
title: Difference-in-Differences
domain: economics
course: econometrics
prerequisites:
- id: causal-inference-econometrics
  type: hard
- id: potential-outcomes-framework
  type: hard
- id: dummy-variables-regression
  type: hard
- id: fixed-effects-models
  type: soft
- id: selection-bias-econometrics
  type: soft
tags:
- DiD
- difference-in-differences
- parallel-trends
- policy-evaluation
stage: formal-systems
status: validated
---
# Difference-in-Differences

## Core Idea
Difference-in-differences (DiD) estimates causal treatment effects by comparing the pre-to-post change in the treatment group to the pre-to-post change in a comparison group. The estimator is β̂_DiD = (Ȳ_treated,post − Ȳ_treated,pre) − (Ȳ_control,post − Ȳ_control,pre), which differences out both pre-existing differences and aggregate time trends. The critical identifying assumption is parallel trends: in the absence of treatment, the treatment and control groups would have followed the same trajectory. This assumption is untestable at the exact period of treatment but is supported by showing parallel pre-trends in the data.

## How It's Best Learned
Replicate Card and Krueger's (1994) minimum wage study using New Jersey and Pennsylvania as treatment and control — this is the canonical DiD application in labor economics.

## Common Misconceptions
- Parallel trends is an assumption about counterfactual outcomes, not about the levels of outcomes before treatment — groups can differ in levels.
- With staggered treatment timing across units, simple two-way FE DiD can be biased; recent 'heterogeneous treatment effects' literature addresses this.
