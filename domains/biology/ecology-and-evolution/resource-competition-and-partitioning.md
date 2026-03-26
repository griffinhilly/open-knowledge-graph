---
id: resource-competition-and-partitioning
title: Resource Competition and Partitioning
domain: biology
course: ecology-and-evolution
prerequisites:
- id: competition-types-outcomes
  type: hard
- id: ecological-niche-overlap-and-differentiation
  type: soft
builds-toward:
- community-assembly-rules-and-coexistence
tags:
- competition
- resources
- partitioning
- ecology
stage: formal-systems
status: validated
---

# Resource Competition and Partitioning

## Core Idea
Competition for limited resources (food, water, light, space, mates) shapes community structure. Species coexist through resource partitioning—using resources differently in space, time, or quality. Competitive exclusion occurs when one species outcompetes another for all shared resources. Competition intensity depends on resource scarcity, overlap in resource use, and competitor abilities.

## Questions

```yaml
- question: "Two warbler species occupy the same spruce forest and eat similar insects. Species A forages in the upper canopy; Species B forages in the lower branches. Both populations remain stable over many years. What best explains this coexistence?"
  type: multiple-choice
  options:
    - "Competitive exclusion — Species A is the superior competitor and Species B will eventually go extinct"
    - "Spatial resource partitioning — by using different parts of the habitat, each species limits its own population more than it limits the other's"
    - "Character displacement — both species have evolved similar traits to reduce competition"
    - "Mutualism — the two species have evolved a cooperative relationship that allows both to persist"
  answer: 1
  explanation: "This mirrors MacArthur's classic warbler study. Spatial partitioning (different foraging heights) reduces niche overlap enough that intraspecific competition within each species exceeds interspecific competition between them — the condition for stable coexistence. Option A is wrong because both populations are stable, so exclusion hasn't occurred and won't. Option C has the direction wrong — character displacement produces divergence, not similarity. Option D misidentifies the relationship: these are competitors, not mutualists."

- question: "The competitive exclusion principle predicts that two species competing for exactly the same limiting resource cannot coexist. How does resource partitioning reconcile this principle with the high diversity of natural communities?"
  type: multiple-choice
  options:
    - "Resource partitioning shows the principle is wrong — coexistence is always possible regardless of niche overlap"
    - "Resource partitioning means competing species are not actually exploiting exactly the same limiting resource in the same way, so the principle's core assumption is never met"
    - "Resource partitioning replaces competition with cooperation, which stabilizes communities"
    - "The competitive exclusion principle only applies in laboratory conditions, not in natural ecosystems"
  answer: 1
  explanation: "The competitive exclusion principle isn't violated — it's escaped. The principle says two species can't stably coexist on exactly the same limiting resource. Resource partitioning (different times, places, or food types) means they're not actually using exactly the same resource. Each species is primarily regulated by intraspecific competition for its own particular resource subset, not by the other species. Option A incorrectly rejects the principle; Option C mischaracterizes partitioning as cooperation; Option D is false — the principle holds in nature."

- question: "Character displacement — the evolutionary divergence of competing species in resource use — can produce stable coexistence by increasing niche partitioning, even when species initially overlapped strongly in resource use."
  type: true-false
  answer: true
  explanation: "When competing species come into contact, natural selection favors individuals that diverge in resource use from the competitor, reducing direct competition. Over evolutionary time this produces measurable differences between sympatric populations (co-occurring) versus allopatric ones (each alone). Darwin's finches on islands where two species co-occur show greater beak size divergence than on single-species islands — direct evidence that competition drives evolutionary partitioning that reduces overlap and enables coexistence."

- question: "For two competing species to coexist stably, interspecific competition (between species) is expected to be stronger than intraspecific competition (within species)."
  type: true-false
  answer: false
  explanation: "This has the direction exactly backwards. Stable coexistence requires that each species limits its own population growth MORE than it limits the other's — i.e., intraspecific competition must exceed interspecific competition. When this holds, a species that becomes rare faces less intraspecific competition and can recover, producing a stabilizing negative feedback. If interspecific competition exceeds intraspecific, the rarer species cannot recover and competitive exclusion follows."

- question: "Explain the relationship between resource partitioning and competitive exclusion. How does partitioning allow coexistence without violating the competitive exclusion principle?"
  type: short-answer
  answer: "The competitive exclusion principle says two species cannot coexist when competing for exactly the same limiting resource — the superior competitor will drive the inferior one extinct. Resource partitioning allows coexistence by ensuring no two species use exactly the same limiting resource: they eat at different times, in different places, or specialize on different food types. Each species' most intense competition is with conspecifics (same-species individuals) rather than heterospecifics. When intraspecific competition exceeds interspecific competition, rare individuals of each species face less competition and can recover — producing a stable equilibrium. Resource partitioning doesn't violate the principle; it shows the conditions under which the principle's key assumption of identical resource use simply isn't met."
  explanation: "The limiting similarity concept formalizes this: there is a maximum degree of niche overlap compatible with stable coexistence. Beyond that threshold, interspecific competition becomes too strong relative to intraspecific competition, and one species excludes the other."
```

## Explainer

From your work on competition types, you know that interspecific competition can be exploitative (indirect, through shared resource depletion) or interference (direct, through aggression or chemical inhibition). The central puzzle of community ecology is how so many competing species manage to coexist when the **competitive exclusion principle** predicts that two species competing for exactly the same limiting resource cannot stably coexist — the superior competitor will inevitably drive the other to extinction. The answer lies in **resource partitioning**: species divide up resources so that no two species compete for exactly the same thing in exactly the same way.

Resource partitioning occurs along three main axes. **Spatial partitioning** means species use different parts of the habitat — warblers in a spruce forest famously feed at different heights and positions within the same trees, as Robert MacArthur demonstrated. **Temporal partitioning** separates species by when they use a resource — hawks hunt by day while owls hunt at night, reducing direct competition for similar prey. **Diet or quality partitioning** means species specialize on different subsets of a shared resource type — seed-eating finches on the same island may evolve different beak sizes to crack seeds of different sizes, reducing overlap in exactly which seeds each species exploits.

The niche overlap concept from your prerequisite work helps formalize this. Two species can coexist when each species limits its own population growth more than it limits the other's — that is, when **intraspecific competition** (within species) exceeds **interspecific competition** (between species). This happens when species differ enough in resource use that they are not direct substitutes for each other. The more similar two species are in their resource requirements, the stronger the competition between them and the less likely coexistence becomes. This generates a pattern known as **limiting similarity**: there is a maximum degree of niche overlap compatible with stable coexistence.

Competition also drives evolutionary change. When two competing species come into contact, natural selection favors individuals that diverge in resource use from the competitor — a process called **character displacement**. The classic example is Darwin's finches on islands where two species co-occur: their beak sizes diverge compared to islands where each species lives alone. Over evolutionary time, competition sculpts communities toward greater resource partitioning, explaining why diverse communities tend to contain species that are ecologically distinct rather than ecologically redundant. Resource partitioning is not a passive outcome but an active evolutionary response to the cost of sharing.
