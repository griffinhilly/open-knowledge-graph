---
id: causal-inference-econometrics
title: Causal Inference and the Identification Problem
domain: economics
course: econometrics
prerequisites:
- id: econometrics-intro
  type: hard
- id: omitted-variable-bias
  type: hard
builds-toward:
- potential-outcomes-framework
- difference-in-differences
- regression-discontinuity
tags:
- causality
- identification
- natural-experiment
- selection-bias
stage: formal-systems
status: draft
---

# Causal Inference and the Identification Problem

## Core Idea
Causal inference asks what would have happened to unit i had treatment status been different — the fundamental problem being that we only ever observe one potential outcome per unit. In economics, randomized controlled trials are rarely feasible, so identification relies on 'natural experiments': institutional rules, policy changes, or geographic discontinuities that create quasi-random variation in treatment. The identification strategy is the researcher's argument for why variation in the regressor of interest is as-good-as-random conditional on observables. All credible empirical economics papers lead with their identification strategy.

## How It's Best Learned
Read landmark natural experiment papers (Card-Krueger minimum wage, Angrist Vietnam draft lottery) to understand how economists construct identification arguments from non-experimental settings.

## Common Misconceptions
- Controlling for more covariates does not solve selection bias if the controls themselves are endogenous.
- 'As-good-as-random' does not mean literally random — it means the remaining variation in x is uncorrelated with potential outcomes.
