---
id: thermohaline-overturning-circulation
title: Thermohaline Overturning Circulation
domain: earth-and-space-sciences
course: oceanography
prerequisites:
- id: water-mass-formation-types
  type: hard
- id: thermohaline-circulation-physics
  type: hard
builds-toward:
- deep-ocean-abyssal-currents
- ocean-heat-transport-mechanism
- atlantic-meridional-overturning-circulation
tags:
- thermohaline
- overturning
- deep-circulation
- meridional
- climate-regulation
stage: formal-systems
status: validated
---

# Thermohaline Overturning Circulation

## Core Idea
Cold, dense water formed at high latitudes sinks and flows toward the equator while warm surface water flows poleward, creating a global overturning circulation that regulates ocean heat distribution and climate on timescales of centuries to millennia.

## Questions

```yaml
- question: "Climate models project that accelerating Greenland ice melt will add large volumes of freshwater to the North Atlantic surface. What is the most likely effect on the thermohaline overturning circulation, and why?"
  type: multiple-choice
  options:
    - "The circulation strengthens, because the additional freshwater lowers surface density and causes more vigorous upwelling that pulls deep water upward"
    - "The circulation weakens, because freshwater reduces surface salinity and density, inhibiting the sinking of North Atlantic Deep Water"
    - "The circulation is unaffected, because salinity differences only drive circulation in the tropics, not at high latitudes"
    - "The circulation reverses direction, because the freshwater input creates a density gradient that pushes deep water toward the surface"
  answer: 1
  explanation: "The thermohaline overturning depends on North Atlantic surface water being dense enough to sink to 2,000–4,000 m depth. This density requires both cold temperatures AND high salinity — salinity the water accumulated by evaporation in the subtropical Atlantic as it traveled northward via the Gulf Stream. Freshwater addition dilutes salinity, reducing density below the threshold for deep sinking. If NADW formation weakens or stops, the poleward transport of warm surface water that feeds the sinking also weakens, reducing heat delivery to northern Europe. This mechanism drove the rapid climate disruptions of the last glacial period and is an active concern today."

- question: "Deep water that sinks in the North Atlantic and around Antarctica must eventually return to the surface. What primarily drives this return flow?"
  type: multiple-choice
  options:
    - "Hydraulic pressure from continuous sinking pushes the deep water upward along ocean basin margins worldwide"
    - "Wind-driven upwelling around Antarctica (Ekman transport) and slow turbulent mixing throughout the ocean interior"
    - "Geothermal heating from the ocean floor uniformly warms the deep water until it becomes buoyant and rises"
    - "A spontaneous reversal of the thermohaline gradient in the tropics, where warm deep water rises to meet cold surface water"
  answer: 1
  explanation: "The return flow is not a simple pressure-driven reversal. Two mechanisms dominate: (1) strong westerly winds around Antarctica drive northward Ekman transport at the surface, pulling deep water upward from below — this is the most important return pathway; (2) turbulent mixing driven by tides and internal waves throughout the ocean interior slowly diffuses deep water upward over centuries. This complexity explains the ~1,000-year circuit time. The intuitive 'piston' model — that sinking water simply pushes other water up — is incorrect; ocean dynamics require specific dynamical drivers for upwelling, not just mass conservation."

- question: "The Atlantic thermohaline overturning transports enough heat poleward to make northwestern Europe significantly warmer than it would otherwise be at its latitude."
  type: true-false
  answer: true
  explanation: "The Atlantic overturning transports approximately 1.3 petawatts of heat northward — enormous by any standard. This heat flux maintains northwestern Europe (UK, Norway, Iceland) several degrees warmer than comparable latitudes on the Pacific coast of North America. Countries like Iceland and Norway, which sit at very high latitudes, have far milder climates than their position alone would predict. A weakening of the overturning is therefore a genuine climate risk for European populations — not just an abstract oceanographic concern. This heat transport is the primary reason concern about overturning slowdown focuses on European climate impacts."

- question: "The thermohaline overturning circulation is primarily driven by wind stress at the ocean surface, which pushes dense polar water toward the equator to create the deep ocean circulation."
  type: true-false
  answer: false
  explanation: "This confuses two distinct ocean circulation systems. Wind-driven circulation creates surface gyres — including the wind-driven component of the Gulf Stream. Thermohaline (overturning) circulation is driven by density gradients: cold, salty water at high latitudes loses buoyancy and sinks to great depths under gravity, pulling warm surface water poleward to replace it. Wind does participate in the return flow (Ekman upwelling around Antarctica), but sinking itself is driven by buoyancy loss, not wind push. The term 'thermohaline' names the cause directly: temperature (thermo) and salinity (haline) together control the density that drives the overturning."

- question: "Explain why a sustained influx of freshwater into the North Atlantic could significantly weaken or disrupt the thermohaline overturning circulation."
  type: short-answer
  answer: "The thermohaline overturning depends on surface water in the North Atlantic becoming dense enough to sink to depths of 2,000–4,000 m, forming North Atlantic Deep Water (NADW). This density requires both cold temperatures (from polar air) and elevated salinity — salinity acquired through evaporation as warm, salty subtropical water travels northward via the Gulf Stream system. Freshwater influx dilutes this salinity, reducing density below the sinking threshold. If surface water can no longer sink, NADW formation weakens or stops. With less deep water sinking, the surface flow that compensates — drawing warm water northward — also weakens, reducing heat delivery to northwestern Europe. Paleoclimate records confirm this mechanism: massive glacial meltwater pulses caused rapid North Atlantic cooling events (Younger Dryas, Heinrich events) by exactly this pathway."
  explanation: "The feedback is self-reinforcing: less sinking → less warm surface water transported northward → cooler North Atlantic → more sea ice → more freshwater from sea ice melt → further salinity reduction. This positive feedback is why abrupt climate transitions associated with overturning disruptions appear in ice core records as rapid shifts — not gradual changes — over years to decades."
```

