---
id: metamorphic-equilibrium-phase-diagrams
title: Metamorphic Equilibrium and Phase Diagrams
domain: earth-and-space-sciences
course: geology
prerequisites:
- id: metamorphic-rocks
  type: hard
- id: earths-interior-density-composition
  type: soft
- id: phase-diagrams-binary-mixtures
  type: soft
- id: gibbs-free-energy-spontaneity
  type: soft
- id: equilibrium-expression-kc-kp-constants
  type: soft
- id: phase-diagrams
  type: hard
- id: gibbs-free-energy
  type: hard
- id: phase-diagrams-clausius-clapeyron
  type: hard
builds-toward:
- thermobarometry-estimates-metamorphic
tags:
- metamorphism
- phase-diagram
- equilibrium
- pressure-temperature
stage: advanced
status: validated
---

# Metamorphic Equilibrium and Phase Diagrams

## Core Idea
Mineral assemblages in metamorphic rocks reflect equilibrium at specific pressure-temperature (P-T) conditions. Phase diagrams show which minerals are stable at different P-T; mineral boundaries define metamorphic facies. Comparing observed minerals to phase diagrams reveals the P-T path rocks followed during metamorphism.

## Questions

```yaml
- question: "A geologist finds a metamorphic rock containing both kyanite and sillimanite, which have a reaction boundary separating their stability fields on a P-T phase diagram. What is the most geologically reasonable interpretation?"
  type: multiple-choice
  options:
    - "The rock formed simultaneously from two different magmas with incompatible mineral compositions"
    - "The rock crossed the kyanite-sillimanite reaction boundary during metamorphism, and one mineral is a relic preserved from earlier conditions"
    - "Both minerals are stable across all metamorphic facies, so their coexistence is unremarkable"
    - "The sample was contaminated during collection and the minerals did not form in the same rock"
  answer: 1
  explanation: "Coexistence of minerals across a reaction boundary records a changing P-T history. As the rock passed through the kyanite-to-sillimanite transition, the reaction may not have gone to completion, leaving kyanite relics enclosed in sillimanite overgrowths (or vice versa). This textural evidence — which mineral is the inclusion and which is the host — tells geologists the direction of P-T change. This is precisely why metamorphic rocks are powerful recorders: they preserve snapshots of past conditions, not just current ones."

- question: "A rock is found at the surface containing diamond, which is only stable at pressures exceeding ~40,000 atmospheres (mantle depths). A student concludes the rock currently equilibrates at mantle conditions. What is the fundamental flaw in this reasoning?"
  type: multiple-choice
  options:
    - "Diamonds form through ordinary organic processes and don't require high pressure"
    - "Phase diagrams only apply to sedimentary rocks, not metamorphic ones"
    - "Diamond is metastably preserved at surface conditions because conversion to graphite requires activation energy that is kinetically unavailable at surface temperatures"
    - "The student has misread the phase diagram — diamond is actually stable at low pressure"
  answer: 2
  explanation: "This is the critical caveat of metamorphic petrology: equilibrium is an idealization. Diamond is thermodynamically unstable at the surface (graphite has lower free energy), but the conversion requires breaking and reforming strong C-C bonds — a kinetically hindered process at low temperatures. Diamond persists as a metastable relic because the activation energy barrier is enormous. This is why identifying which minerals achieved equilibrium (and which are metastable relics) is the central interpretive skill, not just reading stability fields off a phase diagram."

- question: "A metamorphic rock that equilibrated in the amphibolite facies will always display only amphibolite-facies mineral assemblages when examined at Earth's surface."
  type: true-false
  answer: false
  explanation: "Metamorphic minerals can be preserved metastably outside their stability fields during exhumation. As a rock is uplifted from depth, it passes through lower P-T conditions where its high-grade minerals are no longer thermodynamically stable. However, if temperature drops quickly enough that reaction kinetics are too slow, the original minerals survive as relics. This is why high-pressure minerals like eclogite assemblages and even ultra-high-pressure phases (coesite, diamond) are found in surface outcrops."

- question: "The metamorphic facies of a rock identifies the pressure-temperature region in which the rock's mineral assemblage reached thermodynamic equilibrium."
  type: true-false
  answer: true
  explanation: "Metamorphic facies (greenschist, amphibolite, granulite, blueschist, eclogite, etc.) are defined as regions of P-T space where specific mineral assemblages are stable. Assigning a rock to a facies means identifying which stability fields its coexisting minerals share — i.e., finding the P-T conditions where the whole assemblage could have been at equilibrium simultaneously. The facies concept is a shorthand for this P-T location."

- question: "Why does the presence of a mineral in a metamorphic rock not necessarily indicate that the rock currently occupies that mineral's thermodynamic stability field?"
  type: short-answer
  answer: "Mineral reactions require activation energy and sufficient atomic mobility, which depend on temperature, fluid presence, and time. During exhumation, as a rock cools and decompresses, temperatures may drop too quickly for minerals to re-equilibrate. Minerals that were stable at peak P-T conditions persist metastably because the kinetics of converting them to the lower-temperature stable phase are too slow at ambient surface conditions. The presence of a mineral records where the rock was, not where it is now."
  explanation: "This kinetic barrier is geologically fortunate — it is the reason we can read P-T histories from surface outcrops. If metamorphic minerals always equilibrated to surface conditions, we would find only zeolites and clay minerals in all metamorphic rocks, and the entire record of deep-crustal and mantle conditions would be erased."
```

