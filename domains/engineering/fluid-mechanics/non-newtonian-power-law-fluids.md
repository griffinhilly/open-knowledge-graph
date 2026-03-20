---
id: non-newtonian-power-law-fluids
title: Non-Newtonian Fluids and Power-Law Models
domain: engineering
course: fluid-mechanics
prerequisites:
- id: non-newtonian-fluids
  type: hard
- id: viscosity-and-newtonian-fluids
  type: soft
tags:
- non-newtonian
- power-law
- viscosity
stage: advanced
status: draft
---

# Non-Newtonian Fluids and Power-Law Models

## Core Idea
Non-Newtonian fluids exhibit shear-dependent viscosity; polymers, suspensions, and slurries are common examples. Power-law models τ = K(dV/dy)^n simplify analysis: n < 1 gives shear-thinning (viscosity decreases with shear rate), n > 1 gives shear-thickening. Friction factors, pressure drops, and flow rates deviate significantly from Newtonian predictions; modified correlations account for the behavior index and consistency index K.

## Explainer

Your prior study of Newtonian fluids established that shear stress and shear rate are proportional: τ = μ·(dV/dy), where μ is a constant that depends only on temperature and pressure, not on how fast you stir or pump the fluid. Water, air, and most simple liquids behave this way. But many important engineering fluids — polymer solutions, paints, blood, drilling muds, food products — violate this rule in a way that has dramatic practical consequences. The key insight is that for these fluids, the **apparent viscosity** (the ratio τ/(dV/dy) at any given moment) changes as the flow accelerates or decelerates.

The **power-law model** captures this behavior with two parameters: τ = K·(dV/dy)ⁿ. The **consistency index** K has units that depend on n and represents the fluid's overall resistance to flow — higher K means more viscous in a general sense. The **flow behavior index** n is the key diagnostic parameter. When n = 1, the model reduces exactly to Newtonian behavior with μ = K. When n < 1, the fluid is **shear-thinning** (also called pseudoplastic): apparent viscosity decreases as shear rate increases. Ketchup is the classic example — it barely moves when you tap the bottle gently (low shear rate, high apparent viscosity), but flows freely when you shake hard (high shear rate, low apparent viscosity). Polymer melts, blood at physiological shear rates, and most paints are shear-thinning. When n > 1, the fluid is **shear-thickening** (dilatant): it becomes more resistant to flow the harder you push. A cornstarch-water slurry is the vivid example — you can run across the surface of a deep enough pool of it but slowly sink if you stand still.

The molecular origin of shear-thinning is instructive: at rest, long polymer chains are randomly coiled and entangled, creating high resistance to flow. Under high shear, chains align with the flow direction and disentangle, reducing resistance. The molecular origin of shear-thickening is different: particles in suspension are normally lubricated by fluid between them, but at high shear rates this lubrication breaks down and particles jam together. Understanding which mechanism dominates tells you whether you should expect the behavior to be reversible when shear is removed (polymers re-coil rapidly; particle jamming is also reversible).

For engineering calculations, substituting τ = K·(dV/dy)ⁿ into the momentum equation for pipe flow yields a modified velocity profile that is no longer parabolic. The pressure drop for laminar power-law pipe flow requires a **generalized Reynolds number** Reₙ = ρV²⁻ⁿDⁿ/[K·8ⁿ⁻¹·((3n+1)/4n)ⁿ], which collapses the laminar friction factor back to f = 64/Reₙ — the same formula as Newtonian laminar flow, but with the modified Re. This generalization is why the power-law model is so useful in practice: it extends familiar Newtonian pipe-flow tools to a much wider class of fluids, at the cost of measuring two parameters (K and n) rather than one (μ). For turbulent non-Newtonian flow, the corrections are more complex and often require specialized empirical correlations, since the cascade of turbulent eddies interacts differently with shear-dependent viscosity.
