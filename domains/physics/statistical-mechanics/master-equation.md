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

## Explainer

From your background in probability you know how to describe the state of a random system using a probability distribution, and from the Fokker-Planck equation you know how to describe how that distribution changes over time for a continuous-state system. The **master equation** is the discrete-state analogue: instead of a probability density P(x,t) over a continuous variable, you have probabilities P_n(t) for being in state n at time t, and you write down how each probability changes.

The structure of the master equation dP_n/dt = Σ_m [W_{nm}P_m − W_{mn}P_n] has a transparent physical interpretation. The first term, W_{nm}P_m, is a **gain** term: it represents all the transitions *into* state n from any other state m, weighted by the probability of currently being in m and the rate W_{nm} of that transition. The second term, W_{mn}P_n, is a **loss** term: it represents all transitions *out of* state n, weighted by the probability of being in n. The difference is the net rate of change of P_n. This gain-minus-loss structure is sometimes called the **balance equation** and is completely general for Markovian systems.

The **Markov property** — that transition rates W_{nm} depend only on the current state, not on the history — is the key physical assumption. It holds when the relaxation time of the environment is much shorter than the transition timescale, so the system has "forgotten" how it got to the current state before the next transition happens. This is often an excellent approximation: a molecule deciding whether to isomerize does not remember its collision history from a microsecond ago.

At steady state, dP_n/dt = 0, and one sufficient condition is **detailed balance**: W_{nm}P_m = W_{mn}P_n for every pair (n, m). Detailed balance means the rate of transitions from n to m exactly balances the rate of transitions from m to n — the system is in equilibrium, not just in a non-equilibrium steady state. For systems in contact with a thermal bath, detailed balance requires the ratio W_{nm}/W_{mn} = exp(−(E_n − E_m)/k_BT), connecting microscopic transition rates to macroscopic thermodynamic equilibrium. When you take the continuum limit — letting the discrete states become densely packed — the master equation reduces to the Fokker-Planck equation, connecting the two formalisms your prerequisites introduced.
