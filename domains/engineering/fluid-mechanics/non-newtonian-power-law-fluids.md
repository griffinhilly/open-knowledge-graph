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
stage: formal-systems
status: validated
---

# Non-Newtonian Fluids and Power-Law Models

## Core Idea
Non-Newtonian fluids exhibit shear-dependent viscosity; polymers, suspensions, and slurries are common examples. Power-law models τ = K(dV/dy)^n simplify analysis: n < 1 gives shear-thinning (viscosity decreases with shear rate), n > 1 gives shear-thickening. Friction factors, pressure drops, and flow rates deviate significantly from Newtonian predictions; modified correlations account for the behavior index and consistency index K.

## Questions

```yaml
- question: "You tap a ketchup bottle gently and nothing flows out. You shake it hard and ketchup flows freely. Which power-law behavior does this demonstrate, and what is the value of n relative to 1?"
  type: multiple-choice
  options:
    - "Shear-thickening (dilatant), n > 1 — harder shaking increases viscosity, eventually overcoming friction"
    - "Shear-thinning (pseudoplastic), n < 1 — higher shear rate reduces apparent viscosity, allowing flow"
    - "Newtonian, n = 1 — the viscosity is constant, but the applied force must exceed a yield stress"
    - "Shear-thickening, n < 1 — n less than 1 means more resistance at higher shear"
  answer: 1
  explanation: "Ketchup is a classic shear-thinning fluid. At rest (low shear rate), polymer chains and particles are randomly arranged and entangled, producing high apparent viscosity — ketchup won't pour. Under high shear (hard shaking), chains align with the flow direction and disentangle, dramatically reducing apparent viscosity — ketchup flows easily. In the power-law model τ = K(dV/dy)ⁿ, the apparent viscosity is τ/(dV/dy) = K(dV/dy)^(n-1). For n < 1, this decreases as shear rate increases — shear-thinning. Option D has the logic backwards: n < 1 means shear-thinning, not shear-thickening."

- question: "A cornstarch-water slurry (oobleck) behaves as a nearly solid surface when struck quickly but flows like a liquid when touched gently. What does this tell you about n in the power-law model?"
  type: multiple-choice
  options:
    - "n < 1, because the fluid resists fast motion more than slow motion"
    - "n = 1, because the fluid has a single well-defined viscosity"
    - "n > 1, because apparent viscosity increases with shear rate — the fluid becomes more resistant as you push harder or faster"
    - "n = 0, because the shear stress is independent of shear rate"
  answer: 2
  explanation: "Oobleck is shear-thickening (dilatant): resistance increases with shear rate. In the power-law model, apparent viscosity = K(dV/dy)^(n-1). For n > 1, this quantity increases with shear rate — you encounter more resistance the faster you try to move through the fluid. The physical mechanism is particle jamming: at high shear rates, the fluid lubricating particles breaks down and they jam together, increasing resistance. At low shear rates, particles remain dispersed and lubricated, so the fluid flows readily. This is the opposite of ketchup's behavior."

- question: "A shear-thinning fluid has a lower apparent viscosity at high shear rates than at low shear rates."
  type: true-false
  answer: true
  explanation: "This is the defining characteristic of shear-thinning (pseudoplastic) behavior, corresponding to n < 1 in the power-law model. Apparent viscosity, defined as the ratio τ/(dV/dy) at a given shear rate, equals K(dV/dy)^(n-1). When n < 1, the exponent (n-1) is negative, so apparent viscosity decreases as shear rate increases. This is why polymer solutions, paints, and blood are easier to pump at high flow rates than at low flow rates — a practically important property for processing and circulatory design."

- question: "In the power-law model τ = K(dV/dy)^n, a Newtonian fluid corresponds to n = 0, and the consistency index K equals the dynamic viscosity."
  type: true-false
  answer: false
  explanation: "Newtonian behavior corresponds to n = 1, not n = 0. When n = 1, the power-law model reduces to τ = K(dV/dy)^1 = K(dV/dy), which is identical to Newton's law of viscosity τ = μ(dV/dy) with μ = K. At n = 0, the shear stress would equal K regardless of shear rate — that would describe a perfectly rigid solid or a Bingham-plastic at yield, not a Newtonian fluid. The consistency index K has units that depend on n (not the standard Pa·s of dynamic viscosity unless n = 1), so equating K to viscosity is only valid at n = 1."

- question: "What physical mechanism causes polymer solutions to be shear-thinning, and how does this differ from the mechanism causing cornstarch-water suspensions to be shear-thickening?"
  type: short-answer
  answer: "In polymer solutions, long chain molecules are randomly coiled and entangled at rest, creating high resistance. Under shear, chains uncoil and align with the flow direction, reducing entanglement and lowering apparent viscosity — shear-thinning results. This process is largely reversible: remove the shear and chains re-coil. In cornstarch-water (and dense particle suspensions generally), particles are normally separated by a thin lubricating fluid layer. At high shear rates, this lubrication breaks down and particles come into direct frictional contact or jam together, dramatically increasing resistance — shear-thickening results. Both mechanisms are reversible when shear is removed, but they arise from completely different microstructural physics: molecular conformation change (polymers) versus particle contact forces (suspensions)."
  explanation: "Understanding the mechanism matters for engineering applications. A shear-thinning polymer solution becomes easier to pump at higher flow rates — an advantage. A shear-thickening suspension becomes nearly impossible to pump if shear rate exceeds a critical threshold — a hazard. Knowing the mechanism also predicts temperature sensitivity, time-dependence (thixotropy vs. rheopexy), and how to modify the behavior through formulation changes."
```

