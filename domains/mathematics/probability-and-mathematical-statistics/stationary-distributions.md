---
id: stationary-distributions
title: Stationary Distributions of Markov Chains
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: markov-chains
  type: hard
builds-toward:
- markov-chains-convergence
tags:
- markov-chains
- stationary-distribution
- equilibrium
stage: abstract-reasoning
status: draft
---

# Stationary Distributions of Markov Chains

## Core Idea
A stationary distribution π satisfies πP = π. For irreducible, aperiodic, finite-state Markov chains, a unique stationary distribution exists and is the limiting distribution regardless of initial state. Stationary distributions model long-run behavior and are crucial for MCMC: if the chain has the posterior as stationary distribution, samples approximate the posterior.
