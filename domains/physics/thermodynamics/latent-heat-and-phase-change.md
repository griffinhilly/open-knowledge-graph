---
id: latent-heat-and-phase-change
title: Latent Heat and Phase Changes
domain: physics
course: thermodynamics
prerequisites:
- id: phase-transitions
  type: hard
- id: enthalpy-definition-and-significance
  type: soft
tags:
- latent-heat
- phase-change
- vaporization
- condensation
stage: formal-systems
status: draft
---

# Latent Heat and Phase Changes

## Core Idea
Latent heat is energy absorbed or released during a phase transition without temperature change. The heat of vaporization (L_v) is energy to convert liquid to gas; the heat of fusion (L_f) is energy to convert solid to liquid. These are intensive properties (per unit mass) and critically important in calorimetry and engineering.

## Explainer

When you heat a solid, you add energy and its temperature rises — this is the familiar behavior governed by heat capacity. But when the solid reaches its melting point, something qualitatively different happens: you continue adding energy and the temperature *stops rising* until the entire sample has melted. The energy added during this plateau goes into restructuring intermolecular bonds and changing the organization of matter, not into increasing molecular kinetic energy. This energy absorbed or released during a phase transition without temperature change is **latent heat** — "latent" from the Latin for hidden, because it does not manifest as a temperature change visible on a thermometer.

The molecular picture makes the mechanism clear. In a solid, molecules are locked in a lattice by attractive interactions and vibrate around fixed positions. Melting requires enough energy input to liberate molecules from these lattice positions so they can flow past one another. The **latent heat of fusion** L_f is this energy per unit mass. Vaporization requires even more: molecules in a liquid still attract each other at short range and must be completely separated to enter the gas phase. The **latent heat of vaporization** L_v is always much larger than L_f for the same substance — for water, L_f ≈ 334 J/g while L_v ≈ 2260 J/g — because complete separation from all neighbors requires far more energy than simply disrupting long-range lattice order while keeping neighbors nearby.

Your prerequisite on phase transitions established that phase boundaries represent thermodynamic equilibrium between two coexisting phases. At the melting or boiling point, adding heat converts one phase into the other at constant temperature while both phases coexist. If you have studied enthalpy, the connection is immediate: at constant pressure, latent heat equals the enthalpy change of the transition, ΔH_fus or ΔH_vap. The enthalpy perspective clarifies why the temperature is constant: all the heat input at constant pressure goes into changing the system's enthalpy (bond energy and PV work against atmospheric pressure), with no increase in internal kinetic energy and therefore no temperature rise.

Calorimetry problems involving phase changes require careful bookkeeping that distinguishes two types of heat transfer. **Sensible heat** (q = mcΔT) describes heat that changes temperature within a single phase. **Latent heat** (q = mL) describes heat exchanged at a phase boundary at constant temperature. When a substance passes through a phase transition, both contributions must be added: for example, converting 50 g of ice at −10°C to steam at 120°C requires heat for warming the ice, melting it, warming the liquid, vaporizing it, and then superheating the steam — five separate terms. Treating the phase transition as just another temperature step is the most common calorimetry error. Practically, water's enormous L_v is why sweating cools so effectively: each gram of water that evaporates from skin carries away 2260 J, far more than any sensible-heat mechanism over a few degrees of temperature difference.
