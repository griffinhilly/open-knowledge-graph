---
id: population-bottleneck-drift-inbreeding
title: 'Population Bottlenecks: Drift, Inbreeding, and Recovery'
domain: biology
course: ecology-and-evolution
prerequisites:
- id: genetic-drift-in-small-populations
  type: hard
- id: inbreeding-consequences
  type: hard
- id: effective-population-size
  type: hard
- id: probability-axioms
  type: soft
builds-toward:
- population-viability-analysis
- conservation-genetics-effective-size
tags:
- bottleneck
- drift
- inbreeding
- conservation
stage: formal-systems
status: validated
---

# Population Bottlenecks: Drift, Inbreeding, and Recovery

## Core Idea
Population bottlenecks (sudden reductions in size) accelerate genetic drift, causing random loss of alleles and inbreeding. After a bottleneck, heterozygosity decreases and deleterious mutations may drift to fixation. Recovery depends on mutation rate and selection strength; some lineages never fully regain lost variation. This is critical for conservation of endangered species.

## Questions

```yaml
- question: "A population of 10,000 individuals is reduced to 50 for a single generation due to a disease outbreak, then recovers to 8,000 over the following decades. Compared to a population that was never bottlenecked, how much genetic diversity has been lost?"
  type: multiple-choice
  options:
    - "Very little — the population recovered to near its original size, so diversity should be largely restored"
    - "A small amount — only the rarest alleles would be lost in a single-generation bottleneck"
    - "Substantial diversity — the effective population size during the bottleneck (Ne ≈ 50) drives severe allele loss regardless of recovery"
    - "All diversity — a single-generation bottleneck through 50 individuals eliminates nearly all variation"
  answer: 2
  explanation: "It is the effective population size *during* the bottleneck, not before or after, that determines diversity loss. With Ne ≈ 50 for one generation, the founder sample carries only a random subset of the original variation: rare alleles (present in only a few individuals) are almost certainly lost, and common alleles may shift dramatically in frequency. Even after recovering to 8,000, that diversity cannot be recovered quickly — it requires new mutations accumulating over thousands of generations. Option A is the classic misconception: population size recovery does not restore genetic diversity."

- question: "Two bottlenecked populations both recover to 10,000 individuals. Population X passed through a bottleneck of 20 individuals for 5 generations; Population Y passed through a bottleneck of 200 individuals for 1 generation. Which is expected to retain more genetic diversity?"
  type: multiple-choice
  options:
    - "Population X — the longer bottleneck allowed more time for new mutations to accumulate"
    - "Population Y — the larger bottleneck size and shorter duration mean less allele loss due to drift"
    - "They will retain equal diversity — census size at recovery is what matters"
    - "Population X — smaller populations evolve faster, generating more variation"
  answer: 1
  explanation: "Population Y experienced less severe drift: higher Ne (200 vs 20) and fewer generations of small size means the random allele losses from sampling were less severe. The harmonic mean of Ne across generations determines cumulative diversity loss, and even a single generation of very small Ne can be devastating. Population X's smaller Ne (20) means stronger drift each generation, and 5 generations of this compounded the losses. Option C is the error: it is Ne *during* the bottleneck, not after recovery, that determines diversity retained."

- question: "A species that was bottlenecked but has since recovered to its pre-bottleneck census size will typically have restored most of its pre-bottleneck genetic diversity within a few generations."
  type: true-false
  answer: false
  explanation: "Recovery of genetic diversity is not driven by population size recovery — it depends on the slow accumulation of new mutations, which occurs at a rate of roughly 10⁻⁸ per base pair per generation in most organisms. Restoring diversity across thousands of loci takes thousands of generations even in large populations. Northern elephant seals recovered to over 100,000 individuals from fewer than 30 in the 1890s, yet they still show dramatically reduced genetic variation compared to non-bottlenecked southern elephant seals over a century later. Population size recovery restores demographic viability but not genetic diversity."

- question: "During a population bottleneck, rare alleles are disproportionately likely to be lost compared to common alleles."
  type: true-false
  answer: true
  explanation: "A bottleneck samples a small number of individuals from the larger population. Rare alleles — those present in only a handful of individuals — are statistically unlikely to be represented in that small sample. Common alleles, by contrast, are present in many individuals and are much more likely to appear in any random subset. This is why bottlenecks consistently erode allelic diversity (the number of alleles) more severely than heterozygosity (the frequency of the most common alleles), and why rare-allele loss is one of the first genetic signatures of a past bottleneck."

- question: "Why do biologists argue that preventing population bottlenecks is far more effective for conservation than trying to restore genetic diversity after one has occurred?"
  type: short-answer
  answer: "Recovery of genetic diversity after a bottleneck depends almost entirely on new mutations — a process that occurs at roughly 10⁻⁸ per base pair per generation and requires thousands of generations to meaningfully restore diversity across the genome. Once alleles are lost from a population, they cannot be recovered except through mutation (or immigration from another population). In contrast, maintaining a large effective population size preserves existing variation indefinitely because drift is weak and allele losses are rare. The asymmetry is stark: diversity is lost in a single catastrophic generation but can only be restored over geological timescales."
  explanation: "This asymmetry explains why conservation geneticists prioritize habitat preservation and maintaining connectivity between populations above all other interventions. Interventions after a bottleneck — captive breeding, translocation — can help, but they primarily restore census size, not genetic diversity. The cheetah example illustrates the permanence of bottleneck effects: 10,000 years after their severe bottleneck, cheetahs still show near-zero immunological diversity, and no amount of population growth has changed this."
```

