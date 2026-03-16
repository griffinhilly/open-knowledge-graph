---
id: markov-chains-convergence
title: Convergence of Markov Chains
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: stationary-distributions
  type: hard
- id: convergence-in-distribution
  type: soft
tags:
- markov-chains
- convergence
- mixing
stage: advanced
status: draft
---

# Convergence of Markov Chains

## Core Idea
An irreducible, aperiodic Markov chain converges in distribution to its stationary distribution π: P(X_n = j) → π(j). The convergence rate depends on the spectral gap (largest minus second-largest eigenvalue of P); larger gaps mean faster mixing. Convergence ensures MCMC samples approach the target distribution.
