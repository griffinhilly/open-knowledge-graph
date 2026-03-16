---
id: fuel-combustion-products-analysis
title: Analysis of Combustion Products and Emissions
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: combustion-stoichiometry-energy-release
  type: hard
- id: gas-mixture-thermodynamics-daltons
  type: soft
builds-toward:
- adiabatic-flame-temperature-calculation
tags:
- combustion
- products
- emissions
- analysis
stage: advanced
status: draft
---

# Analysis of Combustion Products and Emissions

## Core Idea
Combustion products include CO₂, H₂O, N₂, and excess O₂ for lean conditions; incomplete combustion produces CO, soot, and unburned hydrocarbons. NOx formation depends on flame temperature and residence time. Analysis of product composition and sensible enthalpy enables determination of flame temperature and emission estimates for environmental compliance and efficiency calculations.

## Explainer

From combustion stoichiometry, you know how to write a balanced reaction for complete combustion: a hydrocarbon fuel reacts with the theoretically required amount of oxygen (stoichiometric air) to produce only CO₂ and H₂O. In practice, combustion is never perfectly stoichiometric. The ratio of actual air supplied to stoichiometric air — the **air-fuel equivalence ratio** λ (lambda) — governs what products actually emerge from the flame, and analyzing those products is the starting point for both efficiency calculations and emissions compliance.

When λ > 1 (lean combustion, excess air), there is more oxygen than the fuel can consume. Products include CO₂, H₂O, N₂, and unreacted O₂. The excess air carries nitrogen and oxygen through the combustion zone and out the exhaust, diluting the products and carrying away sensible heat that could have done useful work. When λ < 1 (rich combustion, fuel-excess), there is insufficient oxygen for complete combustion. Some carbon ends up as CO rather than CO₂ (carbon monoxide is both toxic and represents wasted chemical energy), and some fuel exits as unburned hydrocarbons (UHC) or soot. A real combustion device must balance these regimes: lean enough to minimize CO and soot, but not so lean that excess air losses destroy efficiency.

**NOx emissions** (primarily NO and NO₂) are a distinct category: they form not from the fuel carbon or hydrogen but from the high-temperature reaction of atmospheric nitrogen (N₂) with oxygen. The dominant mechanism — **thermal NOx** — depends exponentially on flame temperature and linearly on residence time at high temperature. A hotter flame produces more NOx even if stoichiometry is otherwise identical. This creates a design tension: combustion engineers want high temperatures for efficiency (thermodynamic performance scales with peak temperature), but high temperatures breed NOx. Modern control strategies include exhaust gas recirculation (EGR), lean premixed combustion, and selective catalytic reduction (SCR) to navigate this tradeoff.

Quantitative product analysis uses the **molar product composition** derived from the balanced stoichiometry — accounting for actual λ — plus enthalpy data for each species. Each product carries **sensible enthalpy** above a reference temperature (typically 298 K), and the sum of these enthalpies, when equated to the heat of combustion, yields the **adiabatic flame temperature**: the upper bound on how hot the products get if no heat is lost to the surroundings. Real flames are cooler due to heat transfer, but the adiabatic flame temperature sets the scale. From it, engineers estimate NOx formation rates, material temperature limits, and whether the combustion chamber design will survive. Gas mixture thermodynamics (your Dalton's law prerequisite) enters here: the exhaust stream is a mixture of gases at a common pressure, and each species contributes its partial enthalpy to the total.

