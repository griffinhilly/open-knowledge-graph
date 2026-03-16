---
id: regression-discontinuity
title: Regression Discontinuity Design
domain: economics
course: econometrics
prerequisites:
- id: causal-inference-econometrics
  type: hard
- id: potential-outcomes-framework
  type: hard
- id: bivariate-regression
  type: hard
tags:
- RDD
- regression-discontinuity
- threshold
- local-ATE
- bandwidth
stage: formal-systems
status: validated
---

# Regression Discontinuity Design

## Core Idea
Regression discontinuity (RD) exploits a sharp threshold in a 'running variable' x that determines treatment assignment: units just above the cutoff receive treatment while units just below do not. The key insight is that units near the threshold are nearly identical in all respects — observed and unobserved — making the discontinuous jump in outcomes at the threshold a credible causal effect estimate. The RD estimator is the difference in the intercepts of the regression lines fitted on each side of the cutoff. Identification requires that agents cannot precisely manipulate their position around the threshold; the McCrary density test checks for sorting.

## How It's Best Learned
Study Thistlethwaite and Campbell's (1960) original scholarship threshold study, then examine Lee (2008)'s incumbency advantage study to understand how running variables and cutoffs are chosen and validated.

## Common Misconceptions
- RD estimates a Local ATE at the threshold, not the ATE for the full population — external validity is often limited.
- Choosing a very narrow bandwidth around the cutoff reduces bias but also reduces precision; bandwidth selection involves a bias-variance tradeoff.

## Explainer

Your prerequisite on causal inference introduced the core identification problem: you can never observe the same unit in both treated and untreated states simultaneously. The potential outcomes framework formalized this — the causal effect for unit i is Yᵢ(1) − Yᵢ(0), but only one of these is ever observed. Regression discontinuity offers an elegant solution to this problem by finding a setting where nature approximates a randomized experiment: a sharp threshold rule that determines who gets treated.

The canonical example is a scholarship test: students scoring above 50 receive a scholarship, those scoring below do not. A student who scores 51 is treated; one who scores 49 is not. These two students are almost certainly very similar in ability, background, and other characteristics — the single point separating them is essentially random noise in test performance. This is the **local randomization** intuition behind RD. The **running variable** (the test score) determines treatment, and the **cutoff** (score = 50) creates two groups that are locally comparable. The RD estimator computes the **jump** in the outcome at the cutoff: the vertical gap between the regression line fitted on the right side (treated units) and the regression line fitted on the left side (control units), both evaluated at exactly x = 50.

Formally, the RD estimate is the **Local Average Treatment Effect at the threshold**: LATE = lim_{x↓c} E[Y|X=x] − lim_{x↑c} E[Y|X=x]. Notice this is inherently a local quantity — it estimates the effect for units at the cutoff, not the whole population. A student with a score of 70 might respond very differently to the scholarship than a student at 50. This limited external validity is RD's principal weakness relative to other methods.

The key identifying assumption is that agents cannot **precisely** manipulate their position around the threshold. Some manipulation is fine — students may study harder knowing the cutoff exists — but if students can precisely sort to just above 50, the "local randomization" analogy breaks down: the treated group just above the cutoff would systematically differ from the control group just below. The **McCrary density test** checks for this by looking for a discontinuous jump in the density of the running variable at the cutoff. A suspicious pile-up of observations just above the threshold is a red flag. Bandwidth selection also matters: too narrow and you have very few observations and imprecise estimates; too wide and you are comparing units that are less similar, introducing bias if the underlying outcome function is nonlinear. Reporting results across multiple bandwidth choices is standard practice in credible RD papers.
