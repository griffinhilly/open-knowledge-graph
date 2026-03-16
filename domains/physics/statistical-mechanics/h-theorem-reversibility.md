---
id: h-theorem-reversibility
title: The H-Theorem and the Arrow of Time
domain: physics
course: statistical-mechanics
prerequisites:
- id: boltzmann-transport-equation
  type: hard
- id: statistical-interpretation-of-entropy
  type: soft
builds-toward:
- non-equilibrium-basics-statmech
tags:
- h-theorem
- entropy-increase
- irreversibility
stage: advanced
status: draft
---

# The H-Theorem and the Arrow of Time

## Core Idea
Boltzmann's H-theorem shows that the quantity H = ∫ f ln(f) dv is monotonically decreasing under the Boltzmann equation, as long as collisions respect molecular chaos. Since entropy S = -k H, this explains the microscopic origin of the second law: irreversibility emerges from the statistics of many collisions, not from time-reversal violation at the microscopic level.

## Explainer

One of the deepest puzzles in physics is explaining why time has a preferred direction. The microscopic laws of physics — Newton's equations, quantum mechanics — are time-reversal symmetric: any valid mechanical trajectory run backward is also a valid trajectory. Yet we observe irreversibility everywhere: heat flows from hot to cold, gases expand to fill containers, broken eggs don't spontaneously reassemble. Boltzmann's **H-theorem** is the first rigorous bridge between reversible microscopic dynamics and irreversible macroscopic behavior.

The context is the **Boltzmann transport equation**, which governs the single-particle distribution function f(v, t) — the probability density for a molecule to have velocity v at time t. Boltzmann defined H = ∫ f ln(f) d³v and showed, using the collision integral, that dH/dt ≤ 0 as long as collisions satisfy **molecular chaos** (the Stosszahlansatz): the velocities of two colliding molecules are uncorrelated before they collide. Since entropy S = −kH, entropy can only increase — recovering the second law from molecular collisions. The minimum of H (maximum entropy) corresponds exactly to the **Maxwell-Boltzmann distribution**, the equilibrium velocity distribution. The H-theorem explains why any non-equilibrium distribution evolves toward Maxwell-Boltzmann: it is the unique fixed point of the collision dynamics.

The derivation's key assumption — molecular chaos — is also its vulnerability. Loschmidt's **reversibility paradox** followed immediately: take a gas that has just equilibrated (H at its minimum) and reverse all velocities. The system will evolve backward, and H must increase — apparently contradicting the theorem. Boltzmann's response is subtle but correct: the reversed initial condition is extraordinarily special. It corresponds to a single finely tuned microstate designed to maximize future correlations between colliding pairs, violating molecular chaos from the outset. In contrast, a gas prepared in any typical out-of-equilibrium state has uncorrelated molecular velocities, validating the molecular chaos assumption and the monotonic decrease of H.

The resolution is statistical: the second law is not a consequence of time-asymmetric microscopic laws, but of the **overwhelming probability** of high-entropy configurations. There are vastly more microstates corresponding to equilibrium than to any particular ordered arrangement. Starting from a low-entropy state, almost all microscopic trajectories lead to higher entropy — not because entropy must increase, but because nearly all neighboring microstates are higher entropy. The H-theorem makes this precise and quantitative: under typical (uncorrelated) collision dynamics, the distribution inevitably relaxes toward the overwhelmingly probable Maxwell-Boltzmann form. The arrow of time is statistical, not fundamental.
