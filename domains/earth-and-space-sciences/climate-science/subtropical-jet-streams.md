---
id: subtropical-jet-streams
title: Subtropical Jet Streams and Upper-Level Winds
domain: earth-and-space-sciences
course: climate-science
prerequisites:
- id: hadley-cell-dynamics
  type: hard
- id: rossby-waves-barotropic
  type: soft
builds-toward:
- baroclinic-instability
- enso-mechanisms-teleconnections
tags:
- jets
- subtropical
- wind
- upper-troposphere
- circulation
stage: advanced
status: draft
---

# Subtropical Jet Streams and Upper-Level Winds

## Core Idea
Subtropical jet streams form at the poleward edge of the Hadley cell (~30° latitude), where poleward-moving aloft air encounters the Coriolis effect and is deflected strongly. These narrow, fast-moving currents (>50 m/s) are concentrated in the upper troposphere and are maintained by the thermal wind balance. Jet streams steer weather systems, separate tropical from mid-latitude air masses, and strongly influence regional precipitation and temperature patterns on subseasonal to seasonal timescales.

## How It's Best Learned
Examine zonal wind profiles and identify jet cores. Apply the thermal wind equation to relate jet strength to the poleward temperature gradient.

## Common Misconceptions
Jet streams are not fixed in position; they meander (forming ridges and troughs) and shift poleward/equatorward seasonally. Also, jets are maintained by thermal gradients, not direct heating; they weaken when meridional temperature gradients weaken.

## Questions

```yaml
- question: "The subtropical jet stream weakens during summer compared to winter primarily because:"
  type: multiple-choice
  options:
    - "The Hadley cell reverses direction in summer, reducing upper-level poleward flow"
    - "The Coriolis effect weakens at subtropical latitudes during summer months"
    - "The equator-to-pole temperature gradient is smaller in summer"
    - "Upper-tropospheric humidity increases in summer, creating drag on the jet"
  answer: 2
  explanation: "Jet stream strength is governed by the thermal wind relationship: a stronger meridional temperature gradient produces stronger vertical wind shear and a faster jet. In winter, the poles cool dramatically while the tropics stay warm, maximizing the temperature contrast. In summer, the poles warm and the gradient relaxes, weakening the jet. The Hadley cell does not reverse direction, and the Coriolis effect does not vary seasonally."

- question: "What is the primary mechanism that concentrates upper-level winds into the subtropical jet stream?"
  type: multiple-choice
  options:
    - "Differential solar heating creating a direct pressure gradient at 30° latitude"
    - "Coriolis deflection of poleward-moving Hadley cell air conserving angular momentum"
    - "Convergence of trade winds at the ITCZ forcing air upward and outward"
    - "Radiative cooling of the tropopause creating a sharp density inversion"
  answer: 1
  explanation: "As air rises near the equator and flows poleward in the upper troposphere, it conserves angular momentum. Moving to smaller-radius latitude circles, it accelerates relative to Earth's surface and is deflected strongly eastward by the Coriolis effect. By ~30° latitude, this deflection has concentrated the air into a fast zonal ribbon — the subtropical jet. This is angular momentum transport driven by the Hadley circulation, not direct heating."

- question: "The subtropical jet stream and the polar front jet stream have different underlying origins: the subtropical jet arises from Hadley cell angular momentum transport, while the polar jet is driven by baroclinic instability along the polar front."
  type: true-false
  answer: true
  explanation: "These are mechanistically distinct features that happen to look similar (both are upper-tropospheric wind maxima). The subtropical jet is a direct consequence of upper-tropospheric poleward flow being deflected by Coriolis as it exits the Hadley cell. The polar jet forms at ~50–60° latitude along the polar front, driven by baroclinic instability where cold polar air meets warmer mid-latitude air. Both are maintained by thermal wind balance, but their energy sources differ."

- question: "Jet streams maintain a nearly fixed east-west path throughout the year, shifting only slightly with the seasons."
  type: true-false
  answer: false
  explanation: "Jet streams meander substantially and continuously, forming large-amplitude ridges and troughs (Rossby wave patterns) that evolve on timescales of days to weeks. They also migrate poleward in summer and equatorward in winter. This variability in position and amplitude is precisely what drives mid-latitude weather changes — when the jet develops persistent large meanders, weather systems stagnate and extreme events (heat waves, floods, cold snaps) become more likely."

- question: "Explain why the subtropical jet stream intensifies in winter. Connect the seasonal change to the physics governing jet stream strength."
  type: short-answer
  answer: "The subtropical jet's strength is governed by the thermal wind relationship: a stronger meridional (pole-to-equator) temperature gradient produces stronger vertical wind shear and thus a faster jet core. In winter, the poles cool dramatically while the tropics remain relatively warm, maximizing this temperature contrast. In summer, polar warming weakens the gradient, reducing vertical wind shear and producing a weaker, more variable jet."
  explanation: "The thermal wind equation quantifies this: ∂u/∂z ∝ −∂T/∂y. A large poleward temperature decrease (large |∂T/∂y|) forces large vertical wind shear, concentrating fast winds at jet level. The seasonal variation in polar versus tropical temperatures is the direct driver of seasonal jet variability — the Hadley cell itself persists year-round, but its associated jet strengthens and weakens with the temperature gradient."
```

## Explainer

From your study of the Hadley cell, you know that air rises near the equator, flows poleward in the upper troposphere, descends at roughly 30° latitude, and returns equatorward at the surface. The subtropical jet stream is a direct consequence of what happens to that poleward-moving upper-level air as it encounters the **Coriolis effect**. Air moving away from the equator conserves angular momentum: as it moves to smaller-radius latitude circles, it must speed up relative to Earth's surface. By the time the air reaches about 30° latitude, it has been deflected so strongly eastward that it forms a concentrated ribbon of fast-moving wind — the subtropical jet — typically blowing at 50 m/s or more near the tropopause.

The jet's strength is not arbitrary; it is governed by the **thermal wind relationship**, which links the vertical wind shear to the horizontal temperature gradient. A strong temperature contrast between the warm tropics and the cooler subtropics produces a stronger jet. This is why the subtropical jet intensifies in winter, when the equator-to-pole temperature difference is greatest, and weakens in summer, when the gradient relaxes. The thermal wind equation, which you may have encountered alongside Rossby wave dynamics, provides the quantitative link: the stronger the meridional temperature gradient at a given altitude, the faster the geostrophic wind increases with height, producing a sharper jet core.

The subtropical jet has enormous practical consequences for weather and climate. It acts as a boundary between tropical air masses and mid-latitude air, steering extratropical cyclones and influencing where precipitation falls. When the jet is strong and zonal (roughly east-west), weather systems move briskly across continents. When it weakens or develops large-amplitude meanders — the ridges and troughs you know from Rossby wave theory — weather patterns can stagnate, producing prolonged heatwaves, cold spells, or flooding. The jet's seasonal migration also determines the timing of monsoons: as the jet shifts poleward in spring and summer, it allows the intertropical convergence zone to migrate, triggering monsoon onset in South and East Asia.

It is important to distinguish the subtropical jet from its cousin, the **polar front jet**, which forms at higher latitudes (~50–60°) along the polar front where cold polar air meets warmer mid-latitude air. While both are upper-tropospheric wind maxima maintained by thermal gradients, they have different origins: the subtropical jet is driven by angular momentum transport in the Hadley cell, while the polar jet is driven by baroclinic instability along the polar front. In practice, the two jets can merge, split, or interact, creating complex upper-level flow patterns that are central to mid-latitude weather forecasting.
