---
id: marine-biological-pump
title: Marine Biological Pump and Carbon Sequestration
domain: earth-and-space-sciences
course: climate-science
prerequisites:
- id: marine-primary-productivity
  type: hard
- id: ocean-chemistry-and-nutrients
  type: soft
builds-toward:
- anthropogenic-carbon-cycle
- paleoclimate-proxies
tags:
- pump
- biological
- carbon
- productivity
- sequestration
stage: expert
status: draft
---

# Marine Biological Pump and Carbon Sequestration

## Core Idea
The biological pump transfers organic carbon from the euphotic zone to the deep ocean: phytoplankton fix dissolved CO₂, zooplankton graze and respire, and sinking particles transport organic matter to depth where it is remineralized. This process reduces surface CO₂ and stores carbon in the deep ocean for centuries to millennia (the soft tissue pump transfers carbon; the carbonate counter-pump involves CaCO₃ sinking). The efficiency of the biological pump is a key control on atmospheric CO₂ levels and nutrient cycling.

## How It's Best Learned
Trace the fate of phytoplankton organic matter: What fraction is respired in the upper ocean? What fraction reaches the seafloor? Use isotope tracers (C-13, C-14, radiocarbon) to quantify residence times.

## Common Misconceptions
Not all sinking organic matter is pumped to the deep; much is remineralized in the upper ocean (<200 m). The pump's efficiency depends on nutrient availability, light, and particle size, all of which vary regionally and seasonally.

## Questions

```yaml
- question: "Ocean warming is projected to increase bacterial decomposition rates, remineralizing sinking organic particles more rapidly and at shallower depths. What would be the likely climate consequence?"
  type: multiple-choice
  options:
    - "Decreased atmospheric CO₂, because faster decomposition releases more nutrients, stimulating greater phytoplankton productivity and CO₂ uptake"
    - "Increased atmospheric CO₂, because more carbon would be remineralized within the shallow, well-mixed surface layer and returned to the atmosphere more quickly"
    - "No net climate effect, because the total amount of carbon fixed by photosynthesis remains unchanged"
    - "Increased ocean acidification only, with no direct effect on atmospheric CO₂"
  answer: 1
  explanation: "The depth of remineralization is the critical variable for climate impact. Carbon remineralized above the thermocline returns to the surface mixed layer and equilibrates with the atmosphere on timescales of years to decades. Carbon remineralized below the permanent thermocline is sequestered from the atmosphere for the duration of the ocean's deep overturning circulation — centuries to a millennium. Shallower remineralization means more carbon cycles back into the atmosphere quickly, weakening the biological pump as a climate regulator. This is a key positive feedback in warming scenarios: higher temperatures reduce pump efficiency, releasing more CO₂, causing more warming."

- question: "Coccolithophores are calcifying phytoplankton that build CaCO₃ shells. What is the direct effect of CaCO₃ formation at the sea surface on the surrounding seawater's CO₂ concentration?"
  type: multiple-choice
  options:
    - "It decreases seawater CO₂ by incorporating dissolved inorganic carbon into the shells, which are then removed when they sink"
    - "It has no immediate effect on seawater CO₂; only the sinking and dissolution of shells affects carbon chemistry"
    - "It increases seawater CO₂ by shifting the carbonate equilibrium — forming CaCO₃ from bicarbonate releases CO₂ to the surrounding water"
    - "The effect depends on depth: it releases CO₂ in shallow water but absorbs CO₂ in deep water"
  answer: 2
  explanation: "The reaction Ca²⁺ + 2HCO₃⁻ → CaCO₃ + H₂O + CO₂ releases CO₂ at the surface, counterintuitively making CaCO₃-forming organisms a local source of CO₂ even while they are sequestering carbon in their shells. This is why the carbonate pump is sometimes called the 'carbonate counter-pump' — it partially offsets the soft-tissue pump's CO₂ drawdown at the surface. The sinking and dissolution of CaCO₃ at depth does increase deep-ocean alkalinity and the ocean's long-term CO₂ absorption capacity, but the surface signal is a CO₂ release."

- question: "The climate significance of the biological pump depends more on the depth at which organic carbon is remineralized than on the total amount of carbon that leaves the surface euphotic zone."
  type: true-false
  answer: true
  explanation: "This is the key insight for understanding the pump's climate relevance. Carbon remineralized at 100 m depth is back in the surface ocean within months to years, effectively bypassing sequestration. Carbon remineralized at 1,000 m or deeper is removed from atmospheric contact for centuries. The Martin curve shows that ~90% of exported carbon is remineralized above 1,000 m — only the remaining fraction that reaches depth contributes to long-term sequestration. A pump that exports a lot of carbon but remineralizes it all at 200 m provides far less climate regulation than a pump that exports less carbon but delivers a higher fraction to deep waters."

- question: "The biological pump transfers most of the organic carbon fixed by phytoplankton in the euphotic zone to the deep seafloor, where it is stored for centuries."
  type: true-false
  answer: false
  explanation: "This dramatically overstates the pump's efficiency. Of the organic carbon fixed by phytoplankton, roughly 10–20% is exported below the euphotic zone (~200 m) as sinking particles, and of that, approximately 90% is remineralized before reaching 1,000 m. Only about 1–3% of total surface production ultimately reaches the seafloor. The pump is a highly 'leaky' system — the vast majority of photosynthetically fixed carbon is recycled within the surface ocean. What matters climatically is not that the pump is efficient, but that even the small fraction that escapes to depth can significantly reduce atmospheric CO₂ compared to a world without any biological pump."

- question: "Explain why the carbonate pump is sometimes called the 'carbonate counter-pump' — what does it counteract, and through what mechanism?"
  type: short-answer
  answer: "The soft-tissue pump removes CO₂ from the surface ocean by fixing it into organic matter that sinks. The carbonate pump partially opposes this at the surface: when calcifying organisms form CaCO₃ shells from dissolved bicarbonate ions, the reaction releases CO₂ into the surrounding seawater (Ca²⁺ + 2HCO₃⁻ → CaCO₃ + H₂O + CO₂). This increases surface ocean pCO₂, promoting outgassing to the atmosphere — the opposite of what the soft-tissue pump does. On longer timescales, the dissolution of CaCO₃ at depth raises deep-ocean alkalinity and enhances the ocean's overall capacity to absorb atmospheric CO₂, but the surface signal remains a net CO₂ source. The ratio of organic carbon to CaCO₃ in sinking material (the 'rain ratio') therefore significantly affects whether the biological pump is a net atmospheric CO₂ sink."
  explanation: "The counter-pump concept is one of the non-obvious features of marine carbon chemistry and a frequent source of confusion. The intuitive expectation — that organisms building carbon-based shells should remove CO₂ — is wrong for the inorganic carbonate pathway because of carbonate chemistry. This distinction has practical importance for climate projections: ocean acidification (lower pH) slows calcification in many organisms, which might seem like it would reduce the counter-pump effect and increase net CO₂ uptake, but the reality is more complex because acidification also reduces carbonate ion concentrations needed for shell formation."
```

