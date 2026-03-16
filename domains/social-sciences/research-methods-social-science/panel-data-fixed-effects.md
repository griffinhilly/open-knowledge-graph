---
id: panel-data-fixed-effects
title: Fixed and Random Effects Models
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: longitudinal-data-analysis
  type: hard
- id: multilevel-modeling-hierarchical
  type: soft
- id: linear-regression
  type: hard
builds-toward:
- dynamic-panel-models
- system-gmm-estimators
tags:
- panel-methods
- causal
- confounding
- estimators
stage: advanced
status: draft
---

# Fixed and Random Effects Models

## Core Idea
Fixed-effects estimators use within-unit variation to identify causal effects while removing time-invariant confounds (e.g., personality, geographic characteristics). Random-effects models assume unit-level heterogeneity is uncorrelated with predictors, allowing estimation of between-unit and within-unit effects. The choice between fixed and random effects depends on research assumptions: fixed effects trades precision for robustness when time-invariant confounds are suspected.

## Explainer

You already know from linear regression that omitted variables bias coefficient estimates — if a variable is correlated with both your predictor and your outcome, and you leave it out, your estimate is wrong. From longitudinal data analysis, you know that panel data tracks the same units over time. Fixed-effects models exploit that panel structure to eliminate an entire category of omitted variable bias: everything about a unit that does not change over time.

To see why, imagine you want to estimate the effect of job training programs on earnings, using a dataset of workers observed over five years. The problem is that motivated workers might both seek out training and have higher earnings regardless. Motivation is a confound — and it is very hard to measure directly. A **fixed-effects** model handles this by, in effect, giving each worker their own intercept. The estimation is done entirely from *changes within each worker over time*. Did workers earn more in years when they had training compared to years when they did not? Motivation, ability, and every other stable individual characteristic cancel out because they affect all observations for that worker equally. What remains is the within-worker variation — the signal you actually want.

The mechanics translate to your regression knowledge: a fixed-effects model is equivalent to including a dummy variable for every unit (or equivalently, demeaning all variables by subtracting each unit's mean). The coefficient on your predictor of interest then captures the within-unit effect. The cost is that you cannot estimate effects of any variable that does not change within units — time-invariant variables like gender or country of birth are absorbed into the unit fixed effects and disappear from the estimation. You also need enough within-unit variation; if training status rarely changes for most workers, you have little data to identify the effect.

**Random effects** models take a different approach: they model the unit-level heterogeneity as a random variable drawn from a distribution, rather than estimating a separate parameter for each unit. This allows you to estimate effects of time-invariant variables and produces more precise estimates — but only if the unit-level heterogeneity is *uncorrelated* with your predictors. In the training example, that means assuming workers' motivation is unrelated to whether they receive training. If that assumption is wrong (and it usually is in social science), random effects estimates are biased in the same way as ordinary regression. The **Hausman test** formalizes this choice: it compares fixed and random effects estimates, and if they differ substantially, the random effects assumption is violated and fixed effects is preferred.

The deeper insight is that fixed effects is not really a "model" in the usual sense — it is a research design choice about which variation to use. By restricting attention to within-unit variation and discarding between-unit variation, you gain protection against a broad class of confounds at the cost of external generalizability. A fixed-effects estimate tells you what happened *within* observed units over time, not necessarily what would happen in a new unit. Understanding this scope condition — what the estimate does and does not represent — is as important as understanding how to run the estimator.
