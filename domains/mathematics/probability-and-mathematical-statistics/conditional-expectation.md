---
id: conditional-expectation
title: Conditional Expectation
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: expectation-measure-theoretic
  type: hard
- id: conditional-probability
  type: soft
builds-toward:
- martingales-intro
- bayesian-inference-foundations
tags:
- conditional-expectation
- sigma-algebras
- integration
stage: abstract-reasoning
status: draft
---

# Conditional Expectation

## Core Idea
Conditional expectation E[X|ℊ] given a sigma-algebra ℊ is the orthogonal projection of X onto ℊ-measurable random variables in L². It satisfies ∫_A E[X|ℊ] dP = ∫_A X dP for all A ∈ ℊ. This unifies discrete conditioning, continuous conditioning, and extends to conditioning on sigma-algebras.
