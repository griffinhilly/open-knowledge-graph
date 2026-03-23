---
id: bowen-fractional-crystallization
title: Bowen's Reaction Series and Fractional Crystallization
domain: earth-and-space-sciences
course: geology
prerequisites:
- id: magma-melting-pressure-temperature
  type: hard
- id: mineral-properties-and-identification
  type: hard
builds-toward:
- magma-composition-viscosity
tags:
- crystallization
- Bowen
- igneous
- differentiation
stage: formal-systems
status: validated
---

# Bowen's Reaction Series and Fractional Crystallization

## Core Idea
As magma cools, minerals crystallize in a predictable sequence (Bowen's series) determined by thermodynamic stability. Fractional crystallization—where crystals separate from liquid—changes the liquid's composition over time, explaining why a single magma can produce rocks of different compositions.

## How It's Best Learned
Track how melt composition evolves as minerals remove elements during crystallization. Compare computed trends with natural rock compositions.

## Common Misconceptions
- All minerals crystallize simultaneously as temperature drops.
- Mineral composition remains constant during crystallization.
- Bowen's series applies to all rock types.

## Questions

```yaml
- question: "Two magma chambers start with identical basaltic compositions. In chamber A, crystals continuously react with the melt as temperature falls. In chamber B, dense crystals sink and are physically removed from contact with the melt. How will the final residual liquid compositions differ?"
  type: multiple-choice
  options:
    - "Both chambers produce identical residual liquids, since they started with the same composition"
    - "Chamber A produces a more silicic residual liquid because reactions consume more elements"
    - "Chamber B produces a more silicic residual liquid enriched in Na and K, because early Mg- and Ca-rich minerals were removed"
    - "Chamber B produces a more mafic residual liquid because it lost the silica-bearing early crystals"
  answer: 2
  explanation: "Fractional crystallization depends on physical separation of early-forming crystals. In chamber B, olivine and Ca-plagioclase sink and are removed, stripping Mg, Fe, and Ca from the melt. The residual liquid becomes progressively enriched in silica, sodium, and potassium — the components that form late in Bowen's series. Chamber A re-equilibrates continuously through crystal-melt reactions, limiting differentiation. The physical separation in chamber B is what drives magmatic differentiation."

- question: "According to Bowen's reaction series, which mineral pair forms at the highest temperatures and crystallizes first from a cooling basaltic magma?"
  type: multiple-choice
  options:
    - "Quartz and potassium feldspar"
    - "Amphibole and sodium-rich plagioclase"
    - "Olivine and calcium-rich plagioclase (anorthite)"
    - "Muscovite and biotite"
  answer: 2
  explanation: "Bowen's series places olivine (discontinuous branch) and calcium-rich plagioclase/anorthite (continuous branch) at the highest crystallization temperatures. These mafic minerals form first from cooling basaltic magma. Quartz and K-feldspar form last from the most silica-rich residual melts. Amphibole and biotite form at intermediate temperatures. This sequence explains why mafic minerals dominate early-crystallized igneous rocks like gabbro."

- question: "Early-crystallizing minerals in Bowen's series are enriched in magnesium, iron, and calcium relative to the residual melt."
  type: true-false
  answer: true
  explanation: "High-temperature minerals like olivine (Mg, Fe silicate) and calcium-rich plagioclase incorporate Mg, Fe, and Ca preferentially. Their crystallization removes these elements from the melt, leaving the residual liquid depleted in Mg, Fe, and Ca and enriched in Si, Na, and K. This is precisely why fractional crystallization of basaltic magma can ultimately produce granite — not through mixing of different magmas, but by sequential removal of mafic minerals."

- question: "Bowen's reaction series describes the crystallization sequence for all rock types, including sedimentary and metamorphic rocks."
  type: true-false
  answer: false
  explanation: "Bowen's series was derived experimentally from cooling basaltic magma and applies specifically to igneous (magmatic) crystallization. Sedimentary rocks form through weathering, transport, deposition, and diagenesis — processes governed by stability at Earth's surface. Metamorphic rocks form through solid-state mineral transformations under heat and pressure without melting. The series has no direct application to non-igneous rock types."

- question: "Why does fractional crystallization require physical separation of crystals from the melt, and what happens if crystals remain in contact throughout cooling?"
  type: short-answer
  answer: "Physical separation prevents early-formed crystals from reacting back with the melt as temperature falls. If crystals remain in contact, they re-equilibrate with the liquid through reaction (as in the discontinuous branch), consuming the compositional difference that crystallization created and producing a more uniform final rock. When crystals are removed (by sinking, filtering, or wall accumulation), the melt cannot re-equilibrate, and each removal event progressively enriches the residual liquid in components not incorporated by the departed crystals."
  explanation: "This is why 'fractional' crystallization is distinct from 'equilibrium' crystallization. In equilibrium crystallization, all crystals stay in contact with the melt and the system reaches a uniform final composition. Fractional crystallization removes each batch of crystals as it forms — like repeatedly removing partial batches of sugar crystals from a solution, leaving behind an increasingly concentrated remainder. The cumulate rocks that settle out and the evolved liquid that remains preserve a record of this step-by-step compositional evolution."
```

## Explainer

From your study of magma generation, you know that melting and crystallization depend on temperature, pressure, and composition. **Bowen's reaction series** takes this a step further by showing that as a magma cools, minerals do not all appear at once — they crystallize in a predictable sequence. The minerals that form at the highest temperatures (olivine, calcium-rich plagioclase) appear first, and those stable at lower temperatures (quartz, potassium feldspar, muscovite) form last. This sequence was established experimentally by N.L. Bowen in the early twentieth century and remains one of the most powerful organizing frameworks in igneous petrology.

The series has two branches that operate simultaneously. The **discontinuous branch** on the left side describes ferromagnesian minerals that change abruptly in crystal structure as temperature drops: olivine gives way to pyroxene, then amphibole, then biotite. Each transition involves a reaction between the existing crystals and the remaining liquid — the early crystal becomes unstable and is replaced by a new mineral with a different structure. The **continuous branch** on the right describes plagioclase feldspar, which changes composition smoothly from calcium-rich (anorthite) at high temperatures to sodium-rich (albite) at low temperatures, as calcium and sodium continuously exchange between crystal and melt. Both branches converge at the bottom of the series where potassium feldspar, muscovite, and quartz crystallize from the most silica-rich residual liquid.

**Fractional crystallization** is the process that makes this sequence consequential for rock diversity. If early-formed crystals stay in contact with the melt, they react with it and the final rock is compositionally uniform. But if crystals are physically separated from the liquid — by sinking due to their higher density, by being filtered out as magma migrates, or by being left behind on chamber walls — the remaining melt changes composition. Each mineral that separates removes specific elements: olivine strips out magnesium and iron, plagioclase removes calcium and aluminum. The residual liquid becomes progressively enriched in silica, sodium, and potassium. This is why a single batch of basaltic magma can ultimately produce rocks ranging from gabbro to granite — not by adding new material, but by subtracting crystals at each stage.

Think of it like making maple syrup by boiling sap: as water evaporates (analogous to crystals removing elements), the remaining liquid becomes increasingly concentrated in sugar. In magma, "removing" early minerals concentrates the components that form later minerals. This process — called **magmatic differentiation** — explains much of the compositional diversity observed in igneous rock suites. A layered intrusion like the Bushveld Complex in South Africa preserves this process frozen in stone: dense olivine-rich cumulates at the base, progressively more felsic rocks toward the top, recording the evolutionary path of a cooling and differentiating magma chamber over millions of years.
