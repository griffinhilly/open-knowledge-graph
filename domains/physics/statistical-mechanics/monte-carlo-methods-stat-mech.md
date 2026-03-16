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

## Explainer

From the canonical ensemble, you know that the thermal average of any observable A is ⟨A⟩ = (1/Z) Σ_s A(s) exp(−E(s)/kT), where the sum runs over all microstates s and Z is the partition function. The problem in practice is that this sum is astronomically large — a system of N ~ 10²³ particles has an inconceivably vast configuration space. Worse, computing Z directly requires the full sum anyway, so you can't even normalize correctly. The key insight behind Monte Carlo methods is that you don't need to visit all microstates or compute Z explicitly: you only need to *sample* from the Boltzmann distribution P(s) ∝ exp(−E(s)/kT), and then average A over the samples. The partition function cancels in the ratio.

The **Metropolis algorithm** solves the sampling problem with an elegant trick. Start from any configuration. Propose a random modification (flip a spin, move a particle, change a bond). Compute the energy change ΔE = E_new − E_old. If ΔE < 0 (the proposed state has lower energy), **always accept** — moving to lower energy increases probability according to Boltzmann. If ΔE > 0 (higher energy), **accept with probability exp(−ΔE/kT)**. This acceptance rule ensures that the random walk spends more time in low-energy states proportionally to their Boltzmann weight, without ever computing Z. After the system has run long enough to "forget" its starting configuration (thermalization), subsequent configurations are samples drawn from the correct canonical distribution.

The mathematical guarantee behind this is **detailed balance**: for any two states s and s', the probability of being in s and transitioning to s' equals the probability of being in s' and transitioning to s, when both probabilities are weighted by their Boltzmann factors. Detailed balance ensures the Markov chain has the Boltzmann distribution as its unique stationary state. Run it long enough, and your samples converge to the equilibrium distribution regardless of where you started.

In practice, you use Monte Carlo to study phase transitions, measure thermodynamic quantities like heat capacity (from energy fluctuations), and compute correlation functions. The classic application is the **2D Ising model**: flip spins on a lattice using Metropolis, measure the average magnetization as a function of temperature, and watch it drop to zero at the critical temperature T_c. The challenge at phase transitions is **critical slowing down** — configurations become highly correlated and the algorithm mixes slowly. This motivates more advanced methods: **parallel tempering** runs copies at multiple temperatures and occasionally swaps them, allowing the cold simulation to escape barriers via the hot one. **Cluster algorithms** (Wolff, Swendsen-Wang) flip entire domains at once rather than single spins, dramatically reducing correlation times near T_c. Monte Carlo is not one algorithm but a family of stochastic sampling strategies, all sharing the core idea of turning an intractable sum into a manageable average over representative samples.
