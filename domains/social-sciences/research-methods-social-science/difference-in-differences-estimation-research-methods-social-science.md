---
id: difference-in-differences-estimation-research-methods-social-science
title: Difference-in-Differences Estimation
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: causal-inference-observational-data
  type: hard
- id: linear-regression-social-science
  type: hard
- id: partial-derivatives
  type: soft
- id: optimization-multivariable-basics
  type: soft
- id: limit-laws
  type: soft
- id: conditional-expectation
  type: soft
tags:
- difference-in-differences
- policy-evaluation
- parallel-trends
- natural-experiments
stage: advanced
status: draft
---

# Difference-in-Differences Estimation

## Core Idea
Develops the difference-in-differences estimator for evaluating natural experiments where policy changes affect groups at different times. Covers parallel trends assumption, event study designs, variations for multiple groups and time periods, and robustness checks.

## How It's Best Learned
Design a DD analysis with real policy variation, create event study plots, test parallel trends assumption, conduct robustness checks with alternative specifications.

## Common Misconceptions
- Parallel trends can be tested with pre-treatment data
- DD requires equal group sizes
- Multiple staggered treatments simplify estimation

## Explainer

The **difference-in-differences (DiD)** estimator is a strategy for extracting a causal effect from observational data when a natural experiment creates two groups: one that experienced a policy change and one that did not. You already know from your prerequisite work on causal inference that the fundamental problem is constructing a credible counterfactual — what would have happened to the treated group if they hadn't been treated? DiD solves this by using the control group's trajectory as a substitute for that counterfactual.

The logic works through a double subtraction. First, compare the treated group before and after treatment: this captures the treatment effect but also any time trends unrelated to the policy. Second, make the same before-after comparison for the untreated control group: this captures those background time trends in isolation. Subtracting the second difference from the first removes the confounding time trend and leaves (approximately) the treatment effect. Formally: DiD = (treated_after − treated_before) − (control_after − control_before). The intuition is that the control group serves as a "temperature gauge" — it tells you how much the treated group would have changed anyway.

The critical assumption underlying the entire approach is **parallel trends**: absent the treatment, the treated and control groups would have followed the same trajectory over time. This cannot be directly verified for the post-treatment period (you don't observe the counterfactual), but you can assess its plausibility using **pre-treatment data**. If the two groups had similar trends before the policy changed, that increases confidence they would have continued similarly. An **event study design** plots the treatment effect at each time period — if pre-treatment estimates are near zero and post-treatment estimates diverge, parallel trends looks credible. Be precise about what this test does and doesn't prove: passing a pre-trend test supports the assumption but doesn't guarantee it; a divergence in pre-trends is a red flag, not a definitive refutation.

Modern DiD analysis has grown considerably more complex with **staggered adoption designs**, where different units receive treatment at different times. Contrary to intuition, this does not simplify estimation — it creates subtle bias problems when effects are heterogeneous across cohorts and time periods. Standard two-way fixed effects regression (unit and time fixed effects) was long the workhorse estimator for staggered DiD, but recent methodological work has shown it can produce badly misleading estimates when treatment effects vary. Newer estimators by Callaway-Sant'Anna, Sun-Abraham, and others construct clean comparisons using not-yet-treated units as controls. The key practical lesson: when your treatment rolled out across units at different times, use a modern staggered DiD estimator rather than a naive regression, and report event study plots to make your identifying assumptions visible.
