---
id: joule-thomson-coefficient-and-throttling
title: Joule-Thomson Coefficient and Throttling
domain: physics
course: thermodynamics
prerequisites:
- id: enthalpy-definition-and-significance
  type: hard
- id: partial-derivatives
  type: soft
tags:
- joule-thomson
- throttling
- real-gas
- cooling
stage: formal-systems
status: draft
---

# Joule-Thomson Coefficient and Throttling

## Core Idea
The Joule-Thomson coefficient μ_JT = (∂T/∂P)_H describes temperature change during throttling (isenthalpic) expansion. For ideal gases, μ_JT = 0; real gases deviate. Gases cool (μ_JT > 0) if attractive forces dominate, or heat (μ_JT < 0) if repulsive forces dominate. This is the principle behind refrigeration cycles.

## Explainer

You know enthalpy H = U + PV as the natural thermodynamic potential for constant-pressure processes, and you know how to use partial derivatives to relate thermodynamic variables along constrained paths. The Joule-Thomson experiment combines both: by forcing gas through a porous plug or valve, it probes the molecular interactions of real gases through a cleverly constructed isenthalpic constraint — and the result underlies all modern refrigeration and industrial gas liquefaction.

The **throttling process** is analyzed by energy balance, not by assuming a specific mechanism. Gas at high pressure P₁, temperature T₁ is steadily pushed through a porous plug into a region of lower pressure P₂. The work done by the gas pushing into the low-pressure region is P₂V₂; the work done on the gas by the high-pressure side is P₁V₁. The apparatus is insulated (no heat exchange). First-law energy conservation gives U₂ − U₁ = P₁V₁ − P₂V₂, which rearranges to U₁ + P₁V₁ = U₂ + P₂V₂, or **H₁ = H₂**. Throttling is isenthalpic — an exact result from energy conservation, not an approximation. This makes H the right thermodynamic potential: at constant H, the **Joule-Thomson coefficient** μ_JT = (∂T/∂P)_H tells us how temperature changes as pressure drops.

For an **ideal gas**, internal energy depends only on temperature, and PV = nRT, so H = U + PV depends only on T. If H is conserved and H depends only on T, temperature cannot change: μ_JT = 0 for ideal gases. Real gases deviate because intermolecular interactions make U depend on volume (intermolecular separation) as well as temperature. When gas expands, molecules move apart — doing work against their mutual **attractive forces** (negative potential energy becomes less negative), converting kinetic energy to potential energy, lowering temperature. If **repulsive forces** dominate (high temperature, high density), expansion lets molecules move apart *more freely*, reducing the repulsive contribution to potential energy, releasing kinetic energy, and *raising* temperature. The crossover between these regimes is the **inversion temperature** T_inv, where μ_JT changes sign. Below T_inv, throttling cools; above it, throttling heats.

The practical implications are large. Nitrogen has T_inv ≈ 620 K, well above room temperature, so throttling a nitrogen cylinder at room conditions produces useful cooling — the basis of the **Linde process** for industrial air liquefaction. Hydrogen (T_inv ≈ 205 K) and helium (T_inv ≈ 40 K) must be pre-cooled below their inversion temperatures before throttling will cool them further; this is why liquid nitrogen is used as a pre-cooler stage before liquefying hydrogen, and liquid hydrogen before helium. Refrigerators and air conditioners use the same principle in reverse: a refrigerant gas is compressed, cooled by rejecting heat at high pressure, then throttled through an expansion valve to drop to low temperature, where it absorbs heat from the refrigerated space before returning to the compressor. The choice of refrigerant is partly driven by where its inversion temperature and μ_JT values fall relative to the operating temperature range.
