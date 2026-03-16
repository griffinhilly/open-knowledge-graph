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

## Explainer

You know from the first law and the ideal gas that work can be extracted from a gas by expanding it and input work must be spent compressing it. The **Brayton cycle** chains these two processes through heat addition and rejection: compress the air isentropically, add heat at constant pressure (by burning fuel), expand the hot gas isentropically through a turbine, and reject heat to the atmosphere at constant pressure. Unlike the Rankine cycle's phase change, the Brayton cycle operates entirely in the gas phase — there is no boiler, no condenser, no two-phase region to manage. This simplicity is why gas turbines power aircraft.

The governing efficiency formula for the ideal Brayton cycle, η = 1 − T₁/T₂ = 1 − (P₁/P₂)^((γ-1)/γ), shows that **pressure ratio** r_p = P₂/P₁ is the single control parameter. Higher pressure ratio raises the temperature at the end of compression, which means the heat addition occurs at a higher average temperature — analogous to how the Carnot efficiency improves when the cold reservoir is colder. For air with γ ≈ 1.4, doubling the pressure ratio from 5 to 10 increases efficiency from about 37% to 48%. Modern aircraft engines operate at pressure ratios of 40–50, pushing toward 60% ideal efficiency.

The critical nuance that distinguishes Brayton from Carnot analysis is the **back work ratio**. To run the turbine, you must first drive the compressor — which can consume 40–50% of the gross turbine output. Compare this to the Rankine cycle, where the pump consumes only 1–2% of turbine output because compressing a liquid requires far less work than compressing a gas (liquid is nearly incompressible). This means the Brayton cycle net work is sensitive to compressor inefficiency: a real compressor operating at 85% isentropic efficiency instead of 100% can slash net work output by 30%. The turbine irreversibilities matter too, but compressor performance is often the tighter constraint.

In real gas turbines, the isentropic relations T₂/T₁ = (P₂/P₁)^((γ-1)/γ) require **isentropic efficiencies** for the compressor and turbine: η_c = (ideal compressor work) / (actual compressor work) and η_t = (actual turbine work) / (ideal turbine work). These efficiencies appear as correction factors inside the temperature calculations. Once real irreversibilities are included, there is an optimal pressure ratio that maximizes net work output (not the same as maximum efficiency) — a key design trade-off in sizing industrial gas turbines for power generation versus aircraft engines where thrust-to-weight matters more than absolute efficiency.
