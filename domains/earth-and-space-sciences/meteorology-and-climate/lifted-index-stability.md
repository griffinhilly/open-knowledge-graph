---
id: lifted-index-stability
title: Lifted Index and Atmospheric Stability Classification
domain: earth-and-space-sciences
course: meteorology-and-climate
prerequisites:
- id: atmospheric-inversion-temperature
  type: hard
- id: moist-adiabatic-lapse-rate
  type: hard
builds-toward:
- severe-weather-systems
- thunderstorms-and-lightning
tags:
- stability
- index
- forecast
- instability
stage: advanced
status: draft
---

# Lifted Index and Atmospheric Stability Classification

## Core Idea
The Lifted Index (LI) is the temperature difference between a lifted parcel at 500 hPa and the environment at that level; negative values indicate instability. LI values classify stability: stable (LI > 0), weakly unstable (−2 to 0), unstable (−6 to −2), and very unstable (< −6). Unlike CAPE, LI is a single-point diagnostic that gives a quick snapshot of stability at a key height.

## Explainer

You already understand that atmospheric stability depends on how a rising parcel's temperature compares to its environment, and that inversions create stable layers that resist vertical motion. The **Lifted Index (LI)** takes this concept and distills it into a single number by asking one specific question: if I take air from near the surface and lift it to 500 hPa (roughly 5.5 km altitude), how does its temperature compare to the air already there?

The calculation works like this. Start with a parcel of air representing conditions near the surface (typically averaged over the lowest 100 hPa of the atmosphere to avoid being misled by a thin surface layer). Lift it upward — first along the dry adiabatic lapse rate until it reaches saturation, then along the **moist adiabatic lapse rate** as condensation releases latent heat and slows the cooling. When the parcel arrives at 500 hPa, compare its temperature to the actual environmental temperature at that level. The Lifted Index is the environment's temperature minus the parcel's temperature: LI = T_environment − T_parcel at 500 hPa.

A **positive LI** means the parcel arrived at 500 hPa colder (denser) than its surroundings — it would sink back down, indicating a stable atmosphere. A **negative LI** means the parcel is warmer than its environment at that level — it is buoyant and would continue to accelerate upward, signaling instability. The more negative the value, the greater the instability. Forecasters use rough thresholds: values from 0 to −2 suggest weak instability with possible showers, −2 to −6 indicates moderate to strong instability favorable for thunderstorms, and values below −6 signal extreme instability where severe thunderstorms become likely.

The LI's greatest strength is its simplicity — it reduces a complex atmospheric profile to one number that can be quickly mapped and compared across regions. But this simplicity is also its limitation. Because it only samples one level (500 hPa), it can miss important features: a shallow unstable layer below 500 hPa, or a strong capping inversion at 700 hPa that might prevent convection from ever reaching 500 hPa regardless of what the LI says. That is why forecasters use LI alongside more comprehensive measures like CAPE and CIN — the Lifted Index gives a fast first look at instability, while those integrated quantities capture the full vertical picture.
