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

## Questions

```yaml
- question: "A researcher fits N₂ physisorption data showing a Type II isotherm to the Freundlich model, obtains an excellent fit over the 0.05–0.8 relative pressure range, and attempts to extract a surface area from the fitted parameters. What is the fundamental problem with this approach?"
  type: multiple-choice
  options:
    - "The Freundlich model is designed for multilayer adsorption and gives the same surface area as BET when properly fitted"
    - "The Freundlich equation has no monolayer capacity parameter and no saturation plateau, so it provides no physical basis for extracting surface area"
    - "The Freundlich model requires a log-log plot, which is incompatible with the relative pressure axis"
    - "Excellent fit quality over a wide pressure range validates the Freundlich model for surface area measurement"
  answer: 1
  explanation: "The Freundlich isotherm θ = KP^(1/n) is an empirical equation for surface heterogeneity. Because it has no maximum coverage, it cannot distinguish monolayer capacity from multilayer behavior — and without a physically meaningful monolayer capacity, there is nothing to multiply by a molecular cross-section. Surface area extraction requires a model (like BET) whose parameters directly encode the monolayer amount. Good fit quality in a limited pressure range only means Freundlich captures the slope, not that it describes the correct physics."

- question: "A microporous zeolite and a mesoporous silica are both characterized by N₂ BET at 77 K. A student claims the reported BET surface areas reflect the true geometric surface area of both materials. Which challenge is most specific to the microporous zeolite?"
  type: multiple-choice
  options:
    - "The BET constant C is undefined for microporous materials, making the linearization invalid"
    - "BET assumes uniform multilayer formation on open surfaces, but in pores narrower than ~2 nm the first and second layers overlap, violating the multilayer assumption and making BET overestimate the effective surface area"
    - "The N₂ cross-sectional area of 0.162 nm² is only calibrated for mesoporous materials"
    - "BET cannot be applied below a relative pressure of 0.35, which is the entire accessible range for micropores"
  answer: 1
  explanation: "BET theory assumes each adsorbed layer provides a fresh open surface for the next — a reasonable picture for flat or gently curved surfaces. In micropores (width < 2 nm), opposing pore walls are so close that adsorbate-adsorbate interactions span the entire pore, the distinct-layer picture breaks down, and the BET equation extracts an 'apparent' surface area that can be substantially higher than the true geometric area. Mesoporous and macroporous materials are better candidates for BET analysis, though even there the fixed cross-section assumption introduces some error."

- question: "The Freundlich isotherm can be used to predict adsorption behavior at very high pressures where surface coverage approaches saturation."
  type: true-false
  answer: false
  explanation: "Because the Freundlich equation θ = KP^(1/n) has no plateau — coverage increases indefinitely as pressure rises — it cannot describe saturation. At high pressures, when the surface is nearly filled, the Langmuir or BET model is needed. The Freundlich isotherm is reliable only at moderate coverages where the absence of a saturation limit is not physically absurd."

- question: "A Type II adsorption isotherm, characterized by an inflection at moderate relative pressures followed by a steep rise near the saturation pressure, indicates that multiple adsorbed layers are forming simultaneously rather than completing one layer before the next begins."
  type: true-false
  answer: true
  explanation: "BET theory, which describes Type II isotherms, explicitly allows the second and higher layers to begin forming before the first layer is complete. This co-existence of partial layers at different heights is why the isotherm rises gradually before the steep upturn near saturation. The inflection point marks roughly where the average number of adsorbed layers transitions from less than to greater than one."

- question: "Explain why selecting an adsorption isotherm model is not arbitrary, and what experimental evidence you would use to choose between Langmuir, Freundlich, and BET for a new adsorbent."
  type: short-answer
  answer: "Each isotherm encodes specific physical assumptions: Langmuir assumes monolayer adsorption on identical, non-interacting sites; Freundlich captures surface heterogeneity without a saturation limit; BET accounts for multilayer formation. To choose, examine the shape of the experimental adsorption curve — a sharp rise to a plateau (Type I) fits Langmuir; a gradual rise with an inflection (Type II) fits BET; a curve that linearizes on a log-log plot at moderate coverages may fit Freundlich. Additional checks include testing whether the BET linear region falls in the 0.05–0.35 relative pressure range and whether a log-log plot of the data is straight."
  explanation: "Isotherm selection is model selection — and models are validated by the physical assumptions they encode, not just goodness of fit. A Freundlich fit at moderate pressures may look good even for a Langmuir-type surface, but extrapolating to high pressures will fail catastrophically. BET is the standard for surface area measurement precisely because its physical assumptions (multilayer formation with a fixed monolayer capacity) provide an anchor for quantitative surface area extraction. The shape of the isotherm is the primary diagnostic tool."
```

## Explainer

The Langmuir isotherm you already know makes elegant but restrictive assumptions: every adsorption site is identical, adsorbed molecules do not interact with each other, and only a single monolayer can form. These assumptions work beautifully for chemisorption on well-defined crystal faces at low coverage, but most real surfaces — porous catalysts, activated carbons, metal oxide powders — violate one or more of them. Advanced isotherms each relax a specific Langmuir assumption to better match experimental reality.

The **Freundlich isotherm** addresses surface heterogeneity. Real surfaces have a distribution of binding energies: some sites grip adsorbate molecules tightly while others hold them loosely. The Freundlich equation θ = KP^(1/n) captures this empirically — the exponent 1/n (where n > 1) means that as coverage increases, each additional molecule finds a progressively weaker site, so the adsorption curve flattens gradually rather than saturating sharply. On a log-log plot, Freundlich adsorption appears as a straight line, making it easy to fit. The limitation is fundamental: because the equation has no maximum, it cannot describe saturation. It works well at moderate coverages but fails at both very low and very high pressures.

The **BET (Brunauer–Emmett–Teller) model** tackles multilayer adsorption. When gas molecules physisorb on a surface, the first layer does not need to be complete before a second layer starts forming on top of it — particularly near the saturation pressure. BET extends Langmuir by treating each adsorbed layer as a fresh surface on which the next layer can adsorb. The key parameter is the BET constant C, which reflects how much more strongly molecules bind to the bare surface compared to subsequent layers. Large C values (strong surface interaction) produce a sharp "knee" in the isotherm at low pressure, while small C values give a more gradual curve. The practical payoff is enormous: by fitting experimental nitrogen adsorption data (typically at 77 K) to the linearized BET equation over the relative pressure range 0.05–0.35, you extract the monolayer capacity and multiply by the cross-sectional area of N₂ (0.162 nm²) to get the **BET surface area** — the standard metric reported for catalysts, adsorbents, and nanomaterials.

The **Temkin isotherm** takes yet another approach: it assumes the heat of adsorption decreases linearly with coverage due to repulsive adsorbate–adsorbate interactions. At low coverage, binding is strong; as the surface fills, lateral repulsions weaken binding progressively. This produces an isotherm where coverage varies linearly with the logarithm of pressure over the mid-coverage range. Temkin works well for chemisorption systems where adsorbate interactions are significant, such as hydrogen on metal catalysts.

Choosing the right isotherm is not arbitrary — it requires examining the shape of your experimental curve and understanding which physical assumptions match your system. A Type I isotherm (sharp rise then plateau) fits Langmuir. A Type II isotherm (gradual rise with an inflection) fits BET. A log-log plot that linearizes well suggests Freundlich. The isotherm you choose encodes a physical model, and extracting meaningful parameters (surface area, binding energy, heterogeneity) requires that the model's assumptions are at least approximately valid for your system.
