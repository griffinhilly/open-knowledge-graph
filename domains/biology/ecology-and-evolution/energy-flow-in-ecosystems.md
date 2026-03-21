---
id: energy-flow-in-ecosystems
title: Energy Flow and Ecological Efficiency
domain: biology
course: ecology-and-evolution
prerequisites:
- id: trophic-levels-and-food-webs
  type: hard
- id: cellular-respiration-overview
  type: soft
builds-toward:
- biogeochemical-cycles
- nutrient-cycling
tags:
- ecological-efficiency
- trophic-pyramid
- 10-percent-rule
- primary-productivity
stage: advanced
status: validated
---

# Energy Flow and Ecological Efficiency

## Core Idea
Energy flows unidirectionally through ecosystems: solar energy is captured by producers through photosynthesis (gross primary productivity, GPP), with net primary productivity (NPP = GPP − respiration) available to consumers. Ecological efficiency averages roughly 10% between trophic levels — about 90% of energy is lost as heat through respiration, excretion, and inefficient consumption. This explains why food chains are short (typically 3–5 levels) and why biomass pyramids are narrow at the top. Unlike nutrients, energy cannot be recycled; it must continuously enter ecosystems from solar input.

## How It's Best Learned
Calculate how much primary productivity is needed to support a top predator through multiple trophic transfers. Compare ecological efficiency across different ecosystem types. Construct biomass and energy pyramids and understand why inverted biomass pyramids (e.g., phytoplankton supporting zooplankton) are possible but inverted energy pyramids are not.

## Common Misconceptions
- The 10% rule is an approximation; actual efficiencies range from 5–20% and vary by ecosystem and organism type.
- Energy is not 'recycled' like nutrients — each trophic transfer degrades usable energy irreversibly into heat.
- High biomass at lower trophic levels does not always mean higher energy flow — turnover rate matters.

## Questions

```yaml
- question: "Why are food chains typically limited to 3–5 trophic levels?"
  type: multiple-choice
  options:
    - "Predators become too large to find enough prey above 5 levels, limiting further chain extension"
    - "Each trophic transfer loses roughly 90% of available energy, so little energy remains to support another level after 4–5 transfers"
    - "Longer food chains are unstable because top predators outcompete each other"
    - "Nutrient recycling becomes inefficient beyond 5 trophic levels, limiting productivity"
  answer: 1
  explanation: "The ~10% efficiency rule means energy diminishes geometrically: if producers fix 10,000 kcal, primary consumers capture ~1,000, secondary consumers ~100, tertiary ~10. After 4–5 transfers, the remaining energy pool is too small to support a viable population of another predator. This is a thermodynamic constraint, not a behavioral or competitive one. Nutrients are irrelevant here — nutrients cycle, but energy does not."

- question: "In open ocean ecosystems, zooplankton sometimes have greater total biomass than the phytoplankton that support them. Which explanation is correct?"
  type: multiple-choice
  options:
    - "This violates the 10% rule and indicates the measurement methods are flawed"
    - "Phytoplankton have such high turnover rates that their low standing biomass supports more zooplankton biomass through rapid energy throughput"
    - "Marine food webs are more efficient than terrestrial ones, allowing inverted energy flow"
    - "The energy pyramid is also inverted in this case — more energy flows at the zooplankton level than the phytoplankton level"
  answer: 1
  explanation: "Biomass at a given moment (standing crop) reflects production rate minus loss rate, not energy flow rate. Phytoplankton reproduce so rapidly that even with low standing biomass, they supply enough energy to support a larger biomass of slower-reproducing zooplankton. Energy pyramids cannot invert — more energy always flows at lower levels — but biomass pyramids can invert when turnover at the base is very high. Option D is specifically wrong: energy flow is always greater at lower trophic levels."

- question: "An inverted energy pyramid — where more energy flows through a higher trophic level than through the level below it — is thermodynamically impossible."
  type: true-false
  answer: true
  explanation: "The second law of thermodynamics requires that each trophic transfer lose energy as heat through respiration, waste, and unconsumed biomass. Energy flows in only one direction (from producers upward) and is irreversibly degraded at each step. It is therefore impossible for a higher trophic level to contain or transmit more energy than the level feeding it. Biomass pyramids can invert due to differential turnover rates, but energy pyramids cannot — this distinction is fundamental."

- question: "Unlike nutrients, energy cycles through ecosystems and can be reused by organisms at multiple trophic levels."
  type: true-false
  answer: false
  explanation: "This is a critical reversal. Nutrients (nitrogen, phosphorus, carbon in many forms) do cycle through ecosystems — they are released by decomposers, taken up by producers, and passed through the food web repeatedly. Energy does not cycle. Each trophic transfer degrades useful chemical energy into heat via respiration, and heat cannot be converted back into biological work. Ecosystems therefore require continuous energy input from the sun — they are open systems with respect to energy but nearly closed systems with respect to nutrients."

- question: "Why can biomass pyramids be inverted while energy pyramids cannot, even in the same ecosystem?"
  type: short-answer
  answer: "Biomass is a measurement of how much organic material exists at a given moment (standing crop), while energy flow measures how much energy passes through a trophic level per unit time. If organisms at a lower level reproduce and die very rapidly (high turnover rate), the standing biomass at any moment can be low even though the total energy flux through that level is high. In open ocean ecosystems, phytoplankton have turnover times of days, so zooplankton can accumulate more standing biomass than the phytoplankton present at any snapshot in time. But energy flow must always decrease up the pyramid because ~90% is lost at each transfer to heat — no amount of turnover rate can cause more energy to flow out of a level than flows into it."
  explanation: "The key distinction is snapshot (biomass) versus flux (energy flow). This is why both measurements are necessary to understand ecosystem function — biomass alone can be misleading about the actual energy dynamics."
```

