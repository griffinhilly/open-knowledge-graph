---
id: chemical-exergy-fuel-combustion
title: Chemical Exergy and Fuel Combustion Analysis
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: exergy-concept-availability
  type: hard
- id: combustion-thermodynamic-analysis
  type: hard
builds-toward:
- second-law-efficiency-exergy-based
tags:
- chemical-exergy
- fuel
- combustion
- maximum-work-potential
- environmental-reference
stage: advanced
status: draft
---

# Chemical Exergy and Fuel Combustion Analysis

## Core Idea
Chemical exergy represents the maximum useful work available from a chemical substance relative to the reference environment at equilibrium. For fuels, chemical exergy is approximately the lower heating value; precise values depend on composition and environmental standard state. Chemical exergy accounting reveals true second-law efficiency of combustion-based power cycles and identifies losses to irreversible mixing.

## Explainer

Your prerequisite on exergy (availability) established that exergy measures the maximum work extractable as a system moves to equilibrium with its environment — the **dead state**. That concept applied to thermal and mechanical disequilibrium: a hot gas has thermal exergy, a compressed gas has pressure exergy. Chemical exergy extends the same logic to *chemical* disequilibrium: a fuel is not in chemical equilibrium with the atmosphere (oxygen, nitrogen, CO₂, H₂O in ambient proportions), and that disequilibrium is a potential source of work.

The **chemical exergy** of a fuel is the maximum useful work obtainable if the fuel reacts reversibly to the reference environment composition — meaning complete combustion with all products reaching environmental partial pressures. For a hydrocarbon fuel, this means the carbon fully oxidizes to CO₂ at atmospheric CO₂ partial pressure, and the hydrogen oxidizes to liquid water. The result is approximately equal to the fuel's **lower heating value (LHV)** — the heat released in complete combustion with water vapor remaining as gas. More precisely, chemical exergy slightly exceeds LHV because it includes the Gibbs free energy of mixing products with atmospheric species. For methane, the ratio e_ch/LHV ≈ 1.04; for hydrogen it is closer to 1.18 because of the large entropy change when water condenses.

Why does this matter for engineering? In an actual combustion-based power plant, fuel's chemical exergy enters the system and work exits. First-law analysis compares heat released to work produced and calls the difference "losses to exhaust and heat rejection." But this is misleading — it misses that some work potential is destroyed by the irreversibility of combustion itself. The exergy balance for the combustor shows that burning fuel irreversibly (finite-temperature mixing of fuel and air, kinetically-driven reactions far from equilibrium) **destroys exergy** even before any heat loss occurs. A typical natural gas combustor operating at adiabatic flame temperature destroys 25–30% of the fuel's chemical exergy in the reaction alone. Exergy analysis makes this loss visible and quantifiable.

**Second-law efficiency** for a combustion system is defined as useful exergy output divided by fuel chemical exergy input. A simple gas turbine might achieve 40% thermal efficiency (first law) but only 35% second-law efficiency — the gap representing avoidable internal irreversibilities. Combined cycle plants push second-law efficiency above 55% by recovering exhaust exergy in a steam bottoming cycle. These improvements come from reducing entropy generation: operating combustors at higher equivalence ratios, recovering heat at temperature levels closer to the source, and using staged combustion to reduce irreversible mixing. Chemical exergy accounting is the analytical tool that identifies exactly where the remaining exergy goes — and how much is theoretically recoverable versus fundamentally irreversible.
