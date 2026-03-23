---
id: marine-food-webs
title: Marine Food Webs and Trophic Structure
domain: earth-and-space-sciences
course: oceanography
prerequisites:
- id: marine-primary-productivity
  type: hard
- id: climate-zones-and-biomes
  type: soft
builds-toward:
- coral-reef-ecosystems
- deep-sea-ecosystems
tags:
- food web
- zooplankton
- trophic levels
- trophic efficiency
- pelagic ecosystem
stage: formal-systems
status: validated
---

# Marine Food Webs and Trophic Structure

## Core Idea
Marine food webs transfer energy from phytoplankton (primary producers) through zooplankton, small fish, and up to top predators. Trophic efficiency is typically ~10%, meaning 90% of energy is lost at each trophic transfer. Short food chains (e.g., phytoplankton → krill → whale) are more energy-efficient than long ones. The microbial loop — decomposers and bacteria recycling dissolved organic matter — also plays a critical role in nutrient cycling. Pelagic (open water) and benthic (seafloor) food webs are coupled through the sinking of organic particles.

## How It's Best Learned
Calculate biomass at each trophic level given a known primary production rate and 10% trophic efficiency. Compare the relative fish yields of upwelling zones (short food chains) versus oligotrophic gyres (long food chains).

## Common Misconceptions
- Food webs are not simple food chains — most species eat at multiple trophic levels and energy flows through many pathways.
- The microbial loop is not a dead-end — it recycles nutrients back into the food web rather than simply decomposing matter.

## Questions

```yaml
- question: "Two ocean regions each produce 10,000 units of carbon via photosynthesis annually. Region A has a 3-step food chain (phytoplankton → zooplankton → fish). Region B has a 5-step food chain. Assuming 10% trophic efficiency, how much more energy reaches the top predator in Region A than Region B?"
  type: multiple-choice
  options:
    - "The same — total primary production determines total biomass at every level"
    - "10× more — each extra trophic step multiplies available energy by 10"
    - "100× more — two extra trophic steps each lose 90%, compounding to 1% of Region A's top-level energy"
    - "2× more — each trophic level removes a fixed amount, not a percentage"
  answer: 2
  explanation: "At 10% trophic efficiency, each step retains 10% of the previous level's energy. Region A (3 steps): 10,000 × 0.1 × 0.1 = 10 units at the top. Region B (5 steps): 10,000 × 0.1⁴ = 0.1 units at the top. Region A has 100× more energy available to top predators. This is why the world's most productive fisheries are in upwelling zones with short food chains, not in vast oligotrophic gyres with long chains."

- question: "What is the role of the microbial loop in marine ecosystems?"
  type: multiple-choice
  options:
    - "It decomposes organic matter into inorganic nutrients that sink to the seafloor permanently"
    - "It recycles dissolved organic carbon through bacteria and protists back into the classical food web"
    - "It short-circuits the food web by converting phytoplankton directly into fish biomass"
    - "It is a dead-end pathway that consumes but does not return energy to higher trophic levels"
  answer: 1
  explanation: "The microbial loop is not a dead end. When phytoplankton and other organisms release dissolved organic matter, bacteria consume it and convert it back to particulate biomass. These bacteria are then grazed by protists, which are eaten by larger zooplankton — funneling dissolved carbon back into the classical food web. In nutrient-poor oligotrophic waters, the microbial loop can process more carbon than the direct phytoplankton-to-zooplankton pathway."

- question: "The vast oligotrophic open ocean gyres produce more total fish biomass than coastal upwelling zones because they cover a much larger ocean area."
  type: true-false
  answer: false
  explanation: "Coverage area does not compensate for the combination of low primary productivity AND long food chains in oligotrophic gyres. These regions have sparse phytoplankton (starting energy is low) and support long food chains with many trophic steps (compounding energy loss). Upwelling zones have high primary productivity and typically short food chains (phytoplankton → zooplankton → fish), making them far more productive per unit area despite covering a fraction of the ocean. The world's major commercial fisheries concentrate in upwelling zones and continental shelves."

- question: "Dissolved organic matter released by phytoplankton (through excretion and cell lysis) eventually re-enters the classical food web through bacterial processing."
  type: true-false
  answer: true
  explanation: "This is the microbial loop: bacteria consume dissolved organic matter and convert it back into particulate biomass, which is then grazed by protists (nanoflagellates, ciliates), which are in turn consumed by larger zooplankton that connect back to the classical food web. This pathway was only discovered in the 1980s but is now understood to be the dominant energy conduit in nutrient-poor waters, not a decomposition dead-end."

- question: "Explain why shortening a marine food chain by one trophic level dramatically increases the amount of fish biomass available for harvest from the same primary production."
  type: short-answer
  answer: "Trophic efficiency is approximately 10%, meaning 90% of energy is lost at each transfer as metabolic heat, waste, and incomplete digestion. Removing one trophic level multiplies the energy reaching the harvest level by ~10×. For example, if phytoplankton produce 10,000 units: a 4-step chain yields ~10 units at the top, while a 3-step chain yields ~100 units — a 10-fold increase. This is why krill-eating species (like herring, anchovies, and baleen whales) support far more biomass than tuna, which sit multiple steps above the base."
  explanation: "This principle has direct fisheries implications. Upwelling zones (like Peru/Chile, Benguela current, Somali coast) have short food chains because large diatom phytoplankton bloom directly support large zooplankton like copepods and krill, which in turn support anchovies and sardines. These regions produce disproportionate fractions of global fish catch despite covering a small fraction of ocean area. In contrast, oligotrophic gyres cover ~40% of Earth's surface but contribute minimally to fisheries."
```

