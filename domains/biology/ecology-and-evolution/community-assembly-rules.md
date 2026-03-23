---
id: community-assembly-rules
title: Community Assembly Rules and Metacommunity Dynamics
domain: biology
course: ecology-and-evolution
prerequisites:
- id: community-ecology-intro
  type: hard
- id: competition-types-outcomes
  type: soft
builds-toward:
- biodiversity-patterns-richness-evenness
tags:
- assembly-rules
- metacommunity
- community-composition
- species-sorting
stage: formal-systems
status: draft
---

# Community Assembly Rules and Metacommunity Dynamics

## Core Idea
Community assembly rules describe which species combinations can coexist based on competition, niche requirements, and dispersal. Assembly can be deterministic (species composition determined by environmental filtering and competition) or stochastic (random dispersal events). Metacommunity frameworks integrate local and regional processes to explain spatial patterns of diversity.

## Questions

```yaml
- question: "Two forest patches with identical soil chemistry, climate, and disturbance history have very different tree species compositions. Which explanation is most consistent with the community assembly framework?"
  type: multiple-choice
  options:
    - "The patches must have unmeasured environmental differences that account for the compositional divergence"
    - "Competitive exclusion has already produced identical communities — the observation must be measurement error"
    - "Stochastic processes — which species happened to disperse there first — can produce different compositions in otherwise identical habitats"
    - "Environmental filtering always produces identical communities under identical abiotic conditions"
  answer: 2
  explanation: "Deterministic niche-based assembly predicts that identical environments should support similar communities, but stochastic processes (priority effects, random dispersal, demographic fluctuations) can generate divergent outcomes even under identical conditions. This is one of the key insights from neutral theory and stochastic assembly: historical contingency — who arrived first — can lock in different stable states. Real communities typically reflect a blend of deterministic filtering and stochastic chance."

- question: "Environmental filtering and competitive (biotic) filtering have opposite effects on the functional traits of co-occurring species. Which statement correctly describes this tension?"
  type: multiple-choice
  options:
    - "Environmental filtering makes co-occurring species more functionally different; competition makes them more similar"
    - "Environmental filtering makes co-occurring species more functionally similar (all must tolerate the same conditions); competition pushes them apart in trait space (reduces niche overlap to avoid exclusion)"
    - "Both filters independently increase trait diversity in communities"
    - "Trait patterns emerge only from dispersal limitation — neither filter affects functional similarity"
  answer: 1
  explanation: "Environmental filtering is a convergent force: only species tolerating local conditions persist, so co-occurring species share traits that allow survival in that environment. Competitive filtering is a divergent force: species too similar in resource use cannot stably coexist (competitive exclusion), so the surviving assemblage consists of species spread across niche space. The interplay of these opposing forces shapes the functional and phylogenetic structure of communities."

- question: "Neutral theory, as proposed by Hubbell, predicts that community composition is primarily determined by niche differences among functionally distinct species."
  type: true-false
  answer: false
  explanation: "Neutral theory explicitly assumes the opposite: all species are functionally equivalent (neutral), and community composition is driven by stochastic birth, death, and immigration events — random drift. This is the theory's provocative core: it generates realistic-looking species abundance distributions without invoking niche differences at all. The neutral model serves as a null hypothesis, and deviations from it provide evidence for niche-based assembly."

- question: "A species-rich local community may owe its diversity partly to being embedded in a well-connected landscape that supplies immigrants from diverse surrounding habitats, rather than entirely to favorable local conditions."
  type: true-false
  answer: true
  explanation: "This is the metacommunity insight — local diversity cannot be understood in isolation from the regional context. In the 'mass effects' metacommunity framework, high dispersal allows species to persist locally even in unfavorable conditions through constant immigration. A well-connected patch receives a continuous supply of colonists from diverse habitats, maintaining diversity beyond what local conditions alone would support. Cutting dispersal connections can collapse local diversity even without changing local abiotic conditions."

- question: "What are the three main sequential filters in community assembly, and why does the order in which they operate matter?"
  type: short-answer
  answer: "The three filters are: (1) dispersal — only species that can physically reach the site are candidates; (2) environmental (abiotic) filtering — of those arriving, only species tolerating local conditions persist; (3) biotic filtering — of those persisting, only species that can coexist with residents remain. Order matters because each filter operates on the subset that passed earlier ones. A species excluded by dispersal never faces environmental or biotic filtering at that site; a species that cannot tolerate local conditions never faces competition there."
  explanation: "The sequential filter model clarifies why understanding local community composition requires knowing the regional species pool (dispersal filter), local abiotic conditions (environmental filter), and the identities and traits of resident species (biotic filter). It also clarifies why interventions must target the right filter: if a species is absent because it cannot disperse there, improving local conditions won't help; if it's absent because it loses to a competitor, addressing dispersal is insufficient."
```

## Explainer

From community ecology, you know that species live together in communities and interact through competition, predation, and mutualism. You may also recall that competition can lead to competitive exclusion or niche partitioning. **Community assembly rules** ask a deeper question: out of all the species in a region, why do we find this particular set of species living together at this particular site? The answer involves a series of filters — think of them as successive sieves that narrow the regional species pool down to the local community you actually observe.

The first filter is **dispersal**. A species can only join a community if it can physically get there. Geographic barriers, distance, and dispersal ability determine which species from the regional pool even have a chance of arriving. Seeds that travel by wind reach different sites than seeds dispersed by specific bird species. This filter operates before any ecological interaction takes place — it is purely about access. The second filter is **environmental filtering** (or abiotic filtering). Even if a species arrives, it can only persist if the local conditions — temperature, soil pH, moisture, light availability — fall within its tolerance range. A cactus might disperse to a wetland, but it will not survive there. Environmental filtering tends to make co-occurring species more similar to each other than expected by chance, because they must all tolerate the same conditions.

The third filter is **biotic interactions**, particularly competition. Once species pass through dispersal and environmental filters, they must coexist with the species already present. From your study of competition, you know that species with identical niches cannot stably coexist — one will exclude the other. This means biotic filtering tends to push co-occurring species apart in trait space: species that are too similar in their resource use are less likely to coexist. The interplay between environmental filtering (which pulls species toward similarity) and competitive filtering (which pushes them toward difference) creates a tension that shapes the functional and phylogenetic composition of communities.

A key debate in community ecology is whether assembly is primarily **deterministic** — driven by these predictable filters — or **stochastic**, meaning that random events like which species happens to arrive first, demographic fluctuations, or chance disturbances play a dominant role. **Neutral theory**, proposed by Stephen Hubbell, argues that many species are functionally equivalent and that community composition is largely determined by random birth, death, and immigration events rather than niche differences. In reality, most communities show a blend: strong environmental filtering creates broad predictability (you won't find deep-sea fish in a prairie), while stochastic processes generate variation among sites with similar conditions.

**Metacommunity theory** extends these ideas to landscapes of interconnected local communities. Four frameworks describe different scenarios: **species sorting** (local environments determine composition, with dispersal maintaining supply), **mass effects** (high dispersal allows species to persist in unfavorable habitats through constant immigration), **patch dynamics** (local extinction and colonization of identical patches), and **neutral models** (species are ecologically equivalent). Real landscapes typically involve elements of all four. The metacommunity perspective explains why local diversity cannot be understood in isolation — it depends on the regional species pool, connectivity between sites, and the balance between local and regional processes. A patch of forest may be species-rich not because local conditions favor many species, but because it sits in a well-connected landscape that constantly supplies immigrants from diverse habitats nearby.
