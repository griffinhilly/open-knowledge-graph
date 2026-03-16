---
id: h-theorem-irreversibility
title: H-Theorem and Irreversibility
domain: physics
course: statistical-mechanics
prerequisites:
- id: boltzmann-transport-equation
  type: hard
- id: entropy-intro
  type: hard
builds-toward:
- fluctuation-dissipation-theorem
tags:
- irreversibility
- entropy
- boltzmann-equation
stage: advanced
status: draft
---

# H-Theorem and Irreversibility

## Core Idea
Boltzmann's H-theorem states that H = ∫ d³r d³v f ln f monotonically decreases (dH/dt ≤ 0) until equilibrium is reached, where dH/dt = 0. This 'explains' the second law of thermodynamics and irreversibility from time-reversible microscopic dynamics via the assumption that collisions are uncorrelated (molecular chaos). The resolution of Loschmidt's paradox requires that initial conditions are non-generic.

## Explainer

From your study of the Boltzmann transport equation, you know how it governs the evolution of the phase-space distribution f(r, v, t) through free streaming and collisions. From your study of entropy, you know that the second law demands entropy to increase until equilibrium. Boltzmann's H-theorem makes this connection explicit and raises a profound paradox about time and irreversibility.

Define **H = ∫∫ f ln f d³r d³v** — essentially the negative of entropy: as H decreases, entropy increases. Boltzmann proved that under the Boltzmann equation with the **Stosszahlansatz** (molecular chaos assumption — that the velocities of two molecules about to collide are statistically uncorrelated), dH/dt ≤ 0 always, with equality only at equilibrium when f is a Maxwell-Boltzmann distribution. This appears to derive the second law from kinetic theory: an isolated gas inevitably approaches equilibrium, and H serves as a Lyapunov function guaranteeing convergence. The equilibrium condition dH/dt = 0 also pins down the form of f at equilibrium — exactly the Maxwell-Boltzmann distribution you know from statistical mechanics.

**Loschmidt's paradox** strikes at the heart of this argument. Newton's equations are time-reversible: if you take any trajectory and reverse all velocities at some instant, you get another valid trajectory that runs backward. If there exists a trajectory in which H decreases, then there also exists the time-reversed trajectory in which H increases — apparently contradicting the theorem. Boltzmann's resolution is that the **molecular chaos assumption breaks time-reversal symmetry**. The Stosszahlansatz says pre-collision velocities are uncorrelated; after a collision, the two particles carry correlated velocities. Reversing all velocities creates a state with post-collision correlations (a "special" initial condition), which violates the assumption. The theorem only applies when molecular chaos holds — and the time-reversed state, with its special correlations, violates it.

The deeper lesson is that irreversibility is not derivable from time-reversible mechanics alone. It requires a statistical assumption about initial conditions. The second law is not an absolute statement but a probabilistic one: states that violate it exist but are extraordinarily rare in phase space. A gas will eventually — by Poincaré recurrence — return arbitrarily close to any initial state (even a low-entropy one), but the recurrence time for a macroscopic system is astronomically longer than the age of the universe. The H-theorem establishes that for any macroscopically prepared initial state satisfying molecular chaos, the approach to equilibrium is overwhelmingly likely — which is, ultimately, all the second law claims.
