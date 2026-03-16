---
id: longitudinal-data-analysis
title: Longitudinal and Panel Data Analysis
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: probability-and-statistics
  type: hard
- id: linear-regression-social-science
  type: hard
- id: matrices-intro
  type: soft
- id: covariance-between-random-variables
  type: soft
builds-toward:
- panel-data-fixed-effects
- time-series-cross-section
tags:
- longitudinal
- panel
- temporal
- multilevel
stage: advanced
status: draft
---

# Longitudinal and Panel Data Analysis

## Core Idea
Longitudinal analysis studies change within individuals or units over time, using data collected at multiple waves. Panel data combines the time-series dimension (same units measured repeatedly) with cross-sectional breadth (many units). These designs enable causal inference about within-unit change, lag effects, and dynamic feedback. Fixed-effects models eliminate time-invariant confounds; growth curve models characterize trajectories of change.

## Explainer

Cross-sectional data — a single snapshot of many units — leaves an important question unanswered: when we observe differences between individuals, are those differences caused by the factors we measure, or do they reflect stable underlying characteristics we have not observed? A student who reads more may score higher on vocabulary tests, but is this because reading *causes* vocabulary growth, or because students who are already more intellectually capable do both? Cross-sectional data cannot distinguish these stories. Longitudinal data addresses this by following the same units across time, enabling you to observe *change* within individuals — and within-unit change eliminates everything stable about a person from the comparison.

The workhorse of panel causal inference is the **fixed-effects model**. The logic extends directly from your understanding of linear regression: instead of comparing individuals to each other, you compare each individual to themselves across time. Formally, a unit-specific intercept (the "fixed effect") absorbs all time-invariant unobserved characteristics. If person A is always more productive than person B due to some unmeasured trait — intelligence, conscientiousness, social capital — the fixed effect captures this and removes it from the estimation. What remains is within-unit variation over time, and it is this variation that identifies the causal effect of time-varying predictors. The tradeoff is that you cannot estimate the effect of stable variables (race, sex, country of birth) since these are perfectly collinear with the fixed effects. The fixed-effects estimator is mathematically equivalent to de-meaning each variable by the unit's own time-average before running OLS — a connection your regression background makes tractable.

**Growth curve models** (also called latent trajectory or random-effects growth models) approach the panel structure differently. Rather than eliminating between-unit variation, they model it explicitly. Each unit follows its own trajectory over time, described by a linear or polynomial function: an intercept (initial status) and one or more slopes (rates of change). These individual-level parameters are treated as random variables drawn from a population distribution — hence "random effects." This lets you ask richer questions: not just "what is the average effect of X?" but "do different subgroups follow different trajectories?" and "what predicts who has a steeper growth curve?" Growth curve models require stronger distributional assumptions than fixed-effects models but yield far more information about heterogeneous change processes. Your understanding of covariance between random variables becomes essential here: the model must specify how intercepts and slopes covary across individuals, and the structure of that covariance encodes substantively important assumptions about how trajectories are organized.

The practical challenge that distinguishes longitudinal analysis from cross-sectional work is **attrition** — units that leave the study over time. If dropout is random (completely unrelated to the variables in the model), estimates remain unbiased though precision declines. If dropout is related to the outcome trajectory — sicker patients die and leave, students who are struggling drop out of school — the survivors are systematically unrepresentative, and analyses based only on completers produce biased estimates. Handling non-random attrition requires either modeling the dropout process explicitly (using variables that predict departure) or using inverse probability weighting to upweight units whose characteristics resemble those who left. This connects back to the core logic of causal inference: the key question is always whether the comparison group represents the counterfactual, and attrition can undermine this just as badly as cross-sectional confounding can.
