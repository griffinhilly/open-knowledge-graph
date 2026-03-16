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

## Explainer

The Langmuir isotherm you already know makes elegant but restrictive assumptions: every adsorption site is identical, adsorbed molecules do not interact with each other, and only a single monolayer can form. These assumptions work beautifully for chemisorption on well-defined crystal faces at low coverage, but most real surfaces — porous catalysts, activated carbons, metal oxide powders — violate one or more of them. Advanced isotherms each relax a specific Langmuir assumption to better match experimental reality.

The **Freundlich isotherm** addresses surface heterogeneity. Real surfaces have a distribution of binding energies: some sites grip adsorbate molecules tightly while others hold them loosely. The Freundlich equation θ = KP^(1/n) captures this empirically — the exponent 1/n (where n > 1) means that as coverage increases, each additional molecule finds a progressively weaker site, so the adsorption curve flattens gradually rather than saturating sharply. On a log-log plot, Freundlich adsorption appears as a straight line, making it easy to fit. The limitation is fundamental: because the equation has no maximum, it cannot describe saturation. It works well at moderate coverages but fails at both very low and very high pressures.

The **BET (Brunauer–Emmett–Teller) model** tackles multilayer adsorption. When gas molecules physisorb on a surface, the first layer does not need to be complete before a second layer starts forming on top of it — particularly near the saturation pressure. BET extends Langmuir by treating each adsorbed layer as a fresh surface on which the next layer can adsorb. The key parameter is the BET constant C, which reflects how much more strongly molecules bind to the bare surface compared to subsequent layers. Large C values (strong surface interaction) produce a sharp "knee" in the isotherm at low pressure, while small C values give a more gradual curve. The practical payoff is enormous: by fitting experimental nitrogen adsorption data (typically at 77 K) to the linearized BET equation over the relative pressure range 0.05–0.35, you extract the monolayer capacity and multiply by the cross-sectional area of N₂ (0.162 nm²) to get the **BET surface area** — the standard metric reported for catalysts, adsorbents, and nanomaterials.

The **Temkin isotherm** takes yet another approach: it assumes the heat of adsorption decreases linearly with coverage due to repulsive adsorbate–adsorbate interactions. At low coverage, binding is strong; as the surface fills, lateral repulsions weaken binding progressively. This produces an isotherm where coverage varies linearly with the logarithm of pressure over the mid-coverage range. Temkin works well for chemisorption systems where adsorbate interactions are significant, such as hydrogen on metal catalysts.

Choosing the right isotherm is not arbitrary — it requires examining the shape of your experimental curve and understanding which physical assumptions match your system. A Type I isotherm (sharp rise then plateau) fits Langmuir. A Type II isotherm (gradual rise with an inflection) fits BET. A log-log plot that linearizes well suggests Freundlich. The isotherm you choose encodes a physical model, and extracting meaningful parameters (surface area, binding energy, heterogeneity) requires that the model's assumptions are at least approximately valid for your system.
