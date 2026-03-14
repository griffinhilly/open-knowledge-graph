---
id: potential-outcomes-framework
title: Potential Outcomes and the Rubin Causal Model
domain: economics
course: econometrics
prerequisites:
- id: causal-inference-econometrics
  type: hard
- id: expected-value
  type: hard
- id: probability-axioms
  type: soft
- id: conditional-probability
  type: soft
builds-toward:
- selection-bias-econometrics
- difference-in-differences
- regression-discontinuity
tags:
- potential-outcomes
- ATE
- ATT
- counterfactual
stage: formal-systems
status: validated
---

# Potential Outcomes and the Rubin Causal Model

## Core Idea
The potential outcomes framework (Rubin, 1974) formalizes causality: unit i has two potential outcomes, Y(1) under treatment and Y(0) under control, but only one is observed. The individual treatment effect is Y_i(1) − Y_i(0), which is never directly observable. The Average Treatment Effect (ATE) = E[Y(1) − Y(0)] averages over the population; the ATT = E[Y(1) − Y(0) | D=1] averages only over the treated. Selection bias arises when E[Y(0)|D=1] ≠ E[Y(0)|D=0] — that is, when treated and untreated units would have had different outcomes even absent treatment. Randomization solves this by ensuring independence: {Y(0), Y(1)} ⊥ D.

## How It's Best Learned
Decompose the observed difference in means between treated and control groups into the ATT plus a selection bias term — this derivation makes the identification problem concrete and shows exactly what assumptions eliminate the bias.

## Common Misconceptions
- The ATE and ATT are different objects and answer different policy questions; IV typically estimates a Local ATE (LATE), not the ATE.
- The fundamental problem of causal inference is a missing data problem, not a statistical estimation problem.
