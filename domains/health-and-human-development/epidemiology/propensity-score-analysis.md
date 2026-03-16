---
id: propensity-score-analysis
title: Propensity Score Analysis
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: confounding-epidemiology
  type: hard
- id: multivariable-regression-epi
  type: hard
builds-toward:
- inverse-probability-weighting
- g-estimation-causal-effects
tags:
- causal-inference
- confounding
- observational-studies
stage: advanced
status: draft
---

# Propensity Score Analysis

## Core Idea
Propensity score analysis estimates the probability that an individual receives an exposure conditional on observed confounders. By matching, stratifying, or weighting on propensity scores, analysts can simulate randomization and reduce confounding bias in observational studies without explicitly adjusting for every confounder.

## How It's Best Learned
Start with a simple observational dataset and manually calculate propensity scores using logistic regression, then compare crude vs. adjusted estimates. Practice with real data using matching and weighting approaches in sequence.

## Common Misconceptions
- Propensity scores eliminate all confounding (they only control measured confounders). - Using propensity scores requires 1:1 matching (matching is one option; weighting and stratification are alternatives). - Overlap/common support is not required (perfect overlap is ideal but not always necessary).

## Explainer

From your study of confounding and multivariable regression, you know the core problem in observational research: people who receive an exposure are systematically different from those who do not, and those differences — not the exposure itself — may explain the outcome. In a randomized trial, random assignment ensures that exposed and unexposed groups are on average identical on every measured and unmeasured characteristic. Propensity score analysis is an attempt to approximate that balance in observational data — but only for measured confounders.

The **propensity score** is the predicted probability that a subject received the exposure, given their observed covariates. You estimate it using logistic regression: outcome = exposure (1/0), predictors = all measured confounders (age, sex, comorbidities, socioeconomic status, etc.). The output is a single number between 0 and 1 for each subject. The intuition: two subjects with the same propensity score have the same probability of being exposed given their measured characteristics, so any actual difference in their exposure status looks like it could have been random. Conditioning on the propensity score therefore mimics randomization on the measured covariates — it "balances" the groups without requiring you to model the relationship between each individual confounder and the outcome.

There are three main implementation strategies. **Propensity score matching** pairs each exposed subject with one (or more) unexposed subjects who have a similar propensity score, then analyzes only the matched set. This is intuitive and produces a balanced sample but discards unmatched subjects, potentially reducing precision and generalizability. **Inverse probability weighting (IPW)** keeps all subjects but up-weights those whose treatment assignment was "surprising" (an exposed person with low propensity, or an unexposed person with high propensity). This creates a pseudo-population in which exposure is independent of the confounders, and you analyze it as if it were a randomized trial. **Stratification** divides subjects into quantiles of propensity score (typically quintiles) and estimates the exposure effect within each stratum, then pools. All three approaches require checking **balance** after adjustment — the measured confounders should be similar between groups within propensity score strata. Standardized mean differences are the standard check; a successful analysis should show differences near zero for all covariates.

The key limitation to internalize: propensity scores control only **measured** confounders. Unmeasured confounders remain unaddressed, just as in conventional regression. Propensity scores are not a substitute for randomization — they are a more transparent and sometimes more flexible tool for covariate adjustment than outcome regression, but they make the same identifying assumption: **no unmeasured confounding** (also called exchangeability or ignorability). Where propensity scores offer a genuine advantage over regression is in situations with many covariates relative to outcomes (where outcome models can overfit), or when the researcher wants to separate the "design" stage (building the balanced comparison groups) from the "analysis" stage (estimating effects), improving transparency about which decisions were made before examining outcomes. Understanding these tradeoffs prepares you for the more general methods — instrumental variables, g-estimation, and doubly robust estimators — that build directly on propensity score foundations.
