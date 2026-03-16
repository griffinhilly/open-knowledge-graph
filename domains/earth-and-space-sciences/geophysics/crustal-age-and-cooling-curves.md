---
id: crustal-age-and-cooling-curves
title: Oceanic Crustal Cooling and Age Relationships
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: mid-ocean-ridge-dynamics-and-geophysics
  type: hard
- id: heat-flow-conduction-steady-state
  type: hard
builds-toward:
- lithosphere-thickness-and-age
tags:
- geothermics
- plate-tectonics
- cooling
stage: advanced
status: draft
---

# Oceanic Crustal Cooling and Age Relationships

## Core Idea
Oceanic crust cools as it moves away from mid-ocean ridges following a half-space cooling model. Crustal thickness, heat flow, bathymetry, and seismic velocity all change predictably with age. The relationship between bathymetry and age (approximately 2600 m for young crust, increasing to 6000 m by 80 Ma) is a fundamental constraint on plate tectonics and mantle potential temperature.

## Explainer

From your study of mid-ocean ridges, you know that new oceanic crust forms at spreading centers where hot mantle material rises, partially melts, and solidifies. From heat flow and conduction, you know that thermal energy moves through rock by conduction at a rate governed by thermal diffusivity. These two ideas combine into one of the most elegant quantitative relationships in geophysics: the **half-space cooling model**, which predicts how oceanic lithosphere evolves as it moves away from the ridge.

The model treats the newly formed crust as a semi-infinite half-space initially at mantle temperature (~1300°C at the surface), cooling from above into a zero-temperature ocean. The mathematics is identical to the one-dimensional heat conduction problem you solved in your thermal physics prerequisite. The key result is that the thermal boundary layer — the cooled lithosphere — thickens as the **square root of age**: thickness ∝ √(κt), where κ is thermal diffusivity and t is the time since the crust formed at the ridge. This square-root dependence is the signature of diffusive cooling and appears in every observable property of the aging ocean floor.

As the lithosphere cools, it contracts and becomes denser, causing the seafloor to **subside**. The predicted depth increases as the square root of crustal age: young crust near the ridge sits at roughly 2,600 m depth, while 80-million-year-old crust has sunk to about 5,500–6,000 m. This √t relationship between bathymetry and age was one of the first great confirmations of plate tectonics — it matched observed ocean depth profiles across every major basin. Heat flow measurements tell the same story from the thermal side: surface heat flow decreases as 1/√t, highest at the ridge and declining steadily with age.

The half-space model works remarkably well for crust younger than about 70–80 Ma, but older ocean floor is systematically shallower and warmer than predicted. This **flattening** of the cooling curve led to the development of the **plate model**, which assumes the lithosphere approaches a finite equilibrium thickness (~125 km) rather than cooling indefinitely. The plate model adds a lower thermal boundary condition — heat supply from the underlying asthenosphere — that prevents the lithosphere from growing thicker than observed. Whether this heat comes from small-scale convection beneath old plates or from radiogenic heating remains debated, but the empirical flattening is robust. Together, the half-space and plate models provide the quantitative framework connecting crustal age to nearly every measurable property of the ocean floor: depth, heat flow, seismic velocity, and elastic thickness.
