---
id: thermochemistry-heat-and-energy
title: 'Thermochemistry: Enthalpy and Heat of Reaction'
domain: chemistry
course: general-chemistry
prerequisites:
- id: states-of-matter-phase-changes
  type: soft
- id: energy-conservation
  type: soft
builds-toward:
- oxidation-reduction-reactions
tags:
- thermochemistry
- enthalpy
- exothermic
- endothermic
- heat
stage: formal-systems
status: draft
---

# Thermochemistry: Enthalpy and Heat of Reaction

## Core Idea
Thermochemistry studies heat changes during chemical reactions. Enthalpy (H) is the heat content at constant pressure. Exothermic reactions release heat (ΔH < 0); endothermic reactions absorb heat (ΔH > 0). Standard enthalpy of reaction (ΔH°rxn) quantifies heat released or absorbed. Hess's law allows calculation of reaction enthalpies from other reactions.

## Explainer

From your study of energy conservation, you know that energy is neither created nor destroyed — it only changes form. In chemistry, the form we care about most is **heat**, the energy transferred between a system and its surroundings due to a temperature difference. Thermochemistry puts numbers on that transfer. When methane burns in your stove, the reaction CH₄ + 2O₂ → CO₂ + 2H₂O releases 890 kJ of heat per mole of methane. That number — the **enthalpy of reaction** (ΔH°rxn) — is negative because the system loses energy to the surroundings. The surroundings (your pot of water) get hotter; the reaction is **exothermic**.

**Enthalpy** (H) is defined as the heat content of a system at constant pressure, which is the condition for most bench-top and biological reactions. We never measure H directly — we measure changes in it. When ΔH is negative, products sit at a lower energy than reactants and the difference escapes as heat. When ΔH is positive, the reaction is **endothermic**: it absorbs heat from the surroundings, and dissolving ammonium nitrate in water (the basis of instant cold packs) is a familiar example. The sign convention is critical — ΔH is always stated from the system's perspective: negative means the system released energy, positive means it absorbed energy.

The most powerful tool in thermochemistry is **Hess's law**: because enthalpy is a state function, ΔH for a reaction depends only on the initial and final states, not on the path taken between them. This means you can calculate the enthalpy of a reaction you cannot easily measure by combining reactions whose enthalpies you do know. If you can add, reverse, or scale chemical equations so they sum to your target reaction, the corresponding ΔH values add, reverse sign, or scale in exactly the same way. Standard enthalpies of formation (ΔH°f) exploit this principle systematically: every compound's formation enthalpy is measured relative to its constituent elements in their standard states, so ΔH°rxn = Σ ΔH°f(products) − Σ ΔH°f(reactants). This single equation lets you calculate the heat of any reaction from tabulated formation data.

Understanding thermochemistry also requires distinguishing between heat and temperature. Heat (q) is energy in transit, measured in joules or kilojoules. Temperature is a measure of the average kinetic energy of particles. The relationship between them is q = mcΔT, where m is mass, c is specific heat capacity, and ΔT is the temperature change. Calorimetry experiments use this equation to measure q for a reaction by observing the temperature change in a known mass of water or solution. This is the experimental bridge between the abstract concept of enthalpy and the physical observation of temperature change in the lab.
