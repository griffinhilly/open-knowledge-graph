---
id: biodiversity-patterns-richness-evenness
title: 'Biodiversity Patterns: Richness, Evenness, and Gradients'
domain: biology
course: ecology-and-evolution
prerequisites:
- id: biodiversity-and-conservation
  type: soft
- id: biodiversity-metrics
  type: soft
builds-toward:
- conservation-genetics-effective-size
- island-biogeography
tags:
- biodiversity
- richness
- evenness
- diversity-gradients
- latitudinal
stage: formal-systems
status: draft
---

# Biodiversity Patterns: Richness, Evenness, and Gradients

## Core Idea
Biodiversity includes species richness (number of species), evenness (distribution of abundances), and functional diversity. Diversity varies predictably across the planet—increasing toward the tropics and at intermediate disturbance levels. Understanding these patterns requires considering speciation, extinction, and ecological assembly.

## Questions

```yaml
- question: "Two forest plots each contain 20 bird species. In Plot A, each species makes up roughly 5% of individuals. In Plot B, one species makes up 85% of individuals and the other 19 share the remaining 15%. Which statement is most accurate?"
  type: multiple-choice
  options:
    - "The two plots are equally diverse because species richness is the only valid measure of biodiversity"
    - "Plot A is more diverse because higher evenness means the community is more functionally balanced — no single species dominates"
    - "Plot B is more ecologically stable because a dominant species provides consistent ecosystem function"
    - "Plot B has higher diversity because dominant species support more dependent species in their food web"
  answer: 1
  explanation: "Both plots have the same species richness (20 species), but their evenness is radically different. Diversity indices like Shannon and Simpson combine both components. Plot B is functionally precarious — if the dominant species collapses, most of the community's biomass disappears. Plot A's balanced distribution means the community's function is distributed across many species, making it more resilient. The classic misconception is equating richness with biodiversity; evenness captures something equally important about community structure."

- question: "An ecologist surveys three coral reef sites. A reef with very frequent storms has few species (only fast colonizers survive). A reef undisturbed for decades has few species (a dominant coral has outcompeted others). A reef with occasional storms has the most species. What principle does this illustrate?"
  type: multiple-choice
  options:
    - "The competitive exclusion principle — disturbance prevents any single species from monopolizing resources"
    - "The intermediate disturbance hypothesis — diversity peaks at moderate disturbance because neither competitive dominants nor disturbance specialists can fully exclude the other"
    - "Island biogeography — the moderately disturbed reef has the highest immigration-to-extinction ratio"
    - "The latitudinal diversity gradient — storm frequency correlates with distance from the tropics"
  answer: 1
  explanation: "The intermediate disturbance hypothesis predicts exactly this pattern. High disturbance favors only fast-colonizing species with little competitive ability; no disturbance allows competitive dominants to exclude everything else. At intermediate disturbance, competitive dominants haven't had time to monopolize, but disturbance isn't so frequent that slow-growing species are wiped out before establishing — so a mix persists. This applies to coral reefs, forests, grasslands, and many other systems."

- question: "A community can have identical species richness to another community but be meaningfully less diverse if one community is strongly dominated by a single species."
  type: true-false
  answer: true
  explanation: "True. Richness counts species; evenness describes how individuals are distributed among those species. Two communities with 10 species each are very different if one is 91% one species vs. one where each is 10%. Diversity indices (Shannon, Simpson) were specifically developed to capture both dimensions. Conservation decisions based on richness alone can miss the functional fragility of dominance-skewed communities."

- question: "The latitudinal diversity gradient — more species in the tropics than at the poles — is explained by a single well-established mechanism: higher solar energy input supporting greater productivity."
  type: true-false
  answer: false
  explanation: "False. The latitudinal gradient is one of ecology's most robust patterns, but its explanation remains multi-causal and contested. Energy-productivity hypotheses, greater climatic stability in the tropics (allowing long-term species accumulation without mass extinction), and geometric area effects (the tropics occupy more surface area) are all supported by evidence and are not mutually exclusive. No single mechanism fully accounts for the pattern across all taxa and regions."

- question: "Why does protecting a square kilometer of tropical forest preserve far more biodiversity than the same area of boreal forest? What does this imply for conservation prioritization?"
  type: short-answer
  answer: "Tropical forests have both higher species richness (more species per area due to the latitudinal gradient — energy, stability, and area effects) and higher evenness in many groups, meaning a given area contains a disproportionate share of Earth's total biodiversity. A hectare of tropical rainforest may contain more tree species than all of temperate Europe. For conservation prioritization, this means that protecting tropical areas yields a much higher return on investment in species conserved per dollar or per hectare. It also implies that tropical deforestation is a biodiversity catastrophe disproportionate to the area lost — and that conserving high-richness, high-evenness systems should be prioritized over ecologically impoverished areas of equal size."
  explanation: "The practical implication connects the descriptive patterns (richness, evenness, latitudinal gradient) to conservation strategy. Understanding that diversity is non-uniformly distributed — concentrated in predictable places for identifiable reasons — transforms conservation from a uniformly distributed concern into a spatially strategic one."
```

## Explainer

When ecologists talk about biodiversity, they mean more than just counting species. Two components matter independently. **Species richness** is the raw count — how many species are present in a defined area. **Evenness** describes how individuals are distributed among those species. A forest with 10 tree species where each makes up 10% of the canopy is more diverse in a meaningful sense than a forest with 10 species where one species accounts for 91% and the other nine share the remaining 9%. Both have the same richness, but the second community is dominated by a single species, making it functionally less diverse. Diversity indices like the **Shannon index** and **Simpson's index** combine richness and evenness into a single number, weighting rare versus common species differently.

The most striking global pattern in biodiversity is the **latitudinal diversity gradient**: species richness increases dramatically from the poles to the tropics, across virtually all taxonomic groups — birds, insects, trees, marine invertebrates. A single hectare of tropical rainforest may contain more tree species than all of temperate Europe. Multiple hypotheses explain this pattern, and they are not mutually exclusive. Greater solar energy input at the equator supports higher productivity and more individuals, which can sustain more species. Tropical regions have been climatically stable for longer, allowing species to accumulate without mass extinction events. And the larger area of the tropics (the geometric effect of Earth's shape) provides more space for populations to diverge and speciate.

At smaller scales, the **intermediate disturbance hypothesis** predicts that diversity peaks at moderate levels of disturbance — not too frequent (which eliminates slow-growing species) and not too rare (which allows competitive dominants to exclude other species). Think of a coral reef battered by occasional storms: frequent storms leave only fast-colonizing species, total calm lets a few competitive corals dominate, but intermittent disturbance maintains a mix. Similarly, **elevation gradients** often show a mid-elevation diversity peak, where temperature and moisture conditions are neither extreme.

Understanding these patterns matters for conservation because they reveal that diversity is not randomly distributed — it concentrates in predictable places for identifiable reasons. Protecting a square kilometer of tropical forest preserves far more species than the same area of boreal forest, and maintaining natural disturbance regimes can be as important as preventing habitat loss. Richness tells you how many species you have; evenness tells you whether the community is balanced or fragile; and gradient patterns tell you where to focus conservation effort for maximum impact.
