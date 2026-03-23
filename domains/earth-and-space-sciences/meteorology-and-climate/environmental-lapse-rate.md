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
stage: formal-systems
status: validated
---

# Environmental Lapse Rate

## Core Idea
The environmental lapse rate is the observed temperature decrease with altitude in a specific atmosphere at a given time, measured directly from radiosondes or remote sensing. Unlike the adiabatic lapse rate, it varies with location, season, and time of day. Comparing the environmental lapse rate to the adiabatic rates determines atmospheric stability and convective potential.

## Questions

```yaml
- question: "On a summer afternoon, radiosondes record an environmental lapse rate of 12°C/km near the surface. A dry air parcel is nudged upward and cools at the dry adiabatic rate of 9.8°C/km. What happens to that parcel?"
  type: multiple-choice
  options:
    - "The parcel cools faster than the surrounding air, becomes denser than its surroundings, and sinks back to its original level"
    - "The parcel cools more slowly than the surrounding air, remains warmer and less dense than its surroundings, and continues rising spontaneously"
    - "The parcel and environment cool at exactly the same rate, producing neutral stability and no net vertical motion"
    - "The parcel's behavior depends entirely on its moisture content, not on the temperature difference"
  answer: 1
  explanation: "When the ELR (12°C/km) exceeds the dry adiabatic lapse rate (9.8°C/km), the environment loses temperature with altitude faster than the rising parcel does. At every level, the parcel is warmer — and therefore less dense — than the surrounding air. Buoyancy continues to accelerate the parcel upward. This is absolute instability. The atmosphere vigorously promotes vertical mixing and convection. Option A describes the opposite condition — absolute stability — and represents the most common confusion: reversing which is the parcel and which is the environment."

- question: "A temperature inversion is observed — temperature increases rather than decreases with altitude over a layer. What does this imply for atmospheric stability in that layer?"
  type: multiple-choice
  options:
    - "The atmosphere is absolutely unstable because warm air aloft will descend rapidly, replacing cooler air below"
    - "The atmosphere is conditionally unstable — stability depends on whether rising parcels become saturated"
    - "The atmosphere is absolutely stable — any parcel displaced upward immediately becomes cooler and denser than the surrounding air and sinks back"
    - "Stability cannot be assessed from temperature alone; humidity measurements are required"
  answer: 2
  explanation: "In a temperature inversion, temperature increases with altitude. Any parcel that rises cools at the adiabatic rate, while the environment is getting warmer. The parcel becomes rapidly cooler and denser than its surroundings and sinks back immediately — strong suppression of vertical motion. This is why inversions trap pollution (smog layers), suppress thunderstorm development, and mark the top of the stable boundary layer at night. The common error is thinking that warm air aloft means instability because heat rises — but it is the *relative* temperature of parcel and environment that determines buoyancy, not the absolute temperature aloft."

- question: "The environmental lapse rate is a fixed physical constant, approximately 6.5°C/km, characteristic of the standard atmosphere."
  type: true-false
  answer: false
  explanation: "The 6.5°C/km value is the average environmental lapse rate in the standard atmosphere — a useful reference, not a physical constant. The actual ELR varies enormously by location, time of day, season, and weather conditions. On a hot afternoon over a desert, the near-surface ELR can exceed 15°C/km. On a calm, clear night, radiative cooling can create a surface inversion where temperature increases with altitude (negative ELR). This variability is precisely why meteorologists launch radiosondes twice daily — the ELR must be measured, not assumed."

- question: "If the environmental lapse rate in a layer exceeds the dry adiabatic lapse rate, that layer of the atmosphere is absolutely unstable."
  type: true-false
  answer: true
  explanation: "Absolute instability occurs when the ELR exceeds the dry adiabatic lapse rate (≈9.8°C/km). In this condition, any parcel — dry or moist — that is displaced upward will be warmer than its environment at every level above its starting point and will continue rising without additional forcing. This is the most unstable condition possible and produces vigorous, deep convection. In practice, superadiabatic lapse rates are common in the lowest few meters above a strongly heated surface on sunny days."

- question: "What is the fundamental difference between the environmental lapse rate and the dry adiabatic lapse rate, and why does comparing them determine atmospheric stability?"
  type: short-answer
  answer: "The dry adiabatic lapse rate (9.8°C/km) is a property of a moving air parcel — it describes how a parcel cools as it rises and expands, without exchanging heat with its surroundings. It is a fixed thermodynamic quantity. The environmental lapse rate is a property of the surrounding atmosphere at a specific time and place — it describes how temperature actually changes with altitude in the ambient air, measured by a weather balloon. Atmospheric stability is determined by comparing these two rates: if a parcel rises and remains warmer than the environment (ELR > DALR), buoyancy keeps it rising — instability. If the parcel becomes cooler than the environment after rising (ELR < DALR or inversion), it sinks back — stability. The comparison is a competition between what happens inside the parcel versus what the environment looks like outside."
  explanation: "This distinction — parcel vs. environment — is the conceptual foundation of atmospheric stability analysis. Many students confuse the two lapse rates or treat them as alternative descriptions of the same phenomenon. They describe entirely different things: one is a law of thermodynamics applied to a parcel, the other is an observed measurement of the ambient atmosphere."
```

## Explainer

From your study of atmospheric pressure and altitude, you know that pressure decreases with height and that this relationship governs much of atmospheric behavior. You may also recall the adiabatic lapse rates — the predictable rates at which a rising air parcel cools as it expands (about 9.8°C/km for dry air, less for saturated air). Those rates describe what happens inside a moving parcel. The **environmental lapse rate (ELR)** is a completely different measurement: it describes the actual temperature profile of the surrounding atmosphere at a specific place and time, as recorded by a weather balloon (radiosonde) ascending through the air column.

Think of it this way: the adiabatic lapse rate is a theoretical prediction about a traveling parcel — "if this air rises, it will cool at this rate." The environmental lapse rate is a snapshot of reality — "right now, at this location, the temperature at 1 km is X, at 2 km is Y, at 3 km is Z." The ELR is not a fixed number. On a hot summer afternoon over a sun-baked desert, the surface heats intensely and the ELR near the ground might exceed 15°C/km. On a calm winter night with clear skies, the surface radiates heat to space, the ground cools faster than the air above it, and the ELR can actually become negative — temperature *increasing* with altitude — creating a **temperature inversion**.

The reason the ELR matters so much is that atmospheric stability is determined by comparing it to the adiabatic rates. Imagine a parcel of air nudged upward from the surface. As it rises, it cools at the dry adiabatic rate (9.8°C/km). Meanwhile, the surrounding environment has its own temperature profile — the ELR. If the environment cools faster with height than the parcel does (ELR > 9.8°C/km), the rising parcel will always be warmer and less dense than its surroundings, so it keeps rising on its own — the atmosphere is **absolutely unstable** and convection is vigorous. If the ELR is less than the moist adiabatic rate (roughly 5–6°C/km), a rising parcel will always be cooler and denser than the environment and will sink back — **absolutely stable**, suppressing vertical motion.

This comparison is the foundation of weather forecasting. Meteorologists launch radiosondes twice daily at hundreds of stations worldwide, plotting the ELR on thermodynamic diagrams alongside the adiabatic curves. Where the ELR crosses the parcel's cooling curve, you can read off the level of free convection, the equilibrium level, and the total convective available potential energy. A steep ELR on a humid afternoon signals thunderstorm potential; a shallow ELR with an inversion layer signals fog, smog trapping, or stable stratiform clouds. The environmental lapse rate is the atmosphere's actual state, and everything in stability analysis begins with measuring it.
