---
id: stationary-distributions
title: Stationary Distributions
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: markov-chains
  type: hard
- id: convergence-in-distribution
  type: soft
builds-toward:
- martingales-introduction
tags:
- stationary-distributions
- markov-chains
- probability
stage: abstract-reasoning
status: draft
---

# Stationary Distributions

## Core Idea
A probability distribution π is stationary for a Markov chain with transition kernel P if π = πP, or equivalently ∫π(dx)P(x, A) = π(A) for all measurable A. For irreducible aperiodic chains, the distribution converges to a unique stationary distribution. Stationary distributions characterize long-run behavior.
