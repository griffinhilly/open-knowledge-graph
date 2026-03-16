---
id: throttling-joule-thomson-effect
title: Throttling and the Joule-Thomson Effect
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: first-law-open-systems
  type: hard
- id: thermodynamic-properties-and-equations-of-state
  type: hard
builds-toward:
- joule-thomson-coefficient-calculations
- vapor-compression-refrigeration-cycle
tags:
- throttling
- joule-thomson
- enthalpy
- cooling
- heating
stage: advanced
status: draft
---

# Throttling and the Joule-Thomson Effect

## Core Idea
Throttling is an isenthalpic process where fluid pressure drops irreversibly with no heat transfer or work. The Joule-Thomson effect describes temperature change during throttling, characterized by the coefficient μ = (∂T/∂P)ₕ. Understanding this effect is critical for refrigeration cycles, natural gas processing, and prediction of cooling or heating during pressure reduction.

## Explainer

Throttling seems paradoxical at first: you force a fluid through a restriction (a valve, an orifice, a porous plug) causing a pressure drop, yet you do no work on or by the fluid, and no heat is exchanged. Where does the energy go? The answer, from your first-law analysis of open systems, is that it goes nowhere — enthalpy is conserved. The first law for a steady-flow device with no heat transfer and no shaft work reduces to h_in = h_out: the **specific enthalpy is unchanged** across the throttle. This is the isenthalpic constraint, and everything else about throttling follows from it.

But if enthalpy is conserved, why does temperature change? The resolution is that enthalpy depends on both temperature and pressure: h = u + Pv. For an **ideal gas**, h depends only on temperature (Pv = RT and u depends only on T), so an isenthalpic process for an ideal gas is also isothermal — no temperature change occurs. For a **real fluid**, intermolecular forces mean that changing pressure at constant enthalpy does change temperature. The **Joule-Thomson coefficient** μ_JT = (∂T/∂P)_h quantifies exactly this: it is the temperature change per unit pressure drop at constant enthalpy. A positive μ_JT means the fluid cools on pressure drop (normal for most gases below their inversion temperature); a negative μ_JT means it heats up (hydrogen and helium at room temperature, for example).

The **inversion temperature** is the temperature above which μ_JT becomes negative. For air, nitrogen, and most common gases, the inversion temperature is well above room temperature, so throttling cools them — which is why Joule-Thomson expansion is used to liquefy air. The process is repeated: partially cooled gas is throttled again, cooled further, eventually reaching the liquid phase. For hydrogen and helium, pre-cooling below their inversion temperatures (around −68°C and −233°C respectively) is required before Joule-Thomson liquefaction is possible.

In refrigeration cycles, the throttling valve between the condenser and evaporator performs exactly this function: it reduces the high-pressure liquid refrigerant to low pressure, causing partial vaporization and a temperature drop that allows the evaporator to absorb heat from the refrigerated space. The process is **irreversible** — entropy is generated — but it requires no moving parts, no power input, and no heat transfer, making it mechanically simple and reliable. The cost of this simplicity shows up in entropy generation: a throttle destroys available work that a turbine could in principle recover, which is why large industrial refrigeration systems sometimes use expansion turbines instead of throttle valves when efficiency justifies the mechanical complexity.
