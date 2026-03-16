---
id: phase-transition-equilibrium
title: Phase Transitions and Equilibrium Phase Diagrams
domain: physics
course: statistical-mechanics
prerequisites:
- id: free-energy-thermodynamic-relations
  type: hard
- id: statistical-interpretation-of-entropy
  type: soft
builds-toward:
- critical-phenomena-statmech
- ising-model-statmech
- landau-theory-phase-transitions
tags:
- phase-transition
- coexistence
- clausius-clapeyron
stage: advanced
status: draft
---

# Phase Transitions and Equilibrium Phase Diagrams

## Core Idea
A phase transition occurs when a small change in control parameters (T, P, H) causes a discontinuous change in macroscopic properties. First-order transitions show discontinuities in density, entropy, or order parameter; second-order transitions have continuous order parameters but divergent susceptibilities. Free energy surfaces determine stability and govern the Clausius-Clapeyron equation for phase boundaries.

## Explainer

You already know that free energy — Helmholtz F = U − TS or Gibbs G = H − TS — determines the equilibrium state: a system at fixed T and V minimizes F, while at fixed T and P it minimizes G. Phase transitions occur when the free energy landscape changes topology as you tune a control parameter, causing the equilibrium state to jump discontinuously or acquire qualitatively new behavior.

For a **first-order transition** like liquid-gas vaporization, imagine plotting the Gibbs free energy G as a function of volume at fixed T and P. Below the boiling point, there is a single minimum corresponding to liquid; above it, the minimum shifts to larger volume (gas). Exactly at the boiling point, G has two minima of equal depth — both phases are equally stable, and **phase coexistence** is possible. A mixture of liquid and gas coexists, with the relative proportions adjusting to minimize total G while conserving total volume. The discontinuous jump in volume and entropy (S = −∂G/∂T|_P) at the transition is what defines it as "first-order." The entropy jump ΔS = L/T, where L is the latent heat, reflects the energy required to break intermolecular bonds and expand against pressure.

The **Clausius-Clapeyron equation** dP/dT = ΔS/ΔV = L/(TΔV) governs the slope of coexistence curves in P-T phase diagrams. Its derivation follows from a simple thermodynamic argument: along the coexistence curve, both phases have equal Gibbs free energy G_liq = G_gas, so as T and P change together along the curve, dG_liq = dG_gas, giving −S_liq dT + V_liq dP = −S_gas dT + V_gas dP, which rearranges to the equation. The positive slope of liquid-gas coexistence (higher pressure raises the boiling point) and the anomalous negative slope for water's solid-liquid transition (pressure melts ice) both follow directly from the sign of ΔV.

**Second-order (continuous) transitions** are qualitatively different. Near a magnetic Curie point, the magnetization (the **order parameter**) decreases continuously to zero — no discontinuous jump, no latent heat. Instead, the free energy has a single minimum whose location shifts continuously to zero as T approaches the critical temperature T_c from below. What diverges is not the order parameter itself but its susceptibility (response to external fields) and the correlation length — the spatial scale over which fluctuations are correlated. Near T_c, this length diverges, producing large fluctuations at all scales, visible as critical opalescence in fluid systems. Phase diagrams encode all of this structure: each line is a first-order boundary, each endpoint is a critical point where the transition becomes second-order, and the topology of the diagram reflects the underlying free energy landscape.
