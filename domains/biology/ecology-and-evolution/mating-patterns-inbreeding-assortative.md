---
id: mating-patterns-inbreeding-assortative
title: 'Mating Patterns: Inbreeding and Assortative Mating'
domain: biology
course: ecology-and-evolution
prerequisites:
- id: population-genetics-intro
  type: hard
- id: hardy-weinberg-equilibrium
  type: soft
builds-toward:
- population-genetic-structure-metapopulations
- speciation
tags:
- mating
- inbreeding
- assortative-mating
- random-mating
stage: formal-systems
status: draft
---

# Mating Patterns: Inbreeding and Assortative Mating

## Core Idea
Mating patterns deviate from random when individuals preferentially mate with relatives (inbreeding) or with similar phenotypes (assortative mating). Inbreeding increases homozygosity and exposes deleterious recessive alleles. Assortative mating increases linkage disequilibrium and can drive sympatric divergence.

## Explainer

The Hardy-Weinberg model you studied earlier assumes random mating — every individual is equally likely to mate with any other individual in the population. Real populations almost never meet this assumption. **Non-random mating** occurs whenever mate choice is biased by relatedness, phenotype, or proximity, and it systematically changes genotype frequencies even when it does not directly change allele frequencies. Understanding how mating patterns deviate from random is essential for predicting evolutionary trajectories.

**Inbreeding** occurs when relatives mate more often than expected by chance. The most intuitive measure is the **inbreeding coefficient** (*F*), which quantifies the probability that two alleles at a locus in an individual are identical by descent — meaning they trace back to the same copy in a recent ancestor. When *F* increases, heterozygosity decreases and homozygosity increases across the genome. This matters because many deleterious alleles are recessive: they cause harm only when homozygous. In a randomly mating population, these alleles hide safely in heterozygotes. Inbreeding strips away that protection, exposing them. The result is **inbreeding depression** — reduced survival and reproduction in inbred individuals. You see this starkly in small, isolated populations: cheetahs with low genetic diversity and high disease susceptibility, or inbred captive populations with elevated rates of developmental abnormalities.

**Assortative mating** is different from inbreeding because it operates on phenotype rather than pedigree. In **positive assortative mating**, individuals preferentially mate with others who share a trait — large birds pairing with large birds, or humans tending to marry partners of similar height. This increases homozygosity specifically at loci controlling the assorted trait, while leaving the rest of the genome unaffected. Crucially, positive assortative mating also builds **linkage disequilibrium**: alleles at different loci that both contribute to the preferred phenotype become statistically associated, because individuals carrying "large" alleles at multiple loci disproportionately mate with each other. **Negative assortative mating** (disassortative mating), where opposites attract, has the reverse effect — it maintains heterozygosity and can stabilize polymorphisms, as seen in MHC-based mate choice in many vertebrates.

The evolutionary consequences extend beyond single-generation genotype shifts. Prolonged positive assortative mating on ecologically relevant traits can drive **sympatric divergence** — populations splitting into distinct forms without geographic isolation. If large-bodied fish preferentially mate with other large-bodied fish and small-bodied fish do the same, gene flow between the two size classes decreases, and natural selection can push them further apart. This connects mating patterns directly to speciation, one of the topics this concept builds toward. Inbreeding in small populations, meanwhile, interacts with genetic drift to erode adaptive potential, making it a central concern in conservation genetics and metapopulation management.
