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
stage: advanced
status: draft
---

# Gravity Surveys and Data Inversion

## Core Idea
Gravity surveys measure the gravitational acceleration at stations on the surface or from aircraft (airborne gravity). Data reduction (free-air, Bouguer, terrain corrections) isolates the gravitational effect of subsurface masses. Inversion methods (Tikhonov regularization, depth weighting) recover 3D density models from gravity anomalies, with resolution inversely proportional to depth. Modern approaches incorporate constraints from seismic, well-log, and geologic information to improve uniqueness.

## Explainer

From your study of gravity anomalies and potential field theory, you understand that variations in subsurface density produce measurable deviations in gravitational acceleration at the surface. A gravity survey is the practical application of this principle: systematically measuring those tiny variations across a region and then working backward to infer what underground structures caused them.

The measurement itself uses highly sensitive instruments — modern gravimeters can detect differences as small as 0.01 milligal (about one ten-millionth of Earth's surface gravity). But the raw readings are contaminated by effects that have nothing to do with subsurface geology. Elevation matters enormously: a station on a hilltop is farther from Earth's center, so gravity is weaker. The **free-air correction** accounts for elevation alone. The **Bouguer correction** goes further, removing the gravitational effect of the rock slab between the station and sea level — essentially asking, "what would gravity be here if we could slice away the topography?" The **terrain correction** handles the irregular shapes that the simple slab approximation misses: nearby valleys that remove mass and peaks that add it. After all corrections, the resulting **Bouguer anomaly** isolates the signal from lateral density variations in the subsurface — exactly what a geologist wants to see.

The challenging part is **inversion**: converting a 2D map of gravity anomalies into a 3D model of underground density. This is fundamentally a non-unique problem. Many different arrangements of density in the subsurface can produce identical gravity observations at the surface — a deep, dense body may look the same as a shallow, less-dense one. This non-uniqueness is the central challenge of all potential field methods. **Tikhonov regularization** addresses it by adding a smoothness constraint: among all models that fit the data, prefer the simplest one. **Depth weighting** counteracts the natural tendency of unconstrained inversions to smear all density anomalies near the surface (since shallow sources dominate the signal).

In practice, geophysicists never interpret gravity data in isolation. Seismic surveys provide independent constraints on the geometry of subsurface layers. Well logs give direct density measurements at known locations. Geological mapping constrains which rock types are plausible. By feeding these constraints into the inversion, the set of possible models shrinks dramatically, and the resulting density model becomes geologically meaningful. This integration of multiple data types is what makes gravity surveys powerful — they provide continuous spatial coverage (unlike wells, which sample only discrete points) at relatively low cost, making them ideal for reconnaissance exploration, basin mapping, and regional tectonic studies.
