---
id: bose-gas-ideal-quantum
title: The Ideal Bose Gas and Critical Temperature
domain: physics
course: statistical-mechanics
prerequisites:
- id: bose-einstein-distribution-statistics
  type: hard
- id: grand-canonical-ensemble
  type: soft
builds-toward:
- bose-einstein-condensation-statmech
- planck-distribution-blackbody
tags:
- bose-gas
- quantum-degeneracy
- thermal-wavelength
stage: advanced
status: draft
---

# The Ideal Bose Gas and Critical Temperature

## Core Idea
An ideal Bose gas exhibits a critical temperature T_c below which macroscopic occupation of the ground state begins. Above T_c, the gas behaves as an ordinary quantum fluid. Below T_c, a fraction of particles 'condenses' into the zero-momentum state, and the system's thermodynamic properties change discontinuously—a signature of a phase transition.

## How It's Best Learned
Compute the density of states for a free Bose gas and derive the condition for condensation by solving for when the total number of particles in excited states reaches its maximum. Sketch how heat capacity and chemical potential change across T_c.

## Common Misconceptions
Bose-Einstein condensation is not a transition to liquid or solid; it is purely a quantum statistical effect in the ideal gas model. The condensed fraction occupies a single quantum state but spreads throughout the volume, not localized in space.

## Explainer

From the Bose-Einstein distribution, you know that bosons — particles with integer spin — have no restriction on how many can occupy a single quantum state. The mean occupation of a state with energy ε is ⟨n⟩ = 1/[exp((ε − μ)/kT) − 1]. For this to be non-negative, the chemical potential μ must be less than the ground state energy (taken as zero for a free gas), so μ ≤ 0 always. As temperature decreases at fixed density, the system must accommodate the same number of particles in fewer thermally accessible states. The chemical potential μ creeps upward toward zero. The question is: what happens when μ actually reaches zero?

When μ → 0⁻, the occupation of the ground state (ε = 0) becomes ⟨n₀⟩ = 1/[exp(−μ/kT) − 1] → ∞. This divergence signals the **critical temperature** T_c. Below T_c, the ground state can soak up an unlimited number of particles — it becomes **macroscopically occupied**. The number of particles the excited states can hold is bounded: it equals N_excited = N(T/T_c)^{3/2} for a 3D free Bose gas. Any particles above this capacity spill into the ground state. The fraction in the ground state is N₀/N = 1 − (T/T_c)^{3/2}, rising from zero at T_c to unity at absolute zero. This is **Bose-Einstein condensation** (BEC).

The grand canonical ensemble (your other prerequisite) is essential for computing T_c. You set μ = 0 and ask: what is the maximum density of particles that can be distributed among excited states? This is the integral ∫₀^∞ g(ε) · ⟨n(ε)⟩ dε, where g(ε) is the density of states for a 3D free particle, proportional to ε^{1/2}. Evaluating this integral gives n_c = ζ(3/2) / λ³, where λ = h/√(2πmkT) is the **thermal de Broglie wavelength** and ζ(3/2) ≈ 2.612 is a Riemann zeta function value. Condensation occurs when the actual density exceeds n_c — equivalently, when the interparticle spacing becomes comparable to λ, meaning quantum wave packets start to overlap.

The signature of BEC in thermodynamic observables is a **kink** in the heat capacity at T_c. Above T_c, C_V ~ T^{3/2} (a smooth quantum correction to the classical ideal gas); below T_c, C_V ~ T^{3/2} as well but with a different coefficient, so the heat capacity is continuous but its derivative is not — a second-order phase transition. The chemical potential stays pinned at zero for all T < T_c. This pinning is the tell-tale sign of condensation: μ cannot decrease further because the ground state is acting as an infinite reservoir absorbing whatever particles are excess. BEC was first achieved experimentally in ultracold dilute alkali atoms in 1995, confirming a prediction made by Einstein in 1924 — seventy years after the original theoretical proposal.
