---
id: instrumental-variables-methods
title: Instrumental Variables Estimation
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: causal-inference-observational-data
  type: hard
- id: linear-regression-social-science
  type: hard
- id: matrix-inverses
  type: hard
- id: linear-systems-notation
  type: hard
- id: matrices-intro
  type: soft
- id: linear-transformation-definition
  type: soft
- id: linear-regression
  type: hard
- id: matrix-multiplication
  type: hard
tags:
- instrumental-variables
- endogeneity
- two-stage-least-squares
- IV-validity
stage: advanced
status: draft
---

# Instrumental Variables Estimation

## Core Idea
Introduces instrumental variables as a solution to endogeneity when confounders are unobserved. Covers IV assumptions (relevance, exclusion restriction), two-stage least squares estimation, instrument validity testing, and weak instrument problems with examples from social research.

## How It's Best Learned
Identify potential instruments in published studies, design IV estimations with real data, test instrument strength and validity assumptions, practice interpreting TSLS results.

## Common Misconceptions
- Valid instruments are easy to find
- Relevance is testable but exclusion restriction is not
- Any variable correlated with treatment can be an instrument

## Explainer

You already know from linear regression that the ordinary least squares (OLS) estimator finds the line minimizing prediction error. And from causal inference in observational data, you know the central problem: OLS gives unbiased estimates *only* if the error term is uncorrelated with the treatment variable. When unmeasured confounders simultaneously affect the treatment and outcome, the regression coefficient is **endogenous** — it captures both the causal effect and the confounding, making it impossible to isolate either from the other.

The **instrumental variables (IV)** strategy solves this by finding a third variable — the **instrument** — that affects the treatment but affects the outcome *only through* the treatment. Think of a natural experiment: the Vietnam War draft lottery assigned military service by birth date. Birth date is essentially random with respect to earnings (it's not a confounder), yet it affected who served. Economists use birth date as an instrument for military service to estimate the causal effect of service on lifetime earnings. The instrument creates exogenous variation in the treatment — variation not contaminated by unobserved confounders.

This logic formalizes into two conditions. **Relevance** means the instrument must actually predict the treatment — the correlation between instrument and treatment must be nonzero and ideally strong. You can test this: regress treatment on instrument and check the F-statistic; a rule of thumb is F > 10. **The exclusion restriction** says the instrument affects the outcome only through the treatment, not through any other channel. This is *untestable* — it must be defended on theoretical and contextual grounds. A weak exclusion restriction argument is the most common fatal flaw in IV studies.

**Two-Stage Least Squares (2SLS)** is the standard estimator. In stage 1, regress treatment on the instrument to extract only the exogenous variation in treatment. In stage 2, regress outcome on the stage-1 fitted values — the "clean" part of treatment variation. The matrix algebra you know makes this tractable: the 2SLS estimator is (Z'X)⁻¹Z'y, where Z is the instrument matrix, X the treatment, and y the outcome. In practice, software handles this, but understanding the algebra clarifies what's being estimated: only the variation in treatment driven by the instrument identifies the causal effect.

There is a crucial limitation: IV estimates **Local Average Treatment Effects (LATE)** — the causal effect only for the subgroup whose treatment status was actually changed by the instrument (called "compliers"). People who always take the treatment regardless of the instrument, or never do regardless, are not informative for the 2SLS estimate. This means IV findings may not generalize to the full population. The tradeoff is real: IV gives you cleaner causal identification than OLS, but at the cost of estimating an effect for a sometimes-narrow, sometimes-uncharacterized subgroup.
