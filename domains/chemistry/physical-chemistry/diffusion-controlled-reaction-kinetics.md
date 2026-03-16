---
id: diffusion-controlled-reaction-kinetics
title: Diffusion-Controlled Reaction Kinetics
domain: chemistry
course: physical-chemistry
prerequisites:
- id: collision-theory-advanced-kinetics
  type: hard
- id: diffusion-and-ficks-laws
  type: hard
- id: partial-derivatives
  type: soft
builds-toward:
- bimolecular-collision-dynamics-trajectory
tags:
- kinetics
- diffusion
- reaction-rate
stage: advanced
status: draft
---

# Diffusion-Controlled Reaction Kinetics

## Core Idea
Diffusion-controlled reactions reach a rate limit when reactants meet by diffusion before reacting; the measured rate is controlled by how fast reactants can approach, not their intrinsic reactivity. This limit depends on diffusion coefficients and viscosity via the Stokes-Einstein relation. Very fast reactions approach or achieve diffusion-controlled rates.

## Explainer

From collision theory, you know that a bimolecular reaction requires two reactant molecules to meet with sufficient energy and proper orientation. From Fick's laws, you understand that molecules in solution move by diffusion — random thermal motion governed by diffusion coefficients. **Diffusion-controlled kinetics** addresses what happens when the intrinsic chemical step (bond breaking and forming) is so fast that it occurs essentially every time two reactants encounter each other. In this limit, the overall reaction rate is no longer determined by activation energy or molecular orientation — it is determined entirely by how quickly diffusion brings the reactants together.

Think of it this way: every bimolecular reaction in solution involves two sequential processes — diffusion to form an **encounter pair** (the two molecules within reaction distance) followed by the chemical reaction itself. If the chemical step has a high activation barrier, diffusion is fast compared to reaction, and the rate is controlled by the activation energy — this is the typical "activation-controlled" regime covered by Arrhenius kinetics. But if the activation barrier is very low (or zero, as in many radical recombinations, proton transfers, and enzyme-substrate encounters), then molecules react the instant they meet. Now diffusion becomes the bottleneck — the rate cannot exceed the rate at which diffusion delivers reactant pairs.

The **Smoluchowski equation** quantifies this upper limit. It models one reactant as a stationary sphere of radius R and calculates the steady-state flux of the other reactant (with diffusion coefficient D) arriving at its surface. The resulting diffusion-controlled rate constant is k_diff = 4πR·D·Nₐ, where the relevant R and D are sums over both reactants (R = rA + rB, D = DA + DB). Using the **Stokes-Einstein relation** D = kT/(6πηr) to estimate diffusion coefficients, you can see that k_diff depends on temperature and solvent **viscosity** η. In water at room temperature, the diffusion-controlled limit works out to roughly 10⁹–10¹⁰ M⁻¹s⁻¹. Any measured rate constant approaching this magnitude signals that you are in or near the diffusion-controlled regime.

The practical consequences are significant. Diffusion-controlled reactions show an unusual temperature dependence: their rate increases with temperature primarily because viscosity decreases (faster diffusion), not because more molecules overcome an activation barrier. The apparent activation energy is small — typically 10–20 kJ/mol, reflecting the temperature dependence of viscosity rather than a chemical barrier. Solvent viscosity becomes a direct handle on the rate: the same reaction runs faster in water than in glycerol simply because molecules diffuse faster in less viscous media. Acid-base neutralizations, many fluorescence quenching processes, and radical recombinations are classic examples of reactions that operate at or near the diffusion-controlled limit.
