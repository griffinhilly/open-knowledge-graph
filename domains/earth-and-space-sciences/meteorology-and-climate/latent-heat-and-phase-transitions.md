---
id: latent-heat-and-phase-transitions
title: Latent Heat and Water Phase Transitions
domain: earth-and-space-sciences
course: meteorology-and-climate
prerequisites:
- id: latent-heat-and-phase-changes
  type: hard
- id: kinetic-molecular-theory
  type: soft
- id: heat-and-internal-energy
  type: soft
- id: phase-changes-and-diagrams
  type: soft
- id: enthalpy-definition-and-significance
  type: soft
builds-toward:
- saturation-and-dew-point
- latent-heating-in-weather-systems
- surface-energy-budget-fluxes
tags:
- latent-heat
- phase-change
- energy
- vaporization
- condensation
stage: advanced
status: draft
---

# Latent Heat and Water Phase Transitions

## Core Idea
The energy required to change water between phases (vaporization ~2,500 kJ/kg, melting ~334 kJ/kg) is enormous compared to sensible heat. Evaporation from ocean and land surfaces cools the surface while transferring energy to water vapor; when vapor condenses, this latent heat is released to the atmosphere, fueling convection. This energy transfer is the primary driver of atmospheric circulation and the most important energy source for tropical cyclones.

## Questions

```yaml
- question: "A kilogram of water evaporates from the ocean surface. Compared to raising the same kilogram of liquid water by 1°C, approximately how much more energy does evaporation require?"
  type: multiple-choice
  options:
    - "About 6 times more (latent heat of vaporization ≈ 2,500 J/kg vs. 4,186 J/kg·°C × 1°C)"
    - "About the same — both processes require roughly 4 kJ/kg"
    - "About 600 times more (latent heat of vaporization ≈ 2,500 kJ/kg vs. ~4.2 kJ/kg per °C)"
    - "About 60 times more — latent heat is significant but not dramatically larger"
  answer: 2
  explanation: "The specific heat of water is ~4.2 kJ per kg per °C, so raising 1 kg by 1°C requires ~4.2 kJ. Evaporating 1 kg requires ~2,500 kJ — roughly 600 times more. This enormous ratio is why evaporation is such a powerful energy transport mechanism: a thin layer of ocean water evaporating can transfer as much energy as heating a far larger mass of air by many degrees."

- question: "When water vapor condenses in a rising air parcel to form clouds, the latent heat released is lost from the atmospheric system and does not contribute to any further weather processes."
  type: true-false
  answer: false
  explanation: "Latent heat released during condensation directly warms the surrounding air parcel, making it more buoyant and causing it to rise further. This is why cumulonimbus clouds grow so tall — each layer of condensation releases heat that drives the next layer of ascent. The energy is not lost; it converts from latent (stored in water vapor) to sensible (measurable temperature increase), which then drives convection. This feedback loop is the engine of thunderstorms and tropical cyclones."

- question: "Why do tropical cyclones (hurricanes/typhoons) rapidly weaken when they move over land or cooler ocean water?"
  type: short-answer
  answer: "Tropical cyclones are sustained by latent heat released from the condensation of water vapor that evaporated from warm ocean surfaces. Warm water provides the continuous evaporation needed to keep supplying vapor. When the storm moves over land or cooler water, evaporation rates drop sharply, cutting off the latent heat supply that drives the convective updrafts at the cyclone's core. Without this energy input, the circulation weakens and the storm dissipates."
  explanation: "This question connects the abstract concept of latent heat to a concrete, large-scale phenomenon. The warm ocean is not just a moisture source — it is an energy source, and that energy is delivered to the atmosphere specifically as latent heat embedded in water vapor. The phase transition from vapor to liquid inside the cyclone's deep convective towers releases this energy at altitude, where it sustains the storm's outflow and maintains the pressure gradient that drives inflow at the surface."
```

## Explainer

From your prerequisites, you know that changing water's phase requires energy — the **latent heat** — even though the temperature of the water itself doesn't change during the transition. This hidden energy is what makes water's phase transitions so meteorologically important. The numbers are striking: evaporating one kilogram of water requires about 2,500 kJ, while melting the same kilogram of ice takes only ~334 kJ. By comparison, raising 1 kg of water by 1°C requires just ~4.2 kJ. Evaporation is therefore energetically equivalent to cooling 1 kg of water by nearly 600°C — a massive energy transfer accomplished invisibly, without any temperature change in the water vapor itself.

When water evaporates from the ocean or land surface, two things happen simultaneously. The surface cools (evaporative cooling) because the molecules with the most kinetic energy escape as vapor, leaving behind cooler liquid. And the departing vapor carries enormous latent energy with it into the lower atmosphere. This is not "heat" in the conventional sense — you cannot measure it with a thermometer in the vapor — but it is real stored energy that will be released when the vapor later condenses. This storage and transport is the mechanism by which the ocean surface exports energy to the atmosphere at scale.

The release happens in clouds. As air rises and cools to the dew point, water vapor condenses onto condensation nuclei. Each kilogram that condenses releases ~2,500 kJ of latent heat into the surrounding air parcel. This warming makes the parcel more buoyant, causing it to rise further, cool further, condense more vapor, and release more heat — a positive feedback loop. This is why deep convective clouds (cumulonimbus) grow so explosively and why **thunderstorm updrafts** can reach speeds of tens of meters per second. The storm is, in thermodynamic terms, a latent heat engine.

**Tropical cyclones** are the most dramatic illustration of this engine at work. They form and intensify over warm ocean water (surface temperature ≥ 26–27°C) because warm water drives rapid evaporation, loading the lower atmosphere with water vapor. As that vapor rises in the cyclone's eyewall and condenses, the released latent heat warms the upper atmosphere, reduces surface pressure, and accelerates the inflow of more moist air at the surface — a self-reinforcing cycle. When a hurricane crosses cool water or reaches land, the fuel supply (evaporation from warm ocean water) is cut off, and the storm weakens quickly. Understanding this makes clear that tropical cyclones are not just wind events — they are massive latent heat transport systems that redistribute energy from tropical oceans into the upper atmosphere.
