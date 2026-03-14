---
id: conditional-expectation
title: Conditional Expectation
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: expectation-measure-theoretic
  type: hard
- id: independence-sigma-algebras
  type: soft
builds-toward:
- martingales-introduction
- bayesian-inference-foundations
tags:
- conditional-expectation
- sigma-algebras
- probability
stage: abstract-reasoning
status: draft
---

# Conditional Expectation

## Core Idea
Conditional expectation E[X|G] with respect to a sigma-algebra G is the unique G-measurable random variable satisfying E[E[X|G]·1_A] = E[X·1_A] for all A ∈ G. It generalizes discrete conditional expectation and has properties: E[E[X|G]] = E[X], E[aX + bY|G] = aE[X|G] + bE[Y|G], and the tower property E[E[X|G₁]|G₂] = E[X|G₂] when G₂ ⊆ G₁.
