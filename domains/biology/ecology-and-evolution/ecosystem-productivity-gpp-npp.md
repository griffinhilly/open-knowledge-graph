---
id: ecosystem-productivity-gpp-npp
title: 'Ecosystem Productivity: GPP and NPP'
domain: biology
course: ecology-and-evolution
prerequisites:
- id: photosynthesis-overview
  type: hard
- id: cellular-respiration-overview
  type: hard
- id: ecosystem-structure-and-function
  type: hard
builds-toward:
- energy-flow-in-ecosystems
- energy-pyramid-efficiency-trophic-transfer
tags:
- productivity
- gpp
- npp
- photosynthesis
stage: formal-systems
status: validated
---

# Ecosystem Productivity: GPP and NPP

## Core Idea
Gross Primary Productivity (GPP) is the total solar energy fixed by producers through photosynthesis. Net Primary Productivity (NPP) is GPP minus energy lost to respiration by producers themselves. NPP represents the energy available to consumers and is the true measure of organic matter accumulation in an ecosystem.

## Questions

```yaml
- question: "A forest has a GPP of 2,000 g C/m²/year. Autotrophic respiration consumes 800 g C/m²/year. A researcher asks: how much carbon is actually available to herbivores and decomposers? Which answer is correct?"
  type: multiple-choice
  options:
    - "2,000 g C/m²/year — all photosynthetically fixed carbon is available to the food web"
    - "1,200 g C/m²/year — NPP = GPP minus autotrophic respiration"
    - "800 g C/m²/year — respiration represents the net energy gain of the ecosystem"
    - "2,800 g C/m²/year — GPP and respiration together represent total carbon turnover"
  answer: 1
  explanation: "NPP = GPP − Ra = 2,000 − 800 = 1,200 g C/m²/year. Only this remainder — the carbon fixed beyond what producers use for their own metabolism — accumulates as biomass available to consumers. The most common error is treating GPP (total photosynthesis) as the energy available to the food web, ignoring that producers must burn a large fraction of their own production just to stay alive and grow."

- question: "Two ecosystems have equal GPP. Ecosystem A's NPP is 90% of its GPP. Ecosystem B's NPP is only 35% of its GPP. Which statement best describes the consequence for animal communities?"
  type: multiple-choice
  options:
    - "Both ecosystems support equal animal biomass because their GPP is identical"
    - "Ecosystem B supports more animals because higher autotrophic respiration indicates more metabolic activity"
    - "Ecosystem A can support substantially more consumer biomass because a larger fraction of fixed carbon becomes available as biomass — NPP, not GPP, is the constraint on food webs"
    - "GPP is the only ecologically relevant productivity measure; NPP/GPP ratio is a technical detail"
  answer: 2
  explanation: "Consumer biomass is ultimately constrained by NPP — the energy that actually enters the food web as biomass. Ecosystem A has NPP ≈ 0.90 × GPP while Ecosystem B has NPP ≈ 0.35 × GPP. Even with identical GPP, Ecosystem A has roughly 2.6× more energy available to herbivores and decomposers. Comparing GPP values without accounting for autotrophic respiration gives a misleading picture of how much the ecosystem can actually support."

- question: "NPP, not GPP, determines the maximum biomass available to herbivores and all higher trophic levels."
  type: true-false
  answer: true
  explanation: "GPP includes energy that producers use for their own cellular respiration (Ra) — energy that is converted to heat and never enters the food web as biomass. Only NPP (GPP − Ra) accumulates as plant tissue — leaves, wood, seeds, roots — that consumers can eat or decomposers can break down. NPP is the fundamental energy budget constraint on everything above the producer level in a food web."

- question: "A region with high GPP necessarily supports more consumer biomass than a region with lower GPP."
  type: true-false
  answer: false
  explanation: "What matters is NPP (GPP − Ra), not GPP alone. A high-GPP ecosystem with very high autotrophic respiration rates may have lower NPP than a lower-GPP ecosystem whose producers are more efficient at converting fixed carbon to biomass. Consumer biomass is constrained by NPP. Two ecosystems with the same GPP can support dramatically different food webs depending on how much of that GPP the producers themselves consume. Comparing GPP without knowing Ra leads to incorrect predictions."

- question: "Why do ecologists use NPP rather than GPP as the key measure of ecosystem productivity when studying food webs and energy flow?"
  type: short-answer
  answer: "Because GPP includes the energy producers use for their own metabolism (autotrophic respiration, Ra), which is never available to consumers. NPP = GPP − Ra is what actually accumulates as biomass — the plant tissue that herbivores eat and decomposers process. NPP is the energy 'available to the rest of the food web,' so it is the true constraint on how many organisms the ecosystem can support at higher trophic levels. GPP tells you how much sunlight the ecosystem captures; NPP tells you how much of that capture actually enters the food web."
  explanation: "The factory analogy from the explainer captures this: GPP is total production-line output, Ra is the energy cost of running the factory (workers' meals, machinery, lighting), and NPP is the finished goods available for consumers. You cannot feed consumers with the energy used to run the factory."
```

## Explainer

From your study of photosynthesis, you know that plants, algae, and cyanobacteria capture light energy and convert it to chemical energy stored in organic molecules like glucose. From cellular respiration, you know that organisms break down those same molecules to fuel their own metabolism, releasing energy as ATP and heat. **Ecosystem productivity** quantifies this energy capture at the scale of an entire ecosystem and asks a deceptively simple question: how much new organic matter does this system produce over a given period of time?

**Gross Primary Productivity (GPP)** is the total amount of energy (or carbon) fixed by all the producers in an ecosystem through photosynthesis. Think of it as total revenue before expenses. A tropical rainforest with dense canopy cover, abundant water, and year-round sunlight has an enormous GPP — its plants are photosynthesizing at high rates continuously. But the plants themselves are alive, and living costs energy. Every plant cell runs cellular respiration around the clock to maintain its structures, grow, and reproduce. The energy consumed by the producers' own respiration is the "expense." **Net Primary Productivity (NPP)** is what remains after subtracting this cost: NPP = GPP − R_a, where R_a is autotrophic (producer) respiration. NPP represents the actual accumulation of new biomass — the leaves, wood, roots, and seeds that were not burned for the plant's own energy needs.

Why does NPP matter more than GPP for understanding ecosystems? Because NPP is the energy budget available to every other organism in the system. Herbivores eat plant tissue (NPP), carnivores eat herbivores, and decomposers process dead organic matter. If you want to know how many deer a forest can support, or how many tons of fish a lake can yield, NPP is the starting constraint. Typical values span orders of magnitude: tropical rainforests produce roughly 1,000–2,000 g C/m²/year, temperate grasslands around 200–600, and open ocean deserts as little as 30–50. The main factors controlling NPP are **temperature**, **precipitation**, **nutrient availability** (especially nitrogen and phosphorus), and **light**. In terrestrial ecosystems, rainfall and temperature are the strongest predictors; in aquatic systems, nutrient supply and light penetration dominate.

A useful analogy: imagine a factory (the ecosystem) where workers (producers) manufacture goods (organic matter). GPP is the total production line output. But the workers need to eat lunch, heat the building, and maintain the machines — that is autotrophic respiration. NPP is the finished goods that leave the factory and become available for consumers to purchase. Understanding this distinction is the foundation for tracing **energy flow** through trophic levels and calculating the ecological efficiencies you will encounter next — why only about 10% of one trophic level's energy typically transfers to the next, and why top predators are always rare.