## Explainer

From your study of water mass formation and thermohaline circulation physics, you understand that ocean density is controlled by both temperature and salinity, and that distinct water masses form at the surface where these properties are set by atmospheric forcing. The **thermohaline overturning circulation** is what happens when those dense water masses sink and spread through the deep ocean, pulling surface water poleward to replace them and creating a planet-spanning conveyor that redistributes heat, carbon, and nutrients.

The process begins in a few key regions where surface water becomes dense enough to sink to great depths. In the North Atlantic, warm, salty water carried northward by the Gulf Stream and North Atlantic Current cools dramatically upon reaching the Norwegian and Labrador Seas. This cooling, combined with the already elevated salinity (which was acquired in the subtropics through evaporation), produces **North Atlantic Deep Water (NADW)** — a cold, dense water mass that sinks to depths of 2,000–4,000 meters and flows southward through the Atlantic basin. Around Antarctica, an even denser water mass forms: **Antarctic Bottom Water (AABW)** is created when brine rejection during sea ice formation produces extremely cold, salty water that sinks to the very bottom of the ocean and spreads northward, filling the deepest layers of all three major ocean basins.

The sinking of these dense waters at high latitudes must be balanced by the return of water to the surface elsewhere. This return flow is not a simple reversal — it involves a combination of wind-driven upwelling (particularly around Antarctica, where strong westerly winds drive surface water northward via Ekman transport, pulling deep water up from below) and slow, diffuse upwelling driven by turbulent mixing in the ocean interior. The surface limb of the circulation carries warm water poleward, completing the loop. The entire circuit — surface to depth at high latitudes, slow spreading through the deep basins, gradual return to the surface, and poleward transport back to the sinking regions — takes roughly 1,000 years to complete.

The climate consequences of this circulation are profound. The overturning transports approximately 1.3 petawatts of heat northward in the Atlantic, warming northwestern Europe by several degrees relative to comparable latitudes elsewhere. It also ventilates the deep ocean, carrying dissolved oxygen to the abyss and sequestering atmospheric CO₂ in the deep water for centuries. Paleoclimate records show that disruptions to the overturning — caused by massive freshwater inputs from melting ice sheets that reduce surface salinity and prevent sinking — have triggered abrupt climate shifts, including the rapid cooling events of the last glacial period. Today, there is active concern that accelerating Greenland ice melt could weaken the Atlantic overturning, with consequences for European climate, sea level along the North American east coast, and the ocean's capacity to absorb anthropogenic carbon.
