---
id: van-t-hoff-equation
title: "The van't Hoff Equation: Temperature Dependence of Equilibrium"
domain: chemistry
course: physical-chemistry
prerequisites:
- id: statistical-thermodynamics-applications
  type: hard
builds-toward: []
tags:
- van-t-Hoff
- equilibrium-constant
- temperature-dependence
- Le-Chatelier
- enthalpy-of-reaction
- thermodynamic-equilibrium
stage: advanced
status: draft
---

# The van't Hoff Equation: Temperature Dependence of Equilibrium

## Core Idea
The van't Hoff equation d(ln K)/dT = Delta_H_std/(R*T^2) quantifies how the equilibrium constant K changes with temperature, providing the quantitative foundation for Le Chatelier's principle. For an endothermic reaction (Delta_H > 0), K increases with temperature; for exothermic (Delta_H < 0), K decreases. The integrated form ln(K2/K1) = -(Delta_H/R)(1/T2 - 1/T1) assumes Delta_H is approximately constant over the temperature range and enables prediction of K at any temperature from a single measured value. A van't Hoff plot of ln K vs 1/T yields a straight line with slope -Delta_H/R when enthalpy is temperature-independent; curvature indicates significant Delta_Cp, requiring the Kirchhoff equation correction. This relationship connects macroscopic equilibrium measurements directly to molecular-level energetics.

## How It's Best Learned
Collect or look up equilibrium constant data for a reaction at multiple temperatures (e.g., the dissociation of N2O4 or the solubility of a sparingly soluble salt). Construct the van't Hoff plot, extract Delta_H from the slope, and verify consistency with calorimetric measurements.

## Common Misconceptions
- Assuming Delta_H is always temperature-independent; for reactions with large Delta_Cp (heat capacity changes), the van't Hoff plot curves and the simple two-point integrated form becomes inaccurate.
- Confusing the van't Hoff equation with the Arrhenius equation; the former relates K (equilibrium) to temperature while the latter relates k (rate constant) to temperature -- they have similar mathematical forms but describe fundamentally different quantities.

## Explainer

From statistical thermodynamics, you know that the equilibrium constant K is related to the standard Gibbs energy change by ΔG° = −RT ln K. This relationship tells you *where* equilibrium lies at a given temperature, but it does not tell you what happens when you change the temperature. The **van't Hoff equation** fills that gap. By differentiating the Gibbs-temperature relationship with respect to T and applying the Gibbs-Helmholtz equation, you arrive at d(ln K)/dT = ΔH°/(RT²). This elegant result says that the rate at which the equilibrium constant changes with temperature depends on the enthalpy of reaction — and nothing else (assuming ΔH° is roughly constant).

The intuition is thermodynamic. For an **endothermic reaction** (ΔH° > 0), the products are energetically uphill. Raising the temperature provides more thermal energy to climb that hill, so the equilibrium shifts toward products — K increases. For an **exothermic reaction** (ΔH° < 0), the products are energetically downhill, and raising the temperature makes the reverse (endothermic) direction more favorable — K decreases. This is exactly Le Chatelier's principle, but now you have a quantitative equation rather than a qualitative rule. You can calculate *how much* K changes for a given temperature change, not just the direction.

The **integrated form** ln(K₂/K₁) = −(ΔH°/R)(1/T₂ − 1/T₁) is what you will use most often in practice. Given K at one temperature and the enthalpy of reaction, you can predict K at any other temperature. The key assumption is that ΔH° does not change significantly over the temperature range — a reasonable approximation for modest intervals but one that breaks down over hundreds of degrees. When you plot ln K versus 1/T (a **van't Hoff plot**), a straight line confirms that ΔH° is effectively constant, and the slope equals −ΔH°/R. Curvature in the plot signals that the heat capacities of products and reactants differ appreciably, requiring the Kirchhoff equation to account for how ΔH° itself varies with temperature.

A common source of confusion is the superficial resemblance to the **Arrhenius equation**, ln k = −Eₐ/(RT) + constant, which looks almost identical. But these equations describe fundamentally different quantities: van't Hoff governs K (the equilibrium constant — a thermodynamic quantity reflecting the ratio of product to reactant concentrations at equilibrium), while Arrhenius governs k (the rate constant — a kinetic quantity reflecting how fast a reaction proceeds). A reaction can have a large K (thermodynamically favorable) but a tiny k (kinetically slow), or vice versa. The van't Hoff equation tells you nothing about reaction speed; it tells you only about the final balance between forward and reverse reactions once the system has had time to reach equilibrium.
