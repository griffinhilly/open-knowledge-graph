---
id: inverse-probability-weighting
title: Inverse Probability Weighting
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: propensity-score-analysis
  type: hard
- id: stratification-and-adjustment
  type: soft
builds-toward:
- marginal-structural-models
- g-estimation-causal-effects
tags:
- causal-inference
- confounding
- weighting
- marginal-effects
stage: advanced
status: draft
---

# Inverse Probability Weighting

## Core Idea
Inverse probability weighting (IPW) constructs weights so that the weighted sample is pseudo-randomized with respect to measured confounders. IPW directly produces marginal (population-average) treatment effects and is particularly useful for survival and time-to-event analyses where standard adjustment would be biased.

## Explainer

From your study of propensity score analysis, you know that the core challenge in observational research is that treatment assignment is not random — sicker patients get different treatments than healthier ones, and that confounding distorts naive comparisons. Propensity scores summarize this imbalance by estimating each person's probability of receiving treatment given their measured covariates. **Inverse probability weighting** uses those probabilities differently from matching or stratification: instead of discarding or subgrouping observations, it reweights every observation to create a synthetic sample where treatment looks as if it had been assigned independently of measured confounders.

The intuition is borrowed from survey sampling, a field you may recognize from your study of stratification and adjustment. In a stratified survey, respondents from undersampled strata are upweighted to make the sample representative. IPW applies the same logic to treatment groups: someone who received treatment despite a low predicted probability of doing so is unusual among treated people, so they receive a high weight — they are "lending" their contribution to the comparison. Someone who received treatment with very high predicted probability is unremarkable and receives a low weight. After weighting, the distribution of covariates is balanced between treated and untreated groups, mimicking what would happen in a randomized trial. The weighted estimator then simply takes weighted means in each group and differences them.

The resulting effect estimate is a **marginal treatment effect** — averaged over the entire population distribution of covariates, not conditional on holding specific covariates fixed as in regression adjustment. This distinction matters practically: a conditional effect (from a regression model) asks "what is the effect for a person with covariate values X?" A marginal effect asks "what would the average outcome be if we gave everyone the treatment versus no one?" For clinical and policy decisions — what happens at the population level — the marginal effect is often the target of interest.

The key vulnerability of IPW is **weight instability**. When some individuals have propensity scores near 0 or 1 — meaning their treatment was nearly deterministic — their inverse probability weights become very large. A handful of observations with extreme weights can dominate the analysis and inflate variance dramatically. Stabilized weights (multiplying the raw weight by the marginal probability of treatment in the overall population) reduce this instability without introducing bias. Checking the weight distribution — plotting it, examining the maximum, and verifying that no small group of observations carries disproportionate influence — is a required diagnostic step. IPW also inherits the propensity score's limitation: it only adjusts for *measured* confounders. If important confounders are unmeasured, the pseudo-randomization is incomplete, and bias persists regardless of how well the weights balance observed covariates.
