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
stage: expert
status: validated
---

# Mantle Rheology and Viscosity

## Core Idea
Mantle rocks deform by dislocation and diffusion creep, with viscosity temperature-dependent and sensitive to grain size and water content. Mantle viscosity (10²¹–10²³ Pa·s) governs convection rates and plate-driving forces.

## Questions

```yaml
- question: "Scandinavia is currently rising at several millimeters per year, thousands of years after the last ice sheets melted. What does this post-glacial rebound tell us about the mantle?"
  type: multiple-choice
  options:
    - "The mantle is liquid below the lithosphere and is slowly refilling cavities left by the melted ice, like water filling a bowl."
    - "Mantle rock, though solid, deforms as a highly viscous material over geological timescales; the rebound rate and pattern directly constrain mantle viscosity at depth."
    - "The Earth's crust is elastically rebounding on its own, independent of any mantle flow; no mantle deformation is required."
    - "Post-glacial rebound reflects the asthenosphere rising as a melt layer, since asthenosphere temperatures are above the solidus."
  answer: 1
  explanation: "Post-glacial rebound is one of the most important direct measurements of mantle viscosity. The mantle is solid — not liquid — but it deforms by solid-state creep on geological timescales, behaving as an extremely viscous fluid. The rate at which Scandinavia rises (and the pattern of sea-level change across surrounding regions) provides a quantitative record of mantle flow in response to a known load change (the melting ice sheets). By fitting models of viscous mantle flow to these observations, geophysicists directly infer viscosity at different depths — this is how we know asthenospheric viscosity (~10¹⁹–10²⁰ Pa·s) and lower mantle viscosity (~10²²–10²³ Pa·s)."

- question: "The upper mantle is less viscous than the lower mantle despite being at lower pressure. What primarily explains this contrast?"
  type: multiple-choice
  options:
    - "The upper mantle contains elevated water concentrations that weaken crystal bonds through hydrolytic weakening, reducing viscosity by several orders of magnitude."
    - "Temperature — the Arrhenius dependence of viscosity on temperature means the upper mantle, being closer to its solidus, is far less viscous than the cooler (relative to its melting point) lower mantle."
    - "Upper mantle minerals have smaller grain sizes that favor diffusion creep, while lower mantle minerals have larger grains that favor dislocation creep."
    - "The upper mantle deforms elastically on short timescales, which reduces its apparent long-term viscosity."
  answer: 1
  explanation: "Temperature is the dominant control on mantle viscosity through the Arrhenius relationship (η ∝ exp(E*/RT)). The upper mantle (asthenosphere) is close to its melting point — homologous temperature T/Tₘ is high — making its viscosity very low. The lower mantle is far from its melting point at those pressures, making it much stiffer despite higher absolute temperatures. Water content and grain size are secondary modulators, but temperature explains the primary viscosity stratification. A 100°C temperature change can shift viscosity by an order of magnitude, so even modest temperature contrasts create dramatic viscosity contrasts."

- question: "Mantle rocks are solid, but they deform as viscous fluids on geological timescales through creep mechanisms such as diffusion creep and dislocation creep."
  type: true-false
  answer: true
  explanation: "This apparent paradox is central to understanding the mantle. On short timescales (seconds to thousands of years), the mantle transmits seismic S-waves — only solids support shear waves, confirming the mantle is solid. But on geological timescales (millions to billions of years), the same solid rock deforms continuously through thermally activated atomic-scale processes (diffusion or dislocation motion). The distinction is timescale: rock is elastic-solid at seismic frequencies, but viscous-fluid at the million-year frequencies of mantle convection. This dual behavior is what enables plate tectonics."

- question: "A temperature increase of 100°C roughly doubles mantle viscosity because higher temperatures strengthen atomic bonds in silicate minerals."
  type: true-false
  answer: false
  explanation: "This is the opposite of what the Arrhenius relationship predicts. Higher temperature dramatically DECREASES viscosity — a 100°C increase can reduce mantle viscosity by an order of magnitude (factor of 10), not double it. The physical reason is that higher temperatures provide more thermal energy to overcome activation barriers for atomic diffusion and dislocation motion, accelerating creep. This exponential temperature-viscosity relationship is why hot mantle upwellings flow much faster than cold downgoing slabs, and why the shallow asthenosphere (hot relative to its melting point) is far less viscous than the cooler lithosphere above it."

- question: "Why is the Arrhenius temperature dependence of mantle viscosity so important for understanding plate tectonics and mantle convection?"
  type: short-answer
  answer: "Because viscosity controls how fast rock flows, and the Arrhenius relationship makes viscosity exquisitely sensitive to temperature — an order-of-magnitude change per ~100–150°C. This creates a strong self-organizing feedback in the mantle: hot upwellings are less viscous, so they rise faster and spread more easily; cold downgoing slabs are far more viscous (stiffer), so they resist deformation and transmit plate stresses efficiently. The dramatic viscosity contrast between the hot asthenosphere (~10²⁰ Pa·s) and the cold lithosphere (~10²³ Pa·s or higher) is what allows the asthenosphere to flow and decouple from the overlying plates, making lateral plate motion possible. Without temperature-dependent viscosity, the mantle would flow more uniformly and the lithospheric plate structure of plate tectonics would not exist in its current form."
  explanation: "The Arrhenius relationship links temperature to viscosity through the physics of thermally activated creep: atomic-scale motion requires overcoming an energy barrier, and higher temperature provides more thermal energy to surmount those barriers. Because the temperature range across the mantle spans hundreds of degrees (asthenosphere vs. lower mantle), and the activation energy is large, the resulting viscosity spans 3–4 orders of magnitude. This viscosity structure — weak asthenosphere, stiff lithosphere — is the mechanical foundation of plate tectonics. Changes in mantle temperature (e.g., through hotspot plumes or subducting slabs) locally alter this viscosity structure, explaining regional variations in plate behavior."
```

