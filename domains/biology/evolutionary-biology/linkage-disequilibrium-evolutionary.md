---
id: linkage-disequilibrium-evolutionary
title: Linkage Disequilibrium and Evolutionary Dynamics
domain: biology
course: evolutionary-biology
prerequisites:
- id: population-genetics-intro
  type: hard
- id: genetic-drift
  type: hard
tags:
- linkage
- recombination
- genetic-association
- haplotype
stage: advanced
status: draft
---

# Linkage Disequilibrium and Evolutionary Dynamics

## Core Idea
Linkage disequilibrium (LD) is the non-random association of alleles at different loci, caused by limited recombination, genetic drift, or selection on linked sites. LD decays over time through recombination, but patterns of LD across the genome reveal population history, selection, and recombination rates. LD is fundamental to genome-wide association studies (GWAS).

## Explainer

From your work in population genetics, you know that allele frequencies change through drift and selection, and that different loci in a genome can behave independently — in theory. **Linkage disequilibrium** (LD) describes the situation where alleles at two different loci are found together on the same chromosome more often (or less often) than you would predict from their individual frequencies alone. If allele A at one locus and allele B at a nearby locus appear together on 60% of chromosomes, but their individual frequencies predict only 40% co-occurrence, those loci are in linkage disequilibrium.

The key force that creates LD is physical proximity on a chromosome. When two loci are close together, recombination rarely separates them, so allele combinations that arise together — whether by mutation, migration, or drift — persist across generations as a block called a **haplotype**. Genetic drift in small populations can also generate LD by chance, even between unlinked loci, because random sampling creates temporary associations. Selection acting on one locus drags nearby alleles along for the ride, a phenomenon called **genetic hitchhiking**, which creates extended regions of LD around beneficial mutations.

The critical insight is that LD is not permanent — it **decays** over time. Each generation of recombination shuffles allele combinations, gradually breaking apart haplotype blocks. The rate of decay depends on the recombination rate between the loci: tightly linked loci lose LD slowly, while distant or unlinked loci reach equilibrium (linkage equilibrium) quickly. This decay is measured by the parameter D, which starts at its maximum value when a new haplotype appears and halves roughly every generation for unlinked loci, or decays at rate (1 − r) per generation where r is the recombination fraction.

This decay property makes LD a powerful tool for reading evolutionary history. Long blocks of LD suggest recent events — a selective sweep, a population bottleneck, or recent admixture — because recombination has not yet had time to break them apart. Short LD blocks indicate ancient, well-recombined populations. In genome-wide association studies (GWAS), researchers exploit LD to find disease-associated variants: if a causal mutation is in LD with a nearby marker SNP, the marker's statistical association with the disease serves as a proxy for the causal variant. Understanding LD structure across the genome is therefore essential for interpreting both evolutionary patterns and the architecture of complex traits.
