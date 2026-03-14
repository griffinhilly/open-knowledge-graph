---
id: master-equation
title: Master Equation
domain: physics
course: statistical-mechanics
prerequisites:
- id: fokker-planck-equation
  type: soft
- id: probability-and-statistics
  type: soft
tags:
- stochastic
- markov
- discrete
stage: advanced
status: draft
---

# Master Equation

## Core Idea
The master equation dP_n/dt = Σ_m [W_{nm}P_m - W_{mn}P_n] describes time evolution of probability for discrete-state systems. Assuming Markovian dynamics (memoryless transitions), it applies broadly from molecular systems to quantum jumps, and becomes the Fokker-Planck equation in the continuum limit.