## Explainer

From rock rheology, you know that materials can deform elastically, plastically, or viscously depending on stress, temperature, and strain rate. From mantle convection and dynamics, you know that the mantle flows on geologic timescales, driving plate tectonics. Mantle rheology connects these ideas by asking: exactly how does rock flow at mantle conditions, and what controls the rate? The answer determines everything from how fast plates move to how the Earth responds to ice-sheet loading.

At the temperatures and pressures of the mantle (roughly 1000–4000°C, 1–140 GPa), silicate minerals deform by two primary mechanisms. **Diffusion creep** involves atoms migrating through the crystal lattice or along grain boundaries in response to differential stress. It dominates at low stress and small grain sizes, and its strain rate is linearly proportional to stress (Newtonian viscosity). **Dislocation creep** involves the movement of line defects (dislocations) through the crystal lattice. It dominates at higher stress and larger grain sizes, and its strain rate depends on stress raised to a power (typically n ≈ 3–3.5), making it strongly non-Newtonian — doubling the stress increases the strain rate roughly eightfold. The upper mantle likely deforms primarily by dislocation creep, evidenced by the seismic anisotropy that dislocation motion produces through preferential alignment of olivine crystals.

The single most important control on mantle viscosity is **temperature**. Viscosity depends exponentially on temperature through an Arrhenius relationship: η ∝ exp(E*/RT), where E* is the activation energy, R is the gas constant, and T is absolute temperature. A temperature increase of just 100°C can decrease viscosity by an order of magnitude. This extreme sensitivity creates a strong feedback with mantle convection — hot upwellings are less viscous and rise faster, while cold downgoing slabs are stiffer and resist deformation. Beyond temperature, **water content** dramatically reduces viscosity even at parts-per-million concentrations by weakening crystal bonds and enhancing dislocation mobility (the "hydrolytic weakening" effect). **Grain size** matters because diffusion creep rate scales inversely with grain size squared or cubed — finer-grained rock flows more easily by diffusion.

The effective viscosity of the mantle spans roughly two orders of magnitude, from about 10¹⁹–10²⁰ Pa·s in the asthenosphere (the low-viscosity layer beneath the lithosphere where temperatures are near the solidus) to 10²²–10²³ Pa·s in the lower mantle. This viscosity structure is constrained by observations of **post-glacial rebound** — the ongoing uplift of Scandinavia and Canada after the last ice sheets melted — which provides a direct measurement of how fast the mantle flows in response to a known load change. The rate of rebound and the pattern of relative sea-level change are sensitive to viscosity at different depths, making glacial isostatic adjustment one of the most powerful constraints on the mantle's rheological profile. This viscosity structure, in turn, sets the timescale of mantle convection, the coupling between plates and the underlying mantle, and ultimately the vigor of Earth's internal heat engine.
