---
id: fluid-flow-porous-media
title: Fluid Flow in Porous Media and Hydrogeophysics
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: near-surface-geophysics-methods
  type: soft
tags:
- fluid-flow
- porous-media
- hydrogeophysics
stage: advanced
status: draft
---

# Fluid Flow in Porous Media and Hydrogeophysics

## Core Idea
Flow in aquifers is governed by Darcy's law (q = −K∇h). Permeability varies with grain size and cementation. Seismic velocity and electrical conductivity change when water content and pore fluid salinity vary, enabling hydrogeophysical imaging.

## Explainer

Understanding how fluids move through rock and sediment is fundamental to problems ranging from groundwater management to petroleum extraction to contaminant remediation. The starting point is that most geological materials are not solid blocks — they contain interconnected void spaces (pores) through which water, oil, or gas can flow. Two properties govern this flow: **porosity**, the fraction of void space in the rock, and **permeability**, the ease with which fluid can move through those connected pores.

**Darcy's law** is the governing equation: q = −K∇h, where q is the volumetric flow rate per unit area (called the **specific discharge** or Darcy flux), K is the **hydraulic conductivity** (which depends on both the rock's permeability and the fluid's properties), and ∇h is the **hydraulic gradient** — the spatial rate of change of hydraulic head. The negative sign means fluid flows from high head to low head, just as heat flows from hot to cold. Think of it as the subsurface equivalent of water flowing downhill, except "downhill" is defined by pressure and elevation combined, not elevation alone. A clean, well-sorted sand has high permeability because the pores are large and well connected; a clay has low permeability because its tiny pores resist flow, even though clay may actually have higher porosity than sand.

The connection to geophysics comes through the sensitivity of physical properties to pore fluids. **Seismic velocity** depends on the elastic moduli and density of the rock-fluid composite — replacing air with water in the pore space increases both bulk modulus and density, changing P-wave velocity significantly. **Electrical conductivity** is even more sensitive: dry rock is a poor conductor, but saline pore water conducts electricity readily, so resistivity measurements can map water content and salinity variations underground. Ground-penetrating radar, self-potential, and induced polarization methods add further constraints on fluid distribution.

**Hydrogeophysics** exploits these relationships by using geophysical surveys to image subsurface fluid flow non-invasively. For example, time-lapse electrical resistivity tomography can track a contaminant plume as it migrates through an aquifer — the changing resistivity reveals where the plume has traveled. Similarly, seismic monitoring can detect changes in reservoir saturation during oil production or CO₂ injection. The key challenge is converting geophysical measurements (velocity, resistivity) into hydrological quantities (saturation, permeability) through rock physics models, which relate the physical property to porosity, fluid type, and mineral composition. These models are calibrated with borehole data and laboratory measurements, bridging the gap between what geophysics measures and what hydrogeology needs to know.
