---
id: saturation-vapor-pressure-clausius
title: Saturation Vapor Pressure and Clausius-Clapeyron Relation
domain: earth-and-space-sciences
course: meteorology-and-climate
prerequisites:
- id: phase-diagrams-clausius-clapeyron
  type: hard
builds-toward:
- mixing-ratio-saturation-mixing-ratio
- convective-available-potential-energy
tags:
- thermodynamics
- water-vapor
- pressure
- temperature
stage: abstract-reasoning
status: draft
---

# Saturation Vapor Pressure and Clausius-Clapeyron Relation

## Core Idea
Saturation vapor pressure is the maximum pressure exerted by water vapor in equilibrium with a liquid or ice surface, increasing exponentially with temperature following the Clausius-Clapeyron relation (~7% per K). This nonlinear relationship explains why warm air can hold much more moisture than cold air and why tropics are more humid. The relation also drives the strength of latent heat feedbacks in climate.

## How It's Best Learned
Plot saturation vapor pressure against temperature; observe the exponential increase. Apply the Magnus formula for quick estimates.

## Common Misconceptions
- Confusing saturation vapor pressure with actual vapor pressure; they are equal only when air is saturated. - Thinking the relationship is linear instead of exponential.

## Explainer

From your study of phase diagrams and the Clausius-Clapeyron equation, you know that the boundary between liquid and vapor phases on a pressure-temperature diagram is not a straight line but a curve that steepens with increasing temperature. The **saturation vapor pressure** is simply the vapor pressure along this curve — it is the pressure at which water vapor is in equilibrium with a liquid (or ice) surface at a given temperature. If the actual vapor pressure exceeds this value, condensation occurs; if it falls below, evaporation dominates.

The Clausius-Clapeyron relation gives the mathematical form of this curve: de_s/dT = (L · e_s) / (R_v · T²), where e_s is saturation vapor pressure, L is the latent heat of vaporization, R_v is the gas constant for water vapor, and T is temperature in Kelvin. Because e_s appears on both sides of the equation, the solution is exponential — saturation vapor pressure increases roughly **7% for every 1°C increase in temperature**. This means that 30°C air can hold about four times as much water vapor as 10°C air. The nonlinearity is dramatic: going from 0°C to 35°C, saturation vapor pressure increases from about 6 hPa to about 56 hPa — nearly a tenfold increase.

This exponential relationship has cascading consequences throughout meteorology and climate science. It explains why tropical air masses carry enormously more moisture than polar ones, why the most intense precipitation events occur in the warmest environments, and why coastal fog forms so readily when warm moist air flows over cold ocean water. For practical calculations, meteorologists often use the **Magnus formula** — an empirical approximation that gives saturation vapor pressure as a function of temperature without solving the differential equation directly. The Magnus formula (e_s ≈ 6.112 · exp(17.67T / (T + 243.5)), with T in °C and e_s in hPa) is accurate to within about 0.1% over the range of temperatures encountered in weather.

The Clausius-Clapeyron relation also underpins one of the most robust predictions in climate science: the **water vapor feedback**. As the planet warms, saturation vapor pressure rises, allowing the atmosphere to hold more water vapor. Since water vapor is itself a greenhouse gas, this additional moisture amplifies the original warming — a positive feedback loop. Observations confirm that atmospheric water vapor has increased at approximately the 7%/K rate predicted by Clausius-Clapeyron as global temperatures have risen. This same scaling governs extreme precipitation: the intensity of the heaviest rainfall events increases at roughly 7%/K because a warmer atmosphere can deliver more moisture to a storm system before the air is wrung dry.
