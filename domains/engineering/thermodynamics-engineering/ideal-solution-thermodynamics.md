---
id: ideal-solution-thermodynamics
title: Ideal and Non-ideal Solution Behavior
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: partial-molar-properties-solutions
  type: hard
- id: chemical-equilibrium-reaction-analysis
  type: soft
builds-toward:
- gibbs-phase-rule-multicomponent
tags:
- ideal-solution
- raoults-law
- activity-coefficient
- non-ideal
- mixing
stage: advanced
status: draft
---

# Ideal and Non-ideal Solution Behavior

## Core Idea
Ideal solutions follow Raoult's law and require no heat of mixing. Real solutions exhibit deviations quantified by activity coefficients γᵢ; fugacity f̄ᵢ = γᵢ xᵢ fᵢ replaces partial pressure. Common models (Wilson, NRTL, UNIQUAC) predict liquid-liquid and vapor-liquid equilibrium based on component interactions, critical for distillation and extraction design.

## Explainer

From partial molar properties, you know that the chemical potential of component i in a mixture is μᵢ = μᵢ° + RT ln(aᵢ), where aᵢ is the **activity** — a dimensionless measure of how "active" the component is compared to a reference state. The key question is how activity relates to composition. The answer depends on whether the solution is ideal.

An **ideal solution** is one where every molecule experiences the same intermolecular forces regardless of its neighbors. This means mixing is purely entropic — there is no enthalpy of mixing (ΔH_mix = 0) and the volume doesn't change on mixing (ΔV_mix = 0). Under these conditions, **Raoult's law** holds: the partial pressure of component i above the solution equals its mole fraction times its pure-component saturation pressure, pᵢ = xᵢ Pᵢˢᵃᵗ. Activity coefficients γᵢ are all equal to 1. Ideal behavior is a reasonable approximation for mixtures of chemically similar species (e.g., benzene + toluene, or isotopes), but most engineering systems deviate significantly.

Real solutions have **non-unity activity coefficients**. If molecules of different species repel each other more than like molecules do (weaker cross-interactions), the vapor pressure exceeds the Raoult's law prediction — a **positive deviation** (γᵢ > 1). The liquid molecules prefer to escape into the vapor. If cross-interactions are stronger than like-interactions (e.g., hydrogen bonding between different species), vapor pressures fall below Raoult's law — **negative deviation** (γᵢ < 1). The activity coefficient captures this departure: the fugacity in the liquid phase is f̄ᵢ = γᵢ xᵢ fᵢ, where fᵢ is the pure-component fugacity.

The engineering consequences are large. **Azeotropes** occur when the vapor and liquid compositions become equal — no further separation is possible by simple distillation. For a positive-deviation binary mixture, the total vapor pressure has a maximum above what Raoult's law predicts; at that composition, the mixture boils at a temperature lower than either pure component (**minimum-boiling azeotrope**). The ethanol-water system at 95.6 mol% ethanol (78.1°C at 1 atm) is the canonical example — this is why absolute alcohol cannot be made by distillation alone. Negative-deviation systems form **maximum-boiling azeotropes** (the HCl-water azeotrope at 20.2% HCl, 108.6°C). Activity coefficient models like Wilson, NRTL, and UNIQUAC fit experimental phase equilibrium data and extrapolate to other conditions, making them the workhorses of distillation design software.
