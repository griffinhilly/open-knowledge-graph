---
id: seismic-velocity-density-relationships
title: Seismic Velocity-Density-Composition Relationships
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: seismic-body-waves-p-and-s
  type: hard
- id: earth-interior-structure
  type: hard
builds-toward:
- crustal-velocity-structure
tags:
- velocity
- density
- composition
- relationship
stage: advanced
status: draft
---

# Seismic Velocity-Density-Composition Relationships

## Core Idea
Seismic velocity correlates with density and mineralogy (Birch's law). Different rock types and pressure-temperature regimes have characteristic velocity-density trends; these are used to interpret seismic tomography models.

## Explainer

You already know that P and S waves travel at speeds determined by the elastic moduli and density of the material they pass through: Vp = √((K + 4G/3)/ρ) and Vs = √(G/ρ), where K is the bulk modulus, G is the shear modulus, and ρ is density. From your study of Earth's interior structure, you know that these velocities increase dramatically with depth — from about 6 km/s in the upper crust to over 13 km/s in the lower mantle for P waves. The question this topic addresses is: what do those velocity values actually tell us about the rocks and conditions at depth?

The fundamental empirical observation is **Birch's law**, which states that P-wave velocity increases linearly with density for rocks of similar mean atomic weight. Francis Birch showed in the 1960s that when you plot Vp against density for a wide range of silicate rocks and minerals, they fall along roughly parallel lines grouped by composition. Rocks with higher mean atomic weight (iron-rich minerals, for instance) plot on higher lines — they are denser for a given velocity. This means velocity alone does not uniquely determine composition, but a velocity-density pair significantly narrows the possibilities. If you measure Vp = 6.5 km/s, it could be gabbro, granulite, or eclogite depending on the density. Add a density estimate from gravity data, and the ambiguity shrinks considerably.

In practice, laboratory measurements on rock samples under controlled pressure and temperature conditions provide the calibration data. As pressure increases (simulating greater depth), microcracks close and grain contacts tighten, causing velocity to rise steeply at first and then more gradually. As temperature increases, elastic moduli decrease and velocity drops. These competing effects produce characteristic velocity-depth profiles for different rock types. **Crustal rocks** typically show Vp of 5.5–7.0 km/s, with granites and sedimentary rocks at the low end and mafic granulites at the high end. The **upper mantle** shows Vp around 8.0–8.5 km/s, consistent with olivine-dominated peridotite. Abrupt velocity jumps — like the Moho discontinuity at 7.0 to 8.0+ km/s — mark compositional boundaries rather than simple pressure effects.

These relationships are what make seismic tomography interpretable. When a tomographic model shows a low-velocity anomaly in the upper mantle, you can infer elevated temperature, partial melt, or a compositional change toward less dense material — the signature of a mantle plume or asthenospheric upwelling. A high-velocity anomaly suggests cold, dense material — a subducting slab or ancient cratonic root. The velocity-density-composition link is also essential for **gravity-seismic joint inversion**, where seismic velocity models are converted to density models using empirical relationships and then tested against gravity observations. Without these empirical relationships, seismic images would show wave-speed variations with no geological meaning; with them, you can translate travel times into rock types, temperatures, and tectonic processes.
