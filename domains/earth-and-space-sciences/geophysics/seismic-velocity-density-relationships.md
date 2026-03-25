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
status: validated
---

# Seismic Velocity-Density-Composition Relationships

## Core Idea
Seismic velocity correlates with density and mineralogy (Birch's law). Different rock types and pressure-temperature regimes have characteristic velocity-density trends; these are used to interpret seismic tomography models.

## Questions

```yaml
- question: "A seismic tomography model reveals a region of anomalously low P-wave velocity in the upper mantle. What geological interpretation is most consistent with this observation?"
  type: multiple-choice
  options:
    - "The region contains unusually dense, cold material — consistent with a subducting oceanic slab"
    - "The region likely contains elevated temperature, partial melt, or less dense material — consistent with a mantle plume or asthenospheric upwelling"
    - "Low velocity must indicate a compositional boundary where granitic crust extends unusually deep into the mantle"
    - "Velocity anomalies in the mantle cannot be interpreted geologically without direct sampling"
  answer: 1
  explanation: "Seismic velocity decreases when elastic moduli decrease or density decreases relative to the surrounding material. Elevated temperature reduces elastic moduli, and partial melt reduces both moduli and effective density — both lower velocity. Mantle plumes and asthenospheric upwellings are warmer and may contain small fractions of melt, producing the observed low-velocity anomaly. Conversely, cold, dense subducting slabs produce high-velocity anomalies. This velocity-temperature-composition relationship is what makes seismic tomography a tool for imaging mantle dynamics."

- question: "Birch's law predicts that P-wave velocity increases linearly with density for rocks of similar mean atomic weight. What is the practical implication when a seismic model shows Vp = 7.0 km/s in the lower crust?"
  type: multiple-choice
  options:
    - "The rock type is uniquely determined as mafic granulite — no other crustal rock has exactly this velocity"
    - "Without additional density information (e.g., from gravity data), multiple rock types are consistent with this velocity, and composition cannot be uniquely determined"
    - "The velocity exceeds typical crustal values, indicating the model must contain errors"
    - "Birch's law applies only to mantle rocks, so this velocity cannot be interpreted for crustal material"
  answer: 1
  explanation: "Birch's law shows that rocks of different mean atomic weight (iron content, for instance) fall on different Vp-density lines. A measured Vp = 7.0 km/s could correspond to gabbro, mafic granulite, or eclogite — these have similar velocities but different densities and compositions. Adding an independent density estimate from gravity data, and plotting the (Vp, ρ) pair on a Birch's law diagram, significantly narrows the possibilities. Velocity alone is ambiguous; velocity plus density is much more diagnostic. This is why gravity-seismic joint interpretation is standard practice."

- question: "According to Birch's law, measuring P-wave velocity alone is sufficient to uniquely identify the rock type and composition at depth."
  type: true-false
  answer: false
  explanation: "Birch's law plots Vp against density for different rock types, showing that rocks of similar mean atomic weight fall along the same line but rocks of different compositions occupy different lines. This means the same velocity can correspond to different rock types if they have different densities. For example, Vp = 7.0 km/s is consistent with gabbro, granulite, or eclogite depending on the density. Velocity alone is therefore ambiguous for compositional interpretation. Combining velocity with an independent density estimate (from gravity data or mineral physics) dramatically reduces this ambiguity, which is why Birch's law is used in joint seismic-gravity interpretation rather than seismic interpretation alone."

- question: "Abrupt seismic velocity jumps like the Mohorovičić discontinuity are interpreted as compositional boundaries rather than simple effects of increasing pressure."
  type: true-false
  answer: true
  explanation: "Pressure and temperature both affect seismic velocity, but their effects are gradual with depth. If the Moho were purely a pressure effect, velocity would increase smoothly. Instead, the Moho shows a sharp jump from ~7 km/s to ~8 km/s over a narrow depth range — far too rapid to be a pressure-induced gradual change. This abrupt change is consistent with a compositional transition from felsic/mafic crustal rocks to olivine-dominated peridotite mantle. Other sharp discontinuities at 410 km and 660 km depth are interpreted as phase transitions (minerals changing crystal structure under pressure), also distinguishable from gradual pressure effects by their abruptness."

- question: "Explain why seismic tomography images would be geologically meaningless without empirical velocity-density-composition relationships like Birch's law. What information do these relationships add?"
  type: short-answer
  answer: "Seismic tomography produces images of where P- or S-wave velocities are relatively fast or slow compared to a reference model. Without empirical relationships connecting velocity to rock type, temperature, and density, these images show only patterns of wave speed — they are physically real but geologically uninterpretable. Birch's law and laboratory measurements at controlled pressure and temperature provide the translation key: a low-velocity anomaly becomes 'warm mantle or partial melt,' a high-velocity anomaly becomes 'cold, dense subducting slab.' Adding gravity data constrains density independently, and combining the two with Birch's law allows joint inversion that further constrains composition. Without these relationships, tomography would be like seeing different shades of gray in an X-ray with no knowledge of which shades correspond to bone, tissue, or air. The empirical relationships convert abstract wave-speed patterns into actual geology."
  explanation: "This connects to a broader principle in geophysics: observations are always indirect, and interpretation requires a physical model linking the observation to the quantity of interest. Seismology measures travel times; mineral physics provides the velocity-composition link; the combination produces geological insight. Birch's law is one of the most important of these linking relationships, and its empirical robustness across decades of laboratory measurements is what makes quantitative interpretation of Earth's interior possible."
```

## Explainer

You already know that P and S waves travel at speeds determined by the elastic moduli and density of the material they pass through: Vp = √((K + 4G/3)/ρ) and Vs = √(G/ρ), where K is the bulk modulus, G is the shear modulus, and ρ is density. From your study of Earth's interior structure, you know that these velocities increase dramatically with depth — from about 6 km/s in the upper crust to over 13 km/s in the lower mantle for P waves. The question this topic addresses is: what do those velocity values actually tell us about the rocks and conditions at depth?

The fundamental empirical observation is **Birch's law**, which states that P-wave velocity increases linearly with density for rocks of similar mean atomic weight. Francis Birch showed in the 1960s that when you plot Vp against density for a wide range of silicate rocks and minerals, they fall along roughly parallel lines grouped by composition. Rocks with higher mean atomic weight (iron-rich minerals, for instance) plot on higher lines — they are denser for a given velocity. This means velocity alone does not uniquely determine composition, but a velocity-density pair significantly narrows the possibilities. If you measure Vp = 6.5 km/s, it could be gabbro, granulite, or eclogite depending on the density. Add a density estimate from gravity data, and the ambiguity shrinks considerably.

In practice, laboratory measurements on rock samples under controlled pressure and temperature conditions provide the calibration data. As pressure increases (simulating greater depth), microcracks close and grain contacts tighten, causing velocity to rise steeply at first and then more gradually. As temperature increases, elastic moduli decrease and velocity drops. These competing effects produce characteristic velocity-depth profiles for different rock types. **Crustal rocks** typically show Vp of 5.5–7.0 km/s, with granites and sedimentary rocks at the low end and mafic granulites at the high end. The **upper mantle** shows Vp around 8.0–8.5 km/s, consistent with olivine-dominated peridotite. Abrupt velocity jumps — like the Moho discontinuity at 7.0 to 8.0+ km/s — mark compositional boundaries rather than simple pressure effects.

These relationships are what make seismic tomography interpretable. When a tomographic model shows a low-velocity anomaly in the upper mantle, you can infer elevated temperature, partial melt, or a compositional change toward less dense material — the signature of a mantle plume or asthenospheric upwelling. A high-velocity anomaly suggests cold, dense material — a subducting slab or ancient cratonic root. The velocity-density-composition link is also essential for **gravity-seismic joint inversion**, where seismic velocity models are converted to density models using empirical relationships and then tested against gravity observations. Without these empirical relationships, seismic images would show wave-speed variations with no geological meaning; with them, you can translate travel times into rock types, temperatures, and tectonic processes.
