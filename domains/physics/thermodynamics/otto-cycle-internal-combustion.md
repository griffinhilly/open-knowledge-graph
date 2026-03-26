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
status: validated
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

## Questions

```yaml
- question: "According to the Otto cycle efficiency formula η = 1 − 1/r^(γ−1), which change would most directly increase the thermal efficiency of an ideal engine?"
  type: multiple-choice
  options:
    - "Using more fuel per cycle to add more heat Q_in"
    - "Increasing the compression ratio r"
    - "Using a monatomic gas (lower γ) as the working fluid"
    - "Lengthening the time of the power stroke"
  answer: 1
  explanation: "The efficiency formula contains only r (compression ratio) and γ (heat capacity ratio) as variables — Q_in does not appear. Higher r increases η because the gas is compressed more before the power stroke, making it hotter and higher-pressure at combustion, so it extracts more work per unit of heat added. Option A is a common misconception: adding more heat increases both W_net and Q_in proportionally for an ideal cycle, leaving η unchanged. Option C is wrong: lower γ decreases the exponent, reducing efficiency. The cycle's duration doesn't affect ideal efficiency."

- question: "Why does high-octane premium gasoline allow a car engine to achieve higher efficiency than regular gasoline?"
  type: multiple-choice
  options:
    - "It contains more chemical energy per liter, producing more heat per combustion cycle"
    - "It resists premature ignition (knock), allowing the engine to operate at a higher compression ratio"
    - "It burns more slowly, extending the power stroke duration"
    - "It reduces friction in the cylinder walls, lowering mechanical losses"
  answer: 1
  explanation: "Premium fuel's value is not more energy content but a higher resistance to autoignition. At high compression ratios, the fuel-air mixture reaches temperatures that can ignite it prematurely before the spark fires — engine knock. This premature detonation damages the engine and wastes the power stroke. High-octane fuel tolerates higher compression without knock, allowing the engine to run at a higher r, which directly increases η via the efficiency formula. Option A is a common misconception; octane rating is not a measure of energy content."

- question: "The power stroke in the Otto cycle is an isothermal (constant-temperature) expansion."
  type: true-false
  answer: false
  explanation: "The power stroke (step C→D in the Otto cycle) is an *adiabatic* expansion — no heat is exchanged with the surroundings during this rapid process. Temperature and pressure both drop as the gas does work pushing the piston down. An isothermal process requires constant temperature, which would require continuous heat addition to compensate for the work done — the opposite of what happens in an adiabatic expansion. Confusing these two is a common error when first learning thermodynamic cycles."

- question: "Increasing the compression ratio indefinitely would usually increase Otto cycle efficiency in a real engine."
  type: true-false
  answer: false
  explanation: "While the formula η = 1 − 1/r^(γ−1) increases monotonically with r in the ideal case, real engines face a critical constraint: above a certain compression ratio, the fuel-air mixture autoignites from compression heat before the spark fires (engine knock). Knock causes premature, uncontrolled combustion that delivers force at the wrong moment and damages the engine. High-octane fuel raises the knock threshold but cannot eliminate it entirely. Real efficiency is therefore limited by fuel properties, not just thermodynamics."

- question: "Why does higher compression ratio increase the efficiency of the Otto cycle, according to the thermodynamic analysis?"
  type: short-answer
  answer: "Higher compression ratio means the gas is more compressed (smaller volume, higher temperature and pressure) before combustion. When the same amount of heat Q_in is added at this higher temperature, the gas expands from a higher-energy state during the power stroke, doing more work before the exhaust temperature is reached. The waste heat Q_out is therefore a smaller fraction of Q_in, so η = 1 − Q_out/Q_in is higher."
  explanation: "The mathematical expression of this is η = 1 − 1/r^(γ−1): as r increases, 1/r^(γ−1) decreases, so η increases toward 1. The physical interpretation is that more compression before combustion 'pre-loads' the gas thermodynamically, and the longer adiabatic expansion from a higher starting point extracts more work. The exhaust gas leaves at a lower temperature relative to the peak temperature, meaning less energy is wasted."
```

## Explainer

From thermodynamic processes, you know how ideal gases behave under different constraints: isothermal (constant temperature), isobaric (constant pressure), isochoric (constant volume), and adiabatic (no heat exchange). The Otto cycle chains four of these processes together to model what happens inside a gasoline engine — not perfectly (real engines are messier), but accurately enough to explain why compression ratio matters and why there's a fundamental limit to engine efficiency.

Trace the cycle on a P-V diagram, starting with a fixed mass of gas in the cylinder just before compression. **Step 1: adiabatic compression** (A→B). The piston moves up, compressing the gas from volume V₁ to V₂ with no heat exchange (the process is fast enough that heat doesn't have time to flow). Pressure and temperature rise; the gas stores the work done by the piston as internal energy. The ratio r = V₁/V₂ is the **compression ratio** — the key design parameter. **Step 2: isochoric heat addition** (B→C). The spark fires and fuel burns almost instantaneously, adding heat Q_in at constant volume. Pressure and temperature spike sharply. **Step 3: adiabatic expansion** (C→D). The hot, high-pressure gas pushes the piston back down — this is the **power stroke** that does useful work. Volume returns to V₁, temperature and pressure drop. **Step 4: isochoric heat rejection** (D→A). The exhaust valve opens and waste heat Q_out leaves at constant volume (modeled as heat rejection rather than actual exhaust/intake). The cycle repeats.

The efficiency is the net work divided by the heat input: η = W_net/Q_in = 1 − Q_out/Q_in. Working through the adiabatic and isochoric calculations using PV^γ = const for the adiabats and ΔU = Q for the isochoric steps, you arrive at η = 1 − 1/r^(γ−1). This formula has a clean interpretation: higher compression ratio r means the gas is hotter when it enters the power stroke, extracting more work before the exhaust temperature. With γ = 1.4 (diatomic gas) and a typical compression ratio of r = 10, the ideal Otto efficiency is about 60%. Real engines achieve 25–35%, the gap explained by friction, heat losses to cylinder walls, incomplete combustion, and irreversible mixing.

The formula also explains **octane rating**. Higher compression ratios increase efficiency, but if the compression ratio is too high, the air-fuel mixture ignites spontaneously from compression heat before the spark fires — this is **engine knock**, a premature detonation that transmits force at the wrong moment and damages the engine. High-octane fuels resist this premature ignition, allowing higher compression ratios and therefore higher efficiency. "Premium fuel" isn't about more energy content per liter; it's about allowing the engine to operate at a higher r without knock. The Otto cycle thus directly connects thermodynamic theory — the efficiency formula — to the engineering tradeoff that determines what fuel you need at the pump.
