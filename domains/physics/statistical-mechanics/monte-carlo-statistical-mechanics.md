---
id: monte-carlo-statistical-mechanics
title: Monte Carlo Methods and Importance Sampling
domain: physics
course: statistical-mechanics
prerequisites:
- id: statistical-ensembles-intro
  type: hard
- id: canonical-ensemble
  type: soft
builds-toward:
- metropolis-algorithm
- ising-model-statmech
tags:
- monte-carlo
- importance-sampling
- numerical-simulation
stage: advanced
status: draft
---

# Monte Carlo Methods and Importance Sampling

## Core Idea
Monte Carlo methods estimate thermal averages by sampling microstates according to their Boltzmann weight P(state) ∝ exp(-E/kT). Importance sampling biases random walks toward likely states, vastly reducing computation. The algorithm efficiently explores the configuration space and provides results for systems where analytical solutions are intractable, such as the 3D Ising model.
