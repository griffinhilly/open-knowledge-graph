---
id: seismic-velocity-depth-models
title: Seismic Velocity and Depth Models
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: elastic-wave-propagation-in-solids
  type: hard
- id: seismic-waves
  type: hard
builds-toward:
- seismic-ray-tracing-methods
- seismic-tomography-velocity-imaging
tags:
- seismic
- velocity
- modeling
- earth-structure
stage: advanced
status: draft
---

# Seismic Velocity and Depth Models

## Core Idea
Seismic velocity varies with depth due to pressure, temperature, and composition changes in the Earth. Velocity-depth models describe how P-wave and S-wave velocities increase through the crust and mantle, creating the layered structure used in all seismic ray tracing and wave propagation studies. Understanding velocity structures is essential for converting seismic travel times to depth and for inferring Earth's internal composition.

## Explainer

From elastic wave propagation, you know that seismic velocities depend on the elastic moduli and density of the medium: Vp = √((K + 4G/3)/ρ) for P-waves and Vs = √(G/ρ) for S-waves. A velocity-depth model applies these relationships to the real Earth, specifying how Vp and Vs change from the surface to the core. These models are the foundation for everything in observational seismology — without them, you cannot convert a travel time into a depth or locate an earthquake.

The broad pattern is straightforward: **velocity generally increases with depth** because increasing pressure raises elastic moduli faster than it raises density. In the crust, P-wave velocities range from about 5.5–6.5 km/s in typical continental crust (granitic to granodioritic composition) to 6.5–7.0 km/s in oceanic crust (basaltic). At the **Mohorovičić discontinuity** (Moho), velocity jumps sharply to ~8.0 km/s as the composition changes from crustal rocks to olivine-rich mantle peridotite. Through the upper mantle, velocity continues to increase with depth except in the **low-velocity zone** (roughly 80–200 km depth), where partial melting and high temperatures reduce the shear modulus enough to decrease both Vp and Vs — this zone is the seismological signature of the asthenosphere.

Below the low-velocity zone, velocity increases steadily through the transition zone (410–660 km), where olivine undergoes pressure-induced phase transitions to denser crystal structures (wadsleyite, then ringwoodite), producing sharp velocity jumps at those depths. The lower mantle (660–2,890 km) shows a smooth velocity gradient until the **D″ layer** just above the core-mantle boundary, where heterogeneity and ultra-low-velocity zones signal the complex thermal and chemical boundary between silicate mantle and liquid iron core. At the core-mantle boundary itself, P-wave velocity drops dramatically (from ~13.7 to ~8.0 km/s) and **S-waves vanish entirely** — the definitive evidence that the outer core is liquid, since shear waves cannot propagate through fluids.

Reference models like **PREM** (Preliminary Reference Earth Model) and **IASP91** provide standardized one-dimensional velocity-depth profiles that serve as starting points for all seismological analysis. When a seismologist locates an earthquake, they trace rays through such a model using Snell's law to predict arrival times at each station, then adjust the source location until predicted and observed times match. When a tomographer images a mantle plume or subducting slab, they express their results as velocity *perturbations* relative to a reference model — percentage deviations that reflect temperature and composition anomalies. The reference model is thus the common language that connects raw seismograms to three-dimensional Earth structure.
