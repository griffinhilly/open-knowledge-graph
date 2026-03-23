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
stage: formal-systems
status: draft
---

# Adiabatic Lapse Rates

## Core Idea
When an air parcel rises or sinks without exchanging heat with surroundings, its temperature changes at predictable rates called the dry adiabatic lapse rate (~9.8°C/km) for unsaturated air and the saturated adiabatic lapse rate (~5-6°C/km) for saturated air. The difference arises because latent heat release during condensation partially offsets adiabatic cooling, making saturated air cool more slowly as it rises.

## How It's Best Learned
Start with dry adiabatic processes using the ideal gas law to show why temperature drops with decreasing pressure. Then compare with saturated cases by explicitly calculating heat released during condensation and showing how it reduces the cooling rate.

## Common Misconceptions
- The saturated adiabatic lapse rate is constant; it varies with temperature and moisture content. - Adiabatic lapse rates apply to the environment rather than lifted parcels; only the parcel itself follows adiabatic paths.

## Questions

```yaml
- question: "A saturated air parcel near the warm tropical surface rises 1 km. Compared to a dry unsaturated parcel rising the same distance, the saturated parcel will:"
  type: multiple-choice
  options:
    - "Cool at the same rate — both follow the first law of thermodynamics without heat exchange"
    - "Cool more slowly — condensation releases latent heat into the parcel, partially offsetting adiabatic cooling"
    - "Cool more quickly — carrying moisture increases the total heat the parcel must lose"
    - "Stop cooling once condensation begins, then resume cooling at the dry rate"
  answer: 1
  explanation: "As a saturated parcel rises and cools, water vapor condenses and releases latent heat back into the parcel. This heat partially compensates for the adiabatic cooling due to expansion, so the net cooling rate is lower than the dry adiabatic lapse rate (~9.8°C/km). Near warm tropical surfaces where moisture content is high, the SALR can be as low as 3–4°C/km. The cooling does not stop — it just proceeds more slowly than it would without condensation."

- question: "The environmental lapse rate in a particular region is 11°C/km. A dry (unsaturated) air parcel is displaced upward. How will it behave?"
  type: multiple-choice
  options:
    - "It accelerates upward — it cools at 9.8°C/km and stays warmer than the surrounding environment, which is cooling faster at 11°C/km"
    - "It sinks back — it cools faster than the environment and becomes colder than its surroundings"
    - "It remains neutrally buoyant — the parcel always equilibrates with the environment"
    - "It rises only until it becomes saturated, then follows the saturated lapse rate"
  answer: 0
  explanation: "Atmospheric stability is determined by comparing the parcel's cooling rate to the environmental lapse rate. The dry parcel cools at 9.8°C/km; the environment cools at 11°C/km (faster). After rising 1 km, the parcel has cooled 9.8°C but the environment has cooled 11°C — so the parcel is now warmer than its surroundings and positively buoyant. It will accelerate upward. This is absolute instability: the environment cools faster than the DALR."

- question: "The saturated adiabatic lapse rate is approximately constant at 5–6°C/km regardless of the temperature or moisture content of the air."
  type: true-false
  answer: false
  explanation: "The SALR is not constant — it varies strongly with temperature and moisture content. Warmer air holds exponentially more moisture (following the Clausius-Clapeyron relation), so a warm saturated parcel releases far more latent heat per kilometer of ascent than a cold one. Near the warm tropical surface, the SALR can be as low as 3–4°C/km. In the cold upper troposphere, where almost no moisture remains, the SALR approaches the DALR (~9.8°C/km). This contrasts with the DALR, which depends only on gravity and the specific heat of dry air and is essentially constant."

- question: "Adiabatic lapse rates describe the temperature profile of the environment (how temperature actually varies with altitude in the atmosphere), not the behavior of rising or sinking air parcels."
  type: true-false
  answer: false
  explanation: "This is a key misconception. Adiabatic lapse rates describe how the temperature of an air parcel changes as it moves vertically without exchanging heat with its surroundings. The *environmental* lapse rate is the actual observed temperature profile of the surrounding atmosphere, measured by weather balloons. Atmospheric stability is determined by comparing these two: if the environment cools faster than the parcel, the parcel stays warmer than its surroundings and rises freely. The two rates are distinct and must not be confused."

- question: "Why is the saturated adiabatic lapse rate lower than the dry adiabatic lapse rate, and why does the SALR vary with temperature while the DALR does not?"
  type: short-answer
  answer: "The SALR is lower because condensation releases latent heat into the rising parcel, partially offsetting the adiabatic cooling from expansion. The net cooling rate is therefore less than the DALR. The SALR varies with temperature because warmer air holds exponentially more moisture — a warm saturated parcel releases far more latent heat per kilometer than a cold one, making its effective cooling rate much lower. The DALR is constant because it depends only on gravity and the specific heat of dry air, both of which are essentially fixed across atmospheric conditions."
  explanation: "The difference between DALR and SALR is the engine of convective instability. When the environment cools faster than the SALR, any parcel (wet or dry) is buoyant and convection is vigorous. When the environment cools at a rate between SALR and DALR (conditional instability), only saturated parcels are buoyant — explaining why thunderstorms require moisture and a trigger to force parcels to their condensation level."
```

