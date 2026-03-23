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
stage: formal-systems
status: validated
---

# Clausius-Clapeyron Equation and Saturation Conditions

## Core Idea
The Clausius-Clapeyron equation dP/dT = h_fg / (T * v_fg) relates saturation pressure and temperature for phase equilibria. This differential equation predicts how saturation pressure varies with temperature, enabling accurate interpolation in saturation tables and estimation of vapor pressure at unmeasured conditions. The equation reveals why vapor pressure increases rapidly with temperature, affecting equipment design pressure ratings.

## Questions

```yaml
- question: "A pressure cooker sealed at 2 atmospheres reaches a steady temperature of about 120°C instead of 100°C. Which statement best explains this using the Clausius-Clapeyron equation?"
  type: multiple-choice
  options:
    - "Higher pressure compresses the water molecules, raising their kinetic energy and therefore the temperature directly"
    - "At 2 atm, the saturation temperature is higher — water cannot boil until it reaches the temperature where its vapor pressure equals the applied pressure"
    - "Higher pressure reduces the latent heat h_fg, making water easier to vaporize at lower temperatures"
    - "The pressure cooker heats the water above its boiling point because the lid prevents evaporation"
  answer: 1
  explanation: "The Clausius-Clapeyron equation establishes that saturation pressure and saturation temperature are coupled along the phase boundary. Boiling occurs when the vapor pressure of water equals the external pressure — the saturation condition. At 2 atm (≈ 202 kPa), the saturation temperature is about 120°C; the water simply cannot boil until it reaches that temperature. This is not about compression raising kinetic energy (option A) — it is about the thermodynamic equilibrium condition. The practical consequence is that pressure cookers cook faster because the higher temperature accelerates chemical reactions (Maillard browning, protein denaturation) by a factor of roughly 4× over sea-level boiling."

- question: "For water, the ice-water phase boundary has a negative slope (dP/dT < 0) — increasing pressure lowers the melting point. For almost all other substances, this slope is positive. What structural property of water explains the negative slope?"
  type: multiple-choice
  options:
    - "Water has an unusually high latent heat of fusion, which makes h_fg negative in the Clausius-Clapeyron equation"
    - "Liquid water is denser than ice — water expands on freezing, so v_liq < v_solid and v_fg = v_liq − v_solid < 0, giving dP/dT < 0"
    - "The entropy difference between ice and liquid water is negative, reversing the sign of the equation"
    - "The high polarity of water molecules reverses the normal pressure-melting relationship"
  answer: 1
  explanation: "The Clausius-Clapeyron equation gives dP/dT = Δs/Δv = h_fg/(T·v_fg). For melting, v_fg = v_liquid − v_solid. For water uniquely, ice is less dense than liquid water (ice floats), so v_solid > v_liquid and v_fg < 0. With h_fg > 0 and T > 0, the slope becomes negative. For virtually every other substance, the solid is denser than the liquid, v_fg > 0, and the slope is positive (higher pressure raises the melting point). This anomaly has profound consequences — it is why ice skating and glacier motion are possible through pressure-induced melting."

- question: "The Clausius-Clapeyron equation is derived by applying the first law of thermodynamics (energy conservation) to the latent heat released during a phase transition."
  type: true-false
  answer: false
  explanation: "False. The Clausius-Clapeyron equation is derived from the condition for thermodynamic equilibrium at the phase boundary — that the Gibbs free energy of both phases must be equal: g_liq = g_vap. Using the fundamental relation dg = −s dT + v dP and requiring dg_liq = dg_vap as you move along the saturation curve yields dP/dT = Δs/Δv = h_fg/(T·v_fg). This is fundamentally a second-law (entropy and Gibbs energy) result, not a first-law result. The first law alone tells you how much energy is exchanged during a phase change but says nothing about when equilibrium is achieved or how saturation pressure varies with temperature."

- question: "The approximate integrated form of the Clausius-Clapeyron equation, ln(P₂/P₁) = (h_fg/R)(1/T₁ − 1/T₂), predicts that vapor pressure increases exponentially as temperature increases."
  type: true-false
  answer: true
  explanation: "True. Rearranging the integrated form, ln P = constant − h_fg/(RT), shows that ln P is linear in 1/T. This means P = A·exp(−h_fg/RT) — vapor pressure is exponential in the inverse of temperature. As T increases, 1/T decreases, the exponent becomes less negative, and P rises rapidly. This explains why small temperature increases near the boiling point produce large changes in vapor pressure, and why the saturation curve is concave upward on a P-T diagram. The exponential relationship also means linear interpolation in steam tables slightly underestimates saturation pressure between table entries."

- question: "Why must the derivation of the Clausius-Clapeyron equation invoke Gibbs free energy rather than just applying enthalpy balance to the phase transition?"
  type: short-answer
  answer: "Enthalpy balance (the first law) tells you how much energy is exchanged when a phase change occurs — the latent heat h_fg. But it does not tell you under what conditions the two phases are in equilibrium or how that equilibrium condition changes with temperature and pressure. Equilibrium between two phases requires that their chemical potentials (Gibbs free energies per mole) be equal: g_liq = g_vap. This is a second-law condition. Differentiating this equality along the phase boundary using dg = −s dT + v dP is what generates dP/dT = Δs/Δv, and substituting h_fg = TΔs converts this to the standard form. Without the Gibbs equality, you have no equation relating the slope of the phase boundary to the properties of the substance."
  explanation: "This reflects a general principle in thermodynamics: equilibrium conditions are governed by minimizing the appropriate free energy, not just conserving energy. The first law constrains what processes are possible energetically; the second law (via entropy or free energy) determines which state the system reaches. The Clausius-Clapeyron equation is a thermodynamic identity that follows from applying the equilibrium condition along the phase boundary — it is geometry on the P-T diagram, expressed in thermodynamic language."
```

