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
status: draft
---

# Source-Sink Population Dynamics

## Core Idea
In heterogeneous environments, source patches have positive growth with excess dispersers; sink patches have negative growth and persist only through immigration. Understanding source-sink dynamics is critical for conservation: protecting sources and maintaining connectivity to sinks is necessary for persistence. Disrupting connectivity can tip sink populations toward extinction.

## Explainer

From population growth models, you know that a population's trajectory depends on whether births exceed deaths. A population with a positive intrinsic growth rate expands; one with a negative rate declines toward extinction. **Source-sink dynamics** apply this logic to a landscape where habitat quality varies from patch to patch, and individuals can move between them. The result is a system where some populations are self-sustaining producers of emigrants, while others are demographic dead ends kept alive only by a steady stream of immigrants.

A **source** habitat is one where conditions are good enough that local reproduction exceeds local mortality. The population grows beyond what the patch can hold, and surplus individuals disperse outward. A **sink** habitat is the opposite: conditions are poor, mortality exceeds reproduction, and the local population would decline to zero without immigration. The key insight is that a sink can appear healthy — occupied, even dense — while being entirely dependent on the source for its persistence. If you counted individuals in a sink patch, you might mistakenly conclude it was prime habitat. But cut the connection to the source, and the sink population collapses.

This distinction has profound consequences for conservation. Imagine a bird species occupying forest patches across a fragmented landscape. A naive survey finds birds in every patch and concludes the species is doing well. But a demographic study reveals that only two large patches are true sources — the rest are sinks sustained by dispersers from those two patches. If a highway or housing development destroys one of the sources, the entire network unravels, and sink populations wink out one by one as their supply of immigrants dries up. Protecting the wrong patches — the sinks, which may be more numerous and more visible — wastes limited conservation resources.

Source-sink models also connect to gene flow. Immigration from sources does more than prop up sink numbers — it introduces genetic variation, counteracting the drift and inbreeding that threaten small isolated populations. This is why maintaining **connectivity** between source and sink patches matters doubly: it sustains both demographic rescue and genetic rescue. The practical lesson is that landscape-level thinking is essential. Managing individual patches in isolation ignores the flows of individuals that link them into a functioning system. Identifying which patches are sources, which are sinks, and what maintains the connections between them is the first step toward effective conservation planning in any fragmented landscape.
