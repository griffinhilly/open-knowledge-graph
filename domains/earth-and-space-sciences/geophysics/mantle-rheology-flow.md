---
id: mantle-rheology-flow
title: Mantle Rheology and Viscosity
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: rock-rheology-elastic-plastic-deformation
  type: hard
- id: mantle-convection-and-dynamics
  type: hard
builds-toward:
- subduction-zone-thermal-structure
tags:
- mantle
- rheology
- viscosity
- flow
stage: advanced
status: draft
---

# Mantle Rheology and Viscosity

## Core Idea
Mantle rocks deform by dislocation and diffusion creep, with viscosity temperature-dependent and sensitive to grain size and water content. Mantle viscosity (10²¹–10²³ Pa·s) governs convection rates and plate-driving forces.

## Explainer

From rock rheology, you know that materials can deform elastically, plastically, or viscously depending on stress, temperature, and strain rate. From mantle convection and dynamics, you know that the mantle flows on geologic timescales, driving plate tectonics. Mantle rheology connects these ideas by asking: exactly how does rock flow at mantle conditions, and what controls the rate? The answer determines everything from how fast plates move to how the Earth responds to ice-sheet loading.

At the temperatures and pressures of the mantle (roughly 1000–4000°C, 1–140 GPa), silicate minerals deform by two primary mechanisms. **Diffusion creep** involves atoms migrating through the crystal lattice or along grain boundaries in response to differential stress. It dominates at low stress and small grain sizes, and its strain rate is linearly proportional to stress (Newtonian viscosity). **Dislocation creep** involves the movement of line defects (dislocations) through the crystal lattice. It dominates at higher stress and larger grain sizes, and its strain rate depends on stress raised to a power (typically n ≈ 3–3.5), making it strongly non-Newtonian — doubling the stress increases the strain rate roughly eightfold. The upper mantle likely deforms primarily by dislocation creep, evidenced by the seismic anisotropy that dislocation motion produces through preferential alignment of olivine crystals.

The single most important control on mantle viscosity is **temperature**. Viscosity depends exponentially on temperature through an Arrhenius relationship: η ∝ exp(E*/RT), where E* is the activation energy, R is the gas constant, and T is absolute temperature. A temperature increase of just 100°C can decrease viscosity by an order of magnitude. This extreme sensitivity creates a strong feedback with mantle convection — hot upwellings are less viscous and rise faster, while cold downgoing slabs are stiffer and resist deformation. Beyond temperature, **water content** dramatically reduces viscosity even at parts-per-million concentrations by weakening crystal bonds and enhancing dislocation mobility (the "hydrolytic weakening" effect). **Grain size** matters because diffusion creep rate scales inversely with grain size squared or cubed — finer-grained rock flows more easily by diffusion.

The effective viscosity of the mantle spans roughly two orders of magnitude, from about 10¹⁹–10²⁰ Pa·s in the asthenosphere (the low-viscosity layer beneath the lithosphere where temperatures are near the solidus) to 10²²–10²³ Pa·s in the lower mantle. This viscosity structure is constrained by observations of **post-glacial rebound** — the ongoing uplift of Scandinavia and Canada after the last ice sheets melted — which provides a direct measurement of how fast the mantle flows in response to a known load change. The rate of rebound and the pattern of relative sea-level change are sensitive to viscosity at different depths, making glacial isostatic adjustment one of the most powerful constraints on the mantle's rheological profile. This viscosity structure, in turn, sets the timescale of mantle convection, the coupling between plates and the underlying mantle, and ultimately the vigor of Earth's internal heat engine.
