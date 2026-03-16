---
id: fuzzy-regression-discontinuity-design
title: Fuzzy Regression Discontinuity Design
domain: economics
course: econometrics
prerequisites:
- id: regression-discontinuity
  type: hard
- id: instrumental-variables
  type: hard
tags:
- causal-inference
- regression-discontinuity
- instrumental-variables
stage: formal-systems
status: draft
---

# Fuzzy Regression Discontinuity Design

## Core Idea
In fuzzy RDD, the probability of treatment jumps discontinuously at the threshold c*, but not from 0 to 1. The running variable serves as an instrument for treatment. The estimand is the LATE (Local Average Treatment Effect) for units near the cutoff whose treatment status is affected by the discontinuity.

## Explainer

From your study of sharp RDD, you know the basic idea: if assignment to treatment is determined by whether a running variable crosses a threshold, units just below and just above the cutoff are nearly identical, making the discontinuity a natural experiment. The clean assumption in sharp RDD is that every unit above the threshold receives treatment and every unit below does not — the assignment rule is perfectly enforced. But in many real applications, the threshold only *changes the probability* of treatment — some units above it don't receive treatment, and some below it do. This is the **fuzzy RDD** setting.

The classic example is a scholarship program that automatically sends an eligibility letter to students scoring above a test cutoff. Most students who receive the letter take up the scholarship, but some don't bother, and a few below the cutoff receive it through discretionary decisions by administrators. The running variable (test score) no longer perfectly determines treatment — it only shifts the probability. Near the cutoff, you observe a jump in the fraction treated, but not from 0 to 1. Graphically, if you plot treatment takeup against the running variable, you see a discontinuous *jump* at the threshold, but the treatment probability remains strictly between 0 and 1 on both sides.

Here is where your knowledge of **instrumental variables** becomes essential. Being just above versus just below the cutoff serves as an instrument for actual treatment receipt. Think through the IV conditions: (1) **Relevance**: crossing the threshold increases the probability of treatment — this is the first stage, and it is directly visible as the jump in treatment rate. (2) **Exclusion**: being just above the cutoff only affects outcomes through its effect on treatment take-up, not through any direct channel. The local nature of RDD — comparing only units very close to the cutoff — makes this exclusion assumption far more credible than in a typical IV setup, because units just above and just below are nearly identical in all other respects.

The fuzzy RDD estimand is the **Local Average Treatment Effect**: the effect of treatment for "compliers" near the cutoff — those whose treatment status would change depending on which side of the threshold they fall. This is the same LATE you encountered in IV: compliers are the units who take treatment when nudged by the instrument but would not otherwise. The estimator is the ratio of the reduced-form discontinuity (the jump in outcomes at the threshold) to the first-stage discontinuity (the jump in treatment probability). This is exactly the IV ratio estimator, implemented locally. When the first-stage jump is 1 — when everyone above takes up and no one below does — fuzzy and sharp RDD coincide, and the LATE equals the ATE for compliers at the cutoff.
