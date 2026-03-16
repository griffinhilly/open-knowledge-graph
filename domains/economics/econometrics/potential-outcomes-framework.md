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

## Explainer

You already know from your work on causal inference that observational data does not automatically yield causal answers — the question is *why*. The potential outcomes framework gives the sharpest possible answer: for every unit i, there are two potential states of the world. **Y_i(1)** is the outcome that would occur if unit i receives treatment; **Y_i(0)** is the outcome if it does not. The individual treatment effect is the difference Y_i(1) − Y_i(0). The problem is not statistical — it is logical. You observe a person either treated or untreated, never both. Y_i(1) and Y_i(0) cannot both be realized simultaneously. This is the **fundamental problem of causal inference**: the individual treatment effect is never observed, and the challenge of causal inference is recovering population-level summaries of it.

Because individual effects are unobservable, the framework shifts focus to averages. The **Average Treatment Effect (ATE)** = E[Y(1) − Y(0)] asks: if we randomly assigned treatment to everyone in the population, what would the average effect be? The **Average Treatment Effect on the Treated (ATT)** = E[Y(1) − Y(0) | D=1] asks a more targeted question: among those who actually received treatment, what was the effect? These are distinct estimands that answer different policy questions. If a job training program works well for the people who self-select into it but would be less effective for the general population, ATE < ATT. Both numbers are real and meaningful — they just answer different questions about who benefits.

Why does naive comparison fail? The observed difference in means between treated and untreated groups can be decomposed as: E[Y|D=1] − E[Y|D=0] = ATT + **selection bias**. The selection bias term is E[Y(0)|D=1] − E[Y(0)|D=0]: the difference in untreated potential outcomes between those who chose treatment and those who didn't. If people who receive job training would have found employment at higher rates anyway (because they are more motivated), the selection bias is positive, and naive comparison overstates the treatment effect. This is not a subtle statistical issue — it is a direct consequence of the assignment mechanism not being random.

**Randomization** solves the problem cleanly. When treatment D is randomly assigned, {Y(0), Y(1)} ⊥ D — potential outcomes are independent of treatment status. This means E[Y(0)|D=1] = E[Y(0)|D=0]: the average untreated outcome of those assigned to treatment equals the average untreated outcome of those assigned to control. Selection bias is zero by construction, and the observed difference in means recovers the ATE. All subsequent methods in this course — difference-in-differences, regression discontinuity, instrumental variables — are ways of achieving the same independence condition when randomization is not available, by exploiting quasi-random variation in treatment assignment. The potential outcomes framework is the common language that makes each method's identifying assumption precise.
