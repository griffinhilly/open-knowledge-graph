---
id: carbon-dioxide-ocean-circulation
title: Carbon Dioxide Solubility and Ocean Circulation
domain: earth-and-space-sciences
course: climate-science
prerequisites:
- id: ocean-carbonate-system
  type: hard
- id: ocean-circulation-and-climate
  type: hard
- id: solubility-equilibria
  type: soft
builds-toward:
- marine-biological-pump-mechanisms
- ocean-acidification
tags:
- carbon-cycle
- ocean-chemistry
- circulation
- uptake
stage: expert
status: draft
---

# Carbon Dioxide Solubility and Ocean Circulation

## Core Idea
CO₂ solubility in seawater decreases with temperature and increases with pressure and alkalinity, controlling how much atmospheric CO₂ dissolves at the surface. Ocean circulation then transports dissolved inorganic carbon into the deep, creating a large storage reservoir. The solubility pump and circulation patterns determine the ocean's capacity to absorb atmospheric CO₂ and sequester it for centuries to millennia.

## Questions

```yaml
- question: "Climate models project that the thermohaline circulation could weaken significantly due to freshwater input from melting ice sheets. What effect would this have on atmospheric CO₂ levels?"
  type: multiple-choice
  options:
    - "Atmospheric CO₂ would decrease, because more surface water would be exposed to the atmosphere for gas exchange"
    - "Atmospheric CO₂ would increase, because deep water formation would slow, reducing transport of CO₂-rich surface water into the deep ocean"
    - "Atmospheric CO₂ would be unaffected, because ocean chemistry controls CO₂ levels, not circulation"
    - "Atmospheric CO₂ would decrease, because slower circulation means carbon stays near the surface longer and re-releases to the atmosphere"
  answer: 1
  explanation: "The solubility pump works by having cold, CO₂-saturated surface water sink into the deep ocean, physically removing carbon from contact with the atmosphere. If deep water formation slows, less CO₂-rich water descends, the deep-ocean carbon reservoir fills more slowly, and more CO₂ remains in the atmosphere. Paleoclimate records support this: glacial periods with stronger ventilation of deep Southern Ocean waters corresponded to lower atmospheric CO₂ than interglacials. A weakened thermohaline circulation would reduce this carbon sink."

- question: "Why do high-latitude oceans tend to absorb CO₂ from the atmosphere while tropical oceans tend to release it?"
  type: multiple-choice
  options:
    - "High-latitude organisms photosynthesize more, consuming CO₂, while tropical organisms respire more"
    - "Cold polar waters dissolve more CO₂ than warm tropical waters, making polar surface water undersaturated relative to the atmosphere and tropical water supersaturated"
    - "Trade winds push CO₂ from the tropics to the poles, forcing it into the water at high latitudes"
    - "High-latitude ocean currents are slower, giving more time for CO₂ to dissolve before water moves away"
  answer: 1
  explanation: "CO₂ solubility in seawater follows the same temperature-dependence as in any solvent: cold water dissolves more gas. Polar surface waters, cooled by contact with cold air and sea ice, are undersaturated in CO₂ relative to the atmosphere and absorb it. Tropical waters, warmed at the surface, become supersaturated and release CO₂. This temperature-driven gradient is the physical heart of the solubility pump — the fact that CO₂ is absorbed where water is about to sink is what makes the pump effective at transferring carbon to the deep ocean."

- question: "Cold seawater dissolves more CO₂ than warm seawater at the same pressure."
  type: true-false
  answer: true
  explanation: "Gas solubility in liquids decreases with temperature — the same principle that makes a warm soda go flat faster than a cold one. For CO₂ in seawater, this effect is significant: polar waters (~2°C) can hold roughly twice as much dissolved CO₂ as tropical surface waters (~25°C) at equivalent atmospheric CO₂ concentrations. This temperature-solubility relationship is the physical basis for the solubility pump and explains why the high-latitude ocean is the primary entry point for atmospheric CO₂ into the deep carbon reservoir."

- question: "As the ocean absorbs more anthropogenic CO₂, its capacity to absorb additional CO₂ in the future increases, because more carbonate chemistry is available to buffer the incoming gas."
  type: true-false
  answer: false
  explanation: "This reverses the reality. When CO₂ dissolves in seawater, it reacts with carbonate ions (CO₃²⁻) to form bicarbonate (HCO₃⁻), consuming carbonate and reducing alkalinity. As carbonate ion concentrations fall, the ocean's buffering capacity decreases — each additional mole of CO₂ acidifies the ocean more and is absorbed less efficiently. This is a positive feedback on atmospheric CO₂: as humans emit more CO₂, the ocean becomes progressively less able to absorb the next increment, so a larger fraction stays in the atmosphere. The fraction of annual emissions absorbed by the ocean is expected to decline over time."

- question: "Explain why the ocean's capacity to absorb anthropogenic CO₂ is expected to decline over time, even setting aside the effect of rising ocean temperatures."
  type: short-answer
  answer: "When CO₂ dissolves in seawater, it reacts with carbonate ions (CO₃²⁻) to form bicarbonate (HCO₃⁻). This reaction consumes carbonate ions, reducing the ocean's alkalinity and buffering capacity. As carbonate ion concentrations fall, the thermodynamic resistance to further CO₂ uptake increases — each additional molecule of CO₂ encounters less buffering and drives the equilibrium further toward atmospheric retention. The Revelle factor quantifies this: a high Revelle factor means the ocean must change its dissolved CO₂ concentration a lot for a given atmospheric change, indicating reduced uptake efficiency."
  explanation: "This is distinct from the temperature effect (warmer water holds less CO₂) but acts in the same direction. Both effects together — reduced solubility from warming and reduced buffering from acidification — mean the ocean's current role as absorbing ~25% of annual emissions will likely decline as atmospheric CO₂ rises. This creates a self-amplifying dynamic: more CO₂ in the atmosphere makes the ocean absorb proportionally less, leaving even more CO₂ in the atmosphere."
```

