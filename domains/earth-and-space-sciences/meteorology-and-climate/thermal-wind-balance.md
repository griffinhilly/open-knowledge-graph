---
id: thermal-wind-balance
title: Thermal Wind Balance and the Relationship Between Temperature and Wind
domain: earth-and-space-sciences
course: meteorology-and-climate
prerequisites:
- id: geostrophic-wind-and-balance
  type: hard
- id: thermal-structure-of-atmosphere
  type: soft
builds-toward:
- jet-stream-variability-climate
- barotropic-and-baroclinic-atmospheres
- zonal-meridional-circulation
tags:
- thermal-wind
- temperature-gradient
- wind-shear
- dynamics
stage: advanced
status: draft
---

# Thermal Wind Balance and the Relationship Between Temperature and Wind

## Core Idea
Horizontal temperature gradients must be balanced by vertical wind shear through the thermal wind balance equation. A warm air mass to the south and cool air to the north requires westerly wind shear that increases with height, explaining why the jet stream is strongest where the equator-to-pole temperature gradient is largest. This balance explains the seasonal intensification of mid-latitude jets in winter (when temperature contrasts are strong) and their weakness in summer.

## Explainer

You already understand geostrophic balance: in the free atmosphere above the friction layer, the wind blows parallel to the isobars (lines of equal pressure), with the pressure gradient force balanced by the Coriolis force. The geostrophic wind at any given level depends on the pressure gradient at that level. The **thermal wind** concept extends this by asking: how does the geostrophic wind change between two levels, and what determines that change?

The key physical link is the **hypsometric equation**, which says that the thickness of an atmospheric layer — the vertical distance between two pressure surfaces — is proportional to the mean temperature of that layer. Warm air is less dense and expands vertically, so a warm column of air is thicker than a cold column between the same two pressure levels. Now imagine a region where the south is warm and the north is cold: the layer thickness is greater in the south. At the lower pressure surface, the height contours might be relatively flat, but at the upper pressure surface, the heights are tilted — higher in the warm south, lower in the cold north. This tilt creates a stronger pressure gradient aloft than at the surface, and therefore a stronger geostrophic wind.

The **thermal wind** is defined as the vector difference in geostrophic wind between the upper and lower levels — it is not an actual wind but a measure of vertical wind shear. The thermal wind equation states that this shear is proportional to the horizontal temperature gradient and is directed parallel to the isotherms (lines of constant temperature) with the warm air to the right in the Northern Hemisphere. In the most common mid-latitude situation — warm tropics to the south, cold poles to the north — the thermal wind is westerly, meaning the westerly geostrophic wind increases with height. This is exactly why the jet stream exists: the strong equator-to-pole temperature contrast in the upper troposphere produces intense westerly shear that accumulates with height, reaching a maximum near the tropopause.

This relationship has immediate diagnostic and forecasting power. In winter, when the pole-to-equator temperature difference is greatest, the thermal wind is strongest and the jet stream intensifies — often exceeding 200 km/h at the tropopause level. In summer, the gradient weakens and the jet relaxes. You can also use the thermal wind to check weather data for consistency: if you know the temperature field, you can predict how the wind should change with height, and vice versa. When observations violate this balance, it signals that ageostrophic processes — friction, acceleration, or curvature effects — are at work, often associated with active weather development. The thermal wind is thus both a conceptual framework for understanding the atmosphere's vertical structure and a practical tool for synoptic meteorology.
