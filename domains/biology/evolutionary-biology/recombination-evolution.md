---
id: recombination-evolution
title: Evolution of Recombination Rates
domain: biology
course: evolutionary-biology
prerequisites:
- id: population-genetics-intro
  type: hard
- id: linkage-disequilibrium-evolutionary
  type: hard
- id: genetic-drift
  type: soft
builds-toward:
- effective-recombination-rate
- efficacy-selection-finite-populations
tags:
- recombination
- evolution
- linkage
- selection
stage: advanced
status: draft
---

# Evolution of Recombination Rates

## Core Idea
Recombination rates evolve in response to selection. Regions of low recombination accumulate deleterious mutations (Hill-Robertson interference), reducing fitness. Increased recombination is selected when it breaks unfavorable linkage between beneficial and deleterious alleles.

## Explainer

From population genetics, you know that allele frequencies change through selection, drift, mutation, and migration. From your study of linkage disequilibrium, you know that alleles at different loci can be statistically associated — inherited together more often than expected by chance. Recombination breaks these associations by shuffling alleles between homologous chromosomes during meiosis. But recombination rates themselves are not fixed — they vary across the genome and across species, and they evolve under natural selection. Understanding *why* recombination rates evolve requires connecting linkage, selection, and finite population size.

The key concept is **Hill-Robertson interference** (sometimes called the Hill-Robertson effect). In a finite population, selection at one locus interferes with selection at linked loci. Imagine a beneficial mutation arising on a chromosome that also carries a deleterious allele nearby. If recombination between the two sites is rare, selection cannot easily separate the good allele from the bad one — the beneficial mutation may be dragged to extinction by the linked deleterious allele, or the deleterious allele may hitchhike to fixation with the beneficial one. In regions of very low recombination, this interference compounds across many loci simultaneously: every selected site interferes with every other linked site, reducing the overall **efficacy of selection**. The result is that low-recombination regions accumulate more deleterious mutations and fix fewer beneficial ones than high-recombination regions.

This creates a selective advantage for modifiers that increase recombination. An allele at one locus that increases the crossover rate at nearby loci will, over time, tend to be found on fitter genetic backgrounds — because it breaks apart the unfavorable combinations that Hill-Robertson interference creates. This is an **indirect selection** effect: the recombination modifier is not itself more fit, but it becomes statistically associated with higher-fitness chromosomes because it generates them. The effect is strongest when populations are finite (so drift matters), when selection is common across many loci, and when linkage disequilibrium is prevalent — exactly the conditions predicted by your understanding of genetic drift and LD.

Empirical evidence supports these predictions. In many species, recombination rates are higher near genes under strong selection and lower in regions with few functional elements. The non-recombining portions of Y chromosomes and W chromosomes show dramatic degeneration over evolutionary time — losing genes and accumulating repetitive DNA — consistent with Hill-Robertson interference operating without the rescue of recombination. Conversely, organisms facing rapidly changing environments (such as host-pathogen arms races) often maintain or increase recombination rates in genomic regions involved in immune defense. The evolution of recombination is thus a window into how genomes solve the fundamental problem of maintaining adaptive potential in finite populations.
