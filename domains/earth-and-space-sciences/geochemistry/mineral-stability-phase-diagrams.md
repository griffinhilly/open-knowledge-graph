---
id: mineral-stability-phase-diagrams
title: Mineral Stability and Phase Diagrams
domain: earth-and-space-sciences
course: geochemistry
prerequisites:
- id: geochemical-thermodynamics
  type: hard
builds-toward:
- mantle-geochemistry
- crustal-evolution-geochemistry
- weathering-soil-chemistry
tags:
- phase-diagrams
- mineral-stability
- metamorphism
- petrology
stage: expert
status: validated
---

# Mineral Stability and Phase Diagrams

## Core Idea
Phase diagrams map the stability fields of minerals and mineral assemblages as functions of temperature, pressure, and composition. Each region of the diagram represents conditions where a specific mineral or assemblage has the lowest Gibbs free energy and is therefore thermodynamically stable. Boundaries between fields represent conditions where two assemblages coexist in equilibrium (univariant reactions). The Clausius-Clapeyron equation (dP/dT = delta-S/delta-V) governs the slope of these boundaries. Phase diagrams are the primary tool for interpreting metamorphic grade, predicting magmatic crystallization sequences, and understanding the mineralogical structure of Earth's interior.

## Questions

```yaml
- question: "The Al2SiO5 system has three polymorphs: andalusite (low P, moderate T), kyanite (high P), and sillimanite (high T). A metamorphic rock contains kyanite partially replaced by sillimanite. What does this indicate about the rock's thermal history?"
  type: multiple-choice
  options:
    - "The rock cooled rapidly from magmatic temperatures"
    - "The rock experienced increasing temperature at relatively high pressure, crossing the kyanite-sillimanite phase boundary during prograde metamorphism"
    - "The rock was weathered at the surface"
    - "Kyanite transformed to sillimanite during decompression at constant temperature"
  answer: 1
  explanation: "The kyanite-sillimanite boundary has a positive slope in P-T space -- crossing it requires temperature increase at pressures where kyanite is initially stable (above the andalusite field). The partial replacement texture records the reaction in progress, indicating the rock was heating. This mineral transition is diagnostic of upper amphibolite to granulite facies metamorphism and is a classic example of using phase diagrams to interpret metamorphic history."

- question: "A univariant reaction boundary on a P-T phase diagram has zero width because the reaction occurs at a single precise temperature for any given pressure."
  type: true-false
  answer: true
  explanation: "For a univariant reaction in a pure system (one degree of freedom along the boundary by the phase rule), at any given pressure there is exactly one temperature where the reactant and product assemblages coexist in equilibrium. Above that temperature, products are stable; below, reactants are stable. The boundary is a line, not a band. In natural systems with solid solutions, reactions may occur over a narrow T-P interval, but the fundamental thermodynamic constraint makes the boundary a sharp line in end-member systems."

- question: "Explain how the Clausius-Clapeyron equation predicts the slope of the graphite-diamond phase boundary and what this slope tells us about diamond formation."
  type: short-answer
  answer: "The Clausius-Clapeyron slope dP/dT = delta-S/delta-V. Diamond has lower molar volume than graphite (denser packing) so delta-V (graphite to diamond) is negative. The entropy change is small and slightly negative (diamond is more ordered). The ratio gives a steep positive slope in P-T space, meaning diamond stability requires very high pressure (>4 GPa) regardless of temperature. This tells us diamonds form only at depths exceeding ~150 km in the mantle, where pressures are sufficient. The steep slope means temperature variations matter much less than pressure for crossing this boundary."
  explanation: "The negative delta-V dominates: converting to the denser phase requires high pressure. The steep positive slope means diamonds are a pressure indicator -- they require mantle depths, not just high temperatures."
```

## Explainer

Phase diagrams are to geochemists what circuit diagrams are to electrical engineers -- they encode the fundamental constraints governing the system's behavior into a visual map. Reading a phase diagram means understanding what minerals exist under what conditions and what happens when conditions change.

The thermodynamic foundation is simple: at any given T-P-X condition, the stable assemblage is the one with the lowest total Gibbs free energy. Phase boundaries are the T-P loci where two assemblages have equal free energy. The Gibbs phase rule (F = C - P + 2) determines how many intensive variables (T, P, composition) can be independently varied while maintaining the observed assemblage. A divariant field (F=2) allows both T and P to change freely. A univariant line (F=1) constrains one variable once the other is fixed. An invariant point (F=0) fixes both T and P -- these are the diagnostic triple points or reaction intersections that calibrate geothermometers and geobarometers.

P-T diagrams are most commonly used for metamorphic petrology. A rock's mineral assemblage records the P-T conditions where it last equilibrated, and the sequence of mineral reactions (preserved as inclusion textures, reaction rims, and pseudomorphs) traces the rock's P-T path through time. Clockwise P-T paths (burial, heating, then exhumation) characterize collision zones; counterclockwise paths characterize contact metamorphism. These P-T paths, reconstructed from phase diagrams, constrain tectonic models.

T-X (temperature-composition) diagrams govern igneous crystallization. Binary and ternary phase diagrams predict the sequence of minerals that crystallize from a cooling magma: which mineral appears first, how compositions evolve with cooling (fractional crystallization), and what happens at eutectic and peritectic points. The lever rule quantifies the proportions of solid and liquid at any temperature. These diagrams explain why basalts and granites have characteristic mineral assemblages and why fractional crystallization produces compositional diversity in igneous suites.
