---
id: biodiversity-metrics
title: 'Measuring Biodiversity: Species Richness, Diversity Indices, and Evenness'
domain: biology
course: ecology-and-evolution
prerequisites:
- id: community-ecology-intro
  type: hard
- id: cladistics-and-systematics
  type: soft
- id: logarithms-intro
  type: soft
- id: simple-probability
  type: soft
- id: ecological-succession
  type: soft
builds-toward:
- biodiversity-and-conservation
- island-biogeography
tags:
- biodiversity
- species-richness
- Shannon-diversity
- evenness
- alpha-beta-gamma
stage: advanced
status: validated
---
# Measuring Biodiversity: Species Richness, Diversity Indices, and Evenness

## Core Idea
Biodiversity can be measured at multiple levels: genetic diversity (within populations), species diversity (within communities), and ecosystem diversity (variety of habitats). Species richness counts the number of species; diversity indices like Shannon-Wiener H' incorporate both richness and evenness (relative abundance distribution). Alpha diversity measures local diversity, beta diversity measures turnover between sites, and gamma diversity captures regional diversity. Phylogenetic diversity adds evolutionary distinctiveness to species counts, providing a richer conservation metric.

## How It's Best Learned
Calculate Shannon and Simpson indices for two communities with the same richness but different evenness to see how they diverge. Decompose gamma diversity into alpha and beta components using additive or multiplicative partitioning. Compare communities before and after a disturbance using diversity metrics.

## Common Misconceptions
- More species does not always mean higher ecological function — a community can have high richness but low functional diversity.
- Beta diversity is not simply the difference in species lists — multiple metrics capture different aspects of turnover and nestedness.

## Explainer

From community ecology, you know that ecological communities consist of multiple species interacting within a shared environment. But how do we quantify how "diverse" a community actually is? Simply counting species is a start, but it misses something important: a forest with 20 tree species where one species comprises 95% of all individuals feels very different from a forest with 20 species in equal proportions. **Biodiversity metrics** give us rigorous tools to capture these distinctions and compare communities in meaningful ways.

The simplest measure is **species richness** — a raw count of how many species are present. A pond with 15 fish species has higher richness than one with 8. But richness tells you nothing about relative abundance. This is where **diversity indices** become essential. The **Shannon-Wiener index (H')** calculates diversity as H' = −Σ(pᵢ × ln pᵢ), where pᵢ is the proportion of individuals belonging to species i. If you recall logarithms and basic probability, this formula weights each species by its proportional abundance: rare species contribute little, common species contribute more, and maximum diversity occurs when all species are equally abundant. The **Simpson index** takes a complementary approach, measuring the probability that two randomly chosen individuals belong to different species. Both indices increase with richness and with **evenness** — the degree to which individuals are spread equally among species. A community of 10 species with equal abundances has higher Shannon diversity than one where a single species dominates 90% of individuals.

These indices measure diversity at a single site, which ecologists call **alpha diversity**. But biodiversity also has a spatial dimension. **Beta diversity** captures how much species composition changes between sites — the turnover as you move from one habitat to another. If two forest plots share all the same species, beta diversity is zero; if they share none, beta diversity is maximal. **Gamma diversity** is the total diversity of an entire region, and it can be decomposed: gamma = alpha + beta (additive partitioning) or gamma = alpha × beta (multiplicative). This decomposition reveals whether regional diversity comes from each site being individually rich (high alpha) or from sites differing from one another (high beta). A landscape of many similar meadows has high alpha but low beta; a landscape with distinct habitat types (wetland, forest, grassland) may have moderate alpha but high beta, yielding high gamma.

Beyond species counts and abundances, **phylogenetic diversity** adds evolutionary information. Two communities might each have 10 species, but if one contains species from 10 different families and the other contains 10 closely related species within a single genus, they differ profoundly in the evolutionary heritage they harbor. Phylogenetic diversity — often measured as the total branch length on a phylogenetic tree connecting all species in a community — captures this distinction. For conservation, phylogenetic diversity matters because losing an evolutionarily isolated species (one with no close relatives) erases more unique genetic information than losing one of several closely related species. By combining richness, evenness, turnover, and phylogenetic distinctiveness, ecologists build a multidimensional picture of biodiversity that informs both basic science and conservation priorities.
