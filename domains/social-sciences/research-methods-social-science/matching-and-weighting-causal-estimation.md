---
id: matching-and-weighting-causal-estimation
title: 'Matching, Stratification, and Weighting: Creating Comparable Groups'
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: propensity-score-methods
  type: hard
- id: causal-inference-from-observation
  type: soft
- id: probability-mass-functions
  type: soft
- id: optimization-multivariable-basics
  type: soft
tags:
- matching
- stratification
- weighting
- covariate-balance
stage: advanced
status: draft
---

# Matching, Stratification, and Weighting: Creating Comparable Groups

## Core Idea
Matching, stratification, and weighting create comparable groups by balancing covariate distributions between treated and control units. Propensity score methods use a summary of confounders for balance. These identify causal effects under unconfoundedness.

## Explainer

The core problem these methods address is one you already understand from causal inference: in observational data, treatment and control groups differ not just in their treatment status but in the background characteristics that led to treatment in the first place. People who receive a job training program tend to be more motivated than those who don't; countries that adopt a policy tend to differ systematically from those that don't. Naive comparisons produce **confounding bias** — the treatment effect is mixed up with the effect of these background differences. Matching, stratification, and weighting all attack this problem by constructing comparison groups that are as similar as possible to the treated group on observed confounders.

**Exact matching** is the most intuitive approach: for each treated unit, find a control unit with identical values on all confounders. A 45-year-old woman with a college degree who lives in a urban county gets matched to another 45-year-old woman with a college degree who lives in an urban county but did not receive treatment. The treatment effect estimate is the average difference in outcomes across matched pairs. The problem is the **curse of dimensionality** — with many confounders, exact matches become impossible because no two units share the same profile across ten or twenty variables. This is why propensity score methods, which you studied in your prerequisite, are so useful: they collapse all the confounders into a single number (the predicted probability of treatment), so matching on one dimension achieves approximate balance on all.

**Stratification** divides the sample into strata (blocks) with similar propensity scores and estimates the treatment effect within each stratum, then averages across strata. **Inverse probability weighting (IPW)** takes a different approach: rather than selecting matched pairs, it reweights the entire sample so that the covariate distribution in the control group resembles the treated group. Units in the control group who look like treated units receive high weights; those who don't look like treated units receive low weights. Both approaches rest on the same mathematical insight — that under **unconfoundedness** (all confounders observed and measured), the propensity score is sufficient to remove selection bias.

The assumptions underlying these methods deserve scrutiny. Unconfoundedness — also called **ignorability** or "no unmeasured confounders" — is the key identifying assumption, and it cannot be tested from the data itself. It requires that you have measured every variable that jointly influences treatment assignment and the outcome. In practice this means that these methods are only as good as your covariate set: variables you forgot to measure or cannot measure (parental motivation, employer discrimination) remain as unmeasured confounders. The other assumption is **overlap** (or common support) — for every value of the covariates, there must be some probability of being in either treatment or control. If a certain type of person *always* receives treatment and *never* doesn't, there is no valid counterfactual for them. Diagnostics like checking propensity score distributions and testing covariate balance after matching — not before — are how you evaluate whether these assumptions hold in practice and whether your comparison groups are genuinely comparable.


