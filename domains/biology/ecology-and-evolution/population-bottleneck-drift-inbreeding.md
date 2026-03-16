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
status: draft
---

# Population Bottlenecks: Drift, Inbreeding, and Recovery

## Core Idea
Population bottlenecks (sudden reductions in size) accelerate genetic drift, causing random loss of alleles and inbreeding. After a bottleneck, heterozygosity decreases and deleterious mutations may drift to fixation. Recovery depends on mutation rate and selection strength; some lineages never fully regain lost variation. This is critical for conservation of endangered species.

## Explainer

From your study of genetic drift, you know that allele frequencies fluctuate randomly in finite populations and that smaller populations experience stronger drift. From your work on inbreeding, you know that mating among relatives increases homozygosity and can expose deleterious recessive alleles. A **population bottleneck** is where these two forces collide with devastating effect: a sudden, drastic reduction in population size — caused by a natural disaster, disease, habitat destruction, or hunting — amplifies both drift and inbreeding simultaneously.

Imagine a population of 10,000 individuals carrying hundreds of alleles at various loci. A catastrophic event kills 99% of the population, leaving just 100 survivors. Those 100 individuals carry only a random sample of the original genetic diversity. Rare alleles — which were present in only a handful of individuals — are almost certainly lost entirely. Even common alleles may be lost or shifted in frequency by chance. This is drift on fast-forward: what might take thousands of generations in a large population happens in a single generation during a bottleneck. The **effective population size** during the bottleneck, not the size before or after, determines how much diversity is lost.

The genetic consequences compound over time. With reduced diversity, the surviving individuals are more closely related to each other than they were before the bottleneck. When they breed, **inbreeding** is unavoidable — even if they mate randomly, they share more alleles by descent. Increased homozygosity means deleterious recessive alleles that were hidden in heterozygous carriers become exposed in homozygous offspring, causing **inbreeding depression**: reduced fertility, immune function, and survival. Worse, in the small post-bottleneck population, purifying selection is less effective against mildly deleterious alleles because drift overpowers selection when population size is small (recall that drift dominates when the selection coefficient *s* is less than 1/2N_e). Harmful alleles can drift to fixation — a phenomenon called **mutational meltdown** in extreme cases.

Real examples illustrate the severity. Cheetahs passed through a severe bottleneck roughly 10,000 years ago and today show remarkably low genetic diversity — skin grafts between unrelated cheetahs are not rejected because their immune genes are nearly identical. Northern elephant seals were hunted to fewer than 30 individuals in the 1890s; despite recovering to over 100,000, they retain far less genetic variation than southern elephant seals that were never bottlenecked. Recovery of genetic diversity after a bottleneck is painfully slow because it depends on new mutations accumulating — a process that takes thousands of generations. For conservation, this means that preventing bottlenecks is far more effective than trying to restore diversity after one has occurred, and it explains why maintaining large effective population sizes is a central goal of conservation genetics.
