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
stage: formal-systems
status: draft
---

# Saturation Vapor Pressure and Clausius-Clapeyron Relation

## Core Idea
Saturation vapor pressure is the maximum pressure exerted by water vapor in equilibrium with a liquid or ice surface, increasing exponentially with temperature following the Clausius-Clapeyron relation (~7% per K). This nonlinear relationship explains why warm air can hold much more moisture than cold air and why tropics are more humid. The relation also drives the strength of latent heat feedbacks in climate.

## How It's Best Learned
Plot saturation vapor pressure against temperature; observe the exponential increase. Apply the Magnus formula for quick estimates.

## Common Misconceptions
- Confusing saturation vapor pressure with actual vapor pressure; they are equal only when air is saturated. - Thinking the relationship is linear instead of exponential.

## Questions

```yaml
- question: "If the temperature of a parcel of air increases from 20°C to 30°C, by approximately how much does its saturation vapor pressure change?"
  type: multiple-choice
  options:
    - "It increases by about 10%, because temperature increased by about 10°C out of a ~100°C range"
    - "It approximately doubles, increasing by about 70–80%"
    - "It increases by about 7%, reflecting the Clausius-Clapeyron rate"
    - "It remains the same — saturation vapor pressure depends on humidity, not temperature alone"
  answer: 1
  explanation: "The Clausius-Clapeyron relation predicts approximately 7% increase per 1°C, so a 10°C increase yields roughly 1.07^10 ≈ 1.97 — nearly double. This exponential scaling means equal temperature increments produce larger and larger absolute increases in moisture-holding capacity. The 7%/°C rate applies per degree, not per 10°C — the common error is treating it linearly (option C gives 7% total, as if the rate applies to the whole interval rather than compounding). At 20°C, saturation vapor pressure is about 23 hPa; at 30°C it is about 42 hPa — close to double."

- question: "Global mean temperature increases by 2°C due to climate change. What does Clausius-Clapeyron predict for the change in the atmosphere's water-vapor holding capacity, and what feedback does this drive?"
  type: multiple-choice
  options:
    - "About 2% increase in water vapor; a small cooling feedback as water reflects more sunlight"
    - "About 14% increase in water vapor; a positive feedback amplifying the initial warming because water vapor is itself a greenhouse gas"
    - "About 14% increase in water vapor; a negative feedback because additional evaporation cools the surface"
    - "No change — the actual amount of water vapor is set by ocean evaporation rates, not temperature"
  answer: 1
  explanation: "At ~7%/°C, a 2°C warming increases saturation vapor pressure by about 1.07² ≈ 15%. As the ocean warms, evaporation increases until the atmosphere reaches this new higher saturation ceiling, so actual water vapor content increases at approximately the Clausius-Clapeyron rate. Since water vapor is the most important atmospheric greenhouse gas, this additional moisture amplifies the initial warming — a positive feedback. Observations confirm that atmospheric water vapor has tracked the ~7%/K prediction as global temperatures have risen, making this one of the most robust and observed climate feedbacks."

- question: "The intensity of extreme precipitation events is expected to increase under climate warming at approximately the same rate as saturation vapor pressure increases — roughly 7% per degree of warming."
  type: true-false
  answer: true
  explanation: "Because a warmer atmosphere can hold more moisture (following Clausius-Clapeyron), more water vapor is available to be converted to precipitation in storm systems. The theoretical scaling for extreme precipitation is indeed ~7%/°C, and observations of extreme rainfall events broadly confirm this relationship. This is one of the most directly measurable climate change signals in precipitation data and explains why the heaviest rainfall events are intensifying faster than average precipitation as the climate warms."

- question: "When a meteorologist says the air is 'saturated,' this means the actual vapor pressure equals the saturation vapor pressure — and condensation will occur if any more water vapor is added."
  type: true-false
  answer: true
  explanation: "Saturation vapor pressure is the maximum pressure water vapor can exert at a given temperature before condensation begins. When actual vapor pressure reaches this value, the air is saturated and any additional water vapor input (or any cooling that lowers the saturation threshold) triggers condensation. This is the mechanism behind cloud formation, fog, and dew: air cools until saturation vapor pressure drops to meet actual vapor pressure, at which point water vapor condenses into liquid droplets. The saturation vapor pressure sets the ceiling; actual vapor pressure reflects how much water vapor is present."

- question: "Why does the exponential (rather than linear) relationship between saturation vapor pressure and temperature matter for understanding climate change impacts on precipitation and humidity?"
  type: short-answer
  answer: "If the relationship were linear, equal temperature increments would always add the same absolute amount to moisture-holding capacity. The exponential relationship means that each additional degree of warming adds more absolute moisture capacity than the previous degree — the increments compound. This matters enormously: the difference between 0°C and 35°C represents roughly a tenfold increase in saturation vapor pressure, not a linear proportional one. Under climate warming, this means the most moisture-rich environments (warm tropics, warm summers) gain disproportionately more moisture-holding capacity than cold ones, intensifying contrasts between wet and dry regions and making extreme precipitation events increasingly severe in already-warm places."
  explanation: "The exponential scaling creates nonlinear, compounding effects that linear thinking would dramatically underestimate. A simple 'more warmth, a bit more moisture' mental model misses the accelerating nature of the relationship. This is why climate scientists emphasize that warming doesn't just shift weather patterns but fundamentally changes the moisture budget of the atmosphere in ways that compound with initial warming through the water vapor feedback."
```