## Explainer

Your prior study of Newtonian fluids established that shear stress and shear rate are proportional: τ = μ·(dV/dy), where μ is a constant that depends only on temperature and pressure, not on how fast you stir or pump the fluid. Water, air, and most simple liquids behave this way. But many important engineering fluids — polymer solutions, paints, blood, drilling muds, food products — violate this rule in a way that has dramatic practical consequences. The key insight is that for these fluids, the **apparent viscosity** (the ratio τ/(dV/dy) at any given moment) changes as the flow accelerates or decelerates.

The **power-law model** captures this behavior with two parameters: τ = K·(dV/dy)ⁿ. The **consistency index** K has units that depend on n and represents the fluid's overall resistance to flow — higher K means more viscous in a general sense. The **flow behavior index** n is the key diagnostic parameter. When n = 1, the model reduces exactly to Newtonian behavior with μ = K. When n < 1, the fluid is **shear-thinning** (also called pseudoplastic): apparent viscosity decreases as shear rate increases. Ketchup is the classic example — it barely moves when you tap the bottle gently (low shear rate, high apparent viscosity), but flows freely when you shake hard (high shear rate, low apparent viscosity). Polymer melts, blood at physiological shear rates, and most paints are shear-thinning. When n > 1, the fluid is **shear-thickening** (dilatant): it becomes more resistant to flow the harder you push. A cornstarch-water slurry is the vivid example — you can run across the surface of a deep enough pool of it but slowly sink if you stand still.

The molecular origin of shear-thinning is instructive: at rest, long polymer chains are randomly coiled and entangled, creating high resistance to flow. Under high shear, chains align with the flow direction and disentangle, reducing resistance. The molecular origin of shear-thickening is different: particles in suspension are normally lubricated by fluid between them, but at high shear rates this lubrication breaks down and particles jam together. Understanding which mechanism dominates tells you whether you should expect the behavior to be reversible when shear is removed (polymers re-coil rapidly; particle jamming is also reversible).

For engineering calculations, substituting τ = K·(dV/dy)ⁿ into the momentum equation for pipe flow yields a modified velocity profile that is no longer parabolic. The pressure drop for laminar power-law pipe flow requires a **generalized Reynolds number** Reₙ = ρV²⁻ⁿDⁿ/[K·8ⁿ⁻¹·((3n+1)/4n)ⁿ], which collapses the laminar friction factor back to f = 64/Reₙ — the same formula as Newtonian laminar flow, but with the modified Re. This generalization is why the power-law model is so useful in practice: it extends familiar Newtonian pipe-flow tools to a much wider class of fluids, at the cost of measuring two parameters (K and n) rather than one (μ). For turbulent non-Newtonian flow, the corrections are more complex and often require specialized empirical correlations, since the cascade of turbulent eddies interacts differently with shear-dependent viscosity.