## Explainer

From the ocean carbonate system you know that dissolved CO₂ reacts with water to form carbonic acid, which dissociates into bicarbonate and carbonate ions, creating a chemical equilibrium that governs how much carbon the ocean can hold. From ocean circulation you know that surface and deep waters are connected by the thermohaline circulation, a global conveyor driven by density differences from temperature and salinity. The interaction of these two systems — CO₂ chemistry and ocean circulation — determines the ocean's role as Earth's largest active carbon reservoir, holding roughly 50 times more carbon than the atmosphere.

The **solubility pump** is the physical mechanism that moves CO₂ from atmosphere to deep ocean. Cold water dissolves more CO₂ than warm water — the same reason a cold soda stays fizzy longer than a warm one. At high latitudes, surface waters cool dramatically, absorbing large quantities of atmospheric CO₂. These cold, dense, CO₂-rich waters then sink to the deep ocean through processes like North Atlantic Deep Water formation. Once in the deep ocean, this carbon-laden water is isolated from the atmosphere for centuries to a millennium as it slowly circulates through the ocean basins before eventually upwelling in the tropics or Southern Ocean.

The efficiency of this pump depends on several factors. **Temperature** is the primary control on solubility: polar oceans absorb CO₂ while tropical oceans tend to release it, creating a net poleward transport of carbon. **Alkalinity** — the ocean's acid-buffering capacity, governed by carbonate and bicarbonate ion concentrations — determines how much additional CO₂ the water can absorb before the carbonate equilibrium shifts to resist further uptake. Higher alkalinity means more capacity; as the ocean absorbs anthropogenic CO₂, this buffering capacity decreases because the reaction consumes carbonate ions, reducing the ocean's future uptake efficiency.

**Circulation speed and pattern** set the timescale of sequestration. If the thermohaline circulation is vigorous, carbon-rich surface water is transported to the deep quickly and replaced by water that can absorb more CO₂. If circulation weakens — as may happen with freshwater input from melting ice sheets — deep water formation slows, the solubility pump weakens, and more CO₂ remains in the atmosphere. Paleoclimate records show that changes in ocean circulation during glacial-interglacial transitions were closely linked to atmospheric CO₂ changes, with weaker ventilation of deep Southern Ocean waters during ice ages helping to keep CO₂ locked in the deep ocean and atmospheric concentrations low. Today, the ocean absorbs roughly 25% of annual anthropogenic CO₂ emissions, but this fraction is expected to decline as warming reduces solubility and acidification erodes buffering capacity.
