---
id: bioaccumulation-and-ecological-toxicology
title: Bioaccumulation and Ecological Toxicology
domain: biology
course: ecology-and-evolution
prerequisites:
- id: energy-pyramid-efficiency-trophic-transfer
  type: hard
- id: trophic-levels-and-food-webs
  type: soft
builds-toward:
- ecosystem-stability-resilience-and-tipping-points
tags:
- toxicology
- bioaccumulation
- pollution
- food-web
stage: formal-systems
status: draft
---

# Bioaccumulation and Ecological Toxicology

## Core Idea
Toxic substances (metals, persistent organic pollutants, radionuclides) accumulate in food webs; bioaccumulation is uptake and retention from the environment, while biomagnification is the increase in toxin concentration at higher trophic levels. Because energy decreases up food chains but toxins do not proportionally decrease, top predators accumulate extremely high concentrations. This disproportionate toxin load can cause population declines even at low environmental levels.

## Questions

```yaml
- question: "A persistent pesticide is measured in a lake at 0.001 parts per million — a concentration that causes no detectable harm to individual algal cells. What does biomagnification predict about osprey feeding on large fish in this lake?"
  type: multiple-choice
  options:
    - "Osprey will be similarly unaffected since the concentration is below a harm threshold for all organisms"
    - "Osprey may accumulate concentrations millions of times higher than ambient, potentially causing reproductive failure or death"
    - "Osprey will accumulate more pesticide than fish in proportion to their larger body mass"
    - "The pesticide will be diluted as it passes through more organisms, reducing osprey exposure"
  answer: 1
  explanation: "Biomagnification concentrates persistent toxins at each trophic level. An osprey eats many fish over its lifetime; each fish concentrated toxin from hundreds of small fish; each small fish concentrated from millions of zooplankton. While energy is lost (~10%) at each trophic transfer, a non-metabolized toxin is retained and concentrated. The result is a magnification factor that can exceed one million from ambient water to apex predator tissue. Option A is the classic oversight — ambient concentration tells you almost nothing about risk to top predators. Option D inverts the process: toxins do not dilute upward, they concentrate."

- question: "Which property of a chemical is most essential for biomagnification across trophic levels to occur?"
  type: multiple-choice
  options:
    - "High acute toxicity at low concentrations"
    - "Rapid metabolism and excretion in vertebrate predators, so it does not persist"
    - "Persistence — the substance resists metabolic breakdown and is not efficiently excreted"
    - "High water solubility, which facilitates uptake across gills and gut epithelia"
  answer: 2
  explanation: "The asymmetry between biomagnification and the energy pyramid hinges entirely on persistence. Energy is lost as heat at each transfer — metabolic processes consume it. If a toxin were similarly metabolized and excreted, its tissue concentration would also decrease up the food chain. The reason it doesn't is that persistent toxins (mercury, DDT, PCBs) bind tightly to proteins or dissolve in lipids and are not broken down or expelled efficiently. High acute toxicity (option A) is a consequence of biomagnification, not a prerequisite. High water solubility (option D) actually tends to work against biomagnification — lipid-soluble substances accumulate in fatty tissues far more effectively."

- question: "Because energy is lost (~90%) at each trophic level, the concentration of persistent pollutants in tissues should also decrease from prey to predator, mirroring the energy pyramid."
  type: true-false
  answer: false
  explanation: "This is the central misconception the topic is designed to correct. The energy pyramid and the toxin pyramid operate on entirely different principles. Energy is lost as heat through metabolic processes at every trophic transfer. Persistent toxins — by definition — are not metabolized or excreted efficiently, so they are not 'lost' in the same way. A predator must consume many prey items to sustain itself (because energy transfer is inefficient), and it retains nearly all of the toxin from each prey item. The result is that toxin concentration *increases* at each trophic step, the opposite of what the energy logic would predict."

- question: "Species that are large-bodied, long-lived, and occupy high trophic positions — such as killer whales, bald eagles, and bluefin tuna — are the most vulnerable to biomagnification effects."
  type: true-false
  answer: true
  explanation: "All three characteristics compound biomagnification risk. High trophic position means many steps of concentration have already occurred before the individual eats. Long lifespan means the individual accumulates toxin over decades rather than months. Large body size is less directly a risk factor on its own, but large predators typically eat the highest-quality (and most contaminated) prey and live the longest. In addition, many persistent organic pollutants are lipophilic (fat-soluble), so species with high body fat percentages — marine mammals in particular — accumulate them in especially high concentrations. This is why killer whales, polar bears, and eagles are sentinel species for persistent pollution monitoring."

- question: "Why is measuring pollutant concentration only in water or soil an inadequate strategy for assessing the ecological risk of persistent pollutants, and what additional information is required?"
  type: short-answer
  answer: "Ambient concentration in abiotic media reflects exposure at the base of the food web, but persistent toxins do not remain at that concentration as they move through living systems. Because they resist metabolism and excretion, they accumulate in organism tissues at concentrations that can be orders of magnitude higher than the surrounding environment — and this amplification multiplies at each trophic transfer. A water concentration that harms no individual organism may represent a catastrophic dose for an apex predator after three or four rounds of biomagnification. Adequate risk assessment requires measuring tissue concentrations across multiple trophic levels and estimating the biomagnification factor for each toxin in the specific food web — not just a single environmental baseline."
  explanation: "The practical implication is that regulatory frameworks historically based only on ambient concentration thresholds systematically underestimated risk to top predators. The DDT crisis demonstrated this: DDT at parts-per-trillion in water reached parts-per-thousand in eagle tissues — a difference of nine orders of magnitude. Understanding that toxin and energy flow in opposite directions through food webs is the conceptual tool that makes this failure of intuition correctable."
```

