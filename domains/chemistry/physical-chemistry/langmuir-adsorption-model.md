---
id: langmuir-adsorption-model
title: 'Adsorption Isotherms: Langmuir and BET Models'
domain: chemistry
course: physical-chemistry
prerequisites:
- id: chemical-equilibrium
  type: hard
- id: intermolecular-forces
  type: soft
- id: statistical-mechanics-foundations
  type: soft
builds-toward:
- surface-chemistry-and-catalysis
tags:
- adsorption
- Langmuir
- BET
- surface-coverage
- chemisorption
- physisorption
- isotherm
stage: advanced
status: validated
---

# Adsorption Isotherms: Langmuir and BET Models

## Core Idea
Adsorption isotherms describe how the amount of gas adsorbed on a surface varies with pressure at constant temperature. The Langmuir model assumes monolayer adsorption on equivalent, non-interacting sites at equilibrium: θ = Kp/(1+Kp), where θ is fractional surface coverage and K is the adsorption equilibrium constant. The BET (Brunauer-Emmett-Teller) model generalizes this to multilayer physisorption and is used to measure surface areas of porous materials. Chemisorption involves covalent bond formation (strong, irreversible) while physisorption involves weak van der Waals interactions (weak, reversible). The coverage-pressure relationship determines catalyst activity and selectivity in heterogeneous catalysis.

## How It's Best Learned
Fit the Langmuir equation to experimental isotherm data for CO on Pd or N₂ on silica. Extract K, compute ΔG_ads, and check linearity of the Langmuir linearization plot (p/n vs p). Compare BET plots for microporous vs mesoporous materials.

## Common Misconceptions
- Assuming the Langmuir model is always accurate; it fails for heterogeneous surfaces and when adsorbate-adsorbate interactions matter.
- Confusing adsorption (surface process) with absorption (bulk process).

## Explainer

From chemical equilibrium, you know that a dynamic balance exists between forward and reverse reactions, and that the equilibrium position depends on thermodynamic quantities like ΔG and temperature. Adsorption applies this equilibrium concept to surfaces: gas molecules land on a solid surface (adsorb) and leave it (desorb), and at equilibrium, the rates of these two processes are equal. The **adsorption isotherm** describes how the amount of adsorbed gas depends on pressure at a fixed temperature — it is the surface-chemistry analog of a titration curve or a binding curve.

The **Langmuir model** is the simplest and most elegant treatment. It assumes the surface has a fixed number of equivalent, independent binding sites. Each site is either empty or occupied by exactly one molecule — no stacking allowed (monolayer coverage only). Adsorption is the forward reaction (gas molecule + empty site → occupied site) and desorption is the reverse. At equilibrium, the fractional surface coverage θ follows the equation θ = Kp/(1 + Kp), where K is the adsorption equilibrium constant and p is the gas pressure. At low pressure (Kp ≪ 1), θ increases linearly with pressure — every molecule that hits the surface finds an empty site. At high pressure (Kp ≫ 1), θ approaches 1 — the surface is saturated, and adding more gas has no effect. The characteristic shape is a curve that rises steeply and then levels off, much like enzyme saturation kinetics (Michaelis-Menten), which follows identical mathematics.

The **BET model** (Brunauer-Emmett-Teller) extends Langmuir to **multilayer adsorption**. In many real systems, once a monolayer forms, additional layers of gas molecules can stack on top through weaker van der Waals interactions. The BET isotherm accounts for this by allowing each adsorbed molecule to serve as a site for the next layer, with the first-layer binding energy differing from subsequent layers (which approximate the heat of liquefaction). The BET equation is widely used experimentally to measure the surface area of porous materials like catalysts and adsorbents: by fitting experimental data to the BET isotherm, you extract the monolayer capacity, which directly gives the surface area when multiplied by the cross-sectional area of the adsorbate molecule.

Understanding the distinction between **chemisorption** and **physisorption** helps you know which model applies. Chemisorption involves forming real chemical bonds between the adsorbate and surface (high binding energy, ~40–400 kJ/mol), is specific to particular surface-adsorbate pairs, and typically forms only a monolayer — Langmuir conditions. Physisorption involves weak van der Waals forces (~5–40 kJ/mol), is nonspecific, and readily forms multilayers — BET conditions. In heterogeneous catalysis, the reactant first chemisorbs (activating bonds), reacts on the surface, and then the product desorbs. The Langmuir isotherm directly enters catalytic rate laws: if the rate depends on surface coverage, and coverage depends on pressure through the Langmuir equation, you can derive rate expressions that transition from first-order (low pressure, θ ∝ p) to zero-order (high pressure, θ ≈ 1) behavior.
