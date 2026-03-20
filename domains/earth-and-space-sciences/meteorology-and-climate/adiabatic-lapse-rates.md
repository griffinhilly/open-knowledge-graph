---
id: adiabatic-lapse-rates
title: Adiabatic Lapse Rates
domain: earth-and-space-sciences
course: meteorology-and-climate
prerequisites:
- id: thermal-structure-of-atmosphere
  type: hard
- id: latent-heat-and-phase-changes
  type: hard
- id: ideal-gas-law
  type: soft
- id: first-law-of-thermodynamics
  type: hard
- id: adiabatic-processes
  type: hard
builds-toward:
- convective-instability-indices
- atmospheric-stability-convection
- latent-heating-in-weather-systems
tags:
- adiabatic
- temperature
- lapse-rate
- convection
- thermodynamics
stage: advanced
status: draft
---

# Adiabatic Lapse Rates

## Core Idea
When an air parcel rises or sinks without exchanging heat with surroundings, its temperature changes at predictable rates called the dry adiabatic lapse rate (~9.8°C/km) for unsaturated air and the saturated adiabatic lapse rate (~5-6°C/km) for saturated air. The difference arises because latent heat release during condensation partially offsets adiabatic cooling, making saturated air cool more slowly as it rises.

## How It's Best Learned
Start with dry adiabatic processes using the ideal gas law to show why temperature drops with decreasing pressure. Then compare with saturated cases by explicitly calculating heat released during condensation and showing how it reduces the cooling rate.

## Common Misconceptions
- The saturated adiabatic lapse rate is constant; it varies with temperature and moisture content. - Adiabatic lapse rates apply to the environment rather than lifted parcels; only the parcel itself follows adiabatic paths.

## Explainer

From your study of adiabatic processes, you know that a parcel of air changing pressure without exchanging heat with its surroundings will change temperature — expanding air cools, compressing air warms. The **adiabatic lapse rate** quantifies exactly how fast this cooling or warming occurs as the parcel moves vertically through the atmosphere. Because pressure decreases with altitude (as you learned from the thermal structure of the atmosphere), a rising parcel always expands and cools. The question is: how quickly?

For unsaturated air, the answer comes directly from the first law of thermodynamics and the ideal gas law. When no condensation is occurring, the only energy exchange is between the parcel's internal energy and the work it does expanding against lower surrounding pressure. This gives the **dry adiabatic lapse rate (DALR)** of approximately 9.8°C per kilometer of ascent. This value is essentially constant because it depends only on gravity and the specific heat of dry air, neither of which varies meaningfully across typical atmospheric conditions. A parcel of dry air rising from the surface will cool at this fixed rate regardless of how warm or cold it starts.

The situation changes dramatically when the parcel reaches saturation. As a saturated parcel continues to rise and cool, water vapor condenses into droplets, and condensation releases **latent heat** back into the parcel. This latent heat partially compensates for the adiabatic cooling, so the parcel cools more slowly than it would if it were dry. The resulting **saturated (or moist) adiabatic lapse rate (SALR)** is typically around 5–6°C/km, but unlike the DALR, it is not constant. Warmer air holds exponentially more moisture (from the Clausius-Clapeyron relation), so a warm saturated parcel releases far more latent heat per kilometer of ascent than a cold one. Near the tropical surface, the SALR can be as low as 3–4°C/km; in the cold upper troposphere, it approaches the DALR because there is almost no moisture left to condense.

The practical importance of these two rates is enormous. The actual temperature profile of the atmosphere — the **environmental lapse rate** — is measured by weather balloons, not predicted by adiabatic theory. But by comparing the environmental lapse rate to the DALR and SALR, meteorologists determine atmospheric stability. If the environment cools faster than the DALR, any displaced parcel (whether saturated or not) will be warmer than its surroundings and will accelerate upward — the atmosphere is absolutely unstable and convection is vigorous. If the environment cools more slowly than the SALR, displaced parcels always end up cooler than their surroundings and sink back — the atmosphere is absolutely stable. Between these extremes lies conditional instability, where dry parcels are stable but saturated parcels are unstable. This conditional regime is where most thunderstorm development occurs: the atmosphere resists dry lifting but, once a parcel is forced to its condensation level and becomes saturated, latent heat release can trigger explosive convective growth.
