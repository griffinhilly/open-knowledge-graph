---
id: salinity-composition-seawater
title: Salinity and Seawater Composition
domain: earth-and-space-sciences
course: oceanography
prerequisites:
- id: colligative-properties
  type: soft
builds-toward:
  - ocean-carbonate-system-buffering
  - thermohaline-circulation
tags:
- salinity
- dissolved-ions
- seawater
- chemical-composition
stage: formal-systems
status: validated
---
# Salinity and Seawater Composition

## Core Idea
Seawater contains dissolved salts—primarily sodium, chloride, magnesium, and sulfate—in roughly constant proportions, totaling approximately 35 parts per thousand (ppt). Salinity variations between regions affect density structure, create stable or unstable stratification, and influence biological productivity and chemical cycling.

## Questions

```yaml
- question: "An oceanographer measures only chloride concentration in a seawater sample and confidently reports total salinity. How is a single ion measurement sufficient?"
  type: multiple-choice
  options:
    - "Chloride dominates seawater composition so completely that other ions contribute negligibly to total salinity"
    - "The principle of constant proportions means major ion ratios are fixed ocean-wide, so one ion's concentration determines total salinity"
    - "She is using a regional calibration table specific to that ocean basin where the composition is locally homogeneous"
    - "Modern instruments measure chloride but automatically calculate total salinity from factory-set universal constants"
  answer: 1
  explanation: "Marcet's principle (constant proportions) holds because the residence times of major ions (millions of years for Na⁺ and Cl⁻) far exceed the ocean's mixing time (~1,000 years), so the ocean equilibrates its composition many times over. The ratio between Cl⁻ and total dissolved solids is therefore nearly constant everywhere, allowing one measurement to stand in for all. Option 0 is a misconception: chloride constitutes about 55% of dissolved material, meaning the other ions are collectively ~45% — not negligible. It is the *constancy of ratios*, not the dominance of chloride, that makes the calculation valid."

- question: "When seawater in polar regions freezes to form sea ice, what happens to the dissolved ions?"
  type: multiple-choice
  options:
    - "They are incorporated into the ice crystal lattice alongside water molecules, preserving the original salinity"
    - "They are excluded from the ice and concentrated in the remaining liquid water, forming cold dense brine"
    - "They precipitate as solid mineral crystals and sink to the seafloor during the freezing event"
    - "They are released as gas into the atmosphere as the water molecules change phase"
  answer: 1
  explanation: "Ice crystal formation requires a pure water lattice; dissolved ions are geometrically and energetically incompatible with the crystal structure and are expelled during freezing — a process called brine rejection. The remaining liquid water becomes cold and hypersaline (dense brine), which sinks and contributes to deep water mass formation (e.g., Antarctic Bottom Water). Option 0 is the most common misconception and explains why melting old sea ice produces nearly fresh, drinkable water — the salt was rejected long ago."

- question: "Surface salinity tends to be highest in the subtropical gyres (around 20–30° latitude) and lower both at the equator and at high latitudes."
  type: true-false
  answer: true
  explanation: "Surface salinity is governed by the local freshwater balance: evaporation removes fresh water (concentrating salt) while precipitation and river runoff add fresh water (diluting salt). Subtropical gyres sit beneath persistent high-pressure systems with strong solar heating and little precipitation — evaporation dominates, driving salinity to 36–37 ppt. The equatorial zone receives intense tropical rainfall, freshening the surface layer. High latitudes receive precipitation and input from melting ice. The result is a latitudinal salinity pattern with subtropical maxima, not a uniform distribution."

- question: "When seawater freezes to form sea ice, the resulting ice has approximately the same salinity as the parent seawater it formed from."
  type: true-false
  answer: false
  explanation: "Sea ice is nearly fresh — far less saline than the parent seawater. Dissolved ions cannot fit into the ice crystal lattice and are expelled (brine rejection), leaving the ice with only minor salt inclusions from trapped brine pockets, which themselves drain over time as the ice ages. This is why polar explorers historically melted old sea ice for drinking water. The expelled salt remains in the liquid water, raising its salinity and density — exactly the mechanism that drives dense brine to the ocean floor and initiates deep circulation."

- question: "Explain why the principle of constant proportions holds for major seawater ions, and what oceanographic measurements this principle makes possible."
  type: short-answer
  answer: "The principle holds because the residence times of major ions in the ocean (millions of years for Na⁺ and Cl⁻, thousands for Ca²⁺) are orders of magnitude longer than the ocean's mixing time (~1,000 years). The ocean circulates and homogenizes its composition many times over before ionic ratios can drift, so any local addition (rivers, hydrothermal vents) or removal (burial, evaporite formation) is quickly smoothed out. This constancy enables salinity measurement by proxy: rather than measuring every ion individually, oceanographers measure chlorinity or electrical conductivity — both quick and precise — and calculate total salinity from known fixed ratios. This simplification underlies all seawater density calculations, which in turn drive models of ocean stratification and circulation."
  explanation: "The practical implication is enormous: a single conductivity sensor on a profiling float can generate continuous salinity data at every depth. Without the constancy of proportions, every salinity determination would require separate analysis of multiple ions — impractical for autonomous instruments. The principle also means that historical chlorinity measurements made before conductivity sensors can be converted to modern salinity values, giving oceanographers a century of comparable data."
```

## Explainer

If you have studied colligative properties, you know that dissolved solutes change the physical behavior of a solvent — lowering freezing points, raising boiling points, and increasing density. Seawater is the most consequential example of this on Earth: the roughly 35 grams of dissolved salts in every kilogram of seawater fundamentally alter its density, freezing point, and ability to absorb gases, with cascading effects on ocean circulation, climate, and life.

The composition of seawater is remarkably uniform. About 86% of the dissolved material is sodium chloride, with the remainder dominated by magnesium, sulfate, calcium, and potassium ions. This consistency is described by the **principle of constant proportions** (Marcet's principle): while total salinity varies from place to place, the ratios between major ions remain nearly fixed. This constancy exists because the residence times of these ions in the ocean — millions of years for sodium and chloride — are far longer than the ocean's mixing time of roughly 1,000 years. The ocean mixes itself thoroughly many times over before the composition can drift. This means that measuring just one property, typically chloride concentration or electrical conductivity, allows you to calculate total **salinity** with high accuracy.

Despite the constant proportions of major ions, total salinity itself varies significantly across the ocean. Surface salinity is highest in the subtropical gyres (around 36–37 ppt) where evaporation exceeds precipitation, and lowest near the equator and at high latitudes (as low as 30–33 ppt) where rainfall and river runoff dilute the surface water. These patterns create horizontal and vertical salinity gradients. Where the surface is freshened by rain or meltwater, a **halocline** forms — a layer across which salinity increases rapidly with depth. This halocline contributes to density stratification because fresher water is lighter than saltier water at the same temperature.

Salinity's influence on density is the foundation of much of deep ocean circulation. In polar regions, cooling alone increases density, but the formation of sea ice amplifies the effect dramatically: when seawater freezes, salt is excluded from the ice crystal lattice and rejected into the surrounding water, creating cold, extremely salty **brine** that is dense enough to sink to the ocean floor. This process of **brine rejection** is one of the primary mechanisms driving the formation of deep water masses like Antarctic Bottom Water. Salinity also affects the ocean's capacity to dissolve gases — saltier water holds less dissolved oxygen and CO₂ — and influences the osmotic environment that marine organisms must regulate. Understanding salinity and seawater composition is therefore a prerequisite for nearly every other topic in physical and chemical oceanography, from stratification and circulation to the carbonate system and biological productivity.
