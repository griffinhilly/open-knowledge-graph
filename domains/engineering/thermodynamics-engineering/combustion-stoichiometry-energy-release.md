---
id: combustion-stoichiometry-energy-release
title: Combustion Stoichiometry and Energy Release
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: chemical-equilibrium-reaction-analysis
  type: hard
- id: thermochemistry-formation-properties
  type: hard
- id: stoichiometry-calculations
  type: hard
builds-toward:
- fuel-combustion-products-analysis
- adiabatic-flame-temperature-calculation
tags:
- combustion
- stoichiometry
- energy
- heating-value
stage: advanced
status: draft
---

# Combustion Stoichiometry and Energy Release

## Core Idea
Combustion is exothermic oxidation of fuel; stoichiometric air (equivalence ratio φ = 1) completely burns fuel with no excess oxygen or incomplete products. Higher heating value (HHV) includes latent heat of water vapor condensation; lower heating value (LHV) assumes vapor remains gaseous. Energy released is the heat input Q_in for power and refrigeration cycles.

## Explainer

From your stoichiometry background, you know how to balance chemical equations — ensuring atoms are conserved across a reaction. Combustion adds the thermodynamic dimension: we now care not just about what atoms appear in the products, but about how much energy is released in the process. The **complete combustion** of a hydrocarbon CₓHᵧ with oxygen produces only CO₂ and H₂O. Balancing the equation is your first step, and the molar ratios it provides determine every subsequent calculation.

The concept of **stoichiometric air** addresses the fact that practical combustion uses air (mostly nitrogen) rather than pure oxygen. The stoichiometric air-fuel ratio is the exact mass of air needed to completely combust one unit mass of fuel — no oxygen left over, no unburned fuel remaining. The **equivalence ratio** φ = (actual fuel-air ratio) / (stoichiometric fuel-air ratio) encodes how the mixture deviates from ideal. At φ = 1 (stoichiometric), combustion is theoretically complete. At φ < 1 (lean, excess air), there is leftover oxygen in the products but the fuel is fully consumed. At φ > 1 (rich, excess fuel), some fuel remains unburned and CO appears — incomplete combustion that wastes fuel and produces pollutants. Real engines operate lean or rich depending on their design priorities: lean for fuel economy, rich for power.

The **higher heating value (HHV)** and **lower heating value (LHV)** both measure the energy released per unit mass of fuel, but they differ in what they assume happens to the water produced. HHV — the "higher" value — accounts for the latent heat recovered when water vapor in the products condenses back to liquid. LHV treats the water as remaining as vapor, which is the realistic assumption for most engines where exhaust gases leave at temperatures well above condensation. The difference between HHV and LHV for a natural gas can be around 10%, so the choice matters significantly for efficiency calculations. Engineering datasheets almost always specify LHV for combustion engines; furnace and boiler efficiency ratings often use HHV.

To connect combustion to cycle analysis, the energy released by combustion is the heat input Q_in that drives the thermodynamic cycle. For a gas turbine, Q_in is the enthalpy increase from the combustion chamber inlet to outlet; for a spark-ignition engine analyzed as a closed system, it is the heat added during the constant-volume (Otto cycle) or constant-pressure (Diesel cycle) process. Computing Q_in requires the fuel's heating value, the air-fuel ratio, and the mass flow rate through the system. The stoichiometric balance gives you the product composition; the heating value gives you the energy; the first law gives you what temperature rise results. These three tools together are the complete combustion analysis toolkit.
