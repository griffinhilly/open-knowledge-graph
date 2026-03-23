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
stage: formal-systems
status: draft
---

# Mixing Ratio and Saturation Mixing Ratio

## Core Idea
Mixing ratio is the mass of water vapor per unit mass of dry air, independent of pressure (unlike relative humidity). Saturation mixing ratio is the maximum mixing ratio air can hold at a given temperature and pressure. Comparing actual to saturation mixing ratio gives relative humidity, essential for understanding convective instability and cloud formation.

## Questions

```yaml
- question: "An unsaturated air parcel with a mixing ratio of 12 g/kg rises from 900 hPa to 700 hPa without reaching saturation. Which statement correctly describes the parcel's moisture properties at 700 hPa?"
  type: multiple-choice
  options:
    - "The mixing ratio has decreased because the parcel expanded and the water vapor diluted"
    - "The mixing ratio is still 12 g/kg, but the relative humidity has increased because the saturation mixing ratio decreased as the parcel cooled"
    - "Both mixing ratio and relative humidity are unchanged because rising air conserves all moisture properties"
    - "The mixing ratio increased because colder air can hold more water vapor per unit mass"
  answer: 1
  explanation: "Mixing ratio is conservative for an unsaturated parcel: no water has been added or removed, so the mass of vapor per kilogram of dry air stays at 12 g/kg. But as the parcel rises and cools, the *saturation* mixing ratio decreases (cold air has lower saturation capacity per Clausius-Clapeyron). Since relative humidity = (actual mixing ratio) / (saturation mixing ratio), RH rises even though no moisture was added. This is the key contrast: mixing ratio tracks actual moisture, relative humidity tracks proximity to saturation — they can change independently."

- question: "A meteorologist needs to track whether two air parcels that have been lifted to different altitudes originally contained the same amount of water vapor. Which moisture variable should she compare?"
  type: multiple-choice
  options:
    - "Relative humidity, because it is expressed as a percentage and is comparable across altitudes"
    - "Dew point temperature, because it is independent of the parcel's current temperature"
    - "Mixing ratio, because it is conserved during dry adiabatic lifting and directly measures vapor mass per unit dry air mass"
    - "Specific humidity, which is always constant regardless of pressure and temperature changes"
  answer: 2
  explanation: "Mixing ratio is the right choice because it is conserved during dry adiabatic (unsaturated) ascent — it measures the actual mass of water vapor per unit dry air mass, which doesn't change when pressure or temperature change without condensation. Relative humidity is not conserved: it increases as the parcel cools, even with no moisture change. Dew point is useful but changes with pressure as well. Specific humidity is also approximately conservative, but mixing ratio is the most direct measure of absolute moisture content."

- question: "When an unsaturated air parcel rises and cools, its relative humidity increases because moisture is being added to the parcel from the surrounding environment."
  type: true-false
  answer: false
  explanation: "No moisture is exchanged with the environment during dry adiabatic lifting. Relative humidity increases solely because the parcel cools — its saturation mixing ratio (the denominator of the RH fraction) decreases with temperature, making the existing moisture a larger fraction of what the air could hold. This distinction is critical: it means RH alone cannot tell you whether a parcel gained or lost moisture. The mixing ratio, not RH, tells you whether actual moisture content changed."

- question: "At the dew point temperature, an air parcel's actual mixing ratio equals its saturation mixing ratio, so relative humidity is 100%."
  type: true-false
  answer: true
  explanation: "The dew point is defined as the temperature to which air must be cooled (at constant pressure and moisture content) to reach saturation. At that temperature, the saturation mixing ratio has decreased to exactly equal the actual mixing ratio. Since RH = (actual mixing ratio)/(saturation mixing ratio) × 100%, RH = 100% at the dew point. This is the thermodynamic definition connecting dew point, mixing ratio, and saturation mixing ratio in a single consistent framework."

- question: "Explain why mixing ratio is more useful than relative humidity for tracking a parcel's moisture content as it rises through the atmosphere."
  type: short-answer
  answer: "Mixing ratio (mass of water vapor per kg of dry air) is conserved during unsaturated ascent — it doesn't change unless water actually condenses out or is added. Relative humidity, by contrast, rises as the parcel cools even with no change in actual water vapor, because the saturation capacity decreases with temperature. Using RH to track moisture as a parcel rises would give the false impression that moisture is increasing, when in reality only the temperature changed."
  explanation: "The practical implication is significant for sounding analysis: meteorologists plot mixing ratio on thermodynamic diagrams to identify where a parcel originated and how much moisture it carries, then compare to the saturation mixing ratio line at each level to find where clouds form (where the two values converge). Using RH instead would conflate the temperature effect with actual moisture changes, making the analysis ambiguous."
```

## Explainer

You already understand dew point and saturation — the idea that air at a given temperature can hold only so much water vapor before condensation begins. The **mixing ratio** makes this concept precise and quantitative by expressing moisture content as a mass ratio: grams of water vapor per kilogram of dry air. A typical midlatitude surface value might be 10 g/kg, meaning each kilogram of dry air carries 10 grams of water vapor mixed through it.

Why use mixing ratio instead of simpler measures like relative humidity? Because mixing ratio is a **conservative quantity** — it does not change when an unsaturated air parcel rises or sinks. As a parcel ascends and pressure drops, its volume changes and its temperature falls, but the ratio of water vapor mass to dry air mass stays the same (no water has been added or removed). Relative humidity, by contrast, increases as the parcel cools even though no moisture was added, because the denominator — the saturation capacity — is shrinking. This makes relative humidity unreliable for tracking a parcel's actual moisture content through the atmosphere. Mixing ratio stays constant until condensation begins, making it far more useful for thermodynamic calculations.

The **saturation mixing ratio** is the mixing ratio at which the air is fully saturated — the maximum water vapor the air can hold at its current temperature and pressure. It depends strongly on temperature (from the Clausius-Clapeyron relationship you already know) and weakly on pressure. At 30°C and sea-level pressure, the saturation mixing ratio is roughly 27 g/kg; at 0°C, it drops to about 3.8 g/kg. This dramatic temperature dependence is why warm tropical air can carry vastly more moisture than cold polar air, and why cooling air to its dew point inevitably leads to condensation.

The relationship between these two quantities connects directly to what you know about dew point and relative humidity. **Relative humidity** is simply the actual mixing ratio divided by the saturation mixing ratio, expressed as a percentage. When the mixing ratio equals the saturation mixing ratio, relative humidity is 100% and the air is at its dew point — condensation begins. On a thermodynamic diagram, forecasters plot both values for a sounding: the gap between the mixing ratio line and the saturation mixing ratio line tells you how far the air is from saturation at each level, which is critical for identifying where clouds will form, how much moisture is available for precipitation, and whether a lifted parcel will reach its level of free convection.
