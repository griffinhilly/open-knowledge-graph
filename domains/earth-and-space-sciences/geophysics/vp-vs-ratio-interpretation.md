---
id: vp-vs-ratio-interpretation
title: Vp/Vs Ratio and Rock Properties
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: seismic-body-waves-p-and-s
  type: hard
- id: rock-forming-minerals
  type: soft
builds-toward:
- seismic-velocity-depth-models
tags:
- seismic
- rock-properties
- interpretation
stage: advanced
status: draft
---

# Vp/Vs Ratio and Rock Properties

## Core Idea
The Vp/Vs ratio (ratio of P-wave to S-wave velocity) is a sensitive indicator of rock composition, porosity, and fluid content. Dry rocks typically have Vp/Vs ratios around 1.7–1.8, while water-saturated rocks exceed 1.9. This ratio is independent of pressure and stress, making it a robust diagnostic tool in seismic interpretation and subsurface characterization.

## How It's Best Learned
Examine Vp/Vs values from well logs and compare them to core samples and laboratory measurements. Practice computing Vp/Vs from multichannel seismic data using seismic inversion techniques.

## Common Misconceptions
Vp/Vs uniquely determines rock type (multiple lithologies can have identical ratios). The ratio is constant across all rock types (it varies significantly with composition, porosity, and fluids).

## Explainer

From your study of P- and S-wave body waves, you know that these two wave types travel at different speeds determined by different elastic properties of the rock. **P-waves** depend on both the bulk modulus (resistance to compression) and shear modulus, while **S-waves** depend only on the shear modulus. The **Vp/Vs ratio** exploits this difference: because P- and S-waves respond differently to changes in rock properties, their ratio isolates information that neither velocity alone can provide.

For a simple elastic solid, the Vp/Vs ratio relates directly to **Poisson's ratio** (ν), a fundamental elastic constant: Vp/Vs = √((2 − 2ν)/(1 − 2ν)). For most common minerals and dry rocks, Poisson's ratio falls between 0.20 and 0.30, yielding Vp/Vs values of about 1.63 to 1.87. The theoretical minimum for a stable elastic solid is √2 ≈ 1.414 (when ν = 0), and values approaching infinity occur as ν approaches 0.5 — the condition of a fluid, which has zero shear modulus and therefore zero S-wave velocity. This is why the Vp/Vs ratio is so sensitive to fluids.

The practical diagnostic power shows up clearly in **fluid detection**. Dry sandstone might have Vp/Vs ≈ 1.6–1.7. Saturate the same rock with water, and Vp increases (because water's bulk modulus adds to the rock frame's resistance to compression) while Vs barely changes (because water has no shear strength), pushing Vp/Vs above 1.9 or even 2.0. Replace the water with gas, and Vp drops sharply (gas is highly compressible) while Vs remains nearly the same — Vp/Vs may fall below 1.6. This is why seismic interpreters in hydrocarbon exploration watch Vp/Vs closely: a zone with anomalously low Vp/Vs in a sandstone reservoir is a strong indicator of gas saturation.

Beyond fluids, Vp/Vs varies systematically with **lithology and composition**. Quartz-rich rocks (sandstones, quartzites) tend to have lower ratios (~1.6–1.7) because quartz has an unusually low Poisson's ratio. Carbonate rocks (limestones, dolomites) cluster around 1.8–1.9. Mafic igneous rocks and clay-rich shales push higher, often above 1.8. At crustal and mantle scales, Vp/Vs helps distinguish between felsic and mafic compositions — a valuable constraint when direct rock sampling is impossible. The key advantage of the ratio over absolute velocities is that it **cancels out the dominant effect of pressure**: both Vp and Vs increase with confining pressure at similar rates, so their ratio remains relatively stable, isolating the effects of composition and fluid content from the effect of burial depth.