## Explainer

From your study of trophic levels and food webs, you know that organisms are organized into feeding levels — producers, primary consumers, secondary consumers, and so on. From cellular respiration, you know that organisms extract energy from organic molecules and lose much of it as heat. **Energy flow** connects these ideas: it traces how energy enters an ecosystem, passes through trophic levels, and is progressively lost, explaining fundamental patterns like why there are more plants than herbivores and more herbivores than top predators.

Energy enters most ecosystems as sunlight captured by **primary producers** through photosynthesis. The total energy fixed is called **gross primary productivity (GPP)**, but producers use a substantial fraction of this energy for their own respiration — building and maintaining cells, growing roots, reproducing. What remains after the producers' own metabolic costs is **net primary productivity (NPP)**, and this is the energy actually available to the rest of the food web. NPP varies enormously across ecosystems: tropical rainforests and coral reefs are highly productive, while deserts and open oceans produce far less per unit area. Understanding NPP tells you the energy budget that herbivores, predators, and decomposers must share.

The critical concept is **ecological efficiency** — the fraction of energy at one trophic level that gets transferred to the next. On average, this is roughly **10%**, though it varies from about 5% to 20% depending on the organisms and ecosystem. The other 90% is lost through three main pathways: metabolic heat from respiration (organisms burn energy to live), unconsumed biomass (not all plant material gets eaten; not all prey gets caught), and undigested material (feces and other waste). This compounding loss explains the **pyramid of energy**: if producers fix 10,000 kcal, herbivores capture about 1,000, secondary consumers about 100, and tertiary consumers about 10. After just four or five transfers, there is simply not enough energy left to support another trophic level — this is why food chains rarely exceed five links.

Unlike nutrients, which cycle through ecosystems and can be reused indefinitely, energy follows the second law of thermodynamics: with each transfer, usable energy is irreversibly degraded into heat. An ecosystem is therefore an open system that requires continuous energy input from the sun. This has practical consequences: producing a kilogram of beef requires roughly ten times the plant biomass as producing a kilogram of grain for direct human consumption, because each trophic transfer loses ~90% of the energy. It also explains why biomass pyramids can occasionally appear inverted — in open ocean ecosystems, phytoplankton have low standing biomass but reproduce so rapidly (high **turnover rate**) that they support a larger biomass of zooplankton at any given moment — but energy pyramids never invert, because thermodynamics does not permit more energy to flow out of a level than flows in.
