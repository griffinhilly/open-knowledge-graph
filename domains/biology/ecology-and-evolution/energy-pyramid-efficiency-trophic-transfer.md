---
id: energy-pyramid-efficiency-trophic-transfer
title: Energy Pyramids and Trophic Transfer Efficiency
domain: biology
course: ecology-and-evolution
prerequisites:
- id: trophic-levels-and-food-webs
  type: hard
- id: ecosystem-productivity-gpp-npp
  type: hard
builds-toward:
- population-growth-models
- predator-prey-dynamics
tags:
- energy
- pyramids
- trophic-efficiency
- 10-percent-rule
stage: advanced
status: draft
---

# Energy Pyramids and Trophic Transfer Efficiency

## Core Idea
Energy decreases at each trophic level due to metabolic costs, growth, and movement. Approximately 10% of energy transfers from one trophic level to the next (ranging from 5-20% depending on ecosystem). This creates pyramids of energy and biomass, with progressively fewer organisms at higher trophic levels.

## Questions

```yaml
- question: "An ecosystem has net primary productivity of 10,000 kcal/m²/year. Using the 10% rule, how much energy is available to primary carnivores (organisms that eat herbivores)?"
  type: multiple-choice
  options:
    - "1,000 kcal — primary carnivores are one step from the producers"
    - "100 kcal — energy passes through herbivores first, losing 90% at each step"
    - "10 kcal — two 10% transfers occur between producers and primary carnivores"
    - "500 kcal — half the energy is lost at each trophic transfer"
  answer: 1
  explanation: "The chain is: producers (10,000 kcal) → herbivores (1,000 kcal, after 90% loss) → primary carnivores (100 kcal, after another 90% loss). Primary carnivores are at the third trophic level, two steps from producers, so two 10% transfers have occurred: 10,000 × 0.1 × 0.1 = 100 kcal. Option A (1,000 kcal) reflects the common error of counting only one step."

- question: "Why are apex predators typically rare in ecosystems, despite being the most powerful animals in their food web?"
  type: multiple-choice
  options:
    - "They reproduce slowly and invest heavily in each offspring, limiting population growth"
    - "Intense competition among apex predators eliminates most individuals"
    - "Cumulative energy losses at each trophic transfer leave very little energy to support top-level populations"
    - "Apex predators are inefficient hunters who waste most of the prey they catch"
  answer: 2
  explanation: "Apex predators are rare because thermodynamics, not biology, limits them. With ~10% efficiency at each step, a food chain starting at 10,000 kcal/m²/year leaves only about 10 kcal by the fourth trophic level — far too little to support a dense population. Options A and B may be true in some cases but are secondary; the fundamental constraint is energetic. Option D is backwards — apex predators are often efficient hunters, but efficiency of hunting has nothing to do with the energy available at their trophic level."

- question: "Endothermic animals (birds and mammals) tend to have higher trophic transfer efficiency than ectotherms (fish, insects) because they can sustain higher metabolic rates."
  type: true-false
  answer: false
  explanation: "False — the relationship is inverted. Endotherms burn enormous energy maintaining body temperature, leaving less energy available for growth and reproduction (biomass production). Their trophic transfer efficiency is typically only 1–5%. Ectotherms, by contrast, do not spend energy on thermoregulation, so more of the energy they consume can be converted into biomass — giving them efficiencies of 10–15%. This is why aquaculture of herbivorous fish is far more energy-efficient than cattle ranching."

- question: "Most energy lost between trophic levels escapes as metabolic heat through cellular respiration, rather than being lost as undigested waste."
  type: true-false
  answer: true
  explanation: "True. While some energy is lost as undigested material (feces, inedible body parts) and some prey is never consumed at all, the dominant pathway of energy loss is metabolic respiration — organisms burn calories to move, thermoregulate, grow, reproduce, and repair tissues. This metabolic heat is the 'thermodynamic tax' that explains the ~90% loss at each level. Understanding this distinguishes the energy pyramid from a simple feeding efficiency story: it reflects the second law of thermodynamics operating in living systems."

- question: "Explain why food chains rarely extend beyond 4–5 trophic levels, using the logic of trophic transfer efficiency."
  type: short-answer
  answer: "With approximately 10% efficiency at each trophic transfer, energy diminishes by an order of magnitude at every level. Starting from 10,000 kcal of net primary productivity: herbivores receive ~1,000 kcal, primary carnivores ~100 kcal, secondary carnivores ~10 kcal, and a fifth level would have only ~1 kcal — too little to sustain a viable population. This is a hard thermodynamic constraint: it doesn't matter how efficient the predators are as hunters; there simply isn't enough energy flowing through the top levels to support another trophic tier."
  explanation: "The key insight is that short food chains are not a biological accident but a thermodynamic necessity. Every trophic level is an energy bottleneck. The 10% rule is an approximation — actual efficiency ranges from 1–20% depending on ecosystem and organism type — but even the most efficient chains cannot extend indefinitely without an implausibly large base. This also explains why the total biomass supported at higher trophic levels is so much smaller than at lower levels, forming the characteristic pyramid shape."
```

## Explainer

From trophic levels and food webs, you know that energy enters ecosystems through producers (plants, algae, chemotrophs) and flows upward through herbivores, predators, and top predators. From ecosystem productivity, you know the difference between gross primary productivity (GPP) and net primary productivity (NPP) — the total energy fixed by photosynthesis minus what plants use for their own respiration. **Energy pyramids** visualize what happens to that energy as it passes through the food web, and the picture is dramatic: at every step, most of the energy disappears.

The **10% rule** is a rough but useful approximation: only about 10% of the energy available at one trophic level is converted into biomass at the next level. Where does the other 90% go? Most is lost as **metabolic heat** through cellular respiration — organisms burn calories to maintain body temperature, move, grow, reproduce, and repair tissues. Some energy is never consumed at all: leaves fall and decompose, prey animals escape predation, and inedible structures like bones and shells pass through the food web without being assimilated. Of the food that is consumed, a portion passes through the digestive system undigested and enters the detrital pathway. Only the fraction that is both consumed and assimilated — then allocated to growth and reproduction rather than respiration — becomes available to the next trophic level.

This relentless energy loss explains why food chains are typically short — usually only 4 or 5 links. Consider a concrete example: if a grassland fixes 10,000 kcal/m²/year of net primary productivity, herbivores (grasshoppers, cattle) capture roughly 1,000 kcal. Primary carnivores (frogs, small birds) get about 100 kcal. Secondary carnivores (hawks, snakes) get roughly 10 kcal. By the time you reach a top predator, there simply is not enough energy to support a viable population. This is why **apex predators are rare** — not because they are inefficient hunters, but because the thermodynamic tax on energy transfer leaves very little for the top of the pyramid.

The actual **trophic transfer efficiency** varies considerably across ecosystems and organism types. Ectotherms (cold-blooded animals like insects and fish) tend to have higher efficiencies (around 10–15%) because they spend less energy on maintaining body temperature. Endotherms (birds and mammals) are less efficient (often 1–5%) because they burn enormous amounts of energy generating heat. Aquatic ecosystems often show higher transfer efficiencies than terrestrial ones because phytoplankton are small, fast-growing, and almost entirely edible, whereas terrestrial plants invest heavily in inedible structural tissue like wood and bark. These differences have practical consequences: aquaculture of herbivorous fish is far more energy-efficient than cattle ranching, and ecosystems dominated by ectothermic food webs can support relatively more biomass at higher trophic levels. The energy pyramid is not just an ecological diagram — it is a fundamental constraint shaped by thermodynamics that determines the structure, length, and productivity of every food web on Earth.
