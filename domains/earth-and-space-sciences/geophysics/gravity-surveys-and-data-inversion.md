---
id: gravity-surveys-and-data-inversion
title: Gravity Surveys and Data Inversion
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: gravity-anomalies-and-interpretation
  type: hard
- id: potential-field-methods-gravity-magnetics
  type: hard
tags:
- gravity
- surveys
- inversion
- data-processing
stage: expert
status: validated
---

# Gravity Surveys and Data Inversion

## Core Idea
Gravity surveys measure the gravitational acceleration at stations on the surface or from aircraft (airborne gravity). Data reduction (free-air, Bouguer, terrain corrections) isolates the gravitational effect of subsurface masses. Inversion methods (Tikhonov regularization, depth weighting) recover 3D density models from gravity anomalies, with resolution inversely proportional to depth. Modern approaches incorporate constraints from seismic, well-log, and geologic information to improve uniqueness.

## Questions

```yaml
- question: "A gravity inversion produces two models that fit the observed surface data equally well: Model A places a dense body at 5 km depth, Model B places a less-dense body at 2 km depth. Which model should a geophysicist prefer?"
  type: multiple-choice
  options:
    - "Model A, because deeper sources produce stronger gravity anomalies"
    - "Model B, because shallower sources are more geologically realistic"
    - "Either — without additional constraints such as seismic data, neither model can be ruled out"
    - "Model A, because Tikhonov regularization always favors deeper solutions"
  answer: 2
  explanation: "Gravity inversion is fundamentally non-unique: many different density distributions can produce identical surface anomalies. Without external constraints — seismic profiles, well logs, or geologic mapping — both models are equally valid solutions. This non-uniqueness is the central challenge of all potential field methods, and it is why integration with other data types is essential. Regularization like Tikhonov constrains solutions to be smooth or simple, but it does not uniquely determine depth without independent information."

- question: "What does the Bouguer correction accomplish in gravity data reduction?"
  type: multiple-choice
  options:
    - "It corrects for the gravitational effect of Earth's rotation and latitude"
    - "It removes the gravitational contribution of the rock mass between the station and sea level"
    - "It accounts for the free-air gradient due to the station's elevation above sea level"
    - "It isolates gravity anomalies caused by surface topography only"
  answer: 1
  explanation: "The Bouguer correction removes the gravitational effect of the rock slab between the measurement station and sea level. This step goes beyond the free-air correction (which only accounts for elevation) by asking: 'What would gravity look like if we could slice away the topography?' After both corrections, the Bouguer anomaly reflects lateral density variations in the subsurface — the signal geologists actually care about. The free-air correction handles elevation; the Bouguer correction handles the rock mass at that elevation."

- question: "Gravity inversion can uniquely recover the subsurface density distribution from a complete set of surface gravity measurements."
  type: true-false
  answer: false
  explanation: "Gravity inversion is inherently non-unique. Infinitely many different density distributions can produce identical gravity observations at the surface — a fundamental mathematical property of potential fields. A deep, dense body may produce the same anomaly as a shallow, less-dense body. Resolving this non-uniqueness requires incorporating independent constraints from seismic surveys, well logs, or geologic knowledge. Regularization techniques like Tikhonov add a smoothness preference but do not eliminate non-uniqueness."

- question: "Terrain corrections in gravity data reduction account for nearby hills and valleys, since a simple slab approximation misses the gravitational effect of irregular topography near the station."
  type: true-false
  answer: true
  explanation: "The Bouguer correction uses an infinite slab approximation to remove the topographic mass. But in rugged terrain, nearby peaks add gravitational pull and nearby valleys represent missing mass that reduces it. The terrain correction accounts for both effects, refining the Bouguer correction. Without it, the Bouguer anomaly in mountainous regions would contain significant terrain-related artifacts unrelated to subsurface geology."

- question: "Why is integration of gravity data with seismic, well-log, and geologic constraints so important in practice? What specific problem does this integration solve?"
  type: short-answer
  answer: "It addresses the non-uniqueness of gravity inversion. Because many density models can fit the same surface observations, gravity data alone cannot identify a single correct subsurface model. Independent constraints narrow the solution space: seismic data defines the geometry of subsurface layers, well logs provide direct density measurements at known depths, and geologic mapping constrains which rock types are plausible. Together, these reduce the set of valid models from infinite to a geologically reasonable few."
  explanation: "The inability to uniquely determine subsurface structure is a mathematical property of potential fields — not a limitation of measurement precision. No amount of additional gravity data can solve it. Only independent, non-redundant data types can constrain the solution, which is why integration is the standard practice rather than an optional enhancement."
```

## Explainer

From your study of gravity anomalies and potential field theory, you understand that variations in subsurface density produce measurable deviations in gravitational acceleration at the surface. A gravity survey is the practical application of this principle: systematically measuring those tiny variations across a region and then working backward to infer what underground structures caused them.

The measurement itself uses highly sensitive instruments — modern gravimeters can detect differences as small as 0.01 milligal (about one ten-millionth of Earth's surface gravity). But the raw readings are contaminated by effects that have nothing to do with subsurface geology. Elevation matters enormously: a station on a hilltop is farther from Earth's center, so gravity is weaker. The **free-air correction** accounts for elevation alone. The **Bouguer correction** goes further, removing the gravitational effect of the rock slab between the station and sea level — essentially asking, "what would gravity be here if we could slice away the topography?" The **terrain correction** handles the irregular shapes that the simple slab approximation misses: nearby valleys that remove mass and peaks that add it. After all corrections, the resulting **Bouguer anomaly** isolates the signal from lateral density variations in the subsurface — exactly what a geologist wants to see.

The challenging part is **inversion**: converting a 2D map of gravity anomalies into a 3D model of underground density. This is fundamentally a non-unique problem. Many different arrangements of density in the subsurface can produce identical gravity observations at the surface — a deep, dense body may look the same as a shallow, less-dense one. This non-uniqueness is the central challenge of all potential field methods. **Tikhonov regularization** addresses it by adding a smoothness constraint: among all models that fit the data, prefer the simplest one. **Depth weighting** counteracts the natural tendency of unconstrained inversions to smear all density anomalies near the surface (since shallow sources dominate the signal).

In practice, geophysicists never interpret gravity data in isolation. Seismic surveys provide independent constraints on the geometry of subsurface layers. Well logs give direct density measurements at known locations. Geological mapping constrains which rock types are plausible. By feeding these constraints into the inversion, the set of possible models shrinks dramatically, and the resulting density model becomes geologically meaningful. This integration of multiple data types is what makes gravity surveys powerful — they provide continuous spatial coverage (unlike wells, which sample only discrete points) at relatively low cost, making them ideal for reconnaissance exploration, basin mapping, and regional tectonic studies.
