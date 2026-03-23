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
stage: formal-systems
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

## Questions

```yaml
- question: "A gas turbine produces 900 kJ/kg of gross turbine work and has a back work ratio of 45%. What is the net work output?"
  type: multiple-choice
  options:
    - "900 kJ/kg — the back work ratio in gas turbines is negligible"
    - "495 kJ/kg"
    - "810 kJ/kg — only friction losses reduce the gross output"
    - "450 kJ/kg"
  answer: 1
  explanation: "Back work ratio = compressor work / turbine work = 0.45, so compressor work = 0.45 × 900 = 405 kJ/kg. Net work = 900 − 405 = 495 kJ/kg. Option A is the classic misconception from confusing the Brayton cycle with the Rankine cycle, where the pump consumes only 1–2% of turbine output. In the Brayton cycle, compressing a gas (rather than a nearly incompressible liquid) requires enormous work, making the back work ratio one of the cycle's defining characteristics."

- question: "A Rankine cycle pump and a Brayton cycle compressor each raise the working fluid from 1 bar to 100 bar. The pump consumes about 10 kJ/kg while the compressor consumes about 450 kJ/kg. What is the fundamental reason for this 45-fold difference?"
  type: multiple-choice
  options:
    - "The Brayton compressor is less aerodynamically efficient than the Rankine pump"
    - "The Rankine cycle operates at lower pressure ratios in practice, reducing pump work"
    - "Compressing a gas requires far more work than compressing a nearly incompressible liquid to the same pressure, because a gas has much larger specific volume throughout compression"
    - "The Brayton cycle uses air as the working fluid, which has a higher molecular weight than steam"
  answer: 2
  explanation: "The work required to compress a fluid equals the integral of v dP along the compression path. For liquid water, specific volume v is tiny and nearly constant, making pump work ≈ v(P₂ − P₁) — very small. For air (a gas), specific volume is orders of magnitude larger throughout compression, making the integral far larger. This is a fundamental thermodynamic consequence of the state of the working fluid, not an engineering imperfection. It is precisely why Rankine cycles condense steam to liquid before pumping — doing so dramatically reduces compression work."

- question: "In the ideal Brayton cycle, increasing the pressure ratio always increases the thermal efficiency."
  type: true-false
  answer: true
  explanation: "The ideal Brayton efficiency is η = 1 − (P₁/P₂)^((γ−1)/γ) = 1 − 1/r_p^((γ−1)/γ). Since the exponent (γ−1)/γ is positive (≈ 0.286 for air with γ ≈ 1.4), r_p^((γ−1)/γ) increases monotonically with pressure ratio, so the subtracted term decreases and η increases. Real engines have a practical optimum because compressor irreversibilities grow at high pressure ratios and turbine inlet temperature is materials-limited — but these are departures from the ideal, not contradictions of it."

- question: "In a real Brayton cycle, turbine irreversibilities are more damaging to net work output than compressor irreversibilities of the same fractional magnitude, because the turbine produces all the useful work."
  type: true-false
  answer: false
  explanation: "Compressor irreversibilities are typically more damaging in practice, precisely because of the large back work ratio. A 10% increase in compressor work (due to irreversibility) on a baseline of 400 kJ/kg cuts net work by 40 kJ/kg. Additionally, compressor fouling from airborne particles is a common real-world degradation mechanism. The claim that turbine irreversibilities are worse confuses gross output with net output — the compressor's large fraction of turbine work means the multiplied effect of compressor inefficiency is severe, and it is often the tighter design constraint."

- question: "Explain why the back work ratio in the Brayton cycle is so much larger than in the Rankine cycle, and what consequence this has for how sensitive gas turbine net output is to compressor isentropic efficiency."
  type: short-answer
  answer: "In the Brayton cycle the working fluid is always a gas, and compressing a gas requires work proportional to its specific volume integrated over the pressure rise — far more than compressing a liquid to the same pressure. The Rankine cycle avoids this by condensing steam to liquid before pumping, making pump work negligible. Because the Brayton compressor consumes 40–50% of gross turbine output, a small drop in compressor isentropic efficiency has a large absolute effect on net work: if the compressor needs 10% more work due to internal losses, that 10% is applied to the already-large compressor baseline, cutting net output by a disproportionate fraction."
  explanation: "This explains why gas turbine designers invest heavily in compressor aerodynamics and why compressor fouling — from airborne particles coating blade surfaces — is a major maintenance concern in industrial and aviation gas turbines. A few percent reduction in compressor efficiency can meaningfully reduce power output and increase specific fuel consumption."
```

## Explainer

You know from the first law and the ideal gas that work can be extracted from a gas by expanding it and input work must be spent compressing it. The **Brayton cycle** chains these two processes through heat addition and rejection: compress the air isentropically, add heat at constant pressure (by burning fuel), expand the hot gas isentropically through a turbine, and reject heat to the atmosphere at constant pressure. Unlike the Rankine cycle's phase change, the Brayton cycle operates entirely in the gas phase — there is no boiler, no condenser, no two-phase region to manage. This simplicity is why gas turbines power aircraft.

The governing efficiency formula for the ideal Brayton cycle, η = 1 − T₁/T₂ = 1 − (P₁/P₂)^((γ-1)/γ), shows that **pressure ratio** r_p = P₂/P₁ is the single control parameter. Higher pressure ratio raises the temperature at the end of compression, which means the heat addition occurs at a higher average temperature — analogous to how the Carnot efficiency improves when the cold reservoir is colder. For air with γ ≈ 1.4, doubling the pressure ratio from 5 to 10 increases efficiency from about 37% to 48%. Modern aircraft engines operate at pressure ratios of 40–50, pushing toward 60% ideal efficiency.

The critical nuance that distinguishes Brayton from Carnot analysis is the **back work ratio**. To run the turbine, you must first drive the compressor — which can consume 40–50% of the gross turbine output. Compare this to the Rankine cycle, where the pump consumes only 1–2% of turbine output because compressing a liquid requires far less work than compressing a gas (liquid is nearly incompressible). This means the Brayton cycle net work is sensitive to compressor inefficiency: a real compressor operating at 85% isentropic efficiency instead of 100% can slash net work output by 30%. The turbine irreversibilities matter too, but compressor performance is often the tighter constraint.

In real gas turbines, the isentropic relations T₂/T₁ = (P₂/P₁)^((γ-1)/γ) require **isentropic efficiencies** for the compressor and turbine: η_c = (ideal compressor work) / (actual compressor work) and η_t = (actual turbine work) / (ideal turbine work). These efficiencies appear as correction factors inside the temperature calculations. Once real irreversibilities are included, there is an optimal pressure ratio that maximizes net work output (not the same as maximum efficiency) — a key design trade-off in sizing industrial gas turbines for power generation versus aircraft engines where thrust-to-weight matters more than absolute efficiency.
