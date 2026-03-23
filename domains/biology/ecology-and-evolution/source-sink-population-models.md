---
id: source-sink-population-models
title: Source-Sink Population Dynamics
domain: biology
course: ecology-and-evolution
prerequisites:
- id: population-growth-models
  type: hard
- id: gene-flow-migration
  type: soft
builds-toward:
- metapopulation-dynamics-connectivity
- conservation-genetics-and-population-recovery
tags:
- source-sink
- population
- metapopulation
- dispersal
stage: formal-systems
status: validated
---

# Source-Sink Population Dynamics

## Core Idea
In heterogeneous environments, source patches have positive growth with excess dispersers; sink patches have negative growth and persist only through immigration. Understanding source-sink dynamics is critical for conservation: protecting sources and maintaining connectivity to sinks is necessary for persistence. Disrupting connectivity can tip sink populations toward extinction.

## Questions

```yaml
- question: "A conservation survey finds birds occupying 20 forest patches across a fragmented landscape. Detailed demographic analysis reveals that only 3 patches have positive local population growth (births exceed deaths). A highway is proposed that would destroy one of those 3 productive patches. Based on source-sink theory, what outcome should the conservation biologist predict?"
  type: multiple-choice
  options:
    - "Minimal impact — 17 other occupied patches remain, so the species retains most of its range"
    - "Gradual collapse across the whole network — destroying a source will starve the sink patches of immigrants, causing them to decline toward extinction one by one"
    - "The sink patches will become self-sustaining once immigration from the lost source stops, because competition pressure will be reduced"
    - "Only the patches directly adjacent to the destroyed source will be affected; distant sinks receive immigrants from multiple sources and will be buffered"
  answer: 1
  explanation: "The 17 unproductive patches are sinks — they persist only because of immigration from the 3 sources. Eliminating a source removes the demographic subsidy those sinks depend on. With fewer immigrants arriving, mortality continues to exceed births in the sink patches, and populations decline until extinction. The survey finding 'birds in every patch' gives a false impression of habitat quality. The correct conservation priority is identifying and protecting sources, not just any occupied patch."

- question: "Which definition correctly describes a sink habitat in source-sink population dynamics?"
  type: multiple-choice
  options:
    - "A habitat patch with low population density due to strong interspecific competition from neighboring patches"
    - "A habitat patch where local mortality exceeds reproduction, so the population persists only through continued immigration from better-quality patches"
    - "A habitat patch that receives more immigrants than it exports, causing local density to exceed carrying capacity"
    - "A habitat patch where individuals reproduce successfully but emigrate before local density builds, keeping the resident population artificially low"
  answer: 1
  explanation: "The defining feature of a sink is negative intrinsic population growth: locally, deaths exceed births, and the population would decline to zero without immigration. The population is 'rescued' demographically by a continuous supply of dispersers from source patches. Crucially, this means abundance alone tells you nothing — a sink can be dense and appear healthy while being entirely subsidized. Only demographic data (birth rates, death rates, immigration rates) distinguishes sources from sinks."

- question: "A sink population can appear occupied and even dense while being entirely dependent on immigration from a source population for its long-term persistence."
  type: true-false
  answer: true
  explanation: "This is the central, counter-intuitive insight of source-sink theory. Because immigrants from the source continuously replenish the sink, the sink can maintain a substantial, apparently stable population. A naive count of individuals would suggest healthy occupancy. Only a demographic analysis showing that local births fail to replace local deaths reveals the sink's dependence. This insight has major conservation implications: abundance is a misleading indicator of habitat quality when immigration is occurring."

- question: "In source-sink landscapes, sink populations are always smaller and less dense than source populations, making sources relatively easy to identify through census data alone."
  type: true-false
  answer: false
  explanation: "Sink density can be high — sometimes even higher than source density — if immigration rates are large. The presence of abundant immigrants can maintain sink populations well above what local reproduction would support. This is precisely why source-sink dynamics are easy to misread: conservation surveys based on abundance data alone may protect the wrong patches. Identifying sources and sinks requires demographic rates (per-capita birth and death rates), not just counts."

- question: "Why is immigration from a source important not just demographically but also genetically to a sink population, and what conservation management practice does this motivate?"
  type: short-answer
  answer: "Demographically, immigrants prevent the sink from collapsing by replacing individuals lost to excess mortality. Genetically, immigrants introduce alleles from the larger, more genetically diverse source population, counteracting the genetic drift and inbreeding depression that threaten small isolated populations. This motivates maintaining or restoring connectivity — habitat corridors, stepping-stone patches, or translocation programs — between source and sink patches so that both demographic rescue and genetic rescue can operate."
  explanation: "The dual benefit of connectivity (demographic + genetic rescue) makes it especially valuable in conservation planning. A sink that is demographically stable but genetically isolated will still slowly accumulate inbreeding effects, reducing fitness over generations. Landscape-level management that preserves the source patches and the movement corridors linking them to sinks addresses both problems simultaneously. Fragmentation that severs these connections can lead to extinction even when sink habitats appear intact."
```

## Explainer

From population growth models, you know that a population's trajectory depends on whether births exceed deaths. A population with a positive intrinsic growth rate expands; one with a negative rate declines toward extinction. **Source-sink dynamics** apply this logic to a landscape where habitat quality varies from patch to patch, and individuals can move between them. The result is a system where some populations are self-sustaining producers of emigrants, while others are demographic dead ends kept alive only by a steady stream of immigrants.

A **source** habitat is one where conditions are good enough that local reproduction exceeds local mortality. The population grows beyond what the patch can hold, and surplus individuals disperse outward. A **sink** habitat is the opposite: conditions are poor, mortality exceeds reproduction, and the local population would decline to zero without immigration. The key insight is that a sink can appear healthy — occupied, even dense — while being entirely dependent on the source for its persistence. If you counted individuals in a sink patch, you might mistakenly conclude it was prime habitat. But cut the connection to the source, and the sink population collapses.

This distinction has profound consequences for conservation. Imagine a bird species occupying forest patches across a fragmented landscape. A naive survey finds birds in every patch and concludes the species is doing well. But a demographic study reveals that only two large patches are true sources — the rest are sinks sustained by dispersers from those two patches. If a highway or housing development destroys one of the sources, the entire network unravels, and sink populations wink out one by one as their supply of immigrants dries up. Protecting the wrong patches — the sinks, which may be more numerous and more visible — wastes limited conservation resources.

Source-sink models also connect to gene flow. Immigration from sources does more than prop up sink numbers — it introduces genetic variation, counteracting the drift and inbreeding that threaten small isolated populations. This is why maintaining **connectivity** between source and sink patches matters doubly: it sustains both demographic rescue and genetic rescue. The practical lesson is that landscape-level thinking is essential. Managing individual patches in isolation ignores the flows of individuals that link them into a functioning system. Identifying which patches are sources, which are sinks, and what maintains the connections between them is the first step toward effective conservation planning in any fragmented landscape.
