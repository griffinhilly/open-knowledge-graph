---
id: gravity-data-reduction
title: 'Gravity Data Reduction: Bouguer, Free-Air, and Terrain Corrections'
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: gravity-surveys-and-data-inversion
  type: hard
- id: gravity-potential-theory-earths-field
  type: hard
builds-toward:
- gravity-forward-modeling-inversion
tags:
- gravity
- data-reduction
- corrections
- bouguer
stage: expert
status: validated
---

# Gravity Data Reduction: Bouguer, Free-Air, and Terrain Corrections

## Core Idea
Observed gravity must be corrected for latitude (normal gravity), elevation (free-air correction), topographic masses (terrain correction), and bathymetry to isolate subsurface anomalies. The Bouguer anomaly (with assumed density slab) reveals density variations with depth.

## Questions

```yaml
- question: "A gravimeter is deployed at a mountain station 1,500 m above sea level. Compared to an identical station at sea level at the same latitude, the mountain station records lower gravity. Which correction specifically accounts for this elevation effect?"
  type: multiple-choice
  options:
    - "The Bouguer correction — it removes the mass of rock beneath the mountain station"
    - "The free-air correction — it compensates for the reduced gravity due to greater distance from Earth's center"
    - "The terrain correction — it accounts for the gravitational pull of surrounding peaks"
    - "The latitude correction — polar stations experience stronger gravity and must be normalized"
  answer: 1
  explanation: "The free-air correction adds back the gravity lost by being farther from Earth's center (~0.3086 mGal per meter of elevation), projecting all stations to a common reference level. The Bouguer correction is applied after — it removes the gravitational attraction of the rock mass between the station and sea level. Confusing these two is a classic error: the free-air correction is purely geometric (elevation), while the Bouguer correction is mass-dependent (density of intervening rock)."

- question: "A geophysicist computes the complete Bouguer anomaly across a sedimentary basin. The anomaly is negative over the basin center. What does this most likely indicate?"
  type: multiple-choice
  options:
    - "The terrain correction was applied incorrectly, subtracting too much gravity"
    - "The basin sediments are less dense than the assumed slab density, producing a gravity deficit"
    - "The basin is at high elevation, and the free-air correction was not applied"
    - "Negative Bouguer anomalies always indicate the presence of water rather than rock"
  answer: 1
  explanation: "A negative Bouguer anomaly means the observed gravity is less than predicted after all corrections — the subsurface contains less mass than the assumed reference model. Sedimentary basin fills (typically 2,200–2,400 kg/m³) are less dense than the standard Bouguer slab density (2,670 kg/m³), creating a mass deficit. The Bouguer anomaly is exactly what is needed to detect this: after removing latitude, elevation, and assumed slab effects, the remaining signal reflects real lateral density variations."

- question: "The free-air anomaly is the fully reduced gravity signal, ready for geological interpretation without further corrections."
  type: true-false
  answer: false
  explanation: "The free-air anomaly removes only the latitude and elevation effects — it still contains the gravitational attraction of all the rock mass between the station and sea level (the topographic mass). Over mountains, this topographic contribution dominates and masks subsurface signals. The Bouguer correction (and terrain correction in rugged terrain) must be applied to remove this rock mass before the anomaly isolates subsurface density variations."

- question: "The terrain correction always adds to the Bouguer anomaly — it never subtracts from it."
  type: true-false
  answer: true
  explanation: "The terrain correction accounts for the fact that surrounding topography exerts gravitational attraction in unexpected directions. Nearby hills pull the gravimeter upward (reducing the vertical reading), and nearby valleys lack mass that the infinite-slab model assumed was present (also effectively pulling upward). Both effects reduce measured gravity relative to the slab model, so the terrain correction always adds a positive increment to restore the anomaly to what a flat reference surface would give."

- question: "Why does the choice of assumed density in the Bouguer correction matter, and what goes wrong if the wrong density is used?"
  type: short-answer
  answer: "The Bouguer correction models the rock between the station and sea level as an infinite horizontal slab of assumed density (typically 2,670 kg/m³ for continental crust). If the actual rock density is higher, the correction under-removes the topographic mass, leaving a positive residual in the Bouguer anomaly that mimics a dense subsurface body. If the actual density is lower, the correction over-removes, creating a spurious negative anomaly. The residual can be used diagnostically: by varying the assumed density until the Bouguer anomaly shows minimum correlation with topography, geophysicists can estimate the actual surface rock density — this is the Nettleton method."
  explanation: "Getting the Bouguer density wrong is especially problematic in areas of unusual surface geology (e.g., igneous intrusions, salt diapirs) where surface and subsurface densities differ from the crust average. The standard 2,670 kg/m³ is a reasonable default for granite-dominated crust but may be wrong by hundreds of kg/m³ in other settings."
```

## Explainer

From your study of gravity surveys and potential theory, you know that a gravimeter measures the total gravitational acceleration at a station. But that raw measurement is a composite of many effects — the station's latitude, its elevation above sea level, the mass of rock and topography surrounding it, and the subsurface density anomalies you actually want to find. **Gravity data reduction** is the systematic process of stripping away the known, predictable contributions so that only the geologically interesting signal remains.

The first correction accounts for latitude. Earth is an oblate spheroid, so gravity varies from about 9.78 m/s² at the equator to 9.83 m/s² at the poles. The **normal gravity** formula (based on the reference ellipsoid) predicts what gravity should be at any latitude on a hypothetical smooth Earth with no topography. Subtracting this removes the largest source of variation and gives you the **gravity anomaly** — the difference between observed and predicted values.

Next comes the **free-air correction**, which accounts for elevation. A station at 1,000 m elevation is farther from Earth's center than one at sea level, so it experiences weaker gravity — roughly 0.3086 mGal per meter of elevation. The free-air correction adds this back, effectively projecting all measurements down to a common reference surface (the geoid). The result is the **free-air anomaly**, which is useful for studying large-scale isostatic balance but still contains the gravitational effect of the rock mass between the station and sea level.

The **Bouguer correction** removes that rock mass by modeling it as an infinite horizontal slab of assumed density (typically 2,670 kg/m³ for continental crust). This subtraction eliminates the gravitational pull of the topographic mass itself. In mountainous terrain, the infinite slab approximation is too crude — nearby peaks and valleys produce gravitational effects that the slab model misses. The **terrain correction** fixes this by calculating the gravitational influence of the actual topography around each station and adding it to the Bouguer anomaly. The fully corrected result — the **complete Bouguer anomaly** — isolates lateral density variations beneath the surface: exactly what you need to detect buried structures like ore bodies, sedimentary basins, or the depth to the Moho.
