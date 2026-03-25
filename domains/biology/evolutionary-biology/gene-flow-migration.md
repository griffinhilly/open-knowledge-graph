---
id: gene-flow-migration
title: Gene Flow and Population Structure
domain: biology
course: evolutionary-biology
prerequisites:
- id: population-genetics-intro
  type: hard
- id: allele-frequency-change
  type: hard
builds-toward:
- allopatric-speciation
tags:
- gene-flow
- migration
- population-structure
- differentiation
stage: formal-systems
status: validated
---

# Gene Flow and Population Structure

## Core Idea
Gene flow (migration) introduces alleles from one population into another, homogenizing allele frequencies across populations and reducing genetic differentiation. Even small amounts of gene flow can counteract local adaptation and prevent speciation by swamping local selection. Conversely, restriction of gene flow allows populations to diverge and can lead to reproductive isolation and speciation.

## Questions

```yaml
- question: "Island lizards have evolved darker coloration as a local adaptation to their volcanic rock habitat (darker = less predation). However, the island receives migrants from a lighter-colored mainland population at rate m = 0.05 per generation, and selection favoring dark coloration has coefficient s = 0.01. What is the expected outcome over many generations?"
  type: multiple-choice
  options:
    - "The island will maintain its dark coloration because natural selection always overcomes migration"
    - "The island lizards will gradually become lighter, matching the mainland, because migration rate exceeds selection strength"
    - "Migration has no effect on the island's allele frequencies because the populations are geographically separate"
    - "The island will become more genetically diverse than the mainland due to the influx of new alleles"
  answer: 1
  explanation: "The outcome depends on the relative strength of gene flow and selection. Here m = 0.05 >> s = 0.01, so gene flow is approximately five times stronger than selection. The island population cannot maintain its local adaptation because each generation, migration imports mainland alleles faster than selection can increase the frequency of the locally adaptive dark allele. This is migration-selection balance: local adaptation persists only when selection substantially exceeds migration (s >> m). Option A is the common misconception — selection does NOT always overcome migration."

- question: "A population geneticist compares two populations of the same bird species and finds FST = 0.35 between them. What does this high FST value imply about their evolutionary history?"
  type: multiple-choice
  options:
    - "The populations have been exchanging many migrants per generation, maintaining similar allele frequencies"
    - "The populations have experienced little historical gene flow, allowing substantial genetic differentiation to accumulate"
    - "The populations have undergone recent bottlenecks that increased heterozygosity within each population"
    - "The populations are reproductively isolated and therefore constitute separate species"
  answer: 1
  explanation: "FST measures genetic differentiation between populations: values near 0 indicate high genetic similarity (high gene flow); values near 1 indicate strong differentiation (low gene flow). FST = 0.35 is high and implies that little historical gene flow has occurred between the populations, allowing allele frequencies to diverge through local selection and/or genetic drift. High FST is evidence for isolation, but it does not by itself confirm speciation (option D) — populations can be highly differentiated but still capable of interbreeding."

- question: "Even a very small rate of gene flow — a few migrants per generation in a large population — can be sufficient to prevent substantial genetic differentiation between populations."
  type: true-false
  answer: true
  explanation: "This is one of the most counterintuitive results in population genetics. The island model shows that the homogenizing effect of gene flow is proportional to the migration rate m, and even m = 0.01–0.05 (1–5% replacement per generation) is strong enough to keep allele frequencies closely tracking the source population over evolutionary time. Small amounts of gene flow act like a spring constantly pulling the recipient population's allele frequencies toward the source, and selection strengths rarely exceed a few percent per generation, so even modest migration can counteract strong local selection."

- question: "Restricting gene flow between two populations is sufficient on its own to cause them to become separate species."
  type: true-false
  answer: false
  explanation: "Restriction of gene flow is necessary but not sufficient for speciation. Gene flow restriction (via geographic, behavioral, or temporal barriers) removes the homogenizing force that keeps populations genetically similar. But divergence into separate species also requires that the isolated populations actually diverge — through natural selection, genetic drift, or sexual selection — and eventually accumulate enough differences to become reproductively isolated even if brought back into contact. Allopatric speciation requires both isolation (reduced gene flow) and divergence; isolation alone, without divergence, produces isolated but genetically similar populations."

- question: "Explain how migration-selection balance works, and describe the conditions under which a locally adaptive allele can be maintained in a population that receives gene flow from a different-environment source population."
  type: short-answer
  answer: "Migration-selection balance is a tug-of-war between two opposing forces: local selection favors increasing the frequency of a locally adaptive allele, while gene flow keeps importing the non-adaptive allele from the source population. The locally adaptive allele can be maintained when selection is substantially stronger than migration (s >> m). When migration rate exceeds selection strength (m >> s), the influx of non-adapted alleles overwhelms selection and the local adaptation is swamped — the recipient population ends up tracking the source population's allele frequencies instead of adapting to its local environment."
  explanation: "This framework explains why populations across strong environmental gradients (where selection is intense) maintain distinct local adaptations, while populations across gentle gradients (where selection differences are small) tend to look genetically similar despite moderate gene flow. It also explains why conservation geneticists worry about migration from large, genetically different populations into small endangered populations — even 'helpful' gene flow can swamp local adaptations critical to survival in specific environments."
```

## Explainer

You have already studied allele frequency change and the forces that drive it — selection, drift, mutation. **Gene flow**, also called **migration** in population genetics models, is the fourth force, and it is unique because it acts between populations rather than within them. Where selection and drift reshape a single population's allele frequencies, gene flow connects populations by transferring alleles from one gene pool to another. Understanding gene flow quantitatively allows you to predict whether populations will remain genetically similar or drift apart toward speciation.

The simplest model is the **island model**: imagine a large mainland population sending migrants to a small island population at rate *m* (the fraction of the island population replaced by migrants each generation). If the mainland has allele frequency *p* and the island has frequency *p'*, then after one generation of migration the island's new frequency shifts toward the mainland by an amount proportional to *m* × (*p* − *p'*). This means gene flow acts like a spring pulling the island frequency toward the mainland frequency, and the strength of that pull is directly proportional to the migration rate. Over many generations, even modest migration (a few percent per generation) is enough to make the island nearly genetically identical to the mainland.

The evolutionary significance becomes clear when you consider gene flow's interaction with other forces. Suppose the island environment favors a locally adaptive allele that is rare on the mainland. Selection pushes that allele's frequency up on the island, but gene flow keeps importing the mainland allele, dragging the frequency back down. The outcome depends on the relative strength: if selection is much stronger than gene flow (*s* >> *m*), local adaptation persists despite migration. If gene flow overwhelms selection (*m* >> *s*), the island population cannot maintain its local adaptation and instead mirrors the mainland genetically. This **migration-selection balance** is why populations of the same species can look very different across strong environmental gradients (where selection overcomes gene flow) but very similar across gentle ones (where gene flow homogenizes).

Gene flow's role in speciation is essentially the flip side of its homogenizing power. For two populations to diverge enough to become separate species, gene flow between them must be reduced below the threshold where it can counteract divergence by drift and selection. Geographic barriers accomplish this most obviously — a mountain range or ocean channel physically prevents migration. But gene flow can also be reduced by behavioral changes (different mating calls), temporal isolation (different breeding seasons), or habitat preferences (feeding in different microhabitats), even when populations are geographically close. This is why population geneticists measure gene flow indirectly through **FST** and related statistics: high genetic differentiation between populations implies low historical gene flow, providing evidence for the isolation that precedes speciation.
