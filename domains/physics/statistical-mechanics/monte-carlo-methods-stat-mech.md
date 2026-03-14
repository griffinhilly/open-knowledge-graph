---
id: monte-carlo-methods-stat-mech
title: Monte Carlo Methods in Statistical Mechanics
domain: physics
course: statistical-mechanics
prerequisites:
- id: canonical-ensemble
  type: hard
- id: probability-axioms
  type: hard
tags:
- simulation
- numerical-methods
- sampling
stage: advanced
status: draft
---

# Monte Carlo Methods in Statistical Mechanics

## Core Idea
Monte Carlo methods sample phase space according to the Boltzmann distribution exp(−E/kT) to compute thermal averages without evaluating the partition function. The Metropolis algorithm uses a random walk with acceptance probability min(1, exp(−ΔE/kT)) to generate a Markov chain sampling the canonical distribution. Other variants include Gibbs sampling and parallel tempering for escaping local minima.
