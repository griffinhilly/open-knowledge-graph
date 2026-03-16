---
id: marginal-structural-models
title: Marginal Structural Models for Longitudinal Data
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: time-varying-confounders
  type: hard
- id: inverse-probability-weighting
  type: hard
tags:
- longitudinal-analysis
- marginal-models
- causal-inference
- time-varying-treatment
stage: advanced
status: draft
---

# Marginal Structural Models for Longitudinal Data

## Core Idea
Marginal structural models estimate causal effects of time-varying exposures on outcomes in the presence of time-varying confounding affected by prior exposure. MSMs use inverse probability weighting of observed outcomes on exposure history, producing marginal treatment effects analogous to those from a randomized experiment following the observed exposure pattern.

## Explainer

Marginal structural models solve a problem that trips up standard regression: what happens when a confounder is itself affected by prior treatment? You know from time-varying confounders that this structure creates a **causal feedback loop** — and you know from inverse probability weighting that we can rebalance covariates by reweighting observations. MSMs combine these two ideas into a unified framework for estimating causal effects of dynamic treatment regimes.

To see why standard regression fails, consider an HIV cohort where patients move on and off antiretroviral therapy (ART) over time, and CD4 count is measured at each visit. CD4 count is a time-varying confounder: lower CD4 predicts both *receiving* ART (doctors prescribe it when immune function drops) and *worse outcomes* (lower CD4 directly indicates disease progression). To control for confounding, you want to adjust for CD4. But CD4 is also affected by *prior* ART — treatment raises CD4 counts. If you condition on CD4 in a regression model, you are partially conditioning on the effect of prior treatment, which **blocks part of the causal pathway** you're trying to estimate. You can't include CD4 without bias, but you can't omit it without confounding. This is the dilemma that time-varying confounding affected by prior exposure creates, and it is not fixable with standard regression regardless of model complexity.

The **marginal structural model** solves this by constructing a **pseudo-population** in which treatment assignment is independent of measured confounders. The idea: assign each person at each time point a weight equal to the inverse of their probability of receiving the treatment they actually received, given their covariate history. A person with low CD4 who received ART (the "expected" treatment) gets a low weight; a person with high CD4 who received ART (counter to expectation) gets a high weight. In the weighted pseudo-population, CD4 no longer predicts treatment (because the weighting balances it), so it is no longer a confounder — it's as if the treatment were assigned randomly. You can now fit a simple regression model (the marginal structural model) in this weighted dataset and obtain a consistent estimate of the causal effect of the treatment regime. The word "marginal" refers to the fact that the model estimates effects **marginalized over** the distribution of confounders in the target population — not conditional on any specific confounder value, which is what standard models estimate.

Two practical concerns govern MSM implementation. First, **weight stabilization**: raw IPT weights can be highly variable (extreme weights for unusual treatment-covariate combinations), inflating variance. Stabilized weights (multiplying numerator and denominator by marginal treatment probabilities) reduce this problem substantially. Second, **positivity assumption**: IPT weighting requires that every combination of covariates and treatment history has nonzero probability of receiving either treatment. If there are covariate regions where doctors would never prescribe or never withhold treatment, the denominator probability approaches zero and weights explode — this is the practical version of the positivity violation you need to diagnose. Diagnostic checks (trimming weights at extreme percentiles, plotting weight distributions) are essential before trusting MSM results.