## Explainer

From your study of marine primary productivity, you know that phytoplankton in the sunlit surface ocean fix dissolved CO₂ into organic matter through photosynthesis. The **biological pump** is the set of processes that transfers some of this organic carbon downward into the deep ocean, effectively removing it from contact with the atmosphere for centuries to millennia. Without the biological pump, atmospheric CO₂ would be roughly 200 ppm higher than it is — making it one of the most important regulators of Earth's carbon cycle and climate.

The pump operates through a chain of biological and physical processes. Phytoplankton grow in the **euphotic zone** (the upper ~200 m where light penetrates), taking up dissolved CO₂ and nutrients like nitrogen, phosphorus, and iron. When these organisms die, are consumed by zooplankton, or aggregate into larger particles, some fraction sinks as **marine snow** — a slow rain of organic debris, fecal pellets, and dead cells falling through the water column. Zooplankton also contribute through **diel vertical migration**: they feed at the surface at night and descend to depth during the day, respiring surface-derived carbon at depth. The sinking particles and migrating organisms carry carbon downward against the concentration gradient that would otherwise keep it dissolved near the surface.

The efficiency of this transfer is far from complete. Most organic matter never reaches the deep ocean. Bacteria and zooplankton **remineralize** (decompose) sinking particles as they fall, converting organic carbon back to dissolved CO₂ and releasing nutrients. The **Martin curve** describes this attenuation: roughly 90% of the export production is remineralized in the upper 1,000 meters. Only about 1–3% of surface production reaches the seafloor. What matters climatically is the depth at which remineralization occurs — carbon remineralized below the permanent thermocline is effectively sequestered from the atmosphere for the ocean's overturning timescale (centuries to a millennium), while carbon remineralized in the upper ocean returns to the surface and atmosphere much faster.

A second component of the pump operates through inorganic carbon. Organisms like coccolithophores and foraminifera build calcium carbonate (CaCO₃) shells that also sink to depth — the **carbonate pump**. Counterintuitively, CaCO₃ production actually releases CO₂ to the surrounding water (because forming CaCO₃ from dissolved bicarbonate shifts the carbonate equilibrium toward CO₂), so the carbonate pump partially opposes the soft-tissue pump at the surface. However, the sinking and dissolution of CaCO₃ at depth increases deep-ocean alkalinity, which on longer timescales enhances the ocean's overall capacity to absorb atmospheric CO₂. The balance between the soft-tissue pump and the carbonate pump, and how each responds to warming, acidification, and changing nutrient supply, is central to predicting the ocean's future role as a carbon sink.
