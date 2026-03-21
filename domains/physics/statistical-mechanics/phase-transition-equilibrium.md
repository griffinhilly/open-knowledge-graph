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

## Questions

```yaml
- question: "At the liquid-gas coexistence curve (boiling point), both liquid and gas phases coexist. What determines the fraction of the system that is in the gas phase?"
  type: multiple-choice
  options:
    - "The temperature alone — the fraction is fixed at each temperature"
    - "The pressure alone — higher pressure means more liquid"
    - "The total volume of the system — the fraction adjusts to satisfy volume conservation at equal Gibbs free energy"
    - "Random fluctuations — the system constantly shifts between all-liquid and all-gas"
  answer: 2
  explanation: "At the coexistence point, G has two equal-depth minima (liquid and gas). The actual fraction in each phase is determined by the lever rule: the total volume of the system must be conserved as it partitions between the two phases at their respective specific volumes. A container with more total volume at fixed temperature will have more gas; less volume means more liquid. Temperature alone doesn't fix the fraction — it only fixes the coexistence condition (equal G). This is why a pressure cooker at its rated pressure contains liquid water as long as liquid remains."

- question: "Why does increasing pressure lower the melting point of ice, while increasing pressure raises the boiling point of water?"
  type: multiple-choice
  options:
    - "Ice is less dense than liquid water, so ΔV < 0 for melting; liquid water is less dense than steam, so ΔV > 0 for vaporization"
    - "The Clausius-Clapeyron equation only applies to liquid-gas transitions"
    - "Ice and water have the same density, so the slope is governed by latent heat alone"
    - "The anomaly arises because ice has lower entropy than water"
  answer: 0
  explanation: "The Clausius-Clapeyron equation dP/dT = ΔS/ΔV = L/(TΔV) shows that the sign of the coexistence curve slope depends on the sign of ΔV. For the solid-liquid transition of water, ice is less dense than liquid water, so melting increases density and ΔV = V_liquid − V_ice < 0. This gives a negative slope: increasing pressure lowers the melting point. For liquid-gas, gas is far less dense than liquid (ΔV > 0), giving a positive slope: increasing pressure raises the boiling point. This is not an anomaly requiring special explanation — it follows directly from the equation and the known density ordering."

- question: "A second-order phase transition involves a discontinuous jump in the order parameter (e.g., magnetization drops abruptly to zero at the Curie temperature)."
  type: true-false
  answer: false
  explanation: "This is the defining difference between first-order and second-order transitions. In a second-order (continuous) transition, the order parameter decreases *continuously* to zero as the critical temperature is approached — no abrupt jump, no latent heat, no phase coexistence. What diverges at a second-order transition is not the order parameter but its *susceptibility* (response to external fields) and the correlation length. A first-order transition like melting does show a discontinuous jump in density and entropy."

- question: "Near a second-order critical point, both the susceptibility and the correlation length diverge, even though the order parameter itself goes smoothly to zero."
  type: true-false
  answer: true
  explanation: "This is precisely what characterizes a second-order transition and distinguishes it from smooth crossovers. As T → T_c, the free energy curvature flattens — the system becomes infinitely responsive to small perturbations (divergent susceptibility). The correlation length — the scale over which fluctuations are correlated — also diverges, meaning fluctuations occur on all length scales simultaneously. This scale-invariance at the critical point is responsible for critical opalescence: light scatters off density fluctuations at all scales, making the fluid appear milky."

- question: "Explain how the Clausius-Clapeyron equation is derived, and what physical insight does it capture about coexistence curves?"
  type: short-answer
  answer: "Along a coexistence curve, both phases have equal Gibbs free energy: G_A = G_B. As T and P vary together along the curve, dG_A = dG_B, which gives −S_A dT + V_A dP = −S_B dT + V_B dP. Rearranging: dP/dT = (S_A − S_B)/(V_A − V_B) = ΔS/ΔV = L/(TΔV). The equation captures that phase boundaries in P-T space are not arbitrary lines but are determined by the competition between entropy gain and volume change accompanying the transition."
  explanation: "The derivation uses only the condition of equal Gibbs free energy along the coexistence curve — no detailed molecular model is needed. The result encodes two key insights: the slope of the coexistence curve depends on the ratio of latent heat to volume change, and the sign of ΔV determines whether increased pressure favors the denser phase (raises its transition temperature) or the less dense phase (lowers it). Water's anomalous negative melting-point slope is explained entirely by the fact that ice is less dense than liquid water."
```

## Explainer

You already know that free energy — Helmholtz F = U − TS or Gibbs G = H − TS — determines the equilibrium state: a system at fixed T and V minimizes F, while at fixed T and P it minimizes G. Phase transitions occur when the free energy landscape changes topology as you tune a control parameter, causing the equilibrium state to jump discontinuously or acquire qualitatively new behavior.

For a **first-order transition** like liquid-gas vaporization, imagine plotting the Gibbs free energy G as a function of volume at fixed T and P. Below the boiling point, there is a single minimum corresponding to liquid; above it, the minimum shifts to larger volume (gas). Exactly at the boiling point, G has two minima of equal depth — both phases are equally stable, and **phase coexistence** is possible. A mixture of liquid and gas coexists, with the relative proportions adjusting to minimize total G while conserving total volume. The discontinuous jump in volume and entropy (S = −∂G/∂T|_P) at the transition is what defines it as "first-order." The entropy jump ΔS = L/T, where L is the latent heat, reflects the energy required to break intermolecular bonds and expand against pressure.

The **Clausius-Clapeyron equation** dP/dT = ΔS/ΔV = L/(TΔV) governs the slope of coexistence curves in P-T phase diagrams. Its derivation follows from a simple thermodynamic argument: along the coexistence curve, both phases have equal Gibbs free energy G_liq = G_gas, so as T and P change together along the curve, dG_liq = dG_gas, giving −S_liq dT + V_liq dP = −S_gas dT + V_gas dP, which rearranges to the equation. The positive slope of liquid-gas coexistence (higher pressure raises the boiling point) and the anomalous negative slope for water's solid-liquid transition (pressure melts ice) both follow directly from the sign of ΔV.

**Second-order (continuous) transitions** are qualitatively different. Near a magnetic Curie point, the magnetization (the **order parameter**) decreases continuously to zero — no discontinuous jump, no latent heat. Instead, the free energy has a single minimum whose location shifts continuously to zero as T approaches the critical temperature T_c from below. What diverges is not the order parameter itself but its susceptibility (response to external fields) and the correlation length — the spatial scale over which fluctuations are correlated. Near T_c, this length diverges, producing large fluctuations at all scales, visible as critical opalescence in fluid systems. Phase diagrams encode all of this structure: each line is a first-order boundary, each endpoint is a critical point where the transition becomes second-order, and the topology of the diagram reflects the underlying free energy landscape.
