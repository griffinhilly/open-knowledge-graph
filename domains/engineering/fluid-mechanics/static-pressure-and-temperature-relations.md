---
id: static-pressure-and-temperature-relations
title: Static Pressure and Temperature Relations in Compressible Flow
domain: engineering
course: fluid-mechanics
prerequisites:
- id: compressible-flow-basics
  type: hard
- id: thermodynamic-property-equations-engineering
  type: soft
builds-toward:
- isentropic-nozzle-flow-choked-conditions
- rayleigh-line-flow-stagnation-conditions
tags:
- temperature
- compressible
- thermodynamics
stage: advanced
status: draft
---

# Static Pressure and Temperature Relations in Compressible Flow

## Core Idea
In compressible flow, static pressure and temperature are coupled through the first law of thermodynamics and isentropic relations. Static temperature (the temperature measured by a thermometer moving with the fluid) differs from stagnation temperature when velocity is significant. For an ideal gas in isentropic flow, the relationship T/T₀ = [2/(γ+1)] [1 + ((γ-1)/2)M²]⁻¹ shows how Mach number affects measured temperature.

## How It's Best Learned
Solve nozzle flow problems where inlet stagnation conditions are known and calculate static properties at different Mach numbers. Compare calculations using property tables and compressibility factor corrections to understand real-gas effects.

## Common Misconceptions
Static temperature is NOT the same as stagnation temperature in moving gas. A thermometer moving with a fast flow will show a higher temperature than a stationary thermometer due to viscous dissipation at the sensor surface.

## Explainer

In low-speed flows, pressure and temperature behave as simple scalars you can read off a gauge or thermometer without worrying about how fast the gas is moving. Compressible flow — flows where the Mach number is no longer negligible — breaks this assumption. The energy in a high-speed gas flow is split between **thermal energy** (random molecular motion, which a thermometer measures) and **kinetic energy** (organized bulk motion). The total energy is conserved, but how it is partitioned between these two forms depends on the local velocity. This is the core of the static-versus-stagnation distinction.

**Static temperature** T is the temperature of the gas as experienced by a fluid parcel — the thermodynamic temperature associated purely with random molecular motion, with no contribution from bulk kinetic energy. **Stagnation temperature** T₀ is the temperature the gas would reach if brought to rest *isentropically* — all the kinetic energy converts back to thermal energy. The relationship T₀ = T(1 + (γ−1)/2 · M²) shows that at M = 0, they are identical, but at M = 1 (sonic), T is only about 83% of T₀ for air (γ = 1.4). At M = 3, static temperature is barely 36% of stagnation temperature. The difference is not small — it is the difference between the gas you feel moving with it and the gas you would feel if you suddenly stopped it.

The same logic applies to **static pressure** P and **stagnation pressure** P₀. For isentropic flow, P/P₀ = [T/T₀]^(γ/(γ−1)), which by substitution gives P/P₀ = [1 + (γ−1)/2 · M²]^(−γ/(γ−1)). These **isentropic relations** are your working tools for nozzle analysis: given the stagnation conditions at a reservoir (where velocity is essentially zero, so static = stagnation), you can compute static pressure and temperature at any downstream Mach number. Conversely, a pitot tube facing the flow measures stagnation pressure; comparing it to static pressure read from a wall tap gives you Mach number directly.

A common trap is forgetting *isentropic* as the qualifier. The isentropic relations assume no heat transfer and no irreversible losses (no shocks, no friction). In a shock wave, entropy increases: stagnation pressure drops across the shock while stagnation temperature remains constant (for an adiabatic shock). This is why the total pressure recovery across a supersonic intake matters — losses in P₀ through shocks and boundary layer separation translate directly into thrust reduction. Understanding that static and stagnation quantities are linked by the Mach number through the isentropic relations, and that shocks break the isentropic assumption for pressure but not for enthalpy, is the conceptual foundation for all compressible flow calculations that follow.
