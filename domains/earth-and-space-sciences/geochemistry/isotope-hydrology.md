---
id: isotope-hydrology
title: Isotope Hydrology
domain: earth-and-space-sciences
course: geochemistry
prerequisites:
- id: oxygen-isotopes-geochemistry
  type: hard
- id: hydrogen-nitrogen-isotopes
  type: hard
- id: aqueous-geochemistry
  type: soft
builds-toward: []
tags:
- isotope-hydrology
- groundwater
- water-tracing
- GMWL
- tritium
stage: expert
status: validated
---

# Isotope Hydrology

## Core Idea
Isotope hydrology uses the natural variations in water isotopes (delta-18O, delta-D) and dissolved solute isotopes (tritium, 14C, 36Cl, 87Sr/86Sr, delta-34S, delta-15N) to trace water sources, determine groundwater recharge conditions, estimate residence times, and track mixing and contamination. The Global Meteoric Water Line (delta-D = 8*delta-18O + 10) provides the baseline against which all water sources are compared. Local meteoric water lines may differ in slope and intercept, reflecting regional climate. Groundwater isotopes preserve the climatic conditions at the time of recharge (paleo-recharge from glacial periods has distinctly lighter isotopic signatures), while radioactive tracers (tritium, 14C) provide residence time estimates ranging from decades (tritium) to tens of thousands of years (14C). These tools are essential for water resource management, contaminant tracking, and understanding groundwater-surface water interactions.

## Questions

```yaml
- question: "Groundwater samples from a deep confined aquifer in the Sahara have delta-18O values of -10 per mil, while modern local precipitation is -3 per mil. What does this isotopic difference indicate?"
  type: multiple-choice
  options:
    - "The groundwater has been contaminated by industrial chemicals"
    - "The groundwater was recharged during a cooler climate period (likely the last glacial period or a pluvial phase) when precipitation was isotopically lighter; the aquifer has preserved this paleo-recharge signal because the confined system has negligible modern recharge"
    - "The groundwater has evaporated underground"
    - "The isotopic difference is caused by mineral dissolution"
  answer: 1
  explanation: "The 7 per mil offset from modern precipitation is too large to explain by within-aquifer processes. During the last glacial period and Saharan pluvial phases, cooler temperatures and different moisture sources produced isotopically lighter precipitation (more negative delta-18O). Deep confined aquifers can preserve this signal for tens of thousands of years because they receive no modern recharge to dilute the paleo-water. This water is a non-renewable resource being mined faster than it can be replenished."

- question: "Tritium (3H, half-life 12.32 years) is useful for determining whether groundwater was recharged before or after 1953."
  type: true-false
  answer: true
  explanation: "Atmospheric nuclear weapons testing (1953-1963) injected massive amounts of tritium into the atmosphere, creating a 'bomb peak' in precipitation tritium that reached 1000+ TU (tritium units) in 1963 northern hemisphere rain versus natural background of ~5 TU. Groundwater recharged before 1953 has had 4+ half-lives of decay and contains essentially no tritium (<0.5 TU). Water recharged during or after the bomb peak contains measurable tritium. The presence or absence of tritium is therefore a binary indicator of modern (post-1953) versus pre-modern recharge."

- question: "Explain how carbon-14 dating of groundwater differs from carbon-14 dating of organic material, and what complications arise."
  type: short-answer
  answer: "In organic material, 14C is fixed at atmospheric levels during life and decays after death. In groundwater, dissolved inorganic carbon (DIC) acquires 14C from soil CO2 during recharge, but the initial 14C activity is diluted by dissolving 14C-dead carbonate minerals in the aquifer. If uncorrected, this dilution makes groundwater appear older than it actually is. Various correction models (Vogel, Tamers, Pearson, NETPATH) estimate the initial 14C activity by accounting for carbonate dissolution, isotope exchange, and geochemical evolution along the flow path. Additional complications include mixing of waters of different ages, methanogenesis (adding dead carbon), and diffusion from the rock matrix. Despite these complications, 14C is the primary tool for dating groundwater in the 1,000-40,000 year range."
  explanation: "The key difference is that groundwater DIC does not start at 100 pMC like organic carbon -- it starts lower due to carbonate dissolution, requiring geochemical corrections to determine the true residence time."
```

## Explainer

Isotope hydrology applies the well-characterized isotopic behavior of water and dissolved species to answer practical questions about water resources: where does the water come from, how old is it, and how does it move through the subsurface? These questions are increasingly urgent as groundwater depletion and contamination challenge water security worldwide.

The delta-18O and delta-D of water are the primary source tracers. Because the isotopic composition of precipitation varies systematically with latitude, altitude, continentality, temperature, and season, a groundwater sample's isotopic signature fingerprints its recharge location and climatic conditions. A Mediterranean aquifer recharged by winter storms has different isotopic composition than one recharged by summer convective rainfall. Mountain-front recharge can be distinguished from valley-floor recharge by the altitude effect. Evaporation before or during recharge shifts samples below the GMWL along a characteristic evaporation line, detectable in isotopic space.

Groundwater age dating uses radioactive tracers with different half-lives to cover different timescales. Tritium (half-life 12.3 years) identifies very recent recharge (post-1950s). Tritium-helium-3 dating measures the ingrowth of 3He from tritium decay, giving a precise apparent age for young groundwater. Krypton-85 (half-life 10.7 years) provides independent confirmation. Carbon-14 (half-life 5,730 years) dates groundwater up to ~40,000 years old. Chlorine-36 (half-life 301,000 years) and krypton-81 (half-life 229,000 years) extend the range to hundreds of thousands of years. Each tracer has distinct geochemical complications, and multiple tracers applied to the same system provide cross-checks and constrain mixing.

Modern isotope hydrology increasingly combines conservative tracers (18O, D, noble gases) with reactive tracers (87Sr/86Sr, delta-34S, delta-15N, delta-13C-DIC) to simultaneously determine water sources and the geochemical processes affecting water quality along flow paths. Strontium isotope ratios identify water-rock interaction with specific lithologies. Sulfur isotopes distinguish sulfate from atmospheric deposition, evaporite dissolution, and sulfide oxidation. Nitrogen isotopes identify pollution sources. This multi-isotope approach transforms groundwater investigations from simple flow characterization to comprehensive geochemical system understanding.
