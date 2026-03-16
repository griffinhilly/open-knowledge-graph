---
id: critical-phenomena-statmech
title: Critical Phenomena and Singularities
domain: physics
course: statistical-mechanics
prerequisites:
- id: phase-transition-equilibrium
  type: hard
- id: free-energy-thermodynamic-relations
  type: soft
builds-toward:
- critical-exponents
- renormalization-group-scaling
- scaling-invariance-universality
tags:
- critical-point
- singularities
- divergences
stage: advanced
status: draft
---

# Critical Phenomena and Singularities

## Core Idea
Near a critical point (T_c, P_c), thermodynamic quantities diverge: heat capacity, compressibility, and susceptibilities all diverge with characteristic power laws. The correlation length ξ → ∞, signaling long-range order correlations. These singularities cannot be predicted by mean-field theory alone and require understanding of fluctuations at all length scales.

## Explainer

Near a phase transition, you've seen that free energy and thermodynamic quantities change continuously or discontinuously depending on the transition order. Critical phenomena are about what happens *exactly* at the transition between phases — and the answer is strange: quantities don't just change, they diverge or vanish following power laws that are the same across wildly different physical systems.

The central quantity is the **correlation length** ξ, which measures how far apart two parts of a system can be and still influence each other statistically. Far from the critical temperature Tc, ξ is finite — a local fluctuation decays exponentially with distance. As you approach Tc from either side, ξ grows: ξ ~ |T − Tc|^{−ν}. At exactly Tc, ξ diverges — the entire system is correlated at all length scales simultaneously. This scale invariance is the defining feature of a critical point and is why power laws, which have no characteristic scale, appear everywhere.

The diverging correlation length forces other thermodynamic quantities to diverge too. The heat capacity C ~ |T − Tc|^{−α} diverges because fluctuations at every scale contribute to the energy. The susceptibility (for a magnet, how easily magnetization responds to an applied field) χ ~ |T − Tc|^{−γ} diverges because the system is maximally sensitive to perturbations — a tiny field can flip correlations across the entire sample. These exponents α, γ, ν are called **critical exponents**. The remarkable fact of **universality** is that they depend only on the symmetry of the order parameter and the spatial dimensionality of the system — not on microscopic details. Water near its liquid-gas critical point and iron near its Curie temperature have the same critical exponents, even though their microscopic physics is completely different.

Mean-field theory, which you've used to approximate thermodynamic behavior, predicts specific exponent values (γ = 1, ν = 1/2) that work well in high dimensions but fail badly in two and three dimensions. The failure is physical: mean-field theory ignores fluctuations by replacing all interactions with an average field. Near the critical point, fluctuations at all scales are enormous — ξ → ∞ means there is no short-distance cutoff, no scale you can ignore. The breakdown of mean-field theory is a signal that the critical point demands a framework that handles all length scales simultaneously, which is exactly what the renormalization group provides.