## Explainer

From your study of genetic drift, you know that allele frequencies fluctuate randomly in finite populations and that smaller populations experience stronger drift. From your work on inbreeding, you know that mating among relatives increases homozygosity and can expose deleterious recessive alleles. A **population bottleneck** is where these two forces collide with devastating effect: a sudden, drastic reduction in population size — caused by a natural disaster, disease, habitat destruction, or hunting — amplifies both drift and inbreeding simultaneously.

Imagine a population of 10,000 individuals carrying hundreds of alleles at various loci. A catastrophic event kills 99% of the population, leaving just 100 survivors. Those 100 individuals carry only a random sample of the original genetic diversity. Rare alleles — which were present in only a handful of individuals — are almost certainly lost entirely. Even common alleles may be lost or shifted in frequency by chance. This is drift on fast-forward: what might take thousands of generations in a large population happens in a single generation during a bottleneck. The **effective population size** during the bottleneck, not the size before or after, determines how much diversity is lost.

The genetic consequences compound over time. With reduced diversity, the surviving individuals are more closely related to each other than they were before the bottleneck. When they breed, **inbreeding** is unavoidable — even if they mate randomly, they share more alleles by descent. Increased homozygosity means deleterious recessive alleles that were hidden in heterozygous carriers become exposed in homozygous offspring, causing **inbreeding depression**: reduced fertility, immune function, and survival. Worse, in the small post-bottleneck population, purifying selection is less effective against mildly deleterious alleles because drift overpowers selection when population size is small (recall that drift dominates when the selection coefficient *s* is less than 1/2N_e). Harmful alleles can drift to fixation — a phenomenon called **mutational meltdown** in extreme cases.

Real examples illustrate the severity. Cheetahs passed through a severe bottleneck roughly 10,000 years ago and today show remarkably low genetic diversity — skin grafts between unrelated cheetahs are not rejected because their immune genes are nearly identical. Northern elephant seals were hunted to fewer than 30 individuals in the 1890s; despite recovering to over 100,000, they retain far less genetic variation than southern elephant seals that were never bottlenecked. Recovery of genetic diversity after a bottleneck is painfully slow because it depends on new mutations accumulating — a process that takes thousands of generations. For conservation, this means that preventing bottlenecks is far more effective than trying to restore diversity after one has occurred, and it explains why maintaining large effective population sizes is a central goal of conservation genetics.
