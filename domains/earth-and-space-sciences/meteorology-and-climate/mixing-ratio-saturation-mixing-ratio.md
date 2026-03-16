---
id: mixing-ratio-saturation-mixing-ratio
title: Mixing Ratio and Saturation Mixing Ratio
domain: earth-and-space-sciences
course: meteorology-and-climate
prerequisites:
- id: saturation-vapor-pressure-clausius
  type: hard
- id: saturation-and-dew-point
  type: hard
builds-toward:
- convective-available-potential-energy
- lifted-index-stability
tags:
- moisture
- concentration
- saturation
stage: abstract-reasoning
status: draft
---

# Mixing Ratio and Saturation Mixing Ratio

## Core Idea
Mixing ratio is the mass of water vapor per unit mass of dry air, independent of pressure (unlike relative humidity). Saturation mixing ratio is the maximum mixing ratio air can hold at a given temperature and pressure. Comparing actual to saturation mixing ratio gives relative humidity, essential for understanding convective instability and cloud formation.

## Explainer

You already understand dew point and saturation — the idea that air at a given temperature can hold only so much water vapor before condensation begins. The **mixing ratio** makes this concept precise and quantitative by expressing moisture content as a mass ratio: grams of water vapor per kilogram of dry air. A typical midlatitude surface value might be 10 g/kg, meaning each kilogram of dry air carries 10 grams of water vapor mixed through it.

Why use mixing ratio instead of simpler measures like relative humidity? Because mixing ratio is a **conservative quantity** — it does not change when an unsaturated air parcel rises or sinks. As a parcel ascends and pressure drops, its volume changes and its temperature falls, but the ratio of water vapor mass to dry air mass stays the same (no water has been added or removed). Relative humidity, by contrast, increases as the parcel cools even though no moisture was added, because the denominator — the saturation capacity — is shrinking. This makes relative humidity unreliable for tracking a parcel's actual moisture content through the atmosphere. Mixing ratio stays constant until condensation begins, making it far more useful for thermodynamic calculations.

The **saturation mixing ratio** is the mixing ratio at which the air is fully saturated — the maximum water vapor the air can hold at its current temperature and pressure. It depends strongly on temperature (from the Clausius-Clapeyron relationship you already know) and weakly on pressure. At 30°C and sea-level pressure, the saturation mixing ratio is roughly 27 g/kg; at 0°C, it drops to about 3.8 g/kg. This dramatic temperature dependence is why warm tropical air can carry vastly more moisture than cold polar air, and why cooling air to its dew point inevitably leads to condensation.

The relationship between these two quantities connects directly to what you know about dew point and relative humidity. **Relative humidity** is simply the actual mixing ratio divided by the saturation mixing ratio, expressed as a percentage. When the mixing ratio equals the saturation mixing ratio, relative humidity is 100% and the air is at its dew point — condensation begins. On a thermodynamic diagram, forecasters plot both values for a sounding: the gap between the mixing ratio line and the saturation mixing ratio line tells you how far the air is from saturation at each level, which is critical for identifying where clouds will form, how much moisture is available for precipitation, and whether a lifted parcel will reach its level of free convection.
