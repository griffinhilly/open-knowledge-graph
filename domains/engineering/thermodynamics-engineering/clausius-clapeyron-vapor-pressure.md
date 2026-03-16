---
id: clausius-clapeyron-vapor-pressure
title: Clausius-Clapeyron Equation and Saturation Conditions
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: entropy-calculation-properties
  type: hard
- id: differential-equations
  type: hard
tags:
- clausius-clapeyron
- vapor-pressure
- saturation
stage: advanced
status: draft
---

# Clausius-Clapeyron Equation and Saturation Conditions

## Core Idea
The Clausius-Clapeyron equation dP/dT = h_fg / (T * v_fg) relates saturation pressure and temperature for phase equilibria. This differential equation predicts how saturation pressure varies with temperature, enabling accurate interpolation in saturation tables and estimation of vapor pressure at unmeasured conditions. The equation reveals why vapor pressure increases rapidly with temperature, affecting equipment design pressure ratings.

## Explainer

The Clausius-Clapeyron equation describes the slope of the saturation curve — the boundary between liquid and vapor on a P-T diagram — and it comes directly from the thermodynamic condition for phase equilibrium. You know from entropy calculations that at equilibrium, the Gibbs free energy of both phases must be equal: g_liq = g_vap. As you move along the saturation curve, both phases remain in equilibrium, so their Gibbs energies stay equal: dg_liq = dg_vap. Using the fundamental relation dg = −s dT + v dP, equating gives −s_liq dT + v_liq dP = −s_vap dT + v_vap dP. Rearranging: dP/dT = (s_vap − s_liq)/(v_vap − v_liq) = Δs_fg/v_fg. Since the latent heat of vaporization satisfies h_fg = T·Δs_fg at constant temperature and pressure, this becomes **dP/dT = h_fg / (T · v_fg)**.

The equation has a clear physical meaning: the steeper the saturation curve (large dP/dT), the more quickly vapor pressure rises with temperature. For water at 100°C and 1 atm, h_fg ≈ 2257 kJ/kg and v_fg ≈ 1.67 m³/kg, giving dP/dT ≈ 3.6 kPa/K. Raising the temperature by 10°C increases saturation pressure by roughly 36 kPa — this is why pressure cookers at 2 atm reach ~120°C instead of 100°C. For **steam tables at intermediate temperatures**, the Clausius-Clapeyron equation justifies why linear interpolation slightly underestimates saturation pressure (the curve is concave-up), and it enables accurate extrapolation beyond table limits.

A useful approximation for low pressures: when the vapor behaves as an ideal gas, v_fg ≈ v_g ≈ RT/P. Substituting: dP/dT = h_fg·P/(RT²), which separates as dP/P = (h_fg/R)·dT/T². Integrating between two states gives the **approximate Clausius-Clapeyron** form: ln(P₂/P₁) = (h_fg/R)·(1/T₁ − 1/T₂). This equation treats h_fg as constant (acceptable over modest temperature ranges), and it lets you estimate vapor pressure at any temperature from a single reference point without needing full steam tables.

The equation's power extends beyond steam: it applies to any phase transition, including solid-liquid (ice melting under pressure) and solid-vapor (sublimation). For ice, v_liq < v_solid (water expands on freezing), so v_fg = v_liq − v_solid < 0, and the slope dP/dT is *negative* — the melting point decreases under pressure. For almost all other substances, liquids are less dense than solids, giving a positive slope. The Clausius-Clapeyron equation is therefore a window into the P-T phase diagram of any pure substance, and its derivation reinforces that equilibrium thermodynamics is fundamentally about entropy and Gibbs energy, not just energy balance.
