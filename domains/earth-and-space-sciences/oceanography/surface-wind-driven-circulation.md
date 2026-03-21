---
id: surface-wind-driven-circulation
title: Wind-Driven Surface Ocean Circulation
domain: earth-and-space-sciences
course: oceanography
prerequisites:
- id: coriolis-effect-ocean-dynamics
  type: hard
- id: wind-driven-ocean-circulation
  type: soft
builds-toward:
- western-boundary-current-intensification
- ocean-gyres-and-boundary-currents
- coastal-upwelling-ekman-dynamics
tags:
- circulation
- wind
- gyres
- Ekman
- Coriolis
stage: advanced
status: draft
---

# Wind-Driven Surface Ocean Circulation

## Core Idea
Wind stress on the ocean surface combined with Coriolis deflection creates large circular currents called gyres. Ekman spiral theory explains how current direction changes with depth in response to wind stress, and the balance between pressure gradients and Coriolis forces shapes ocean circulation patterns.

## Questions

```yaml
- question: "Trade winds in the Northern Hemisphere blow from east to west. What direction does Ekman transport carry surface water?"
  type: multiple-choice
  options:
    - "West, in the same direction as the wind"
    - "North, 90° to the right of the wind"
    - "South, 90° to the left of the wind"
    - "East, opposite to the wind"
  answer: 1
  explanation: "In the Northern Hemisphere, Coriolis deflection is to the right of the direction of motion. Ekman theory shows that the net water transport integrated over the Ekman layer moves 90° to the RIGHT of the wind direction — not in the wind direction. Trade winds blow westward (toward the west), so 90° to the right of westward is northward. This is the key insight: the ocean doesn't flow where the wind blows. This 90° offset is what drives convergence and builds subtropical gyres."

- question: "The center of a Northern Hemisphere subtropical gyre is a region of biological productivity because upwelling brings cold, nutrient-rich water to the surface."
  type: multiple-choice
  options:
    - "True — gyre centers are where cold deep water wells up to fuel plankton growth"
    - "False — gyre centers have downwelling due to Ekman convergence, making them biological deserts"
    - "True — the warm sea surface at gyre centers drives photosynthesis directly"
    - "False — gyre centers are unproductive because currents prevent nutrient mixing"
  answer: 1
  explanation: "This is a common misconception. Ekman transport in a Northern Hemisphere gyre pushes surface water toward the center from all sides (convergence), which piles up water and causes downwelling — not upwelling. This sinks nutrients away from the sunlit surface zone, making subtropical gyre centers among the least biologically productive regions of the ocean (often called 'ocean deserts'). Upwelling and high productivity occur at gyre edges, especially eastern boundaries where offshore Ekman transport draws water up from depth."

- question: "Geostrophic flow in ocean gyres is driven by a balance between the Coriolis effect and the pressure gradient created by the mounded sea surface at the gyre center."
  type: true-false
  answer: true
  explanation: "Ekman transport converges water at the gyre center, raising the sea surface by 1–2 meters. This creates a pressure gradient (water 'wants' to flow downhill, away from the mound). The Coriolis effect deflects this outward flow to the right (Northern Hemisphere), bending it into a circular current rather than letting it escape. When these two forces balance — pressure gradient pushing outward, Coriolis deflecting that flow to the right — the result is steady clockwise (Northern Hemisphere) flow around the gyre. This geostrophic balance maintains the gyre without requiring continuous wind forcing at every point."

- question: "The Ekman spiral means that surface water moves in exactly the same direction as the wind, but deeper water progressively rotates toward that direction."
  type: true-false
  answer: false
  explanation: "The surface layer is already deflected approximately 45° to the RIGHT of the wind in the Northern Hemisphere (not aligned with it). Each successively deeper layer is rotated further to the right and moves more slowly, creating the spiral. The net transport integrated over the full Ekman depth is 90° to the right. So neither the surface water nor any layer below it moves in the wind direction — the deflection starts immediately at the surface and increases with depth."

- question: "Explain why the subtropical ocean centers (like the middle of the North Atlantic gyre) have relatively low biological productivity compared to coastal and subpolar regions."
  type: short-answer
  answer: "Trade winds and westerlies drive Ekman transport toward the gyre center from all sides, causing convergence and downwelling. This pushes surface water (and the nutrients it carries) downward, below the sunlit euphotic zone. Without upward nutrient supply, phytoplankton cannot grow abundantly. In contrast, eastern boundary currents and coastal regions experience offshore Ekman transport (wind-driven surface water moving away from the coast), which draws cold, nutrient-rich water up from depth — fueling high productivity."
  explanation: "The connection between Ekman transport direction and vertical water movement is the key. Convergence → downwelling → nutrient depletion. Divergence (as at the equator or eastern boundaries) → upwelling → nutrient supply. The gyre center's biological poverty is not about temperature or light directly — it's about the vertical motion driven by the Ekman transport pattern, which sequesters nutrients away from where photosynthesis can occur."
```

## Explainer

You already know that the Coriolis effect deflects moving objects to the right in the Northern Hemisphere and to the left in the Southern Hemisphere, and that this deflection is not a real force but a consequence of Earth's rotation. Wind-driven surface circulation is what happens when you combine persistent global wind patterns with this rotational deflection acting on ocean water. The result is a set of large-scale, predictable current systems that dominate the upper few hundred meters of every ocean basin.

Start with the wind. The global atmospheric circulation produces consistent wind belts: **trade winds** blow from east to west in the tropics, and **westerlies** blow from west to east in the mid-latitudes. These winds push on the ocean surface through friction, setting water in motion. But the water does not flow in the same direction as the wind. The **Ekman spiral**, described by Vagn Walfrid Ekman in 1905, explains why: the surface water is deflected roughly 45° to the right of the wind direction (in the Northern Hemisphere) by the Coriolis effect. Each successive layer of water below the surface is dragged along by the layer above it, but deflected further to the right, creating a spiral of decreasing speed and increasing deflection with depth. The net effect, integrated over the full depth of wind influence (the Ekman layer, roughly 50–100 meters), is that the average water transport — called **Ekman transport** — moves at 90° to the wind direction.

This 90° transport is what builds the ocean's great **gyres**. In the North Atlantic, for example, trade winds in the tropics push water westward and, via Ekman transport, slightly toward the center of the basin. Westerlies at higher latitudes push water eastward with Ekman transport also directed toward the center. The result is a convergence of water in the middle of the ocean basin, which piles up slightly — the sea surface in the center of a subtropical gyre is literally about 1–2 meters higher than at the edges. This mound of water creates a pressure gradient pushing outward, and when balanced by the Coriolis deflection, produces a steady clockwise (Northern Hemisphere) or counterclockwise (Southern Hemisphere) flow around the gyre. This balance between the pressure gradient force and the Coriolis effect is called **geostrophic flow**, and it maintains the gyre circulation without requiring continuous wind forcing at every point.

The five major subtropical gyres — North and South Atlantic, North and South Pacific, and Indian Ocean — are the dominant features of surface ocean circulation. Each gyre has a characteristic asymmetry: the western boundary current (like the Gulf Stream or Kuroshio) is narrow, fast, deep, and warm, while the eastern return flow is broad, slow, shallow, and cool. This westward intensification, which you will explore further, is itself a consequence of how the Coriolis effect varies with latitude. Understanding wind-driven circulation is the foundation for explaining why western Europe has a mild climate (the Gulf Stream carries tropical heat northward), why coastal upwelling feeds productive fisheries (Ekman transport pulls surface water offshore), and why the subtropical ocean centers are biological deserts (convergence pushes nutrients downward).
