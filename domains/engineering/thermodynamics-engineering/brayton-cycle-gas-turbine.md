---
id: brayton-cycle-gas-turbine
title: Brayton Cycle and Gas Turbine Engines
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: first-law-closed-systems
  type: hard
- id: ideal-gas-law
  type: hard
- id: carnot-cycle
  type: soft
builds-toward:
- brayton-cycle-intercooling-reheating
tags:
- brayton-cycle
- gas-turbine
- power-cycles
stage: advanced
status: draft
---

# Brayton Cycle and Gas Turbine Engines

## Core Idea
The Brayton cycle (isentropic compression, isobaric heating, isentropic expansion, isobaric rejection) models gas turbines and jet engines operating on ideal gases. Unlike the Rankine cycle, the Brayton cycle occurs entirely in the gas phase and uses pressure ratio as the key parameter controlling efficiency. Real Brayton cycles suffer from compressor irreversibilities that require additional work and turbine pressure drop losses that reduce available power.

## How It's Best Learned
Use ideal gas property relations (T₂/T₁ = (P₂/P₁)^((γ-1)/γ)) for isentropic processes and constant c_p for isobaric processes. Calculate net work (turbine work minus compressor work) and efficiency as a function of pressure ratio. Recognize the trade-off: higher pressure ratio increases efficiency but requires more compressor work, and real device irreversibilities overwhelm ideal gains at very high ratios.

## Common Misconceptions
- The Brayton cycle efficiency exceeds Rankine efficiency; at the same temperature ratio they have similar ideal efficiency, but Brayton's simplicity makes it practical.
- Gas turbines always operate at their design pressure ratio for maximum efficiency; they operate at fixed speed and adjust power by changing inlet guide vane angle or fuel flow.
- The back work ratio (compressor work / turbine work) is negligible in gas turbines; it typically consumes 40–50% of turbine work, limiting net output.
