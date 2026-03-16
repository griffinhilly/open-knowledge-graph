---
id: wind-driven-ocean-circulation
title: Wind-Driven Ocean Circulation and Surface Currents
domain: earth-and-space-sciences
course: oceanography
prerequisites:
- id: global-atmospheric-circulation
  type: hard
- id: coriolis-effect
  type: hard
- id: seawater-properties
  type: soft
- id: newtons-second-law
  type: soft
builds-toward:
- ocean-gyres-and-boundary-currents
- el-nino-southern-oscillation
- ocean-upwelling
tags:
- surface currents
- Ekman transport
- wind stress
- trade winds
- westerlies
stage: abstract-reasoning
status: validated
---

# Wind-Driven Ocean Circulation and Surface Currents

## Core Idea
Persistent wind patterns impart stress on the ocean surface, driving large-scale horizontal circulation in the upper few hundred meters. The Coriolis effect deflects wind-driven water to the right in the Northern Hemisphere and left in the Southern Hemisphere (Ekman transport), causing net water movement at 90° to the wind. Convergence and divergence of Ekman transport forces vertical motion and sets up the pressure gradients that drive large-scale geostrophic currents. Trade winds and westerlies are the primary drivers of the major surface current systems.

## How It's Best Learned
Draw arrows showing global wind belts, then trace Ekman transport directions, then identify resulting zones of convergence (downwelling) and divergence (upwelling). Map this onto observed surface current patterns.

## Common Misconceptions
- Surface currents do not flow in the same direction as the wind — Ekman transport is roughly perpendicular to the wind.
- Wind-driven currents are mostly confined to the upper few hundred meters; deep circulation is driven by density, not wind.

## Questions

```yaml
- question: "In the Northern Hemisphere, the trade winds blow from the northeast toward the southwest. In which direction does Ekman transport move the surface water?"
  type: multiple-choice
  options:
    - "Northeast to southwest — the same direction as the wind."
    - "Roughly 90° to the right of the wind, toward the northwest."
    - "Roughly 90° to the right of the wind, toward the southeast."
    - "Directly downward into the deep ocean."
  answer: 2
  explanation: "The Coriolis effect deflects moving water to the right in the Northern Hemisphere. Trade winds blow toward the southwest, so the net Ekman transport is 90° to the right of that direction — roughly toward the northwest. A common error is assuming water moves in the same direction as the wind; it does not."

- question: "Wind-driven surface currents can extend to several kilometers depth, and are the primary driver of thermohaline circulation in the deep ocean."
  type: true-false
  answer: false
  explanation: "Wind-driven currents are largely confined to the upper few hundred meters (the Ekman layer). Deep thermohaline circulation is driven by density differences — cold, salty water sinking at high latitudes — not by direct wind stress. The two circulation systems are connected but distinct in their driving mechanisms."

- question: "What causes the subtropical convergence zones in the ocean, and what happens to surface water that accumulates there?"
  type: short-answer
  answer: "Trade winds drive Ekman transport poleward (to the right of easterly winds in the Northern Hemisphere), while westerlies drive Ekman transport equatorward (again to the right of westerly winds). These two opposing flows converge in the subtropics, piling water up in a mound. The elevated sea surface then drives geostrophic currents flowing around the subtropical gyre, and the excess water slowly sinks (downwells) into the ocean interior."
  explanation: "Convergence of Ekman transport creates a downwelling zone. The raised sea surface sets up a horizontal pressure gradient that — balanced by the Coriolis force — produces geostrophic flow. This is the mechanism behind the large subtropical gyres like the North Atlantic Gyre."
```

## Explainer

You already know that the atmosphere has persistent wind belts — trade winds blowing toward the equator, westerlies blowing poleward — driven by differential solar heating and the Coriolis effect. These winds do not just blow over the ocean; they drag it. The friction between moving air and the sea surface imparts a **wind stress** that sets the upper ocean in motion. This wind-driven circulation is what produces the great surface current systems visible on any ocean map.

The key to understanding those currents is **Ekman transport**. As wind pushes water, the Coriolis effect deflects it: to the right in the Northern Hemisphere, to the left in the Southern. The net movement of the Ekman layer (roughly the top 100 m) is therefore roughly 90° to the wind direction, not parallel to it. This is a common source of confusion — surface water does not simply flow downwind. In the Northern Hemisphere, a northward wind will drive water eastward; a westward wind will drive water southward.

Where Ekman transport from opposing wind belts converges, water piles up. In the subtropical North Atlantic and North Pacific, trade-wind-driven transport from the south and westerly-driven transport from the north converge in the middle, building a subtle mound of water. The elevated sea surface creates a pressure gradient. Combined with the Coriolis force, this drives **geostrophic flow** — water circling around the high-pressure mound in a clockwise direction (in the Northern Hemisphere). The result is the subtropical gyre, a slowly rotating system of surface currents like the Gulf Stream on its western boundary and the broad, sluggish drift on its eastern side.

Where Ekman transport diverges — such as along the equator or at the eastern edges of gyres — surface water is swept away and deeper, colder, nutrient-rich water rises to replace it. This **upwelling** is why regions like the coasts of Peru and California are some of the most biologically productive ocean zones on Earth, despite being in subtropical latitudes. Recognizing convergence and divergence as consequences of Ekman transport is the key to reading surface current maps with understanding rather than mere memorization.
