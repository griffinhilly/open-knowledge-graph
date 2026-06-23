---
id: marine-food-web-energy-transfer
title: Marine Food Web Structure and Energy Transfer
domain: earth-and-space-sciences
course: oceanography
prerequisites:
- id: marine-food-webs
  type: hard
- id: zooplankton-food-web-structure
  type: hard
- id: phytoplankton-productivity-limiting-factors
  type: soft
builds-toward:
- coral-reef-ecosystems
- deep-sea-ecosystems
tags:
- food-web
- energy-flow
- trophic-levels
- efficiency
- bioaccumulation
stage: formal-systems
status: validated
---

# Marine Food Web Structure and Energy Transfer

## Core Idea
Energy flows from phytoplankton (primary producers) through zooplankton to fish and marine mammals, with approximately 10% energy transfer efficiency per trophic level. Food web structure and energy flow pathways vary dramatically between upwelling regions (short food chains, large fish), tropical reefs (diverse webs), and deep ocean (chemosynthetic base).

## Questions

```yaml
- question: "A coastal upwelling region and a tropical oligotrophic gyre each fix exactly the same amount of primary production per year. Which ecosystem produces more harvestable fish per unit of primary production, and why?"
  type: multiple-choice
  options:
    - "The tropical gyre — greater biodiversity creates more complex food webs that ultimately support more fish"
    - "The upwelling region — its shorter food chain (fewer trophic steps from phytoplankton to fish) means more energy reaches the fish level"
    - "Both produce the same amount — total fish production depends only on total primary production, not food chain length"
    - "The upwelling region, but only because of higher water temperatures that accelerate fish metabolism"
  answer: 1
  explanation: "With 10% efficiency per trophic level, every additional step costs 90% of the energy. In an upwelling region, large diatoms are grazed by large zooplankton, which are eaten directly by schooling fish (3 links from sunlight to fish). In the oligotrophic gyre, the food chain is longer — small picoplankton → microzooplankton → mesozooplankton → small fish → larger fish (5+ links). A 3-link chain delivers ~1% of primary production to fish; a 5-link chain delivers only 0.01% — a 100-fold difference. Option A reverses the logic: biodiversity (longer webs) reduces, not increases, energy efficiency to large fish."

- question: "A great white shark has extremely high mercury concentrations in its tissues despite living in open ocean water with very low dissolved mercury levels. What best explains this?"
  type: multiple-choice
  options:
    - "Sharks produce mercury internally as a byproduct of their unique metabolic pathways"
    - "Mercury bioaccumulates at each trophic transfer — the shark consumes many prey items, each of which concentrated mercury from their own food, amplifying the toxin exponentially up the chain"
    - "Mercury in seawater is selectively absorbed through shark skin and gill membranes over decades"
    - "Sharks filter large volumes of water, removing and concentrating dissolved mercury through gill filtration"
  answer: 1
  explanation: "Bioaccumulation follows the same logic as trophic energy transfer, but in reverse for persistent toxins. Unlike energy (which is lost at each step), toxins like mercury (as methylmercury) are not metabolized or excreted efficiently — they are retained in tissues. Each predator consumes many prey items, accumulating the mercury burden of all of them. A shark at trophic level 5 may have consumed thousands of prey items over its lifetime, each carrying concentrated mercury from their own prey. Concentrations can be 10⁷ times higher in top predators than in surrounding water."

- question: "Removing a top predator from a marine food web (e.g., overfishing sharks) has no significant impact on organisms more than one trophic level below it."
  type: true-false
  answer: false
  explanation: "This is incorrect — trophic cascades can propagate multiple levels through a food web. When top predators are removed, their prey populations typically explode (prey release), which then overgrazes the prey's food source, causing that population to collapse. A classic example: removing large predatory fish → explosion of mid-level fish → collapse of zooplankton → bloom of phytoplankton. Effects can propagate across 3–4 trophic levels and even alter habitat structure (e.g., sea otter removal → sea urchin explosion → loss of kelp forests)."

- question: "In a 4-trophic-level marine food web (phytoplankton → zooplankton → small fish → large fish), approximately 0.1% of the energy fixed by phytoplankton reaches the large fish, assuming 10% efficiency at each level."
  type: true-false
  answer: true
  explanation: "With 10% efficiency per step: phytoplankton → zooplankton retains 10%; zooplankton → small fish retains another 10% (= 1% of original); small fish → large fish retains another 10% (= 0.1% of original). Three trophic transfers at 10% each: 0.1 × 0.1 × 0.1 = 0.001 = 0.1%. This exponential decay explains why top predators are rare relative to primary producers — and why fishing down the food web (targeting smaller, lower-trophic-level fish) can sustainably yield far more biomass than fishing top predators."

- question: "Why do upwelling regions like the coast of Peru support much higher commercial fish yields than subtropical gyres, despite both being ocean systems? Use trophic efficiency in your answer."
  type: short-answer
  answer: "Upwelling regions deliver nutrient-rich deep water to the surface, fueling explosive blooms of large phytoplankton (especially diatoms). These are grazed by large zooplankton, which are eaten directly by schooling fish like anchovies — a food chain of only 3 trophic steps. Subtropical gyres support nutrient-poor waters with small picoplankton, requiring 5 or more trophic steps before energy reaches fish. Since each step loses ~90% of energy, a 3-step chain delivers ~1% of primary production as fish, while a 5-step chain delivers ~0.01% — a 100-fold difference in efficiency. Even with the same primary productivity, the shorter chain in upwelling regions produces far more harvestable fish."
  explanation: "This is why the Peruvian anchovy fishery was historically one of the world's most productive, despite the region's relatively modest size. The combination of high primary productivity AND a short food chain makes upwelling regions extraordinarily productive for large fish. When El Niño events suppress upwelling, the anchovy catch can collapse almost overnight — illustrating how tightly fish abundance is coupled to both nutrient supply and food chain length."
```

