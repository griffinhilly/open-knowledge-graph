---
id: metamorphic-mineral-assemblages-conditions
title: Metamorphic Mineral Assemblages and Pressure-Temperature Conditions
domain: earth-and-space-sciences
course: geology
prerequisites:
- id: mineral-crystal-systems-classification
  type: hard
- id: metamorphic-rocks
  type: soft
builds-toward:
- metamorphic-textures-microstructures
- fold-fault-formation-stress-analysis
tags:
- metamorphic
- petrology
- facies
stage: advanced
status: draft
---

# Metamorphic Mineral Assemblages and Pressure-Temperature Conditions

## Core Idea
Metamorphic rocks form under elevated pressure and temperature; specific mineral assemblages (facies) such as greenschist, amphibolite, and granulite define the P-T conditions during metamorphism. These assemblages preserve a record of deep crustal or mantle processes and plate convergence.

## Questions

```yaml
- question: "A geologist discovers blueschist rocks containing the blue amphibole glaucophane in an ancient mountain belt. What tectonic setting does this most directly indicate?"
  type: multiple-choice
  options:
    - "High-pressure, low-temperature metamorphism consistent with cold oceanic crust subducted to great depths"
    - "High-temperature, low-pressure contact metamorphism from a nearby igneous intrusion"
    - "Regional metamorphism from deep burial during continental collision, similar to amphibolite facies"
    - "Hydrothermal alteration along a mid-ocean ridge spreading center"
  answer: 0
  explanation: "Blueschist facies forms at high pressure but relatively low temperature — exactly the conditions of subduction zones, where cold oceanic crust is driven rapidly to depth before it has time to heat up. Glaucophane is diagnostic because it is only stable under these unusual HP-LT conditions. Option 2 (contact metamorphism) produces low-pressure, high-temperature assemblages — the opposite. Option 3 (amphibolite) forms at moderate-high T and moderate P, not blueschist conditions."

- question: "Two basalt samples — one from India, one from Norway — were metamorphosed under identical pressure-temperature conditions. What mineral assemblage would you expect in each?"
  type: multiple-choice
  options:
    - "The same assemblage in both, because bulk chemical composition and P-T conditions together determine which minerals form, regardless of geographic origin"
    - "Different assemblages, because the geographic origin and tectonic setting of the original rock affect which minerals crystallize"
    - "Different assemblages, because metamorphic reactions proceed faster in warmer climates, producing different minerals"
    - "The same assemblage only if both basalts were formed at mid-ocean ridges with identical magma chemistry"
  answer: 0
  explanation: "This is the key predictive power of metamorphic petrology: mineral assemblage is controlled by bulk chemical composition and P-T conditions — not by geography, climate, or local history. Two rocks with the same starting chemistry under the same P-T conditions will develop the same assemblage worldwide. Option 1 (geographic origin matters) is the misconception being tested — origin is irrelevant once you specify composition and conditions."

- question: "When interpreting metamorphic rocks, the presence of certain minerals is diagnostic of specific P-T conditions, but the absence of particular minerals provides no useful information."
  type: true-false
  answer: false
  explanation: "Mineral absences are often as diagnostic as presences. For example, the absence of hydrous minerals (chlorite, hornblende) in granulite facies rocks — replaced by anhydrous pyroxene and garnet — is a key indicator of high-temperature metamorphism. Similarly, the absence of high-pressure indicator minerals like kyanite or glaucophane constrains what conditions were NOT reached. Petrologists actively use 'forbidden assemblages' as constraints in P-T path reconstruction."

- question: "A clockwise P-T path (increasing pressure and temperature during burial, then decreasing during exhumation) is characteristic of collision-zone metamorphism."
  type: true-false
  answer: true
  explanation: "In continental collision zones, rocks are buried by crustal thickening (increasing P), then heat slowly diffuses in from surrounding rock (T rises). As the orogen erodes and rocks exhume, they cool while decompressing. This burial-heating then uplift-cooling trajectory traces a clockwise loop in P-T space. Counterclockwise paths are characteristic of different settings such as contact metamorphism or oceanic arc environments."

- question: "Why do high-pressure minerals like glaucophane sometimes survive at the Earth's surface rather than reverting to lower-pressure mineral assemblages during exhumation?"
  type: short-answer
  answer: "Mineral reactions require both thermodynamic drive AND sufficient reaction kinetics. When rocks are exhumed rapidly, temperature drops quickly, slowing reaction rates below the threshold needed for mineral transformation. The high-pressure minerals become metastable — thermodynamically unstable at surface conditions but kinetically 'frozen' because there is insufficient thermal energy to break and reform bonds. Fast exhumation preserves the deep P-T record; slow exhumation allows back-reactions that erase it."
  explanation: "This kinetic preservation is why blueschists and eclogites exist at the surface at all — they are thermodynamically unstable under crustal conditions but have not had time to re-equilibrate. The rate of exhumation relative to the rate of retrograde metamorphism determines preservation. This is why rapid tectonic uplift in subduction settings is associated with the best-preserved high-pressure assemblages."
```

