---
id: regression-discontinuity-design
title: Regression Discontinuity Design
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: epidemiologic-study-designs
  type: hard
- id: multivariable-regression-epi
  type: hard
tags:
- quasi-experimental
- natural-experiments
- causal-inference
stage: advanced
status: draft
---

# Regression Discontinuity Design

## Core Idea
Regression discontinuity design (RDD) exploits a sharp cutoff or threshold in treatment assignment (e.g., treatment given above but not below a score cutoff) to estimate causal effects by comparing outcomes just above and below the threshold. It avoids selection bias when assignment is deterministic at the cutoff and provides internally valid causal estimates for the local population at the discontinuity boundary. RDD is a quasi-experimental method that does not require randomization.

## How It's Best Learned
Analyze real examples with natural cutoffs (age eligibility rules, school starting age cutoffs); visualize outcomes as a function of the running variable.

## Common Misconceptions
RDD provides global treatment effects applicable to all subgroups. Fuzzy RDD assumes perfect compliance (probabilistic assignment is common).
