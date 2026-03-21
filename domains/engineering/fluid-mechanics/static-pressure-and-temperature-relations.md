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

## Questions

```yaml
- question: "A temperature sensor is mounted flush with the inner wall of a supersonic wind tunnel operating at M = 2.0 with γ = 1.4. The reservoir stagnation temperature is T₀ = 600 K. Approximately what temperature will the wall-flush sensor measure?"
  type: multiple-choice
  options:
    - "600 K — stagnation temperature is always what a fixed sensor reads in a flow"
    - "333 K — the static temperature, computed from T = T₀ / (1 + (γ−1)/2 · M²)"
    - "475 K — the arithmetic average of static and stagnation temperatures"
    - "Higher than 600 K, because viscous heating at the sensor wall adds energy to the measurement"
  answer: 1
  explanation: "A flush wall sensor measures static temperature — the temperature of the gas as experienced by a fluid parcel at that location, with no contribution from bulk kinetic energy. At M = 2.0, T/T₀ = 1/(1 + 0.2 × 4) = 1/1.8 ≈ 0.556, giving T = 600 × 0.556 ≈ 333 K. The common misconception is that static temperature equals stagnation temperature; they diverge significantly at high Mach numbers. A pitot probe facing the flow would measure the stagnation temperature (~600 K) because it brings the gas to rest, converting kinetic energy to thermal energy. The wall sensor measures what the gas actually 'is' at that speed — much colder."

- question: "A pitot tube in a supersonic flow measures stagnation pressure P₀ = 4 atm; a wall static port reads P = 1 atm. What principle allows the Mach number to be inferred from this measurement?"
  type: multiple-choice
  options:
    - "Stagnation pressure is always exactly 4 times static pressure in any supersonic flow"
    - "For isentropic flow, the ratio P₀/P depends only on Mach number, so the ratio directly yields M"
    - "The pitot tube adds kinetic energy to the flow, raising pressure above the static value by a known amount"
    - "The wall boundary layer reduces static pressure below the freestream value in a predictable way"
  answer: 1
  explanation: "For isentropic flow, P/P₀ = [1 + (γ−1)/2 · M²]^(−γ/(γ−1)), which depends only on M and γ. Given P₀ from the pitot tube and P from the static port, their ratio P₀/P uniquely determines M (for a given γ). This is the operational principle behind the pitot-static system used on aircraft for airspeed measurement. The key insight is that both pressures are measured simultaneously in the same flow, so their ratio directly encodes the Mach number through the isentropic relation."

- question: "In isentropic compressible flow, as Mach number increases, static temperature decreases relative to stagnation temperature."
  type: true-false
  answer: true
  explanation: "The relation T/T₀ = 1/(1 + (γ−1)/2 · M²) shows that T/T₀ decreases as M increases. At M = 0, T = T₀. At M = 1 (sonic), T/T₀ = 2/(γ+1) ≈ 0.833 for air. At M = 3, T/T₀ ≈ 1/2.8 ≈ 0.36. The physical reason is energy conservation: faster flow has more kinetic energy per unit mass, which comes at the expense of thermal energy. The total enthalpy (which corresponds to stagnation temperature) is conserved, but an increasing fraction is in kinetic form."

- question: "For an adiabatic normal shock wave, both stagnation temperature and stagnation pressure are preserved across the shock."
  type: true-false
  answer: false
  explanation: "Stagnation temperature is conserved across an adiabatic shock (no heat transfer means total enthalpy is unchanged, and for a perfect gas, stagnation temperature is proportional to stagnation enthalpy). But stagnation pressure is NOT conserved — it decreases across the shock because the shock is an irreversible process that generates entropy. The entropy increase is precisely what causes stagnation pressure to drop while stagnation temperature remains constant. This is why shock losses are measured as total pressure recovery: P₀_after/P₀_before < 1 tells you how much useful pressure energy was destroyed by the irreversibility of the shock."

- question: "Explain the physical meaning of the difference between static and stagnation temperature. Why are they equal at low speeds but diverge significantly at high Mach numbers?"
  type: short-answer
  answer: "Static temperature T is the thermodynamic temperature of the gas associated with random molecular motion — it is what a thermometer moving with the flow would measure. Stagnation temperature T₀ is what the gas would reach if brought to rest isentropically, converting all kinetic energy back to thermal energy. They are related by T₀ = T(1 + (γ−1)/2 · M²). At low Mach numbers, the kinetic energy term (γ−1)/2 · M² is negligibly small compared to 1, so T ≈ T₀. At high Mach numbers, a substantial fraction of the total energy is in ordered kinetic form, and stopping the gas would liberate that energy as heat — so T₀ >> T. The divergence reflects how much of the gas's total energy is kinetic versus thermal."
  explanation: "A useful physical intuition: in a low-speed flow, a bug sitting in the fluid would feel the same temperature as a bug on a stationary wall. In a high-speed supersonic flow, the fluid parcels are moving at speeds comparable to sound, carrying substantial kinetic energy. Stopping that motion releases energy and heats the gas — the stagnation temperature is the 'heated' value, and the static temperature is what the gas 'is' while moving."
```

## Explainer

In low-speed flows, pressure and temperature behave as simple scalars you can read off a gauge or thermometer without worrying about how fast the gas is moving. Compressible flow — flows where the Mach number is no longer negligible — breaks this assumption. The energy in a high-speed gas flow is split between **thermal energy** (random molecular motion, which a thermometer measures) and **kinetic energy** (organized bulk motion). The total energy is conserved, but how it is partitioned between these two forms depends on the local velocity. This is the core of the static-versus-stagnation distinction.

**Static temperature** T is the temperature of the gas as experienced by a fluid parcel — the thermodynamic temperature associated purely with random molecular motion, with no contribution from bulk kinetic energy. **Stagnation temperature** T₀ is the temperature the gas would reach if brought to rest *isentropically* — all the kinetic energy converts back to thermal energy. The relationship T₀ = T(1 + (γ−1)/2 · M²) shows that at M = 0, they are identical, but at M = 1 (sonic), T is only about 83% of T₀ for air (γ = 1.4). At M = 3, static temperature is barely 36% of stagnation temperature. The difference is not small — it is the difference between the gas you feel moving with it and the gas you would feel if you suddenly stopped it.

The same logic applies to **static pressure** P and **stagnation pressure** P₀. For isentropic flow, P/P₀ = [T/T₀]^(γ/(γ−1)), which by substitution gives P/P₀ = [1 + (γ−1)/2 · M²]^(−γ/(γ−1)). These **isentropic relations** are your working tools for nozzle analysis: given the stagnation conditions at a reservoir (where velocity is essentially zero, so static = stagnation), you can compute static pressure and temperature at any downstream Mach number. Conversely, a pitot tube facing the flow measures stagnation pressure; comparing it to static pressure read from a wall tap gives you Mach number directly.

A common trap is forgetting *isentropic* as the qualifier. The isentropic relations assume no heat transfer and no irreversible losses (no shocks, no friction). In a shock wave, entropy increases: stagnation pressure drops across the shock while stagnation temperature remains constant (for an adiabatic shock). This is why the total pressure recovery across a supersonic intake matters — losses in P₀ through shocks and boundary layer separation translate directly into thrust reduction. Understanding that static and stagnation quantities are linked by the Mach number through the isentropic relations, and that shocks break the isentropic assumption for pressure but not for enthalpy, is the conceptual foundation for all compressible flow calculations that follow.