## Explainer

The Clausius-Clapeyron equation describes the slope of the saturation curve — the boundary between liquid and vapor on a P-T diagram — and it comes directly from the thermodynamic condition for phase equilibrium. You know from entropy calculations that at equilibrium, the Gibbs free energy of both phases must be equal: g_liq = g_vap. As you move along the saturation curve, both phases remain in equilibrium, so their Gibbs energies stay equal: dg_liq = dg_vap. Using the fundamental relation dg = −s dT + v dP, equating gives −s_liq dT + v_liq dP = −s_vap dT + v_vap dP. Rearranging: dP/dT = (s_vap − s_liq)/(v_vap − v_liq) = Δs_fg/v_fg. Since the latent heat of vaporization satisfies h_fg = T·Δs_fg at constant temperature and pressure, this becomes **dP/dT = h_fg / (T · v_fg)**.

The equation has a clear physical meaning: the steeper the saturation curve (large dP/dT), the more quickly vapor pressure rises with temperature. For water at 100°C and 1 atm, h_fg ≈ 2257 kJ/kg and v_fg ≈ 1.67 m³/kg, giving dP/dT ≈ 3.6 kPa/K. Raising the temperature by 10°C increases saturation pressure by roughly 36 kPa — this is why pressure cookers at 2 atm reach ~120°C instead of 100°C. For **steam tables at intermediate temperatures**, the Clausius-Clapeyron equation justifies why linear interpolation slightly underestimates saturation pressure (the curve is concave-up), and it enables accurate extrapolation beyond table limits.

A useful approximation for low pressures: when the vapor behaves as an ideal gas, v_fg ≈ v_g ≈ RT/P. Substituting: dP/dT = h_fg·P/(RT²), which separates as dP/P = (h_fg/R)·dT/T². Integrating between two states gives the **approximate Clausius-Clapeyron** form: ln(P₂/P₁) = (h_fg/R)·(1/T₁ − 1/T₂). This equation treats h_fg as constant (acceptable over modest temperature ranges), and it lets you estimate vapor pressure at any temperature from a single reference point without needing full steam tables.

The equation's power extends beyond steam: it applies to any phase transition, including solid-liquid (ice melting under pressure) and solid-vapor (sublimation). For ice, v_liq < v_solid (water expands on freezing), so v_fg = v_liq − v_solid < 0, and the slope dP/dT is *negative* — the melting point decreases under pressure. For almost all other substances, liquids are less dense than solids, giving a positive slope. The Clausius-Clapeyron equation is therefore a window into the P-T phase diagram of any pure substance, and its derivation reinforces that equilibrium thermodynamics is fundamentally about entropy and Gibbs energy, not just energy balance.