## Explainer

From your study of phase diagrams and the Clausius-Clapeyron equation, you know that the boundary between liquid and vapor phases on a pressure-temperature diagram is not a straight line but a curve that steepens with increasing temperature. The **saturation vapor pressure** is simply the vapor pressure along this curve — it is the pressure at which water vapor is in equilibrium with a liquid (or ice) surface at a given temperature. If the actual vapor pressure exceeds this value, condensation occurs; if it falls below, evaporation dominates.

The Clausius-Clapeyron relation gives the mathematical form of this curve: de_s/dT = (L · e_s) / (R_v · T²), where e_s is saturation vapor pressure, L is the latent heat of vaporization, R_v is the gas constant for water vapor, and T is temperature in Kelvin. Because e_s appears on both sides of the equation, the solution is exponential — saturation vapor pressure increases roughly **7% for every 1°C increase in temperature**. This means that 30°C air can hold about four times as much water vapor as 10°C air. The nonlinearity is dramatic: going from 0°C to 35°C, saturation vapor pressure increases from about 6 hPa to about 56 hPa — nearly a tenfold increase.

This exponential relationship has cascading consequences throughout meteorology and climate science. It explains why tropical air masses carry enormously more moisture than polar ones, why the most intense precipitation events occur in the warmest environments, and why coastal fog forms so readily when warm moist air flows over cold ocean water. For practical calculations, meteorologists often use the **Magnus formula** — an empirical approximation that gives saturation vapor pressure as a function of temperature without solving the differential equation directly. The Magnus formula (e_s ≈ 6.112 · exp(17.67T / (T + 243.5)), with T in °C and e_s in hPa) is accurate to within about 0.1% over the range of temperatures encountered in weather.

The Clausius-Clapeyron relation also underpins one of the most robust predictions in climate science: the **water vapor feedback**. As the planet warms, saturation vapor pressure rises, allowing the atmosphere to hold more water vapor. Since water vapor is itself a greenhouse gas, this additional moisture amplifies the original warming — a positive feedback loop. Observations confirm that atmospheric water vapor has increased at approximately the 7%/K rate predicted by Clausius-Clapeyron as global temperatures have risen. This same scaling governs extreme precipitation: the intensity of the heaviest rainfall events increases at roughly 7%/K because a warmer atmosphere can deliver more moisture to a storm system before the air is wrung dry.
