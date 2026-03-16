---
id: time-correlation-functions
title: Time-Correlation Functions and Relaxation
domain: physics
course: statistical-mechanics
prerequisites:
- id: two-point-correlation-functions
  type: hard
- id: ensemble-theory-fundamentals
  type: hard
builds-toward:
- green-kubo-formula
- response-functions-definition
tags:
- dynamics
- correlations
- relaxation
stage: advanced
status: draft
---

# Time-Correlation Functions and Relaxation

## Core Idea
Time-correlation functions C(t) = ⟨A(t)A(0)⟩ measure how observables decorrelate in time for an equilibrium system. They characterize the timescale of fluctuations, relax to zero for ergodic systems, and provide access to dynamical properties like diffusion coefficients and viscosity through the fluctuation-dissipation theorem.

## Explainer

From your study of two-point correlation functions, you already understand how spatial correlations ⟨A(r)A(0)⟩ measure the degree to which fluctuations at one position are correlated with fluctuations at another. Time-correlation functions are the temporal analog: C(t) = ⟨A(t)A(0)⟩ measures how strongly the value of an observable A at time t is correlated with its value at time 0. For a system in thermal equilibrium, this average is taken over the equilibrium ensemble, and by time-translation invariance, C depends only on the time difference t, not the absolute time.

The intuition is straightforward with a concrete example. Consider the velocity of a single molecule in a gas: A = vx(t). At t = 0, you know exactly what vx is (say, 3 m/s). At t = ε (a tiny instant later), the molecule hasn't been hit by anything yet, so vx is still close to 3 m/s: C(ε) ≈ C(0). After many collisions — a time of order the **collision time** τ_c — the molecule's velocity is randomized. It might now be anything; its current velocity bears no memory of the initial value. So C(t) → 0 as t → ∞ for an **ergodic** system (one that explores all accessible phase space). The correlation function thus decays from C(0) = ⟨vx²⟩ = kT/m (by equipartition) to zero on the timescale τ_c. The shape of the decay — exponential, power-law, oscillatory — encodes the relaxation physics.

The power of time-correlation functions is the **Green-Kubo relations**, which connect equilibrium fluctuations to transport coefficients. For example, the **diffusion coefficient** D = (1/3) ∫₀^∞ ⟨v(t)·v(0)⟩ dt is the time integral of the velocity autocorrelation function. This is remarkable: D is a non-equilibrium transport property (how fast a particle spreads in a diffusing cloud), but it can be computed entirely from equilibrium dynamics. Similarly, shear viscosity is the time integral of the stress-stress correlation function. This bridge between equilibrium fluctuations and non-equilibrium response is the **fluctuation-dissipation theorem** in action.

From your ensemble theory background, you know that equilibrium systems fluctuate around their mean values, with the fluctuation magnitude set by thermodynamic quantities. The fluctuation-dissipation theorem generalizes this: the same thermal fluctuations that cause equilibrium noise also determine how the system dissipates energy when perturbed from equilibrium. A system that fluctuates a lot (large C(0)) will also respond strongly to perturbations and have large transport coefficients, unless the fluctuations are very short-lived. The interplay between fluctuation magnitude C(0) and relaxation timescale τ determines transport. Time-correlation functions are the central mathematical object that makes this connection precise, and computing them — whether analytically, via mode-coupling theory, or numerically via molecular dynamics simulation — is a core activity in modern statistical physics.
