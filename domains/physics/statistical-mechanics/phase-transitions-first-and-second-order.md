---
id: phase-transitions-first-and-second-order
title: 'Phase Transitions: First Order and Second Order'
domain: physics
course: statistical-mechanics
prerequisites:
- id: gibbs-free-energy
  type: hard
- id: helmholtz-free-energy
  type: soft
builds-toward:
- critical-phenomena-critical-exponents
- landau-theory
tags:
- phase-transitions
- thermodynamics
- classification
stage: advanced
status: draft
---

# Phase Transitions: First Order and Second Order

## Core Idea
First-order transitions (e.g., liquid-gas) involve a discontinuous jump in density and latent heat; Gibbs free energy is continuous but its first derivatives (entropy, volume) are discontinuous. Second-order transitions (e.g., ferromagnetic) show no latent heat or density jump; Gibbs energy and its first derivative are continuous, but second derivatives diverge.

## Explainer

Phase transitions are among the most striking phenomena in nature: a substance abruptly changes character — liquid to gas, paramagnet to ferromagnet, normal metal to superconductor — at a precise temperature and pressure. The Ehrenfest classification organizes this diversity into two fundamental categories based on which derivatives of the **Gibbs free energy** G(T, P) are discontinuous at the transition point.

For a **first-order transition**, G itself is continuous across the transition (if it weren't, the system wouldn't choose that point), but its first partial derivatives are discontinuous. Since S = −(∂G/∂T)_P and V = (∂G/∂P)_T, a discontinuous first derivative means a jump in entropy — which is the **latent heat** L = TΔS — and a jump in volume (density change). This is the familiar liquid-gas transition: when water boils at 100°C, it absorbs 2260 J/g of latent heat while its density drops by a factor of ~1600. The two phases coexist along the transition curve, with equal Gibbs free energies. Moving along the coexistence curve toward the **critical point**, the latent heat and density jump shrink continuously, reaching zero at the critical point — where the transition changes character entirely.

A **second-order transition** (also called a **continuous transition**) has no latent heat and no coexistence: the system transforms smoothly in the sense that the **order parameter** — the quantity that characterizes the ordered phase — grows continuously from zero rather than jumping. For a ferromagnet, the order parameter is spontaneous magnetization, which appears below the Curie temperature and grows continuously. However, the second derivatives of G diverge at the transition: the heat capacity C_P = −T(∂²G/∂T²)_P and the compressibility κ_T = −(1/V)(∂²G/∂P²)_T both blow up. This divergence reflects the growth of fluctuations: near a second-order transition, fluctuations occur at all length scales simultaneously, making the system **scale-invariant** and the correlation length infinite.

The free energy framework unifies both cases with a single geometric picture. At a first-order transition, the G(T) curves for two phases cross: each phase has lower G in its own stability region, and they are equal exactly on the coexistence line. At a second-order transition, G approaches the same value from both phases continuously, with matching first derivatives. The practical diagnostic is straightforward: if heating a substance causes it to absorb latent heat at a fixed temperature (with coexisting phases), the transition is first-order. If instead the heat capacity diverges sharply without a finite latent heat, it is second-order. Both types are driven by the competition between energy, which favors ordered states, and entropy, which favors disorder — encoded together in the free energy G = H − TS.
