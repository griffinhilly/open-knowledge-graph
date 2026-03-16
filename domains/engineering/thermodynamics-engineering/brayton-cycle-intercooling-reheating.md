---
id: brayton-cycle-intercooling-reheating
title: 'Brayton Cycle Modifications: Intercooling and Reheating'
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: brayton-cycle-gas-turbine
  type: hard
tags:
- brayton-cycle
- intercooling
- reheating
- gas-turbines
stage: advanced
status: draft
---

# Brayton Cycle Modifications: Intercooling and Reheating

## Core Idea
Intercooling (cooling air between compressor stages) reduces net compression work by exploiting polytropic efficiency, while reheating (adding heat between turbine stages) increases net turbine output. Combined intercooling and reheating improve cycle thermal efficiency, though they add complexity and require multiple heat exchangers. Analysis involves tracking pressure and temperature through each stage, comparing actual polytropic paths to isentropic ideals.

## Explainer

From the basic Brayton cycle you know the thermal efficiency depends on the pressure ratio: η = 1 − (T₁/T₂) = 1 − r_p^(−(γ−1)/γ). The compressor consumes a large fraction of turbine output, and the net work ratio — net work divided by turbine work — is often only 40–60% for simple Brayton cycles. **Intercooling** and **reheating** are modifications that attack this limitation from opposite sides of the cycle.

**Intercooling** splits the compression into two (or more) stages with a heat exchanger between them. After the first compressor stage raises the pressure partway, the air is cooled back toward the inlet temperature before entering the second stage. Why does this help? Because compressor work is proportional to the absolute temperature at the inlet: w_c = c_p(T_out − T_in), and compressing hot gas requires more work than compressing cool gas to the same pressure ratio. Cooling between stages keeps the inlet temperature of the second stage low, approaching the ideal of **isothermal compression** — the theoretical limit where compression follows pT = constant rather than pT^γ = constant. With two equal pressure-ratio stages, the optimal intercooling splits the overall pressure ratio at its geometric mean (√r_p for two stages), minimizing total compressor work.

**Reheating** applies the same logic on the turbine side. After the gas expands through the first turbine stage, it is reheated in a combustor before entering the second stage. This keeps the expansion temperature high, increasing the work extracted. Without reheating, the gas cools rapidly during expansion and exits with less energy remaining; reheating essentially restores the driving temperature difference for the second expansion. The optimal reheat pressure for maximum work is also the geometric mean pressure.

Combined intercooling and reheating together raise the net specific work output significantly and, when paired with a **regenerator** (a heat exchanger recovering exhaust heat to preheat compressed air before combustion), can substantially improve overall efficiency. The regenerator alone cannot work well in the simple Brayton cycle because the compressed air exits hotter than the turbine exhaust; intercooling lowers the compressed-air temperature and reheating raises the exhaust temperature, making regeneration effective. This combination — intercooling + reheating + regeneration — is the thermodynamic basis for high-efficiency industrial gas turbines and some aircraft turbofan designs. Analysis tracks temperature and pressure at each stage boundary, with isentropic relations giving ideal temperatures and polytropic efficiency adjusting them for real compressor and turbine performance.