## Explainer

From your study of adiabatic processes, you know that a parcel of air changing pressure without exchanging heat with its surroundings will change temperature — expanding air cools, compressing air warms. The **adiabatic lapse rate** quantifies exactly how fast this cooling or warming occurs as the parcel moves vertically through the atmosphere. Because pressure decreases with altitude (as you learned from the thermal structure of the atmosphere), a rising parcel always expands and cools. The question is: how quickly?

For unsaturated air, the answer comes directly from the first law of thermodynamics and the ideal gas law. When no condensation is occurring, the only energy exchange is between the parcel's internal energy and the work it does expanding against lower surrounding pressure. This gives the **dry adiabatic lapse rate (DALR)** of approximately 9.8°C per kilometer of ascent. This value is essentially constant because it depends only on gravity and the specific heat of dry air, neither of which varies meaningfully across typical atmospheric conditions. A parcel of dry air rising from the surface will cool at this fixed rate regardless of how warm or cold it starts.

The situation changes dramatically when the parcel reaches saturation. As a saturated parcel continues to rise and cool, water vapor condenses into droplets, and condensation releases **latent heat** back into the parcel. This latent heat partially compensates for the adiabatic cooling, so the parcel cools more slowly than it would if it were dry. The resulting **saturated (or moist) adiabatic lapse rate (SALR)** is typically around 5–6°C/km, but unlike the DALR, it is not constant. Warmer air holds exponentially more moisture (from the Clausius-Clapeyron relation), so a warm saturated parcel releases far more latent heat per kilometer of ascent than a cold one. Near the tropical surface, the SALR can be as low as 3–4°C/km; in the cold upper troposphere, it approaches the DALR because there is almost no moisture left to condense.

The practical importance of these two rates is enormous. The actual temperature profile of the atmosphere — the **environmental lapse rate** — is measured by weather balloons, not predicted by adiabatic theory. But by comparing the environmental lapse rate to the DALR and SALR, meteorologists determine atmospheric stability. If the environment cools faster than the DALR, any displaced parcel (whether saturated or not) will be warmer than its surroundings and will accelerate upward — the atmosphere is absolutely unstable and convection is vigorous. If the environment cools more slowly than the SALR, displaced parcels always end up cooler than their surroundings and sink back — the atmosphere is absolutely stable. Between these extremes lies conditional instability, where dry parcels are stable but saturated parcels are unstable. This conditional regime is where most thunderstorm development occurs: the atmosphere resists dry lifting but, once a parcel is forced to its condensation level and becomes saturated, latent heat release can trigger explosive convective growth.