## Explainer

From your study of metamorphic rocks, you know that pre-existing rocks transform when subjected to elevated temperature and pressure, producing new mineral assemblages and textures. From thermodynamics, you know that Gibbs free energy determines which phase is stable at given conditions, and from phase diagrams, you know how to read stability fields separated by reaction boundaries. **Metamorphic phase diagrams** bring these concepts together: they map out which mineral assemblages are thermodynamically stable at each combination of pressure and temperature, turning a metamorphic rock into a recorder of the conditions it experienced.

The fundamental principle is **chemical equilibrium**. At any given P-T condition, the mineral assemblage with the lowest total Gibbs free energy is the one that should form, given enough time and sufficient atomic mobility. A boundary line on a P-T diagram represents a reaction — say, the transformation of kyanite to sillimanite — where both phases have equal free energy. Cross that boundary, and one phase becomes unstable while the other becomes favored. In practice, metamorphic rocks contain multiple minerals whose mutual stability fields overlap, and identifying which combination of minerals coexists allows you to locate the rock's conditions within a specific region of P-T space. These regions are called **metamorphic facies**: greenschist facies (low-moderate T, low-moderate P), amphibolite facies (moderate-high T, moderate P), granulite facies (high T), blueschist facies (low T, high P), and so on. Each facies name tells an experienced geologist approximately where in P-T space the rock equilibrated.

The real power of this approach emerges when you consider that metamorphic rocks often preserve evidence of *changing* conditions — not just a single P-T point. As a rock is buried during mountain building, heated, and eventually exhumed, it passes through different stability fields. Early-formed minerals may be preserved as inclusions inside later-grown crystals, or reaction rims may develop around minerals that became unstable. By identifying these textural relationships and matching each mineral assemblage to its stability field on a phase diagram, petrologists reconstruct the rock's **P-T path** — the trajectory it followed through pressure-temperature space over millions of years. A path that shows increasing pressure followed by increasing temperature (a clockwise loop in P-T space) tells a story of burial followed by heating, characteristic of continental collision. A path showing high pressure at low temperature (upper-left region of the diagram) indicates subduction.

One important caveat: equilibrium is an idealization. Real metamorphic reactions require activation energy, fluid catalysts, and time. Some minerals persist metastably outside their stability fields because the reaction kinetics are too slow — this is why diamonds, which are only stable at mantle pressures, survive at Earth's surface. The art of metamorphic petrology lies in recognizing which minerals achieved equilibrium and which are metastable relics, and using that judgment to extract reliable P-T estimates from the phase diagram framework.
