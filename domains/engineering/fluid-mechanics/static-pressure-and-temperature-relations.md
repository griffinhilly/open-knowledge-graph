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
stage: formal-systems
status: draft
---

# Static Pressure and Temperature Relations in Compressible Flow

## Core Idea
In compressible flow, static pressure and temperature are coupled through the first law of thermodynamics and isentropic relations. Static temperature (the temperature measured by a thermometer moving with the fluid) differs from stagnation temperature when velocity is significant. For an ideal gas in isentropic flow, the relationship T/T₀ = [2/(γ+1)] [1 + ((γ-1)/2)M²]⁻¹ shows how Mach number affects measured temperature.

## How It's Best Learned
Solve nozzle flow problems where inlet stagnation conditions are known and calculate static properties at different Mach numbers. Compare calculations using property tables and compressibility factor corrections to understand real-gas effects.

## Common Misconceptions
Static temperature is NOT the same as stagnation temperature in moving gas. A thermometer moving with a fast flow will show a higher temperature than a stationary thermometer due to viscous dissipation at the sensor surface.
