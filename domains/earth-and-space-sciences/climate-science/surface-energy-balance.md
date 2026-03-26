---
id: surface-energy-balance
title: Surface Energy Balance and Budget
domain: earth-and-space-sciences
course: climate-science
prerequisites:
- id: energy-balance-models
  type: hard
- id: solar-radiation-and-earth-energy-balance
  type: hard
- id: heat-transfer-radiation
  type: soft
builds-toward:
- forcing-feedback-framework
- ocean-atmosphere-interactions
tags:
- surface-fluxes
- energy-balance
- radiative-budget
- land-surface
stage: advanced
status: validated
---

# Surface Energy Balance and Budget

## Core Idea
The surface energy budget partitions incoming solar radiation into reflected shortwave radiation, latent heat flux, sensible heat flux, and ground heat storage. This balance varies regionally and temporally, determining surface temperature and driving local climate. Changes in surface properties or atmospheric composition alter the balance, making this a critical link between atmospheric forcing and climate response.

## Questions

```yaml
- question: "Two regions receive the same incoming solar radiation. A tropical rainforest has a Bowen ratio of 0.3; a dry desert has a Bowen ratio of 8. Which surface will have the higher daytime air temperature near the surface, and why?"
  type: multiple-choice
  options:
    - "The rainforest, because dense vegetation absorbs more solar radiation"
    - "The desert, because the high Bowen ratio means most available energy goes into sensible heat flux warming the air"
    - "They will reach the same temperature because they receive identical solar input"
    - "The rainforest, because high latent heat flux warms the air above through condensation"
  answer: 1
  explanation: "The Bowen ratio (sensible heat / latent heat) determines how available energy is partitioned. A high Bowen ratio (desert = 8) means almost all energy goes into directly warming the air and surface through sensible heat flux. A low Bowen ratio (rainforest = 0.3) means most energy goes into evapotranspiration — cooling the surface as water changes phase. Same solar input, very different temperatures. This is why humid tropical forests stay cooler than deserts at the same latitude, and why irrigating a crop field dramatically reduces local air temperature."

- question: "A tropical region undergoes widespread deforestation, replacing rainforest with bare soil and pasture. Holding atmospheric composition constant, what is the most direct effect on the surface energy balance?"
  type: multiple-choice
  options:
    - "Increased latent heat flux as the bare soil releases stored groundwater"
    - "Decreased absorbed solar radiation because bare soil reflects more sunlight"
    - "A shift from latent heat flux to sensible heat flux, warming the surface and drying the boundary layer"
    - "Increased ground heat flux as the exposed soil conducts more energy downward"
  answer: 2
  explanation: "Forests transpire enormous quantities of water, directing available energy into latent heat flux. Removing forest eliminates this evapotranspiration pathway. The same net radiation is now partitioned differently: more goes into sensible heat (warming the air), less into latent heat. Surface temperatures rise, the boundary layer dries, and rainfall patterns can shift as less water is returned to the atmosphere. This is the energy balance mechanism behind deforestation-driven regional warming, separate from any greenhouse gas effects."

- question: "A well-watered agricultural field in summer typically has a Bowen ratio less than 1, meaning latent heat flux exceeds sensible heat flux."
  type: true-false
  answer: true
  explanation: "When water is abundantly available, evapotranspiration dominates the energy partition. Crops transpire heavily, channeling most available energy into vaporizing water rather than warming the air. Bowen ratios below 0.5 are common for irrigated fields in summer. This is why agricultural regions tend to be cooler and more humid than nearby dry or urbanized areas receiving the same solar radiation. Contrast this with a harvested field or desert where virtually all energy becomes sensible heat."

- question: "Albedo affects mainly how much incoming solar radiation is reflected and has no influence on how the remaining absorbed energy is partitioned into sensible heat, latent heat, and ground heat fluxes."
  type: true-false
  answer: false
  explanation: "Albedo determines the absorbed shortwave radiation — the first term in the surface energy budget. This absorbed radiation combines with net longwave terms to produce the 'available energy' (net radiation) that is then partitioned among sensible heat, latent heat, and ground fluxes. A surface with high albedo (e.g., fresh snow: 80-90%) absorbs little energy, so *all three* of the outgoing flux terms are constrained to be small — the budget must balance. Albedo thus sets the total energy pie, not just the reflection slice."

- question: "Why do urban areas tend to be warmer than surrounding rural areas (the urban heat island effect)? Explain using the surface energy balance framework."
  type: short-answer
  answer: "Urban surfaces (concrete, asphalt) differ from rural vegetation in three key ways. First, low albedo means urban surfaces absorb more solar radiation, increasing available energy. Second, impervious surfaces have negligible latent heat flux — no vegetation to transpire, and water runs off rather than evaporating — so the Bowen ratio is very high (most energy becomes sensible heat). Third, urban surfaces have low thermal conductivity relative to their heat capacity, storing heat during the day and releasing it slowly at night. The result is that more energy enters the urban surface, and more of that energy goes into warming the air rather than evaporating water, producing the characteristic heat island."
  explanation: "This illustrates why surface energy balance is not just an academic framework — it explains real policy-relevant phenomena. Urban greening (parks, green roofs, street trees) reduces heat islands by restoring latent heat flux. Cool roofs (high albedo coatings) reduce available energy. Both strategies target different terms in the same energy budget equation. Understanding the budget lets you quantify the expected benefit of each intervention."
```

## Explainer

From your work on energy balance models, you know that the Earth system must balance incoming solar energy against outgoing energy to maintain a stable temperature. The **surface energy balance** zooms in on exactly what happens to that energy once it reaches the ground. Think of the surface as an accountant: every watt of energy arriving must be accounted for — reflected, radiated back, used to evaporate water, conducted into the ground, or used to warm the air above. The balance sheet at any location and time determines the local surface temperature.

The incoming side is dominated by **net radiation** — the difference between absorbed solar (shortwave) radiation and emitted terrestrial (longwave) radiation. A fresh snow surface might reflect 80-90% of incoming sunlight, leaving little energy to warm anything, while a dark ocean surface absorbs over 90%. This is why albedo matters so much. The net radiation that remains after reflection and longwave emission is called the **available energy**, and it must be partitioned among three main outgoing terms: sensible heat flux, latent heat flux, and ground heat flux.

**Sensible heat flux** is the direct warming of the air above the surface through conduction and convection — you can feel this as the shimmer of hot air rising from sun-baked pavement. **Latent heat flux** is energy consumed by evaporation or transpiration from plants; the energy is not lost but stored in water vapor and released later when the vapor condenses (this is why humid tropical forests stay cooler than dry deserts at the same latitude, even with similar solar input). **Ground heat flux** is energy conducted downward into the soil or rock, warming the subsurface. The ratio between sensible and latent heat flux is captured by the **Bowen ratio** — a desert might have a Bowen ratio above 5 (almost all sensible heat), while a well-watered cropland might be below 0.5 (latent heat dominates).

This partitioning has profound consequences for climate. Deforestation replaces transpiring trees with bare soil, shifting energy from latent to sensible heat flux — the surface warms, the boundary layer dries, and local rainfall patterns can change. Urbanization replaces vegetated surfaces with concrete and asphalt, dramatically increasing sensible heat flux and creating urban heat islands. Changes in atmospheric greenhouse gas concentrations alter the longwave radiation terms, increasing the net radiation available at the surface. Understanding these feedbacks — how surface changes propagate through the energy budget into temperature and circulation changes — is why the surface energy balance sits at the heart of climate science, connecting radiative forcing to the climate response you will study next.