## Explainer

From your study of mineral crystal systems and metamorphic rocks, you know that metamorphism transforms existing rocks under elevated temperature and pressure, producing new minerals stable under those conditions. The key insight of **metamorphic petrology** is that the specific combination of minerals in a rock — its **mineral assemblage** — is not random. It is controlled by the pressure-temperature (P-T) conditions during metamorphism and the bulk chemical composition of the original rock. Two rocks with the same starting chemistry subjected to the same P-T conditions will develop the same mineral assemblage, regardless of where on Earth they are found. This predictability is what makes mineral assemblages powerful diagnostic tools.

The concept that organizes this relationship is the **metamorphic facies** — a set of P-T conditions defined by characteristic mineral assemblages in rocks of common compositions. The major facies form a map across pressure-temperature space. **Greenschist facies** (~300–500°C, moderate pressure) is named for its green minerals: chlorite, epidote, and actinolite, which give the rock a distinctive green color. **Amphibolite facies** (~500–700°C, moderate to high pressure) is dominated by hornblende amphibole and plagioclase. **Granulite facies** (~700–900°C, moderate pressure) represents the highest-temperature regional metamorphism, where hydrous minerals break down and anhydrous minerals like pyroxene and garnet dominate. At high pressure but relatively low temperature, **blueschist facies** produces the striking blue amphibole glaucophane — diagnostic of subduction zones where cold oceanic crust is driven to great depths. Even higher pressure yields **eclogite facies**, with its distinctive garnet-plus-green-pyroxene (omphacite) assemblage, recording conditions deep in subduction channels.

The reason these assemblages are so informative is that metamorphic minerals reach **chemical equilibrium** at the peak conditions and are then preserved as the rock is brought back to the surface. Consider a basalt dragged down in a subduction zone: at shallow depth it contains zeolites and clay minerals (zeolite facies). As it descends to ~30 km depth and temperatures of 300–400°C, those minerals become unstable and are replaced by chlorite and actinolite (greenschist facies). Driven deeper to 50–70 km and pressures exceeding 1 GPa, glaucophane replaces actinolite and the rock becomes a blueschist. Each transition is a chemical reaction driven by changing stability — minerals that were stable at one set of conditions decompose and reform as new phases at another. If the rock is then exhumed rapidly enough, the high-pressure minerals are preserved rather than reverting to lower-pressure equivalents, giving geologists a direct window into conditions tens of kilometers below the surface.

Reading metamorphic assemblages in the field is therefore a form of geological forensics. By identifying the minerals present, plotting them on a P-T diagram, and noting what is absent (the absence of certain minerals can be as diagnostic as their presence), a petrologist reconstructs the **P-T path** — the trajectory the rock followed through pressure-temperature space during burial, peak metamorphism, and exhumation. These paths reveal the tectonic history of entire mountain belts: clockwise P-T paths (heating during burial, then cooling during uplift) are characteristic of collision zones, while counterclockwise paths suggest contact metamorphism or unusual tectonic settings. Every metamorphic assemblage is a frozen thermometer and barometer, recording conditions that no human could ever directly observe.
