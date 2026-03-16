---
id: stratification-and-adjustment
title: Stratified Analysis and Adjustment for Confounding
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: confounding-epidemiology
  type: hard
- id: effect-modification-interaction
  type: soft
builds-toward:
- multivariable-regression-epi
tags:
- confounder-control
- stratification
- mantel-haenszel
stage: advanced
status: draft
---

# Stratified Analysis and Adjustment for Confounding

## Core Idea
Stratified analysis divides data by levels of a confounder to examine the exposure-outcome association within homogeneous strata, then combines stratum-specific estimates (e.g., via Mantel-Haenszel). This approach allows simultaneous control of confounding and detection of effect modification. Stratification is transparent and interpretable but becomes cumbersome with multiple confounders.

## Explainer

You already understand confounding: a variable associated with both the exposure and the outcome distorts the apparent exposure–outcome relationship. The intuitive fix is simple — look at the exposure–outcome association *separately* within groups that are homogeneous with respect to the confounder. Within each stratum, the confounder cannot confound because it does not vary. If the crude (unstratified) association differs from the stratum-specific associations, confounding was present and the stratum-specific estimates are the valid ones.

To make this concrete: suppose you observe a crude odds ratio of 2.0 for the association between coffee drinking and myocardial infarction (MI). But coffee drinkers also smoke more than non-drinkers. When you stratify by smoking status, you find an odds ratio of 1.0 in smokers and 1.0 in non-smokers. The stratum-specific estimates are homogeneous (both null) and differ from the crude estimate — classic positive confounding. Smoking was making coffee look harmful because it was associated with both the exposure (coffee) and the outcome (MI). Within strata of smoking status, that distortion disappears.

If the stratum-specific estimates are similar across strata, you can combine them into a single summary estimate that is adjusted for the stratifying variable. The **Mantel-Haenszel (MH) estimator** is the standard approach for 2×2 tables: it computes a weighted average of stratum-specific odds ratios (or risk ratios), where the weights reflect the amount of information in each stratum. The MH estimator is computationally simple, statistically efficient when homogeneity holds, and interpretable as the confounder-adjusted association. You can also use the **Woolf method** (variance-based weighting) as an alternative.

The same analysis that controls for confounding also detects **effect modification**: if stratum-specific estimates *differ* substantially across strata, the variable you stratified on is not merely a confounder — it is a modifier of the exposure effect. For example, if the coffee–MI odds ratio is 2.0 among smokers but 0.8 among non-smokers, the effect is genuinely different in the two groups. In this case, combining the estimates into a single adjusted summary would be misleading — the correct report is stratum-specific. The decision to report separate estimates versus a combined estimate hinges on whether heterogeneity is present. This is why stratified analysis is not merely a confounding-control tool but also the foundational method for identifying who benefits or is harmed differently — a question central to clinical and public health decision-making.

Stratification's limitation is the **sparse data problem**: each additional stratifying variable divides the dataset into more cells, many of which may have too few observations to produce stable estimates. Two binary confounders require four strata; three binary confounders require eight. This is why stratification gives way to multivariable regression — logistic, Poisson, Cox — when there are several confounders to control simultaneously. Regression can be understood as a generalization of stratification that handles sparse data through model-based smoothing, trading the transparency of stratification for the capacity to adjust for many variables at once.