## Explainer

From your study of energy pyramids, you know that energy transfers between trophic levels are inefficient — roughly 10% passes from prey to predator, with the rest lost as heat. Toxins, however, do not follow this rule. **Persistent pollutants** like mercury, DDT, and PCBs are not metabolized or excreted efficiently, so instead of diminishing at each trophic level, they accumulate. The energy pyramid shrinks going up; the toxin pyramid grows. This asymmetry is the foundation of ecological toxicology.

The process starts with **bioaccumulation**: an individual organism absorbs a toxin from its environment (water, soil, food) faster than it can eliminate it. A small fish living in water with trace mercury concentrations absorbs mercury through its gills and diet every day. Because mercury binds tightly to proteins and is excreted slowly, its tissue concentration rises steadily over its lifetime — potentially reaching levels thousands of times higher than the surrounding water. The key factor is the substance's **persistence**: if a molecule resists metabolic breakdown, it simply builds up.

**Biomagnification** takes this one level further by operating across trophic levels. When a larger fish eats hundreds of small mercury-laden fish over its lifetime, it absorbs all of their accumulated mercury. Because the predator must eat many prey items to sustain itself (remember, only ~10% of energy transfers), it concentrates the toxin from all of them into its own tissues. A top predator like an eagle or tuna may be several trophic levels removed from the original source, yet carry concentrations millions of times higher than the ambient environment. The classic case is DDT and bald eagles: DDT at parts-per-trillion in lake water reached parts-per-thousand in eagle tissues, thinning their eggshells and driving populations toward collapse.

The ecological consequences are counterintuitive. A pollutant can be present at levels too low to harm any individual plankton cell, yet devastate apex predators. This means environmental monitoring that focuses only on water or soil concentrations will dramatically underestimate risk to top predators. Conservation biologists and toxicologists must therefore measure tissue concentrations across multiple trophic levels and model the magnification factor for each food web. Species with long lifespans, high trophic positions, and fatty tissues (where lipophilic toxins concentrate) are the most vulnerable — which is why marine mammals, raptors, and large predatory fish are the sentinel species for persistent pollution.
