---
id: ekman-spiral-wind-driven-transport
title: Ekman Spiral and Wind-Driven Ocean Transport
domain: earth-and-space-sciences
course: oceanography
prerequisites:
- id: ekman-boundary-layer-transport
  type: hard
- id: coastal-upwelling-ekman-dynamics
  type: hard
- id: geostrophic-balance-ocean
  type: soft
- id: coriolis-effect
  type: soft
- id: vector-fields
  type: soft
- id: coriolis-effect-ocean-dynamics
  type: hard
- id: viscous-flow
  type: hard
builds-toward:
- continental-shelf-circulation
tags:
- ekman
- wind-stress
- boundary-layer
- spiral-rotation
- transport
stage: advanced
status: draft
---

# Ekman Spiral and Wind-Driven Ocean Transport

## Core Idea
Wind stress on the ocean surface creates a spiral pattern of currents that change direction and magnitude with depth due to friction and Coriolis deflection. Net transport (Ekman transport) occurs 90° to the wind direction, driving coastal upwelling and downwelling that redistributes heat, nutrients, and water masses.

## How It's Best Learned
Sketch Ekman spirals for different latitudes and wind directions; calculate net transport. Use current measurements from moorings or gliders to observe velocity rotation with depth. Analyze how latitude, wind strength, and stratification affect spiral geometry.

## Common Misconceptions
The clean spiral is rarely observed in field data due to stratification, variable bathymetry, and nonlinear effects. Ekman transport is not the average of layer velocities but the depth-integrated net flux. Real upwelling is not purely due to Ekman transport; pressure-driven flows also contribute.

## Explainer

You already know that wind stress on the ocean surface sets water in motion, and that the Coriolis effect deflects moving fluids to the right in the Northern Hemisphere (left in the Southern). The **Ekman spiral** describes what happens when you combine these two forces with the frictional coupling between water layers. The surface layer, directly dragged by the wind, deflects about 45° from the wind direction. Each successive layer below is dragged not by the wind but by the layer above it, receiving a weaker push and deflecting further. The result is a spiral of velocity vectors that rotate with depth while shrinking in magnitude, much like a stack of cards where each card is slightly twisted and smaller than the one above.

The depth over which this spiral operates is the **Ekman layer**, typically 50–200 meters depending on latitude and wind strength. What matters most for large-scale oceanography is not any individual layer's motion but the depth-integrated sum — the **net Ekman transport**. This net transport is directed exactly 90° to the right of the wind in the Northern Hemisphere (90° left in the Southern). This perpendicular relationship is not intuitive, but it follows mathematically from integrating the Coriolis-deflected velocity profile over the full Ekman depth. The transport depends only on wind stress and latitude (through the Coriolis parameter), not on the details of turbulent viscosity — a remarkably clean result.

Ekman transport drives some of the ocean's most consequential processes. When wind blows parallel to a coastline with the shore on its left (Northern Hemisphere), net transport pushes surface water offshore. Cold, nutrient-rich deep water rises to replace it — this is **coastal upwelling**, which you studied as a prerequisite. Conversely, when transport pushes water toward shore, it piles up and sinks, producing **downwelling**. At the basin scale, Ekman transport converges water in the center of subtropical gyres (pushing the thermocline down) and diverges water along the equator (pulling the thermocline up), linking wind patterns directly to the ocean's three-dimensional density structure.

In practice, the textbook spiral — a smooth logarithmic rotation of velocity with depth — is rarely observed cleanly. Real oceans have stratification that concentrates the shear near the surface, variable winds that prevent steady-state conditions, and turbulence that departs from the constant-viscosity assumption of Ekman's original model. Modern observations from current-profiling instruments often show a "compressed" spiral or an Ekman-like transport without a well-resolved spiral structure. Despite these complications, the net transport prediction remains robust and is one of the most practically useful results in physical oceanography.
