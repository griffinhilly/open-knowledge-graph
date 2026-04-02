---
id: thermodynamic-diagram-analysis
title: Thermodynamic Diagrams and Atmospheric Sounding Analysis
domain: earth-and-space-sciences
course: meteorology-and-climate
prerequisites:
- id: adiabatic-lapse-rates
  type: hard
- id: saturation-and-dew-point
  type: hard
- id: convective-instability-indices
  type: hard
builds-toward:
- severe-weather-systems
- latent-heating-in-weather-systems
tags:
- skew-T
- sounding
- hodograph
- thermodynamic-diagram
- analysis
stage: expert
status: validated
---

# Thermodynamic Diagrams and Atmospheric Sounding Analysis

## Core Idea
Atmospheric soundings—vertical profiles of temperature, dew point, and wind measured by radiosondes—are plotted on thermodynamic diagrams (like skew-T log-P diagrams) to visualize atmospheric structure. These diagrams allow forecasters to identify stable and unstable layers, estimate parcel lifting levels and heights, calculate CAPE, and analyze wind shear by examining hodographs (wind vectors at different heights). Proper sounding interpretation is essential for severe weather forecasting.

## Questions

```yaml
- question: "On a skew-T log-P sounding, the temperature trace and dew point trace nearly coincide from 850 hPa to 700 hPa, then diverge sharply above 700 hPa. What does this pattern indicate about the atmosphere's vertical structure?"
  type: multiple-choice
  options:
    - "Dry air near the surface with a moist elevated layer above 700 hPa — a typical capping inversion pattern"
    - "A saturated (cloudy) layer from 850 to 700 hPa, with dry air above — the cloud tops are near 700 hPa"
    - "A temperature inversion between 850 and 700 hPa that prevents any upward motion"
    - "Increasing wind shear between 850 and 700 hPa that is tearing apart moisture structures"
  answer: 1
  explanation: "On a skew-T, temperature and dew point converging means the air is approaching saturation — the closer the two traces, the moister the air. When they touch, the relative humidity is 100% and the air is inside a cloud. Divergence above 700 hPa means dew point drops off much faster than temperature, indicating dry air with low relative humidity. A forecaster reading this sounding would identify a cloud layer from 850 to 700 hPa (where the traces coincide) with a clear, dry layer above. This structure is common in stratus or stratocumulus situations."

- question: "Two soundings both show CAPE of 3000 J/kg. Sounding A has a straight hodograph; sounding B has a strongly curved clockwise hodograph with large changes in wind direction from the surface to 6 km. What does this difference imply for severe weather potential?"
  type: multiple-choice
  options:
    - "Both present equal severe weather potential — CAPE determines updraft strength and storm intensity, making hodograph shape irrelevant"
    - "Sounding A is more dangerous because straight hodographs indicate faster storm motion and larger hail"
    - "Sounding B is more favorable for supercell thunderstorms with rotating updrafts, because curved hodographs indicate directional wind shear that promotes mesocyclone development"
    - "Sounding B is less dangerous because the wind turning through many directions reduces effective vertical wind shear"
  answer: 2
  explanation: "CAPE quantifies the energy available for updrafts but says nothing about storm organization. The hodograph reveals wind shear structure. A straight hodograph means winds increase in speed with height but don't turn — this can support multicell storms and some severe weather. A curved (clockwise) hodograph means winds turn clockwise from the surface upward, which generates horizontal vorticity that can be tilted into the vertical by a storm's updraft, producing mesocyclone rotation and supercell thunderstorms. Large curved hodographs are one of the best discriminators between ordinary thunderstorms and tornadic supercells."

- question: "On a skew-T log-P diagram, the area enclosed between a lifted parcel's moist adiabatic path and the environmental temperature sounding — where the parcel is warmer than the environment — represents CAPE (Convective Available Potential Energy)."
  type: true-false
  answer: true
  explanation: "CAPE is precisely this positive area on the skew-T. When the parcel's temperature exceeds the environmental temperature (parcel trace lies to the right of the environmental temperature trace on a standard skew-T), the parcel is positively buoyant — it accelerates upward. Integrating this buoyancy from the Level of Free Convection (LFC) to the Equilibrium Level (EL) gives CAPE in J/kg, which is proportional to the maximum potential updraft velocity. Larger CAPE means more energy available for thunderstorm updrafts."

- question: "A large CAPE value on a sounding guarantees that severe thunderstorms will develop, regardless of other atmospheric conditions."
  type: true-false
  answer: false
  explanation: "CAPE is necessary but not sufficient for severe thunderstorm development. Convective Inhibition (CIN) — the negative area on the skew-T below the LFC — represents an energy barrier that must be overcome to initiate convection. High CAPE with strong CIN means the atmosphere is loaded but 'capped'; storms won't develop without a triggering mechanism (frontal lift, surface heating, outflow boundaries). Moisture must also be sufficient throughout a deep layer, and — as the hodograph analysis shows — wind shear determines whether storms can organize into severe, rotating supercells rather than pulse storms."

- question: "Explain how a forecaster uses the temperature trace, dew point trace, and adiabatic reference lines on a skew-T log-P diagram to assess whether the atmosphere can support deep moist convection."
  type: short-answer
  answer: "The forecaster lifts a surface parcel dry-adiabatically until its temperature matches the dew point — the Lifted Condensation Level (LCL), where cloud forms. Above the LCL, the parcel cools along the moist adiabat (more slowly, due to latent heat release). Wherever the parcel's moist adiabatic path is warmer than the environmental temperature sounding, the parcel is positively buoyant — this is CAPE. A large positive area from the Level of Free Convection (LFC) to the Equilibrium Level (EL) indicates the atmosphere can support deep convection; the CIN below the LFC shows how much lift is needed to trigger it."
  explanation: "The skew-T makes this analysis visual and immediate. The forecaster is essentially asking: 'If I took a parcel of near-surface air and lifted it, would it eventually become buoyant and accelerate on its own?' The intersection of the parcel's path with the environmental sounding marks the LFC (where buoyancy turns positive) and the EL (where it turns negative again). The shape and area of the positive region immediately communicates storm potential, while the shape of the CIN region communicates how strong a trigger is needed. This is why reading skew-T soundings is a core skill for operational weather forecasters."
```

