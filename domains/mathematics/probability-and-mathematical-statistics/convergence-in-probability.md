---
id: convergence-in-probability
title: Convergence in Probability
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: random-variables-as-measurable-functions
  type: hard
- id: limit-definition-intuitive
  type: soft
builds-toward:
- relationships-modes-convergence
- weak-law-of-large-numbers
tags:
- convergence
- probability
- limit-theorems
stage: formal-systems
status: draft
---

# Convergence in Probability

## Core Idea
A sequence {Xₙ} converges to X in probability if for all ε > 0, lim_{n→∞} P(|Xₙ - X| > ε) = 0. Intuitively, Xₙ is close to X with high probability for large n. Convergence in probability is weaker than almost sure convergence but stronger than convergence in distribution.
