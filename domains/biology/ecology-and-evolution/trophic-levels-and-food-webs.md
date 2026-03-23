---
id: trophic-levels-and-food-webs
title: Trophic Levels and Food Webs
domain: biology
course: ecology-and-evolution
prerequisites:
- id: community-ecology-intro
  type: hard
- id: cellular-respiration-overview
  type: soft
- id: photosynthesis-overview
  type: soft
- id: species-interactions
  type: soft
builds-toward:
- energy-flow-in-ecosystems
- keystone-species
tags:
- food-web
- trophic-level
- producers
- consumers
- decomposers
stage: formal-systems
status: validated
---
# Trophic Levels and Food Webs

## Core Idea
A food web maps the feeding relationships among species in a community, with energy flowing from producers (autotrophs) through primary, secondary, and tertiary consumers (heterotrophs) to decomposers. Each feeding level is a trophic level. Food chains are linear sequences within the web; real webs are highly interconnected, conferring stability through redundancy. Omnivores feed at multiple trophic levels, and detritivores/decomposers recycle nutrients from dead organic matter. Food web structure determines how perturbations (species loss, invasions) propagate through communities.

## How It's Best Learned
Draw food webs for well-studied systems (e.g., kelp forest, grassland, salt marsh) and identify trophic positions. Trace energy flow through the web and identify which links are most important to overall stability. Compare food chain length across ecosystems and discuss why it varies.

## Common Misconceptions
- Food webs are not simple linear chains — most species feed on and are eaten by multiple others.
- Decomposers are not 'outside' the food web; they form a critical detrital pathway that processes most ecosystem energy.

## Questions

```yaml
- question: "In a grassland ecosystem, grasses are eaten by grasshoppers, grasshoppers are eaten by frogs, and frogs are eaten by hawks. A disease eliminates most of the frog population. Which outcome is most likely?"
  type: multiple-choice
  options:
    - "Grasshopper populations decline because they lose a food source"
    - "Hawk populations increase because hawks can now eat more grasshoppers directly"
    - "Grasshopper populations increase and grass biomass decreases"
    - "The ecosystem is unaffected because hawks can eat other prey"
  answer: 2
  explanation: "Removing frogs releases grasshoppers from predation pressure (a trophic cascade), causing grasshopper populations to grow. More grasshoppers consume more grass, reducing grass biomass. This illustrates how a perturbation propagates through trophic levels — removing a middle predator can have large cascading effects on both the level above (less food for hawks) and below (more consumption at lower levels)."

- question: "Decomposers such as bacteria and fungi occupy a separate, parallel energy pathway and do not interact with the main food web."
  type: true-false
  answer: false
  explanation: "Decomposers are integral to the food web, not separate from it. They break down dead organic matter (detritus) from every trophic level — dead plants, animals, and waste products — and release nutrients back into the soil and water. In most terrestrial ecosystems, the detrital pathway processes more energy than the grazing (live-plant) pathway. Nutrients released by decomposers are taken up by producers, closing the cycle."

- question: "Why are food chains in nature rarely longer than four or five trophic levels?"
  type: short-answer
  answer: "Because energy is lost at each trophic transfer — typically only about 10% of the energy at one level is available to the next. After four or five transfers, so little energy remains that sustaining a viable population of top predators becomes impossible."
  explanation: "This is the 10% rule of ecological efficiency. When a herbivore eats a plant, roughly 90% of the plant's energy is lost to respiration, heat, and indigestible material. The same occurs at every subsequent level. Starting with, say, 10,000 units of plant energy: ~1,000 reach primary consumers, ~100 reach secondary consumers, ~10 reach tertiary consumers. A fifth trophic level would have only ~1 unit of energy available — too little to sustain a population."
```

## Explainer

Every living thing needs energy, and in any ecosystem that energy enters through *producers* — organisms that fix energy from sunlight or chemical sources through photosynthesis or chemosynthesis. Plants, algae, and cyanobacteria are the classic producers. Every other organism in the ecosystem ultimately gets its energy by eating something that traced its energy back to a producer. This flow of energy through a series of who-eats-whom relationships defines the *food web*.

A *trophic level* is a feeding position in this energy hierarchy. Producers occupy level 1. *Primary consumers* (herbivores) eat producers and occupy level 2. *Secondary consumers* eat primary consumers (level 3), and *tertiary consumers* eat secondary consumers (level 4). In practice, most species do not sit neatly at a single level — an omnivore like a bear eats berries (level 2), fish (level 3 or 4), and insects (level 2 or 3), giving it a fractional trophic position. A *food web* represents all the feeding links in a community simultaneously, which is far more accurate than any single food chain.

A critical insight is how energy is *lost* at each trophic transfer. When a grasshopper eats grass, it does not absorb all the grass's energy — most is lost to heat, respiration, and indigestible material. On average, only about 10% of the energy at one trophic level is incorporated into the biomass of the next. This is called *ecological efficiency* or the 10% rule. Starting with 10,000 units of plant energy: grasshoppers capture ~1,000, frogs ~100, hawks ~10. This rapid energy loss is why food chains are short — a sixth trophic level would have almost no energy to sustain a population — and why the total biomass of top predators in an ecosystem is always much smaller than the biomass of producers.

*Decomposers* — bacteria, fungi, and detritivores like earthworms — are often overlooked but are arguably the most important component of the food web. They break down dead organic matter from every trophic level, releasing bound nutrients back into forms that producers can use again. Without decomposers, nutrients would accumulate in dead biomass and producers would be starved of the nitrogen, phosphorus, and other elements they need. In a forest, far more energy flows through the detrital (decomposer) pathway than through the grazing pathway we typically picture.

Food web *stability* comes from redundancy — the more species that can fill a given role, the more robust the web is to losing any one of them. When a keystone species is removed, the effects can cascade through the entire web: the prey of that predator explodes in number, overconsumes its own prey or food source, and the ripple continues. This is a *trophic cascade*. Real-world examples include the reintroduction of wolves to Yellowstone, which suppressed elk overgrazing and allowed riverside vegetation to recover — a change that reshaped the entire ecosystem.
