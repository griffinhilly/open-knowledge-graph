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
stage: formal-systems
status: validated
---

# Thermal Wind Balance and the Relationship Between Temperature and Wind

## Core Idea
Horizontal temperature gradients must be balanced by vertical wind shear through the thermal wind balance equation. A warm air mass to the south and cool air to the north requires westerly wind shear that increases with height, explaining why the jet stream is strongest where the equator-to-pole temperature gradient is largest. This balance explains the seasonal intensification of mid-latitude jets in winter (when temperature contrasts are strong) and their weakness in summer.

## Questions

```yaml
- question: "In winter, the temperature difference between the tropics and the poles is much larger than in summer. What does thermal wind balance predict about the jet stream?"
  type: multiple-choice
  options:
    - "The jet stream weakens in winter because cold polar air reduces geostrophic wind speeds"
    - "The jet stream intensifies in winter because the stronger pole-to-equator temperature gradient produces greater vertical wind shear, which accumulates with height into a stronger westerly maximum"
    - "The jet stream strength is unrelated to temperature gradients — it depends only on upper-tropospheric pressure patterns"
    - "The jet stream moves equatorward in winter and disappears in summer due to reduced Coriolis force"
  answer: 1
  explanation: "Thermal wind balance directly links the horizontal temperature gradient to vertical wind shear: a stronger temperature gradient produces stronger shear, meaning the westerly wind increases more rapidly with height. In winter, the equator-to-pole temperature contrast is greatest, so the thermal wind (the shear vector) is largest. This shear accumulates from the surface to the tropopause, producing the strongest jet streams of the year — often exceeding 200 km/h at tropopause level. In summer, the gradient weakens, the thermal wind weakens, and the jet relaxes."

- question: "A warm air mass lies to the south and a cold air mass to the north over a mid-latitude region. Compared to the lower-tropospheric pressure gradient, what happens to the pressure gradient between the same two air masses at a higher pressure level?"
  type: multiple-choice
  options:
    - "It weakens at higher levels because pressure decreases with altitude in both air masses equally"
    - "It stays the same — horizontal temperature contrasts do not affect vertical pressure structure"
    - "It strengthens at higher levels because warm air expands more vertically, creating greater height differences between the warm south and cold north at upper pressure surfaces"
    - "It reverses — the cold air develops higher pressure at upper levels due to gravity pulling cold air downward"
  answer: 2
  explanation: "This is the hypsometric mechanism at the heart of thermal wind. Warm air is less dense and expands vertically: the same two pressure surfaces (say, 850 hPa and 500 hPa) are farther apart in warm air than in cold air. Over the warm south, the upper pressure surface is higher; over the cold north, it is lower. This creates a tilted upper pressure surface, which means a stronger pressure gradient at upper levels than at lower levels. The stronger gradient drives a stronger geostrophic wind — exactly the vertical wind shear that thermal wind balance describes."

- question: "The 'thermal wind' is an actual wind that can be measured by a weather balloon at a specific pressure level."
  type: true-false
  answer: false
  explanation: "The thermal wind is not an actual wind — it is the vector *difference* in geostrophic wind between two pressure levels. It is a measure of vertical wind shear, derived mathematically from the horizontal temperature gradient. You cannot fly through the thermal wind or measure it directly; you calculate it from temperature or thickness data. This is a common confusion: the name 'thermal wind' suggests a physical wind, but it is a diagnostic quantity describing how geostrophic winds change with height in a baroclinic atmosphere."

- question: "If the atmosphere's temperature is perfectly uniform horizontally (no horizontal temperature gradient anywhere), thermal wind balance predicts that the geostrophic wind will not change with height."
  type: true-false
  answer: true
  explanation: "The thermal wind equation states that vertical wind shear is proportional to the horizontal temperature gradient. If there is no horizontal temperature gradient, the thermal wind vector is zero — meaning no change in geostrophic wind with height. In such a barotropic atmosphere, the same geostrophic wind blows at every pressure level. Real atmospheres are never perfectly barotropic, but the concept is analytically important: it defines the baseline against which baroclinic (temperature-stratified) atmospheres are measured."

- question: "Explain in physical terms why warm air to the south and cold air to the north produces westerly wind that increases with height in the Northern Hemisphere."
  type: short-answer
  answer: "Warm air is less dense and expands vertically, so the column of atmosphere between two pressure surfaces is thicker in the warm south than in the cold north. At the lower pressure surface, heights may be nearly flat, but at the upper pressure surface, the surface tilts downward from south (high) to north (low). This tilt creates a stronger southward pressure gradient aloft than at the surface. In the Northern Hemisphere, the Coriolis force deflects the geostrophic wind to the right of this gradient, producing a westerly wind. Because the tilt is greater at higher levels, the westerly wind is stronger at higher levels — vertical shear that increases with height."
  explanation: "This causal chain — temperature gradient → thickness gradient → upper-level pressure tilt → enhanced pressure gradient → stronger geostrophic wind — is the complete physical story of thermal wind. Understanding it mechanistically lets you predict seasonal and geographic jet stream behavior from first principles. The key conceptual step that students often miss is that the pressure gradient *changes with height* because of differential thermal expansion, not because of any wind force acting on the atmosphere."
```

## Explainer

You already understand geostrophic balance: in the free atmosphere above the friction layer, the wind blows parallel to the isobars (lines of equal pressure), with the pressure gradient force balanced by the Coriolis force. The geostrophic wind at any given level depends on the pressure gradient at that level. The **thermal wind** concept extends this by asking: how does the geostrophic wind change between two levels, and what determines that change?

The key physical link is the **hypsometric equation**, which says that the thickness of an atmospheric layer — the vertical distance between two pressure surfaces — is proportional to the mean temperature of that layer. Warm air is less dense and expands vertically, so a warm column of air is thicker than a cold column between the same two pressure levels. Now imagine a region where the south is warm and the north is cold: the layer thickness is greater in the south. At the lower pressure surface, the height contours might be relatively flat, but at the upper pressure surface, the heights are tilted — higher in the warm south, lower in the cold north. This tilt creates a stronger pressure gradient aloft than at the surface, and therefore a stronger geostrophic wind.

The **thermal wind** is defined as the vector difference in geostrophic wind between the upper and lower levels — it is not an actual wind but a measure of vertical wind shear. The thermal wind equation states that this shear is proportional to the horizontal temperature gradient and is directed parallel to the isotherms (lines of constant temperature) with the warm air to the right in the Northern Hemisphere. In the most common mid-latitude situation — warm tropics to the south, cold poles to the north — the thermal wind is westerly, meaning the westerly geostrophic wind increases with height. This is exactly why the jet stream exists: the strong equator-to-pole temperature contrast in the upper troposphere produces intense westerly shear that accumulates with height, reaching a maximum near the tropopause.

This relationship has immediate diagnostic and forecasting power. In winter, when the pole-to-equator temperature difference is greatest, the thermal wind is strongest and the jet stream intensifies — often exceeding 200 km/h at the tropopause level. In summer, the gradient weakens and the jet relaxes. You can also use the thermal wind to check weather data for consistency: if you know the temperature field, you can predict how the wind should change with height, and vice versa. When observations violate this balance, it signals that ageostrophic processes — friction, acceleration, or curvature effects — are at work, often associated with active weather development. The thermal wind is thus both a conceptual framework for understanding the atmosphere's vertical structure and a practical tool for synoptic meteorology.
