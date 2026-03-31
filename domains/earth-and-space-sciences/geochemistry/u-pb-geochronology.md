---
id: u-pb-geochronology
title: U-Pb Geochronology
domain: earth-and-space-sciences
course: geochemistry
prerequisites:
- id: geochemical-thermodynamics
  type: soft
- id: trace-element-geochemistry
  type: soft
builds-toward:
- crustal-evolution-geochemistry
- cosmochemistry
tags:
- U-Pb
- zircon
- geochronology
- concordia
stage: expert
status: validated
---

# U-Pb Geochronology

## Core Idea
The U-Pb system exploits two independent decay chains -- 238U to 206Pb (half-life 4.47 Gyr) and 235U to 207Pb (half-life 0.704 Gyr) -- providing a built-in cross-check on age reliability. Zircon (ZrSiO4) is the premier U-Pb mineral because it incorporates U but excludes Pb during crystallization, and it is physically and chemically extremely resistant. On a concordia diagram (206Pb*/238U vs 207Pb*/235U, where * denotes radiogenic), undisturbed samples plot on the concordia curve at a position corresponding to their age. Lead loss displaces analyses below concordia along discordia lines whose upper intercept gives the crystallization age and lower intercept dates the Pb-loss event. U-Pb zircon geochronology is the gold standard for determining crystallization ages from the Hadean (>4.0 Ga) to the Cenozoic (~1 Ma), with precisions reaching 0.1%.

## Questions

```yaml
- question: "Three zircon analyses from a granite plot below the concordia curve but define a linear discordia line with an upper intercept at 2.7 Ga and a lower intercept at 0.5 Ga. How are these intercepts interpreted?"
  type: multiple-choice
  options:
    - "The granite formed at 0.5 Ga and was contaminated at 2.7 Ga"
    - "The zircons crystallized at 2.7 Ga and experienced partial Pb loss during a thermal event at 0.5 Ga; the upper intercept gives crystallization age and the lower intercept dates the disturbance"
    - "The zircons are a mixture of 2.7 Ga and 0.5 Ga populations"
    - "The concordia diagram is unreliable for ages greater than 1 Ga"
  answer: 1
  explanation: "Undisturbed zircons plot on concordia. Partial Pb loss (during metamorphism, fluid interaction, or radiation damage) moves analyses off concordia toward the origin. A linear discordia array indicates a single episode of Pb loss from initially concordant grains. The upper intercept dates the original crystallization; the lower intercept dates the Pb-loss event. Grains that lost more Pb plot farther down the discordia line."

- question: "Zircon is preferred for U-Pb dating primarily because it contains the highest uranium concentrations of any mineral."
  type: true-false
  answer: false
  explanation: "While zircon does contain significant U (typically 100-1000 ppm), the primary reason it is preferred is its near-complete exclusion of initial Pb during crystallization -- meaning essentially all Pb measured is radiogenic (from U decay). This eliminates the need for large and uncertain common-Pb corrections. Additionally, zircon is extremely resistant to physical and chemical weathering, surviving multiple cycles of erosion, transport, and even metamorphism. Other minerals (uraninite, monazite) contain more U but are less robust or less common."

- question: "Explain the advantage of having two independent U-Pb decay systems in a single mineral grain."
  type: short-answer
  answer: "The two decay chains (238U-206Pb and 235U-207Pb) provide an internal consistency check. In an undisturbed grain, both systems must yield the same age (concordant). If the grain has experienced Pb loss or U gain, the two ages will disagree (discordant), immediately flagging the disturbance. This self-checking property is unique to the U-Pb system and allows detection and even correction of open-system behavior through the concordia-discordia framework. No other radiometric system has this built-in redundancy."
  explanation: "Concordance between two independent chronometers in the same grain provides confidence that no other geochronometer can match -- discordance is its own quality control."
```

## Explainer

U-Pb geochronology is the most precise and widely applied method for determining the age of crystalline rocks. The combination of two decay chains, the ideal geochemical properties of zircon, and modern analytical techniques (SHRIMP ion probe, LA-ICP-MS, CA-TIMS) has made U-Pb zircon dating the cornerstone of Earth history chronology.

The concordia diagram is the interpretive framework. The concordia curve plots all possible concordant ages -- points where 206Pb/238U and 207Pb/235U ages agree. An undisturbed zircon crystallized at time t plots on concordia at the position corresponding to t. The curve is non-linear because the two decay constants differ: 235U decays ~6.3 times faster than 238U, so the 207Pb/235U ratio evolves faster, compressing old ages on the 207Pb/235U axis. This non-linearity is what makes discordia lines informative -- a straight line through discordant analyses intersects concordia at two meaningful ages.

Modern analytical methods achieve extraordinary precision. Chemical Abrasion - Thermal Ionization Mass Spectrometry (CA-TIMS) dissolves individual zircon grains after removing radiation-damaged zones (which are prone to Pb loss), achieving age precisions of 0.05-0.1% (50,000 years on a 100 Ma rock). Laser Ablation ICP-MS analyzes 20-30 micrometer spots in polished grain sections, enabling rapid age surveys of detrital zircon populations (hundreds of grains per day) with 1-2% precision. SHRIMP ion probes provide intermediate precision (~1%) with spatial resolution targeting specific growth zones within individual grains.

Detrital zircon geochronology has revolutionized sedimentary provenance studies. Because zircon survives erosion and transport, the age spectrum of detrital zircons in a sandstone records the ages of source rocks in the drainage basin. Thousands of detrital zircon ages from a single sample can fingerprint sediment sources, reconstruct paleodrainage patterns, and constrain maximum depositional ages. Global compilations of detrital zircon ages reveal episodic crustal production, preservation biases, and the supercontinent cycle through >4 billion years of Earth history.
