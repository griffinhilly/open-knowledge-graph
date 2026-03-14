---
id: metropolis-algorithm
title: The Metropolis Algorithm
domain: physics
course: statistical-mechanics
prerequisites:
- id: monte-carlo-statistical-mechanics
  type: hard
- id: canonical-ensemble
  type: soft
tags:
- metropolis
- markov-chain
- detailed-balance
stage: advanced
status: draft
---

# The Metropolis Algorithm

## Core Idea
The Metropolis algorithm constructs a Markov chain that samples from the canonical ensemble. Proposed moves are accepted with probability min(1, exp(-ΔE/kT)). Detailed balance is satisfied, ensuring the stationary distribution is the Boltzmann distribution. The algorithm is simple, scalable, and has become standard for simulating classical statistical systems.
