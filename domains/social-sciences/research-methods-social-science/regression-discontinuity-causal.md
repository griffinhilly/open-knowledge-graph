---
id: regression-discontinuity-causal
title: Regression Discontinuity Design
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: causal-inference-observational-data
  type: hard
- id: linear-regression-social-science
  type: hard
- id: limit-definition-intuitive
  type: soft
- id: linear-regression
  type: hard
- id: limits-continuity-multivariable
  type: soft
tags:
- regression-discontinuity
- threshold-assignment
- local-polynomial
- fuzzy-RD
stage: advanced
status: draft
---

# Regression Discontinuity Design

## Core Idea
Applies regression discontinuity methods when assignment to treatment depends on a continuous running variable crossing a threshold. Covers sharp and fuzzy RD designs, local polynomial estimation, bandwidth selection, and internal validity advantages of RD for causal inference.

## How It's Best Learned
Identify RD applications in real policies (test cutoffs, age eligibility), estimate sharp and fuzzy RD models, create RD plots, conduct falsification tests with placebo cutoffs.

## Common Misconceptions
- RD requires very narrow bandwidths around the cutoff
- Fuzzy RD is always weaker than sharp RD
- RD can only use polynomial functional forms

## Explainer

You know from your causal inference prerequisites that the central challenge in observational data is confounding: people who receive a treatment are systematically different from those who don't, and those differences — not the treatment itself — may explain the outcome differences we observe. Regression discontinuity design (RDD) exploits a simple but powerful idea: if assignment to treatment is determined by whether a continuous variable crosses a threshold, then people just below the cutoff and just above it are nearly identical in all respects except treatment status. The threshold creates a local natural experiment.

The classic example makes the logic vivid. Students who score just above an admissions cutoff gain entry to a selective school; those who score just below do not. Among students very near the cutoff, admission is essentially random — a few points' difference on a test on one day, attributable to noise rather than meaningful ability differences. By comparing outcomes for students just above versus just below the cutoff, you obtain a clean estimate of the effect of selective school admission, free of the selection bias that would contaminate a comparison of all admitted versus non-admitted students. This is the **sharp RD design**: treatment status jumps discontinuously from 0 to 1 at the **cutoff** (also called the threshold), and the **running variable** (test score, age, income, geographic distance) determines that jump precisely.

Your prerequisites on limits and continuity clarify the identifying assumption: in the absence of treatment, potential outcomes would be a *continuous* function of the running variable at the cutoff. The causal estimate is the discontinuous jump in outcomes at the threshold — whatever can't be explained by the smooth trend in the running variable must be the treatment effect. Visually, you plot the outcome against the running variable on both sides of the cutoff. A smooth curve with a sudden jump at the threshold is the signature of a causal effect. **Local polynomial regression** estimates those smooth trends flexibly on each side, avoiding the distortions introduced by high-degree global polynomials. **Bandwidth selection** involves a bias-variance tradeoff: a narrow bandwidth around the cutoff gives you observations most similar to each other (internal validity) but fewer observations (larger standard errors). Optimal bandwidth selection algorithms balance these concerns formally.

The **fuzzy RD design** applies when the cutoff affects the probability of treatment rather than determining it deterministically — some above the cutoff don't take up the treatment, some below obtain it through other means. Here the discontinuity is in the *probability* of treatment, and you use the cutoff as an instrument for actual treatment receipt, combining RD intuition with instrumental variables logic. The resulting estimate is a local average treatment effect (LATE) for compliers near the threshold. **Falsification tests** are essential for validating any RD design: test whether predetermined covariates (baseline characteristics measured before treatment) show no discontinuity at the real cutoff; test for discontinuities at placebo cutoffs where no effect should exist; check for bunching in the running variable distribution just above the cutoff, which would indicate manipulation of the assignment rule.
