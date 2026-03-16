---
id: brayton-cycle-gas-turbine-thermodynamics
title: The Brayton Cycle and Gas Turbines
domain: physics
course: thermodynamics
prerequisites:
- id: thermodynamic-processes
  type: hard
- id: isobaric-and-isochoric-processes
  type: hard
builds-toward:
- pv-diagram-interpretation
- ts-diagram-entropy-temperature
tags:
- cycles
- turbines
- continuous-combustion
stage: formal-systems
status: draft
---

# The Brayton Cycle and Gas Turbines

## Core Idea
The Brayton cycle models gas turbines and jet engines: isentropic compression, isobaric (constant-pressure) heat addition in the combustion chamber, isentropic expansion through the turbine, and isobaric heat rejection. The thermal efficiency is η = 1 - 1/r_p^((γ-1)/γ), where r_p = P_2/P_1 is the pressure ratio; unlike the Otto cycle, Brayton efficiency depends on pressure ratio, not volume ratio. The Brayton cycle explains why turbojets operate efficiently at high altitudes and high speeds.

## How It's Best Learned
Sketch the Brayton cycle on both P-V and T-S diagrams. Derive the efficiency formula. Compare with Otto cycle efficiency behavior.

## Common Misconceptions
- Thinking the compression and expansion are isobaric (they are isentropic).
- Confusing pressure ratio with volume ratio.
- Assuming the Brayton cycle has constant efficiency (it improves with pressure ratio).

## Explainer

From your study of thermodynamic processes, you know that isentropic means adiabatic and reversible — no heat exchange, no entropy change. From isobaric processes, you know that heat can be added at constant pressure, with the gas expanding to absorb it. The Brayton cycle strings together two of each: two isentropic steps and two isobaric steps, in the specific order that models how a continuous-flow gas turbine operates. Understanding why this sequence makes engineering sense requires thinking about what a jet engine or gas turbine actually does with a continuous stream of air.

The four stages of the Brayton cycle trace a path on the P-V diagram. **Stage 1→2 (isentropic compression)**: the compressor takes in ambient air at low pressure P₁ and squeezes it adiabatically to high pressure P₂ = r_p P₁, raising its temperature in the process. No heat is exchanged; the work done on the gas raises its internal energy and temperature. **Stage 2→3 (isobaric heat addition)**: fuel burns in the combustion chamber at constant pressure, dumping heat Q_in into the high-pressure air and raising its temperature dramatically. This is the step unique to the Brayton cycle — in the Otto cycle (piston engine), combustion happens at constant volume. **Stage 3→4 (isentropic expansion)**: hot, high-pressure gas expands through the turbine, doing work (which drives both the compressor and the external load) and cooling adiabatically. **Stage 4→1 (isobaric heat rejection)**: the exhaust exits at low pressure and the cycle resets. In an open-cycle engine, fresh air enters at state 1 and exhaust exits at state 4, but thermodynamically this is equivalent to a closed isobaric cooling step.

The efficiency η = 1 − 1/r_p^{(γ−1)/γ} follows directly from the heat added and rejected. The key insight is that both the heat addition (stage 2→3) and rejection (stage 4→1) occur at constant pressure, and for an ideal gas, Q = c_p ΔT at constant pressure. So η = 1 − Q_out/Q_in = 1 − (T₄ − T₁)/(T₃ − T₂). For isentropic compression and expansion, T₂/T₁ = r_p^{(γ−1)/γ} and T₃/T₄ = r_p^{(γ−1)/γ} — the same ratio. This symmetry causes the temperature differences to cancel in a specific way, giving the remarkably clean efficiency formula. Unlike the Otto cycle, where efficiency depends on compression ratio r_V and the formula is η = 1 − 1/r_V^{γ−1}, the Brayton cycle depends on **pressure ratio** r_p because its compression and expansion are isentropic in a continuous-flow device where pressure — not volume — is the controlled variable.

This is why jet engines run at high altitude and high speed efficiently. The pressure ratio r_p in modern jet engines is 30–50:1, giving theoretical Brayton efficiencies of 55–60%. Higher altitude means lower ambient temperature T₁, which further improves efficiency (the compressor does less work). The actual cycle departs from ideal Brayton in two main ways: compressor and turbine inefficiencies (the actual compressions and expansions are not perfectly isentropic, so entropy is generated) and pressure drops in the combustor. These reduce real efficiencies to 35–45%, but the ideal Brayton analysis correctly identifies the key levers — raise r_p, raise turbine inlet temperature T₃, and minimize inefficiencies in the turbomachinery.
