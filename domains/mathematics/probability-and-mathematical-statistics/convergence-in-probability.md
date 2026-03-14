---
id: convergence-in-probability
title: Convergence in Probability
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: random-variables-as-measurable-functions
  type: hard
- id: epsilon-n-convergence
  type: soft
builds-toward:
- relationships-between-modes-of-convergence
- weak-law-of-large-numbers
tags:
- convergence
- stochastic
- probability
stage: abstract-reasoning
status: draft
---

# Convergence in Probability

## Core Idea
A sequence X_n converges in probability to X if for every ε > 0, P(|X_n - X| > ε) → 0. The random variables become increasingly concentrated near X, though individual realizations can deviate. This is the weakest notion of stochastic convergence.
