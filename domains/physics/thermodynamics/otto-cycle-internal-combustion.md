---
id: otto-cycle-internal-combustion
title: The Otto Cycle and Internal Combustion Engines
domain: physics
course: thermodynamics
prerequisites:
- id: thermodynamic-processes
  type: hard
- id: work-types-mechanical-pdv
  type: soft
builds-toward:
- diesel-cycle-compression-ignition
- pv-diagram-interpretation
tags:
- cycles
- engines
- efficiency
stage: formal-systems
status: draft
---

# The Otto Cycle and Internal Combustion Engines

## Core Idea
The Otto cycle models a four-stroke internal combustion engine: adiabatic compression, constant-volume heat addition (combustion), adiabatic expansion (power stroke), and constant-volume heat rejection. The thermal efficiency is η = 1 - 1/r^(γ-1), where r is the compression ratio and γ = C_p/C_v; higher compression ratios increase efficiency, explaining why high-octane fuels are valuable. The Otto cycle illustrates how thermodynamic principles limit engine performance.

## How It's Best Learned
Sketch the Otto cycle on a P-V diagram. Derive the efficiency formula. Compare theoretical efficiency with real engine values.

## Common Misconceptions
- Thinking the Otto cycle is reversible (it is idealized; real engines are irreversible).
- Confusing compression ratio with expansion ratio.
- Assuming all four strokes occur at constant volume (they do not—intake and exhaust are at atmospheric pressure).

## Explainer

From thermodynamic processes, you know how ideal gases behave under different constraints: isothermal (constant temperature), isobaric (constant pressure), isochoric (constant volume), and adiabatic (no heat exchange). The Otto cycle chains four of these processes together to model what happens inside a gasoline engine — not perfectly (real engines are messier), but accurately enough to explain why compression ratio matters and why there's a fundamental limit to engine efficiency.

Trace the cycle on a P-V diagram, starting with a fixed mass of gas in the cylinder just before compression. **Step 1: adiabatic compression** (A→B). The piston moves up, compressing the gas from volume V₁ to V₂ with no heat exchange (the process is fast enough that heat doesn't have time to flow). Pressure and temperature rise; the gas stores the work done by the piston as internal energy. The ratio r = V₁/V₂ is the **compression ratio** — the key design parameter. **Step 2: isochoric heat addition** (B→C). The spark fires and fuel burns almost instantaneously, adding heat Q_in at constant volume. Pressure and temperature spike sharply. **Step 3: adiabatic expansion** (C→D). The hot, high-pressure gas pushes the piston back down — this is the **power stroke** that does useful work. Volume returns to V₁, temperature and pressure drop. **Step 4: isochoric heat rejection** (D→A). The exhaust valve opens and waste heat Q_out leaves at constant volume (modeled as heat rejection rather than actual exhaust/intake). The cycle repeats.

The efficiency is the net work divided by the heat input: η = W_net/Q_in = 1 − Q_out/Q_in. Working through the adiabatic and isochoric calculations using PV^γ = const for the adiabats and ΔU = Q for the isochoric steps, you arrive at η = 1 − 1/r^(γ−1). This formula has a clean interpretation: higher compression ratio r means the gas is hotter when it enters the power stroke, extracting more work before the exhaust temperature. With γ = 1.4 (diatomic gas) and a typical compression ratio of r = 10, the ideal Otto efficiency is about 60%. Real engines achieve 25–35%, the gap explained by friction, heat losses to cylinder walls, incomplete combustion, and irreversible mixing.

The formula also explains **octane rating**. Higher compression ratios increase efficiency, but if the compression ratio is too high, the air-fuel mixture ignites spontaneously from compression heat before the spark fires — this is **engine knock**, a premature detonation that transmits force at the wrong moment and damages the engine. High-octane fuels resist this premature ignition, allowing higher compression ratios and therefore higher efficiency. "Premium fuel" isn't about more energy content per liter; it's about allowing the engine to operate at a higher r without knock. The Otto cycle thus directly connects thermodynamic theory — the efficiency formula — to the engineering tradeoff that determines what fuel you need at the pump.