## Explainer

From your study of marine primary productivity, you know that phytoplankton at the ocean surface fix carbon using sunlight — they are the base of nearly all marine life. A **food web** maps how that energy flows upward through the ecosystem: who eats whom, and how much energy survives each transfer. Unlike a simple food chain (a single linear sequence), a food web is a network with many branching and overlapping pathways, reflecting the reality that most marine organisms feed at multiple levels and switch prey depending on availability.

The central quantitative fact about marine food webs is **trophic efficiency** — roughly 10% of the energy at one level passes to the next. The other 90% is lost as metabolic heat, waste, and incomplete digestion. This has enormous practical consequences. Consider a productive upwelling zone where phytoplankton fix 10,000 units of carbon. If krill eat the phytoplankton (one step) and whales eat the krill (two steps), the whales receive about 100 units — a short, efficient chain. Now consider an oligotrophic gyre where tiny phytoplankton are eaten by nanoflagellates, then by copepods, then by small fish, then by tuna — four transfers, leaving only about 1 unit at the top. This is why the world's most productive fisheries cluster around upwelling zones and continental shelves, not the vast open ocean, even though the open ocean covers far more area.

Running alongside the classical food web is the **microbial loop**, a parallel pathway that was only recognized in the 1980s. When phytoplankton and other organisms release dissolved organic matter (through excretion, sloppy feeding, or cell lysis), bacteria consume it and convert it back into particulate biomass. These bacteria are then grazed by protists, which are in turn eaten by larger zooplankton — funneling dissolved carbon back into the classical web. In nutrient-poor waters, the microbial loop can process more carbon than the direct phytoplankton-to-zooplankton pathway, making it the dominant energy conduit in much of the ocean.

The pelagic (open water) and **benthic** (seafloor) food webs are not independent systems — they are coupled by the rain of organic particles sinking from the surface, called **marine snow**. Dead phytoplankton, fecal pellets, and aggregates drift downward, delivering food to organisms on the deep seafloor that never see sunlight. The efficiency of this biological pump determines how much surface production reaches the deep ocean, influencing both deep-sea ecosystem richness and the ocean's capacity to sequester carbon. Where surface productivity is high, the seafloor community beneath is richer; where it is low, the deep benthos is sparse. Understanding marine food webs thus connects surface ecology to deep-ocean biogeochemistry and, ultimately, to the global carbon cycle.
