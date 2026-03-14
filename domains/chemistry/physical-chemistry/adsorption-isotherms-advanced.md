---
id: adsorption-isotherms-advanced
title: 'Advanced Adsorption Isotherms: BET, Freundlich, and Beyond'
domain: chemistry
course: physical-chemistry
prerequisites:
- id: langmuir-adsorption-model
  type: hard
- id: surface-chemistry-and-catalysis
  type: soft
builds-toward: []
tags:
- adsorption-isotherms
- BET-theory
- Freundlich
- Temkin
- multilayer-adsorption
- surface-area
stage: advanced
status: draft
---

# Advanced Adsorption Isotherms: BET, Freundlich, and Beyond

## Core Idea
The Langmuir isotherm assumes monolayer adsorption on equivalent, non-interacting sites, but real surfaces are more complex. The Freundlich isotherm theta = K*P^(1/n) empirically accounts for surface heterogeneity (a distribution of binding energies) and fits many experimental systems at moderate coverages. The BET (Brunauer-Emmett-Teller) model extends Langmuir to multilayer adsorption by treating each adsorbed layer as a new surface for subsequent adsorption; the linearized BET equation allows extraction of monolayer capacity and hence surface area from nitrogen physisorption data -- the standard method for measuring surface areas of porous materials. The Temkin isotherm assumes the heat of adsorption decreases linearly with coverage due to adsorbate-adsorbate interactions. Selecting the right isotherm requires examining the shape of the experimental adsorption curve and understanding the physical assumptions each model encodes.

## How It's Best Learned
Fit the same experimental adsorption dataset (e.g., N2 on activated carbon) to Langmuir, Freundlich, and BET models. Compare the quality of fit, extract surface areas from the BET plot, and discuss which physical assumptions match the system.

## Common Misconceptions
- Treating the BET surface area as the "true" geometric surface area; BET assumes each adsorbed molecule occupies a fixed cross-sectional area and that multilayer formation is uniform, which breaks down in micropores.
- Using the Freundlich isotherm to predict saturation behavior; because theta = K*P^(1/n) has no saturation plateau, it is unreliable at high pressures where surface sites are nearly filled.
