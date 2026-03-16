---
id: environmental-lapse-rate
title: Environmental Lapse Rate
domain: earth-and-space-sciences
course: meteorology-and-climate
prerequisites:
- id: atmospheric-pressure-and-altitude
  type: hard
- id: thermal-structure-of-atmosphere
  type: soft
builds-toward:
- atmospheric-inversion-temperature
- stable-neutral-unstable-classification
- convective-available-potential-energy
tags:
- temperature-profile
- measurement
- atmosphere
stage: abstract-reasoning
status: draft
---

# Environmental Lapse Rate

## Core Idea
The environmental lapse rate is the observed temperature decrease with altitude in a specific atmosphere at a given time, measured directly from radiosondes or remote sensing. Unlike the adiabatic lapse rate, it varies with location, season, and time of day. Comparing the environmental lapse rate to the adiabatic rates determines atmospheric stability and convective potential.

## Explainer

From your study of atmospheric pressure and altitude, you know that pressure decreases with height and that this relationship governs much of atmospheric behavior. You may also recall the adiabatic lapse rates — the predictable rates at which a rising air parcel cools as it expands (about 9.8°C/km for dry air, less for saturated air). Those rates describe what happens inside a moving parcel. The **environmental lapse rate (ELR)** is a completely different measurement: it describes the actual temperature profile of the surrounding atmosphere at a specific place and time, as recorded by a weather balloon (radiosonde) ascending through the air column.

Think of it this way: the adiabatic lapse rate is a theoretical prediction about a traveling parcel — "if this air rises, it will cool at this rate." The environmental lapse rate is a snapshot of reality — "right now, at this location, the temperature at 1 km is X, at 2 km is Y, at 3 km is Z." The ELR is not a fixed number. On a hot summer afternoon over a sun-baked desert, the surface heats intensely and the ELR near the ground might exceed 15°C/km. On a calm winter night with clear skies, the surface radiates heat to space, the ground cools faster than the air above it, and the ELR can actually become negative — temperature *increasing* with altitude — creating a **temperature inversion**.

The reason the ELR matters so much is that atmospheric stability is determined by comparing it to the adiabatic rates. Imagine a parcel of air nudged upward from the surface. As it rises, it cools at the dry adiabatic rate (9.8°C/km). Meanwhile, the surrounding environment has its own temperature profile — the ELR. If the environment cools faster with height than the parcel does (ELR > 9.8°C/km), the rising parcel will always be warmer and less dense than its surroundings, so it keeps rising on its own — the atmosphere is **absolutely unstable** and convection is vigorous. If the ELR is less than the moist adiabatic rate (roughly 5–6°C/km), a rising parcel will always be cooler and denser than the environment and will sink back — **absolutely stable**, suppressing vertical motion.

This comparison is the foundation of weather forecasting. Meteorologists launch radiosondes twice daily at hundreds of stations worldwide, plotting the ELR on thermodynamic diagrams alongside the adiabatic curves. Where the ELR crosses the parcel's cooling curve, you can read off the level of free convection, the equilibrium level, and the total convective available potential energy. A steep ELR on a humid afternoon signals thunderstorm potential; a shallow ELR with an inversion layer signals fog, smog trapping, or stable stratiform clouds. The environmental lapse rate is the atmosphere's actual state, and everything in stability analysis begins with measuring it.
