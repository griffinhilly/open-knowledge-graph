---
id: propensity-score-methods-research-methods-social-science
title: Propensity Score Methods
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: causal-inference-observational-data
  type: hard
- id: logistic-regression-binary-outcomes
  type: hard
- id: probability-distributions
  type: hard
- id: conditional-distributions-of-random-variables
  type: hard
- id: probability-mass-functions
  type: soft
- id: conditional-probability
  type: soft
- id: probability-axioms
  type: soft
- id: logistic-regression-binary-categorical
  type: soft
- id: probability-density-functions
  type: hard
tags:
- propensity-score
- matching
- stratification
- weighting
stage: advanced
status: draft
---

# Propensity Score Methods

## Core Idea
Introduces propensity score methods to balance treatment and control groups in observational studies by matching on probability of treatment. Covers PS estimation, matching algorithms (1:1, caliper, replacement), stratification, inverse probability weighting, and sensitivity analysis for hidden bias.

## How It's Best Learned
Estimate propensity scores, create balance diagnostics before/after matching, try different matching algorithms, conduct sensitivity analysis with hidden bias parameters.

## Common Misconceptions
- Matching on propensity scores solves confounding
- Perfect balance is achievable and necessary
- Propensity score matching always improves inference

## Explainer

From your study of causal inference in observational data, you know the central problem: people select into treatments for reasons correlated with outcomes, creating confounding. In a randomized experiment, random assignment breaks this link — treated and control groups are balanced on all variables, observed and unobserved. In observational studies you cannot randomize, so the goal is to construct a comparison that mimics what randomization would have produced. **Propensity score methods** are one strategy for doing this by balancing observed covariates between treatment and control groups.

The **propensity score** is a single summary: the probability that a unit receives treatment given its observed covariates, P(T=1 | X). You already know how to estimate this — it is a logistic regression predicting treatment assignment from the set of confounding variables. The crucial theoretical result (Rosenbaum and Rubin, 1983) is that if you condition on the propensity score, treatment assignment is independent of the covariates — you don't need to match or control for each covariate separately. Instead of finding an exact match in a high-dimensional covariate space, you collapse the problem to one dimension. This dimension-reduction property is what makes propensity scores practically valuable.

There are four main ways to use the propensity score. **1:1 nearest-neighbor matching** pairs each treated unit to the control unit with the closest propensity score; **caliper matching** restricts matches to be within a fixed distance of each other, improving balance at the cost of dropping poor matches; **stratification** divides the propensity score into quantiles and compares outcomes within strata; **inverse probability weighting (IPW)** re-weights the sample so that the distribution of covariates in the weighted comparison group mirrors the treated group. Each approach makes different tradeoffs between bias reduction, variance, and sample retention. IPW retains the full sample but can be unstable when propensity scores are very close to 0 or 1 — a problem sometimes addressed by trimming or stabilizing weights.

**Balance diagnostics** are essential and should drive your workflow: estimate propensity scores, check balance (via standardized mean differences and overlap plots), revise the model if balance is poor, then check balance again. The goal is not a high-accuracy propensity score model — it is adequate covariate balance. Paradoxically, adding more predictors to the propensity model doesn't always improve balance, and can sometimes hurt it. The estimand also matters: propensity matching estimates the **average treatment effect on the treated (ATT)** by default — what the effect of treatment was for those who actually received it — rather than the average treatment effect (ATE) for the whole population.

The deepest limitation is the **conditional independence assumption** (also called ignorability or no hidden confounding): treatment assignment is independent of potential outcomes given observed covariates. This assumption is untestable from the data. If there are unobserved confounders — variables that predict both treatment and outcome — propensity score matching does not eliminate the bias from those variables. **Sensitivity analysis** (Rosenbaum bounds) asks how strong an unobserved confounder would need to be to overturn your conclusion. A finding that is sensitive to small departures from ignorability should be treated as fragile. Propensity score methods are not a substitute for a good research design; they are a tool for squeezing the most valid inference from observational data given the design you have.
