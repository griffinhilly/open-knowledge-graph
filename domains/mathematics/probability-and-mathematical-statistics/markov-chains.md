---
id: markov-chains
title: Markov Chains
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: conditional-probability
  type: hard
- id: independence-of-sigma-algebras
  type: soft
builds-toward:
- markov-chains-convergence
- stationary-distributions
tags:
- markov-chains
- stochastic-processes
- memoryless
stage: abstract-reasoning
status: draft
---

# Markov Chains

## Core Idea
A Markov chain is a sequence X_n where P(X_{n+1}|X_n, X_{n-1}, ...) = P(X_{n+1}|X_n). The memoryless property means future evolution depends only on the current state. Markov chains are defined by a transition matrix P and initial distribution. They model phenomena with no memory and are central to MCMC computational statistics.
