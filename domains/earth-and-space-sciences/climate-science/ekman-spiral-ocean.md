---
id: ekman-spiral-ocean
title: The Ekman Spiral and Wind-Driven Ocean Boundary Layers
domain: earth-and-space-sciences
course: climate-science
prerequisites:
- id: coriolis-effect
  type: hard
- id: ocean-circulation-and-climate
  type: soft
builds-toward:
- thermohaline-circulation-physics
- ocean-heat-transport-mechanism
tags:
- boundary-layer
- ocean
- friction
- wind-driven
- spiral
stage: advanced
status: draft
---

# The Ekman Spiral and Wind-Driven Ocean Boundary Layers

## Core Idea
The Ekman spiral describes how ocean currents change direction and magnitude with depth in the surface boundary layer due to the balance between wind stress, Coriolis force, and friction. The net transport (Ekman transport) is perpendicular to the wind direction (90° to the right in the Northern Hemisphere), which drives upwelling and coastal jets. The Ekman spiral is essential for understanding wind-driven ocean currents, coastal upwelling, and the mechanism of subtropical gyre circulation.

## How It's Best Learned
Solve the steady-state Ekman equations for a simple linear drag law and plot velocity vectors as a function of depth. Vary drag coefficients and observe changes in spiral shape and magnitude.

## Common Misconceptions
The surface current is not in the wind direction; the 45° angle between surface current and wind direction is a characteristic feature. Also, the Ekman depth (where velocity becomes negligible) is shallow (~10–100 m); the interior ocean responds differently.

## Explainer

You already know that the **Coriolis effect** deflects moving objects to the right in the Northern Hemisphere and to the left in the Southern Hemisphere — a consequence of Earth's rotation rather than any real force. The Ekman spiral describes what happens when wind blows steadily over the ocean surface and the Coriolis effect interacts with friction to create a distinctive pattern of currents that change direction with depth.

Start at the surface. Wind pushes the water, but the Coriolis effect immediately begins deflecting the flow — to the right (Northern Hemisphere). The surface current therefore does not flow in the wind direction; it flows at roughly **45° to the right** of the wind. Now consider the next layer down. The surface layer drags this deeper water through friction, acting like a weaker "wind" on the layer below. The Coriolis effect deflects this layer further to the right. Each successive layer is dragged by the one above it, deflected further, and moves more slowly because frictional coupling weakens with depth. The result is a spiraling pattern of velocity vectors that rotate clockwise (Northern Hemisphere) and diminish in magnitude with increasing depth — the **Ekman spiral**. At the **Ekman depth** (typically 10–100 m, depending on wind strength and latitude), the current has decayed to about 4% of the surface value, and below this the wind's influence is negligible.

The most important result is not the spiral itself but the **net transport**. When you add up (integrate) all the velocity vectors through the entire Ekman layer, the total water transport — called **Ekman transport** — points exactly 90° to the right of the wind direction in the Northern Hemisphere. This perpendicular transport has profound consequences. When wind blows parallel to a coastline with the shore on the left (in the Northern Hemisphere), Ekman transport pushes surface water offshore. Cold, nutrient-rich deep water rises to replace it — this is **coastal upwelling**, which drives some of the most productive fisheries on Earth (the California Current, the Benguela Current off South Africa, the Peru Current). Conversely, when Ekman transport pushes water toward a coast or into a convergence zone, it forces surface water downward (**downwelling**).

At the basin scale, Ekman transport explains why subtropical ocean **gyres** exist. The trade winds near the equator drive Ekman transport toward the poles, while the westerlies at higher latitudes drive transport toward the equator. This convergence piles up water in the center of the subtropical ocean, creating a slight mound of elevated sea surface. The resulting pressure gradient, balanced by the Coriolis force, drives the geostrophic currents that form the great circular gyres — including the Gulf Stream, the Kuroshio, and their counterparts in every ocean basin. The Ekman spiral is therefore the link between wind forcing at the surface and the deep, persistent circulation patterns of the global ocean.
