---
id: volcano-classification-magma-types
title: Volcano Classification and Magma Composition
domain: earth-and-space-sciences
course: geology
prerequisites:
- id: igneous-rock-magma-differentiation
  type: hard
- id: plate-boundary-processes-interactions
  type: soft
builds-toward:
- volcanic-hazards-lahars-ash-flows
tags:
- volcanism
- magma
- eruption-styles
stage: formal-systems
status: draft
---

# Volcano Classification and Magma Composition

## Core Idea
Volcanoes are classified by eruption style and magma composition: shield volcanoes erupt low-viscosity basaltic lava with gentle slopes, stratovolcanoes erupt intermediate andesite with explosive behavior, and calderas form from high-viscosity rhyolitic eruptions. Magma source—mantle melting at ridges and arcs, or crustal melting—determines composition.

## Questions

```yaml
- question: "Hawaii has gentle, effusive eruptions while Mount St. Helens erupted explosively in 1980. What is the most fundamental reason for this difference?"
  type: multiple-choice
  options:
    - "Hawaii is a younger volcano with less accumulated pressure"
    - "Hawaii's basaltic magma has low silica content, giving it low viscosity so gases escape easily and lava flows freely; Mount St. Helens' andesitic magma is highly viscous and traps gases until pressure builds to explosive levels"
    - "Hawaiian eruptions occur underwater, which slows the lava and reduces explosive force"
    - "Stratovolcanoes like Mount St. Helens receive more magma per year, generating more pressure"
  answer: 1
  explanation: "The key chain is: silica content → viscosity → gas retention → eruption style. Basaltic magma (~50% SiO₂) has low viscosity because the silica tetrahedra form short polymer chains, allowing gases to escape and lava to flow. Andesitic/dacitic magma (~55–65% SiO₂) has much higher viscosity due to more extensive silica polymerization — dissolved gases cannot escape, pressure builds, and eruptions become explosive. This relationship between silica and eruption style is why you can predict eruption behavior from magma chemistry, and it ultimately traces back to plate tectonic setting (hotspot vs. subduction zone)."

- question: "A newly discovered volcano has a broad, gently sloping profile with very flat flanks, and erupts frequently without major explosions. Which magma type and tectonic setting is most consistent with this description?"
  type: multiple-choice
  options:
    - "Rhyolitic magma from a subduction zone — high silica allows gentle eruption"
    - "Andesitic magma from a hotspot — intermediate composition produces moderate slopes"
    - "Basaltic magma from a hotspot or divergent boundary — low silica gives low viscosity and effusive eruptions that build broad shields"
    - "Dacitic magma from a continental collision zone — collision melts crust to produce gentle lava flows"
  answer: 2
  explanation: "The description matches a shield volcano precisely. The broad, gently sloping profile is the result of low-viscosity basaltic lava spreading over large distances before solidifying. Hotspots and divergent boundaries produce basaltic magma because mantle material melts with minimal crustal interaction, keeping silica content low (~50%). The frequent, non-explosive eruptions confirm low gas trapping. High-silica (rhyolitic) or intermediate (andesitic) magmas would produce steeper profiles or explosive behavior. The volcano's shape is a direct physical record of its magma chemistry."

- question: "The silica content of magma is the primary determinant of whether a volcano erupts explosively or effusively."
  type: true-false
  answer: true
  explanation: "True. Silica content controls viscosity because SiO₄ tetrahedra polymerize into chains and networks that impede flow. High-silica rhyolitic magma (~70%+ SiO₂) is so viscous that dissolved gases (H₂O, CO₂, SO₂) cannot escape — they remain trapped until confining pressure is suddenly released, causing explosive fragmentation. Low-silica basaltic magma (~50% SiO₂) has low viscosity, allowing gases to exsolve gradually and lava to flow rather than explode. This silica-viscosity-eruption relationship is why magma composition is the most important single variable for predicting eruption style."

- question: "Calderas form when volcanic peaks become too large and collapse under their own weight, which is why the largest eruptions produce the deepest craters."
  type: true-false
  answer: false
  explanation: "False. Calderas form when a volcano's magma chamber is rapidly emptied during a massive eruption, removing the structural support for the overlying rock, which then collapses inward. This is not a gravitational collapse due to weight but a structural failure caused by the evacuated chamber. Caldera-forming eruptions involve highly viscous, gas-rich rhyolitic magma that erupts so explosively and voluminously (sometimes hundreds of cubic kilometers) that the chamber drains. The resulting depression is a caldera, not a crater — it is a collapse feature. Yellowstone's caldera is one of the best-known examples."

- question: "Trace the chain of causation from tectonic plate setting to eruption style. Why do subduction zones produce more explosive volcanoes than hotspots?"
  type: short-answer
  answer: "At hotspots and divergent boundaries, hot mantle material melts directly with minimal crustal interaction, producing basaltic magma low in silica (~50% SiO₂). Low silica means low viscosity, so gases escape easily and eruptions are effusive (shield volcanoes). At subduction zones, the descending oceanic plate releases water and CO₂ into the overlying mantle wedge, lowering the melting point and generating magma. This magma interacts with and incorporates continental crust, which is silica-rich. The result is andesitic to dacitic magma with higher silica content (~55–65% SiO₂). Higher silica increases viscosity through silicate polymerization, trapping dissolved gases. The trapped gases build pressure until it catastrophically overcomes the magma's resistance — producing explosive eruptions and the steep layered profiles of stratovolcanoes."
  explanation: "The complete chain is: tectonic setting → magma source and crustal interaction → silica content → silicate polymerization → viscosity → gas retention → eruption style → volcano morphology. Understanding this chain means you can predict eruption behavior from geochemistry and can interpret a volcano's shape as a record of its magma composition and tectonic history."
```

## Explainer

From your study of igneous rock formation and magma differentiation, you know that magmas vary in silica content, viscosity, and volatile (gas) content. These three properties are the key to understanding why volcanoes look and behave so differently from one another. The classification of volcanoes is not arbitrary — it follows directly from the chemistry of the magma feeding them.

**Shield volcanoes** are built by **basaltic magma**, which is low in silica (~50%), low in viscosity, and relatively low in dissolved gases. Because this magma flows easily, eruptions tend to be effusive rather than explosive. Lava pours out and spreads over large areas, building broad, gently sloping structures — like a warrior's shield lying on the ground. Hawaii's Mauna Loa is the classic example. These volcanoes typically form at hotspots and divergent plate boundaries, where mantle material melts directly with minimal crustal contamination.

**Stratovolcanoes** (also called composite volcanoes) erupt **andesitic to dacitic magma** with intermediate silica content (~55–65%). This magma is more viscous than basalt and traps more gas, leading to a mix of explosive eruptions and lava flows. The alternating layers of ash, pyroclastic debris, and solidified lava give these volcanoes their steep, conical profile — think of Mount Fuji or Mount St. Helens. Stratovolcanoes dominate subduction zones, where the descending oceanic plate releases water into the mantle wedge, generating magma that interacts with and incorporates continental crust, raising its silica content.

At the extreme end sit **rhyolitic systems** with silica content above 70%. This magma is so viscous and gas-rich that it cannot flow quietly — pressure builds until catastrophic eruption occurs. These eruptions can be so violent that the volcano collapses into the emptied magma chamber, forming a **caldera** rather than building a peak. Yellowstone's enormous caldera formed this way. The connection between magma source and volcano type is therefore a chain: plate tectonic setting determines what melts, the degree of crustal interaction determines silica content, silica content controls viscosity and gas retention, and those physical properties dictate whether an eruption is a gentle lava flow or a landscape-altering explosion.