## Explainer

From your study of marine food webs and zooplankton trophic structure, you know that ocean ecosystems are built on a foundation of primary production — mostly by phytoplankton converting sunlight and dissolved nutrients into organic matter. The critical concept here is what happens to that energy as it moves upward through the web. At each **trophic level**, organisms use most of the energy they consume for their own metabolism — swimming, breathing, maintaining body temperature. Only about 10% of the energy consumed at one level becomes available to the next. This is the **10% rule of trophic efficiency**, and it has enormous consequences for how marine ecosystems are structured.

Think of it concretely: if phytoplankton in a patch of ocean fix 10,000 units of energy through photosynthesis, roughly 1,000 units are available to the zooplankton that graze on them, 100 units reach small fish, and only 10 units support a top predator like a tuna or shark. This exponential decay explains why top predators are rare compared to their prey and why the ocean cannot support unlimited fishing — removing biomass from upper trophic levels depletes a resource that took enormous primary production to build. It also explains **bioaccumulation**: toxins like mercury concentrate at each step because predators consume many prey items, accumulating whatever persistent chemicals their food contained.

The structure of the food web — not just the number of levels but the pattern of connections — varies dramatically across ocean environments. In **upwelling regions** like the coast of Peru, nutrient-rich water fuels explosive phytoplankton growth, often dominated by large diatoms. These are grazed by large zooplankton and then directly by schooling fish like anchovies. The food chain is short (just 3–4 links), which means energy transfer to harvestable fish is unusually efficient. By contrast, **oligotrophic tropical waters** support complex, highly branched webs with many trophic links. Coral reefs exemplify this: tight nutrient recycling among corals, algae, invertebrates, and hundreds of fish species creates enormous biodiversity but relatively low net export of energy. In the **deep ocean**, the base shifts entirely — hydrothermal vents and cold seeps support food webs founded on **chemosynthesis** rather than photosynthesis, with bacteria oxidizing hydrogen sulfide or methane as the primary energy source.

Understanding these patterns matters because human impacts — overfishing, nutrient pollution, and climate warming — all propagate through food web connections. Removing a mid-level predator can trigger **trophic cascades**, where prey populations explode and their food sources collapse. Warming waters shift the size structure of phytoplankton toward smaller cells, lengthening food chains and reducing the fraction of primary production that reaches fish. Energy transfer efficiency is not just an ecological curiosity — it is the quantitative framework for understanding why marine ecosystems produce what they do and how they respond to change.