## Explainer

You already understand adiabatic lapse rates (how rising parcels cool), saturation and dew point (when moisture condenses), and convective instability indices (how to quantify the atmosphere's potential for thunderstorms). A **thermodynamic diagram** is the tool that brings all of these concepts together on a single chart, letting you visually read the atmosphere's vertical structure and predict what will happen when air is lifted.

The most widely used diagram is the **skew-T log-P diagram**. The vertical axis is pressure (decreasing upward on a logarithmic scale, so that equal vertical distances represent roughly equal altitude intervals). The horizontal axis is temperature, but the isotherms are tilted — "skewed" — to the right, which spreads out the temperature and dew point lines and makes the diagram easier to read. On this chart, a radiosonde sounding appears as two lines: the **temperature trace** (solid, on the right) and the **dew point trace** (dashed, on the left). Where these two lines are close together, the air is moist; where they diverge, the air is dry. When they touch, the air is saturated — you are inside a cloud.

Overlaid on the diagram are reference lines you already know: dry adiabats (the ~9.8°C/km cooling rate of unsaturated rising air), moist adiabats (the slower cooling rate once condensation begins and releases latent heat), and mixing ratio lines (constant moisture content). To assess stability, you trace a hypothetical parcel upward from the surface: it follows the dry adiabat until it reaches its **Lifted Condensation Level** (where temperature meets dew point and a cloud forms), then follows the moist adiabat above that. Wherever the parcel's traced path is warmer than the environmental temperature line, the parcel is buoyant and will accelerate upward — this is unstable air. The area between the parcel's path and the environment where the parcel is warmer represents **CAPE** (Convective Available Potential Energy), the total energy available to fuel thunderstorm updrafts. The larger that area, the more explosive the convection.

A **hodograph** complements the thermodynamic diagram by plotting wind vectors at different heights as a connected curve. The shape of the hodograph reveals wind shear structure: a straight hodograph indicates unidirectional shear (winds strengthening with height but not turning), while a curved hodograph indicates directional shear — winds turning clockwise with height. Curved hodographs are associated with rotating updrafts and supercell thunderstorms. Together, the skew-T and hodograph give a forecaster a complete picture: the skew-T reveals whether the atmosphere can produce deep convection (instability and moisture), while the hodograph reveals whether that convection can organize into severe, rotating storms. Learning to read these diagrams is the gateway to operational weather forecasting.
